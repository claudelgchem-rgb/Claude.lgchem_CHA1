# PCEA — Patent Claim Extraction & Analysis Harness

> # ⛔ 불변 규칙 (THE ONE RULE)
> **청구항 원문(verbatim)은 파이프라인의 어떤 단계에서도 변형·번역·요약·교정·
> 재배열·재번호화되지 않는다.** 문장부호, 세미콜론, 줄 구조, 오타까지 있는 그대로
> 보존한다. 분석은 원문 위에 **덧붙일** 뿐, 절대 원문을 대체하지 않는다.
> 이 규칙을 어기는 순간 그 결과물은 실패다.

---

## 1. 목적
특허 청구항을 **원문 그대로(verbatim)** 추출하고, **독립 재수집 + 코드 기반 diff** 로
검증한 뒤, 검증된 청구항만 분석·통합해 사람이 검토할 수 있는 보고서(MD + DOCX)를
만드는 다중 에이전트 하니스. 핵심 가치는 *권리범위를 바꿀 수 있는 단 한 글자의 차이도
놓치지 않는 것* 이다.

---

## 2. 8대 설계 철학 (모든 에이전트 준수)
1. **Verbatim 원칙은 신성불가침이다.** 청구항은 이해·요약·번역·교정·재정렬하지 않고
   글자 단위로 복사한다. "더 읽기 좋게" 손대면 실패다.
2. **분석과 원문은 물리적으로 분리한다.** `[VERBATIM]` 과 `[ANALYSIS]` 는 같은 블록에
   섞이지 않는다.
3. **검증은 독립 재수집으로 한다.** 검증자는 추출 결과를 신뢰하지 않고 출처를 다시,
   가능하면 다른 소스로 가져와 비교한다.
4. **사람이 아니라 코드가 비교한다.** 일치 판정은 `scripts/claim_diff.py`(Python
   difflib)로 한다. 한 글자라도 다르면 MISMATCH.
5. **Recall over Precision.** 의심스러우면 고치지 말고 휴먼 리뷰 큐로 플래그한다.
   쉼표 하나, `comprising` vs `consisting` 하나가 권리범위를 바꾼다.
6. **Provenance 는 항상 따라다닌다.** 모든 청구항에 특허번호·출처 URL·출처 유형·
   수집 시각이 붙는다.
7. **각 단계는 검사 가능한 산출물(JSON+MD)을 남기고 독립 재실행 가능하다.**
8. **증강이지 대체가 아니다.** 모든 플래그는 최종적으로 사람에게 노출된다.

---

## 3. 파이프라인 흐름도
```
input/patents.yaml
      │  (orchestrator: 모드 판정 + manifest 초기화)
      ▼
[discovery 모드만] patent-discovery ──► work/00_discovery/candidates.{json,md}
      │
      ▼  (특허별 루프)
metadata-collector ──► work/01_metadata/<id>.json
      ▼
claim-extractor   ──► work/02_extracted/<id>.{json,md}      ★verbatim 복사
      ▼
claim-verifier    ──► work/03_verified/<id>.{json,md}       ★독립 재수집 + claim_diff.py
      │   ├─ verified ───────────► Gate 1 통과 (청구항 확정)
      │   └─ needs_rework/unverifiable ─► claim-extractor 재시도(≤retry_limit)
      │                                   실패 시 _review_queue/ + "미검증" 유지
      ▼  (모든 특허 정리 후)
claim-analyst     ──► output/patent_claims_report.md        ★검증본만 + ⚠미검증 포함
      ▼
compilation-reviewer ─► work/04_analysis/compilation_review.{json,md}  Gate 2
      │   └─ needs_revision ─► claim-analyst 재생성(≤retry_limit)
      ▼  (approved)
docx 변환 (docx 스킬 경유) ──► output/patent_claims_report.docx
      ▼
manifest 요약 출력
```

**품질 게이트**
- **Gate 1**: claim-verifier 가 `verified` 를 주기 전엔 그 특허 청구항을 "확정"으로 표시하지 않는다.
- **Gate 2**: compilation-reviewer 가 `approved` 를 주기 전엔 최종 산출물을 `complete` 로 표시하지 않는다.

---

## 4. 에이전트 1줄 요약
| 에이전트 | 역할 |
|---|---|
| `orchestrator` | 전 단계 조율·게이트·재시도·에스컬레이션·manifest 갱신. 청구항은 안 만진다. |
| `patent-discovery` | (discovery 모드) 주제→후보 특허 발견. 번호 추측 금지, confidence 표기. |
| `metadata-collector` | 서지정보(번호/상태/만료/패밀리 등) 수집. 미확인은 "확인불가". |
| `claim-extractor` | ★ 청구항 verbatim 복사. 이해·번역·교정 금지. 추측 금지. |
| `claim-verifier` | ★ 독립 재수집 + `claim_diff.py` 문자 단위 비교. PASS/MISMATCH/MISSING/FABRICATED. |
| `claim-analyst` | 검증본만 통합·분석. 원문 불변, 분석은 추가만. 미검증은 ⚠ 배지로 포함. |
| `compilation-reviewer` | Gate 2. 누락/드리프트(claim_diff 재확인)/혼입/일관성 검사. 직접 수정 금지. |

---

## 5. 입력 모드
- **모드 A — explicit**: `mode: explicit` + `patents:` 리스트. discovery 단계 건너뜀.
- **모드 B — discovery**: `mode: discovery` + `query` + `filters`. patent-discovery 가 후보 수집.
- 공통 `config`: `output_language`, `preferred_sources`, `retry_limit`.
- 입력 파일 예시/주석: `input/patents.yaml` 참조.

---

## 6. 실행법
```
/run-patent-analysis [입력yaml경로]   # 생략 시 input/patents.yaml
```
- orchestrator 를 기동해 전체 파이프라인을 끝까지 돌리고, 끝에 manifest 요약
  (특허 수 / PASS / 리뷰 큐 / 실패 / 산출물 경로)을 출력한다.

---

## 7. 리뷰 큐(휴먼 인 더 루프) 처리 방법
- 위치: `work/_review_queue/`.
- 들어오는 경우: 추출 실패/페이월(`<id>__extraction.md`), 검증 MISMATCH/MISSING/
  FABRICATED(`<id>__verify.md`), 검증불가(unverifiable), 컴파일 리뷰 잔여 이슈.
- 처리: 사람이 해당 파일의 diff/사유를 보고 (a) 올바른 원문을 확인해 재추출 트리거,
  또는 (b) 출처 한계를 인정하고 "미검증" 으로 보고서에 남길지 결정한다.
- **미검증 특허는 절대 드롭하지 않는다.** 보고서에 `⚠ 미검증` 배지로 포함된다.

---

## 8. 빌드 중 내린 기본값 결정 (Decision Log)
- **출처 우선순위**: `google_patents → espacenet → uspto_ppubs → kipris`
  (yaml `config.preferred_sources` 기본값). 추출은 1순위부터, 검증은 가능하면 다른 소스로 교차.
- **출력 언어**: `ko` (분석 산문만. **청구항 원문은 절대 번역하지 않음**).
- **retry_limit**: `2` (추출 재시도·analyst 재생성 공통 상한).
- **diff 정책**: 정규화 없음. 공백·문장부호·줄바꿈·대소문자 모두 비교 대상.
  (`scripts/claim_diff.py` 는 `newline=''` 으로 줄바꿈까지 보존)
- **검증 상태값**: 청구항 단위 `PASS|MISMATCH|MISSING|FABRICATED`,
  특허 단위 verdict `verified|needs_rework|unverifiable`.
- **manifest 상태값**: 단계별 `pending|done|partial|skipped|needs_review|failed`.
- **claim_type/depends_on**: 의미 해석 없이 "claim N"/"청구항 제N항" 참조 문자열로만
  기계적 판정. 애매하면 비우고 리뷰 큐로.
- **docx 생성**: 반드시 `/mnt/skills/public/docx/SKILL.md` 를 먼저 읽고 그 방식으로 생성.
  [VERBATIM] 은 인용/모노스페이스 블록으로 분석과 시각 구분, 표지에 특허 수/검증·미검증/생성일.
- **미검증 특허**: 분석에서 제외하지 않고 `⚠ 미검증` 배지로 보고서에 포함(누락 방지).

---

## 9. 디렉토리 구조
```
pcea-harness/
├── CLAUDE.md                       # (이 파일) 프로젝트 메모리 + 런북 + 결정 기록
├── .claude/
│   ├── agents/                     # 7개 서브에이전트
│   └── commands/run-patent-analysis.md
├── scripts/claim_diff.py           # verbatim 일치 판정용 실제 diff
├── input/patents.yaml              # 입력(두 모드 예시 포함)
├── work/                           # 단계별 산출물 + manifest + 리뷰 큐
│   ├── 00_discovery/ 01_metadata/ 02_extracted/ 03_verified/ 04_analysis/
│   ├── _review_queue/              # 휴먼 인 더 루프 플래그
│   └── manifest.json               # 파이프라인 상태 추적
└── output/
    ├── patent_claims_report.md
    └── patent_claims_report.docx
```
