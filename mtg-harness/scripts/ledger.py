#!/usr/bin/env python3
"""ledger.py — claim 원장 스키마/검증 유틸.

claim 단위 원장(ledger/claims.jsonl)의 스키마를 강제하고, 신뢰도·검증 상태를
정규화한다. 리서치 파이프라인이 만드는 모든 claim 은 이 스키마를 통과해야 한다.

CLI:
  python scripts/ledger.py validate ledger/claims.jsonl
  python scripts/ledger.py stats    ledger/claims.jsonl
"""
from __future__ import annotations
import json, sys
from pathlib import Path

# ── 스키마 ──────────────────────────────────────────────────────
QUESTIONS   = {"Q1", "Q2", "Q3"}
STANCES     = {"pro", "con", "neutral", "finding"}
CONFIDENCE  = {"high", "medium", "low"}
VERIFY      = {"confirmed", "plausible", "refuted", "unverified"}
SRC_TYPES   = {"regulatory", "systematic_review", "peer_reviewed",
               "market_report", "manufacturer", "news_secondary", "other"}

REQUIRED = ["id", "question", "topic", "claim", "stance",
            "sources", "confidence", "verification", "collected_at"]


def _err(cid, msg):
    return f"[{cid}] {msg}"


def validate_record(r: dict) -> list[str]:
    cid = r.get("id", "?")
    errs = []
    for k in REQUIRED:
        if k not in r:
            errs.append(_err(cid, f"필수 필드 누락: {k}"))
    if r.get("question") not in QUESTIONS:
        errs.append(_err(cid, f"question 은 {QUESTIONS} 중 하나 (got {r.get('question')})"))
    if r.get("stance") not in STANCES:
        errs.append(_err(cid, f"stance 는 {STANCES} 중 하나 (got {r.get('stance')})"))
    if r.get("confidence") not in CONFIDENCE:
        errs.append(_err(cid, f"confidence 는 {CONFIDENCE} 중 하나 (got {r.get('confidence')})"))
    v = r.get("verification") or {}
    if not isinstance(v, dict) or v.get("status") not in VERIFY:
        errs.append(_err(cid, f"verification.status 는 {VERIFY} 중 하나"))
    srcs = r.get("sources")
    if not isinstance(srcs, list) or len(srcs) == 0:
        errs.append(_err(cid, "sources 는 최소 1개"))
    else:
        for i, s in enumerate(srcs):
            if not isinstance(s, dict) or not s.get("url"):
                errs.append(_err(cid, f"sources[{i}] url 누락"))
            elif s.get("type") and s["type"] not in SRC_TYPES:
                errs.append(_err(cid, f"sources[{i}].type 비정상: {s.get('type')}"))
    # high 신뢰도는 confirmed/plausible 검증 + 2+ 출처 권장(경고만)
    return errs


def load(path: str) -> list[dict]:
    p = Path(path)
    if not p.exists():
        return []
    out = []
    for ln, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
        line = line.strip()
        if not line:
            continue
        try:
            out.append(json.loads(line))
        except json.JSONDecodeError as e:
            print(f"  ! line {ln} JSON 파싱 실패: {e}", file=sys.stderr)
    return out


def cmd_validate(path: str) -> int:
    recs = load(path)
    all_errs, seen = [], set()
    for r in recs:
        cid = r.get("id")
        if cid in seen:
            all_errs.append(_err(cid, "중복 id"))
        seen.add(cid)
        all_errs.extend(validate_record(r))
    print(f"claims: {len(recs)}  errors: {len(all_errs)}")
    for e in all_errs:
        print("  " + e)
    return 1 if all_errs else 0


def cmd_stats(path: str) -> int:
    recs = load(path)
    by_q, by_conf, by_ver = {}, {}, {}
    for r in recs:
        by_q[r.get("question")]   = by_q.get(r.get("question"), 0) + 1
        by_conf[r.get("confidence")] = by_conf.get(r.get("confidence"), 0) + 1
        st = (r.get("verification") or {}).get("status")
        by_ver[st] = by_ver.get(st, 0) + 1
    print(f"총 claim: {len(recs)}")
    print("  질문별:", by_q)
    print("  신뢰도:", by_conf)
    print("  검증상태:", by_ver)
    return 0


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(__doc__); sys.exit(2)
    cmd, path = sys.argv[1], sys.argv[2]
    sys.exit({"validate": cmd_validate, "stats": cmd_stats}[cmd](path))
