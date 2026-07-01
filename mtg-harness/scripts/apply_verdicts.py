#!/usr/bin/env python3
"""apply_verdicts.py — 적대적 검증 결과(verdicts.jsonl)를 원장에 반영.

verifier 가 재검토한 claim 에 대해 verification.status / confidence 를 덮어쓰고,
extra_sources 를 원 sources 뒤에 병합(중복 url 제거)한다. verifier 가 다루지 않은
claim 은 collector 자체 검증값을 유지한다.

  python scripts/apply_verdicts.py ledger/claims.jsonl work/02_verified/verdicts.jsonl
"""
import json, sys


def load_jsonl(p):
    out = []
    for line in open(p, encoding="utf-8"):
        line = line.strip()
        if line:
            out.append(json.loads(line))
    return out


def main():
    ledger_path, verdicts_path = sys.argv[1], sys.argv[2]
    claims = load_jsonl(ledger_path)
    verdicts = {v["id"]: v for v in load_jsonl(verdicts_path)}

    changed = 0
    for c in claims:
        v = verdicts.get(c["id"])
        if not v:
            continue
        prev = (c.get("verification") or {}).get("status"), c.get("confidence")
        c["verification"] = {
            "status": v["status"],
            "note": v.get("note") or (c.get("verification") or {}).get("note", ""),
        }
        c["confidence"] = v.get("confidence", c.get("confidence"))
        # merge extra_sources (dedupe by url)
        have = {s.get("url") for s in c.get("sources", [])}
        for s in v.get("extra_sources", []) or []:
            if s.get("url") and s["url"] not in have:
                c.setdefault("sources", []).append(s)
                have.add(s["url"])
        if prev != (c["verification"]["status"], c["confidence"]):
            changed += 1

    with open(ledger_path, "w", encoding="utf-8") as f:
        for c in claims:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")

    refuted = sum(1 for c in claims
                  if (c.get("verification") or {}).get("status") == "refuted")
    print(f"applied {len(verdicts)} verdicts; {changed} claims changed; "
          f"{refuted} refuted; total {len(claims)}")


if __name__ == "__main__":
    main()
