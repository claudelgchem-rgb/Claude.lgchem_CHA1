#!/usr/bin/env python3
"""gp_fetch.py — Google Patents authoritative fetcher/parser (PCEA harness).

Now that patents.google.com is reachable, this fetches the raw HTML via curl
and parses it DETERMINISTICALLY (no summarizing model) to extract:
  - claims (verbatim, reassembled by claim number)
  - title, assignee, priority/filing dates, anticipated expiration, legal status

This is an independent source from FreePatentsOnline, enabling true
cross-source verification. Text is NOT normalized beyond joining the
claim-text sub-blocks Google Patents splits a single claim into.

Usage: python3 gp_fetch.py <PATENT_ID> [--out-json path] [--out-md path]
Exit 0 on success (claims found), 3 if page fetched but no claims, 2 on fetch error.
"""
import sys, re, html, json, subprocess, argparse
from datetime import datetime, timezone

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36"

def fetch(pid):
    url = f"https://patents.google.com/patent/{pid}/en"
    r = subprocess.run(["curl", "-s", "-m", "40", "-A", UA, url],
                       capture_output=True, text=True)
    return url, r.stdout

def clean(t):
    t = re.sub(r"<[^>]+>", "", t)
    t = html.unescape(t)
    t = re.sub(r"[ \t\r\n]+", " ", t).strip()
    return t

def parse_claims(htmltext):
    sec = re.search(r'<section[^>]*itemprop="claims".*?</section>', htmltext, re.S)
    chunk = sec.group(0) if sec else ""
    blocks = re.findall(r'<div[^>]*class="claim-text"[^>]*>(.*?)</div>', chunk, re.S)
    blocks = [clean(b) for b in blocks if clean(b)]
    # reassemble: a block starting with "N." begins claim N; others continue it
    claims = {}
    order = []
    cur = None
    for b in blocks:
        m = re.match(r"^(\d+)\.\s", b)
        if m:
            cur = int(m.group(1))
            claims[cur] = b
            order.append(cur)
        elif cur is not None:
            claims[cur] += " " + b
    return [(n, claims[n]) for n in order]

def grab(htmltext, label, span=60):
    # pull a short string after a label (legal status, expiration, etc.)
    m = re.search(re.escape(label) + r"</[^>]+>\s*<[^>]+>([^<]{1,%d})" % span, htmltext)
    if m:
        return clean(m.group(1))
    m = re.search(re.escape(label) + r"[^<]{0,5}<[^>]*>([^<]{1,%d})" % span, htmltext)
    return clean(m.group(1)) if m else ""

def parse_meta(htmltext):
    meta = {}
    for prop in ["title", "priorityDate", "filingDate", "publicationDate", "grantDate"]:
        m = re.search(r'itemprop="%s"[^>]*content="([^"]+)"' % prop, htmltext)
        if not m:
            m = re.search(r'itemprop="%s"[^>]*>([^<]+)<' % prop, htmltext)
        if m:
            meta[prop] = clean(m.group(1))
    # assignee
    a = re.findall(r'itemprop="assigneeCurrent"[^>]*>([^<]+)<', htmltext) or \
        re.findall(r'itemprop="assigneeOriginal"[^>]*>([^<]+)<', htmltext)
    if a:
        meta["assignee"] = [clean(x) for x in a]
    # anticipated/adjusted expiration appears in a dd/td after the label
    # anticipated/adjusted expiration: nearest datetime that precedes the label
    for lbl in ["Adjusted expiration", "Anticipated expiration"]:
        m = re.search(r'datetime="(\d{4}-\d{2}-\d{2})"[^>]*>[\s\S]{0,300}?' + re.escape(lbl), htmltext)
        if m:
            meta["anticipated_expiration"] = m.group(1)
            meta["expiration_label"] = lbl
            break
    ls = re.search(r'itemprop="legalStatusIfi"[^>]*content="([^"]+)"', htmltext) or \
         re.search(r'itemprop="legalStatusIfi"[^>]*>\s*([^<]+)<', htmltext)
    if ls:
        meta["legal_status"] = clean(ls.group(1))
    return meta

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pid")
    ap.add_argument("--out-json")
    ap.add_argument("--out-md")
    args = ap.parse_args()
    url, htmltext = fetch(args.pid)
    if not htmltext or len(htmltext) < 5000:
        print(json.dumps({"patent_id": args.pid, "error": "fetch failed/empty", "len": len(htmltext)}, ensure_ascii=False))
        return 2
    if re.search(r"unusual traffic|/sorry/|recaptcha", htmltext, re.I):
        print(json.dumps({"patent_id": args.pid, "error": "bot challenge"}, ensure_ascii=False))
        return 2
    claims = parse_claims(htmltext)
    meta = parse_meta(htmltext)
    out = {
        "patent_id": args.pid,
        "source_url": url,
        "source_type": "google_patents",
        "retrieved_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "meta": meta,
        "claims": [{"claim_number": n, "claim_text": t, "char_count": len(t)} for n, t in claims],
        "claim_count": len(claims),
    }
    if args.out_json:
        json.dump(out, open(args.out_json, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    if args.out_md:
        with open(args.out_md, "w", encoding="utf-8") as fh:
            fh.write(f"# {args.pid} — Claims (verbatim, Google Patents)\n\n")
            for n, t in claims:
                fh.write(t + "\n\n")
    print(json.dumps({"patent_id": args.pid, "claim_count": len(claims),
                      "meta_keys": list(meta.keys()),
                      "expiration": meta.get("Anticipated expiration") or meta.get("Adjusted expiration", ""),
                      "claim1_preview": (claims[0][1][:160] if claims else "")}, ensure_ascii=False))
    return 0 if claims else 3

if __name__ == "__main__":
    sys.exit(main())
