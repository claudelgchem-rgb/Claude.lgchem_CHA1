# mTG-RESEARCH — 가교제 리서치 하니스 (실런트·지혈재·조직접착제)

> # ⛔ 불변 규칙 (THE ONE RULE)
> **모든 주장(claim)은 근거·출처·신뢰도·검증상태를 달고 원장(ledger)에 적재된다.
> 출처 없는 주장, 검증되지 않은 단정, "일반적으로 알려진 사실"에 기댄 결론은
> 실패다.** 결론(Q1/Q2/Q3 답)은 원장에 적재된 검증 claim 위에서만 합성한다.
> 근거가 없으면 "근거 불충분"으로 남기고 리뷰 큐로 보낸다. 지어내지 않는다.

---

## 1. 목적
실런트·지혈재·조직접착제 산업의 **가교 화학**을 근거 기반으로 규명하고, 그 지배
기술 대비 **mTG(미생물 transglutaminase)** 의 우열과 잠재력을 다축으로 분석해,
사람이 검토 가능한 HTML 보고서(`report/index.html`)를 만드는 다중 에이전트 하니스.
산출물의 신뢰성은 *모든 문장이 추적 가능한 출처를 갖는다* 는 데서 나온다.

## 2. 리서치 목표 (세 질문 = 최종 산출물)
- **Q1**: 업계에서 가교제로 가장 많이 쓰이는 물질/화학은? (시판제품·규제승인·시장점유 근거로 1위 규명)
- **Q2**: 그 대표 가교제 대비 mTG의 장단점 (9축: 겔화·강도·세포독성·혈액의존·면역원성·분해·GMP공급·규제·비용)
- **Q3**: mTG의 기술적 잠재력 (효소공학 변이체·이중가교·biomimetic 응고·적응증 적합·공급 스케일업)

각 답은 claim 단위로 분해해 근거·출처·신뢰도와 함께 `ledger/claims.jsonl` 에 적재.

## 3. 6대 설계 철학 (모든 에이전트 준수)
1. **Claim-first.** 모든 발견은 원자적 claim 으로 쪼갠다. 한 claim = 한 검증 가능한 주장.
2. **출처 없으면 claim 아니다.** 최소 1개(高신뢰는 2+) URL 출처. 규제/메타분석 > 논문 > 시장/제조사 > 2차보도.
3. **가설은 근거로만 확정.** 후보 가교제 목록·"1위" 예상은 가설일 뿐. 근거로 확정/기각/확장.
4. **적대적 검증.** 핵심 claim 은 반증 시도로 검증(confirmed/plausible/refuted/unverified). 편향 출처(제조사)는 감점.
5. **양면 보존.** Q2 는 mTG 의 장점만도 단점만도 아니다. 축마다 pro/con 모두 수집.
6. **증강이지 대체가 아니다.** 근거 불충분/상충은 숨기지 않고 리뷰 큐 + 보고서에 노출.

## 4. 파이프라인 흐름
```
input/research_spec.yaml
      │  (orchestrator: manifest 초기화, 후보/축/방면 로드)
      ▼
[00] landscape-scout ×N  ──► work/00_landscape/<topic>.json   후보별 시판·규제·시장 근거
      ▼
[01] evidence-collector  ──► work/01_evidence/<Q>.jsonl        Q1 랭킹 / Q2 9축 / Q3 방면 claim
      ▼
[02] claim-verifier      ──► work/02_verified/<Q>.jsonl        핵심 claim 독립 재수집·적대 검증  [Gate 1]
      ▼   (검증본 병합)     ──► ledger/claims.jsonl
      ▼
[03] synthesizer         ──► work/03_synthesis/answers.json    세 질문 결론 합성           [Gate 2]
      ▼
scripts/build_report.py  ──► report/index.html                 ★목표 산출물
```

**게이트**
- **Gate 1**: verifier 가 status 를 주기 전엔 claim 을 결론 근거로 인용하지 않는다. refuted 는 원장에 남기되 결론에서 배제.
- **Gate 2**: answers.json 은 Q1 랭킹 근거 + Q2 양면 + Q3 방면 커버를 만족해야 complete.

## 5. 에이전트 1줄 요약
| 에이전트 | 역할 |
|---|---|
| `orchestrator` | 전 단계 조율·게이트·manifest 갱신·리뷰 큐 관리. claim 내용은 판정만, 창작 안 함. |
| `landscape-scout` | 후보 가교제 1종의 시판제품/규제승인/적응증/시장 근거 수집 → 구조화. |
| `evidence-collector` | 질문(Q)별 근거를 원자적 claim 으로 수집. Q2 는 9축, Q3 는 5방면 모두 커버. |
| `claim-verifier` | 핵심 claim 독립 재수집 + 반증 시도. status/note 부여. 편향 출처 감점. |
| `synthesizer` | 검증 원장 위에서 Q1/Q2/Q3 결론 합성. 근거 없으면 "불충분"으로 명시. |

## 6. 실행법
```
/run-mtg-research [research_spec.yaml 경로]   # 생략 시 input/research_spec.yaml
```
orchestrator 가 파이프라인을 끝까지 돌려 `report/index.html` 을 만들고, 끝에
manifest 요약(claim 수 / 검증완료 / 리뷰 큐 / 산출 경로)을 출력한다.

## 7. 원장 스키마 (ledger/claims.jsonl, 1줄=1claim)
```json
{"id":"Q1-C001","question":"Q1","topic":"fibrin","axis":null,"avenue":null,
 "stance":"finding","claim":"...","evidence":"...",
 "sources":[{"title":"...","url":"...","type":"regulatory"}],
 "confidence":"high","verification":{"status":"confirmed","note":"..."},
 "collected_at":"2026-07-01"}
```
- `question`: Q1|Q2|Q3 · `topic`: 가교 화학 · `axis`(Q2)/`avenue`(Q3): 비교축/방면
- `stance`: pro|con|neutral|finding · `confidence`: high|medium|low
- `verification.status`: confirmed|plausible|refuted|unverified
- `sources[].type`: regulatory|systematic_review|peer_reviewed|market_report|manufacturer|news_secondary|other
- 검증: `python scripts/ledger.py validate ledger/claims.jsonl`

## 8. 리뷰 큐 (휴먼 인 더 루프)
- 위치: `work/_review_queue/`. 들어오는 경우: 출처 상충, 시장수치 교차검증 실패,
  refuted claim, 근거 불충분(unverified). 처리: 사람이 확인 후 재수집 또는 "불충분" 유지.
- **근거 불충분 항목은 드롭하지 않는다.** 보고서에 미검증/낮음 배지로 노출된다.

## 9. 빌드 중 내린 기본값 (Decision Log)
- **출처 가중**: regulatory=FDA 510(k)/PMA·CE·PMDA·라벨 최상위, 그다음 메타분석/논문, 시장/제조사는 편향 보정 후 사용, 2차보도 최하.
- **시장 "1위" 판정**: 단일 시장수치에 의존 금지. (규제 승인 폭 + 적응증 범위 + 임상 사용 관행 + 복수 시장출처) 삼각측량.
- **출력 언어**: ko (제품·규제·화학명은 원어 병기).
- **retry_limit**: 2. **min_sources_per_claim**: 1 (高신뢰 2+).
- **면역원성 논쟁**: mTG 의 조직 tTG(자가항원) 모방/항체 이슈는 상충 근거를 양쪽 다 적재하고 결론은 신뢰도 낮춰 표기.
- **as_of**: 2026-07-01 기준. 이후 승인/출시 변동 가능성 명시.

## 10. 디렉토리 구조
```
mtg-harness/
├── CLAUDE.md                     # (이 파일) 프로젝트 메모리 + 런북 + 결정 기록
├── .claude/
│   ├── agents/                   # 5개 서브에이전트 정의
│   └── commands/run-mtg-research.md
├── scripts/
│   ├── ledger.py                 # 원장 스키마 검증/통계
│   └── build_report.py           # 원장+answers → report/index.html
├── input/research_spec.yaml      # Q1/Q2/Q3, 후보 가교제, 비교축, 방면
├── work/
│   ├── 00_landscape/ 01_evidence/ 02_verified/ 03_synthesis/
│   ├── _review_queue/            # 휴먼 인 더 루프
│   └── manifest.json
├── ledger/claims.jsonl           # ★ claim 단위 근거 원장
└── report/index.html             # ★ 최종 산출물
```
