---
description: PCEA 특허 청구항 추출·검증·분석 파이프라인을 끝까지 실행한다
argument-hint: "[입력 yaml 경로] (생략 시 input/patents.yaml)"
---

# /run-patent-analysis

PCEA(Patent Claim Extraction & Analysis) 하니스의 전체 파이프라인을 기동한다.

## 입력
- 인자 `$1` 로 입력 파일 경로를 받을 수 있다. **생략하면 `input/patents.yaml`** 을 사용한다.
- 사용할 입력 파일: `${1:-input/patents.yaml}`

## 실행 절차
`orchestrator` 서브에이전트를 **Task 로 기동**하여 아래 파이프라인을 끝까지 돌린다:

1. 입력 yaml 파싱 → 모드 판정(explicit / discovery) → `work/manifest.json` 초기화.
2. discovery 모드면 `patent-discovery` 로 후보 특허 확정(explicit 모드면 건너뜀).
3. 각 특허: `metadata-collector` → `claim-extractor` → `claim-verifier`.
   - 검증 PASS 아니면 `claim-extractor` 재시도(최대 `retry_limit`). 그래도 실패면
     `work/_review_queue/` 로 에스컬레이션하되 **분석에서 제외하지 않고 "미검증" 으로 포함**.
4. `claim-analyst` 로 `output/patent_claims_report.md` 통합 생성.
5. `compilation-reviewer` 로 Gate 2 검증. 이슈 있으면 analyst 재생성(최대 `retry_limit`).
6. `docx` 스킬(`/mnt/skills/public/docx/SKILL.md`) 경유로
   `output/patent_claims_report.docx` 생성.
7. `work/manifest.json` 을 단계마다 갱신.

## 불변 규칙 (반드시 전달)
- 청구항 원문은 **어떤 단계에서도 변형/번역/요약/교정/재배열되지 않는다.**
- 검증은 독립 재수집 + `scripts/claim_diff.py` 실제 diff 로만 판정한다.
- 미검증 특허도 누락 없이 ⚠ 배지로 보고서에 포함한다.

## 실행 끝에 출력할 요약 (manifest 기반)
- 분석 대상 특허 수
- PASS(verified) 건수 / 리뷰 큐(needs_review) 건수 / 실패(failed) 건수
- 산출물 경로: `output/patent_claims_report.md`, `output/patent_claims_report.docx`
- 리뷰 큐 항목 목록(있으면)
