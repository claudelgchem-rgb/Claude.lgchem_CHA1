#!/usr/bin/env python3
import json, re, os

OUT = "/home/user/Claude.lgchem_CHA1/pcea-harness/work/02_extracted"
REVIEW = "/home/user/Claude.lgchem_CHA1/pcea-harness/work/_review_queue"
RETRIEVED = "2026-06-15T02:03:44Z"
os.makedirs(OUT, exist_ok=True)
os.makedirs(REVIEW, exist_ok=True)

def classify(n, text):
    """Mechanical dependency detection."""
    t = text
    # find "claim N" / "claims N" references
    deps = set()
    # range patterns: "claims 1 to 10", "any one of claims 18-23", "claims 23 to 25"
    for m in re.finditer(r'claims?\s+(\d+)\s*(?:to|-|–|through)\s*(\d+)', t, re.I):
        a, b = int(m.group(1)), int(m.group(2))
        for k in range(a, b+1):
            deps.add(k)
    # single / list: "claim 1", "claim 23", "claims 69 or 70", "claim 4 or claim 16"
    for m in re.finditer(r'claims?\s+((?:\d+\s*(?:,|or|and)\s*)*\d+)', t, re.I):
        frag = m.group(1)
        for num in re.findall(r'\d+', frag):
            deps.add(int(num))
    # "preceding claims" / "any of the preceding" => depends on all prior, mark dependent w/ note
    preceding = bool(re.search(r'preceding claim', t, re.I))
    deps.discard(n)
    if deps:
        return "dependent", sorted(deps)
    if preceding:
        # dependent on all preceding claims
        return "dependent", list(range(1, n))
    return "independent", []

def build(patent_id, source_url, source_type, claims, status, notes):
    out_claims = []
    for n, txt in claims:
        ctype, deps = classify(n, txt)
        out_claims.append({
            "claim_number": n,
            "claim_text": txt,
            "claim_type": ctype,
            "depends_on": deps,
            "char_count": len(txt)
        })
    obj = {
        "patent_id": patent_id,
        "source_url": source_url,
        "source_type": source_type,
        "retrieved_at": RETRIEVED,
        "claims": out_claims,
        "extraction_status": status,
        "notes": notes
    }
    with open(os.path.join(OUT, patent_id + ".json"), "w") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
    # MD verbatim
    md = ["# " + patent_id + " - Verbatim Claims", "",
          "Source: " + source_url, "Retrieved: " + RETRIEVED,
          "Status: " + status, ""]
    for c in out_claims:
        md.append(str(c["claim_number"]) + ". " + c["claim_text"])
        md.append("")
    with open(os.path.join(OUT, patent_id + ".md"), "w") as f:
        f.write("\n".join(md))
    return len(out_claims)

print("script ready")
