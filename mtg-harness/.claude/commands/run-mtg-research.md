---
description: mTG 가교제 리서치 파이프라인을 끝까지 실행해 report/index.html 을 생성한다.
argument-hint: "[research_spec.yaml 경로] (생략 시 input/research_spec.yaml)"
---
`orchestrator` 서브에이전트를 기동해 mTG 리서치 파이프라인을 끝까지 실행하라.

입력 spec: `$ARGUMENTS` (비었으면 `input/research_spec.yaml`).

파이프라인(CLAUDE.md §4):
1. spec 로드 + manifest 초기화
2. [00] landscape-scout ×후보 → work/00_landscape/
3. [01] evidence-collector → work/01_evidence/ (Q1 랭킹 / Q2 9축 / Q3 5방면)
4. [02] claim-verifier (Gate 1) → work/02_verified/ → ledger/claims.jsonl 병합
5. `python scripts/ledger.py validate ledger/claims.jsonl`
6. [03] synthesizer (Gate 2) → work/03_synthesis/answers.json
7. `python scripts/build_report.py --ledger ledger/claims.jsonl --answers work/03_synthesis/answers.json --out report/index.html`

완료 후 manifest 요약(claim 수 / 검증완료 / 리뷰 큐 / 산출 경로)을 출력하라.
근거 없는 결론 금지, 근거 불충분은 리뷰 큐로.
