# icotrokinra (ICOTYDE / JNJ-2113 / PN-235) 특허 청구항 통합 분석 보고서

> **[VERBATIM] 표기 규칙:** 본 보고서에서 코드블록(```)으로 둘러싼 청구항 원문은 권위 소스(authoritative source)인 **Google Patents**의 결정적(deterministic) 파싱 결과 `work/05_gp_authoritative/<id>.md`에서 **한 글자도 수정·번역·정리하지 않고** 그대로 복사한 것이다. OCR/파싱 잔재(예: `Gin`=Gln, `lie`=Ile, `XI 0`=X10, `[Abta]`, 화학구조식이 빠진 빈 청구항 등)도 원문 보존 원칙(THE ONE RULE)에 따라 **그대로** 둔다. 그 위에 덧붙인 한국어 서술은 [ANALYSIS] 블록으로 물리적으로 분리하였으며 청구항 원문과 절대 혼합하지 않는다.

---

## 표지 / 머리말

| 항목 | 내용 |
|---|---|
| 보고서 제목 | icotrokinra (경구 IL-23R 길항 펩타이드) 특허 패밀리 청구항 통합 분석 |
| 분석 대상 약물 | **ICOTYDE / icotrokinra / JNJ-2113 / PN-235** — 경구용 인터루킨-23 수용체(IL-23R) 길항 단환(monocyclic) 펩타이드 |
| 개발 주체 | Protagonist Therapeutics, Inc. + Janssen (Janssen Biotech / Janssen Pharmaceutica NV, J&J 계열) |
| 핵심 물질 정의 | **icotrokinra = SEQ ID NO: 1** (조성물 특허 US11939361B2 / CA3202226A1 / JP2023145581A 패밀리 기준) |
| 후보 총건수 | **27건** (진짜 패밀리 18 + 오귀속 9) |
| 소스 | **2-소스 교차검증**: ① Google Patents (권위 원문, `work/05_gp_authoritative`) ② FreePatentsOnline (FPO, `work/02_extracted`) |
| 교차 비교 방식 | 코드 기반(`scripts/claim_diff.py` 계열) 청구항 단위 substantive diff. 결과: `work/03_verified/_cross_source_GP_vs_FPO.json` |
| 생성일 | **2026-06-16** |

### 후보 27건 분류 요약

| 구분 | 건수 | 비고 |
|---|---|---|
| 진짜 icotrokinra / Protagonist+Janssen 패밀리 | **18건** | 본문 (티어별 정리) |
| 오귀속(misattributed) — icotrokinra 무관 | **9건** | 부록 A |
| **합계** | **27건** | |

> 매니페스트 `genuine_icotrokinra_family` 목록은 19개를 담고 있었으나, 그 중 **US11180535B2**가 검증 단계에서 무관 특허(박테리아 종양침투 키메라 펩타이드, Google Patents 404 + FPO는 박테리아 펩타이드)로 확정되어 부록 A로 이동했다. 따라서 본문(진짜 패밀리)은 **18건**, 부록 A(오귀속)는 **9건**(매니페스트 misattributed 7 + US11180535B2 + 중복분류 정리)이다.

### 교차검증 배지 체계 (NEW — 2-소스 반영)

| 배지 | 의미 |
|---|---|
| ✅교차검증 | GP↔FPO 둘 다 존재하고 청구항 substantive diff == 0 (완전 일치) |
| ☑️부분교차검증 | GP↔FPO 둘 다 존재하나 일부 청구항 substantive diff > 0 (차이 청구항 번호 명시) |
| ⚠️단일소스(GP) | FPO 없음/실패/잘림 → GP 단독 (그래도 권위 소스) |
| ❌오귀속 | icotrokinra 무관 특허 → 부록 A |

---

## Executive Summary

- **icotrokinra = SEQ ID NO: 1**. 가장 강력하게 검증된 권리는 **조성물(composition) 특허 US11939361B2**로, **GP↔FPO 16/16 청구항 완전일치(substantive_diff=0)** ✅교차검증을 통과했다. 이 특허는 SEQ ID NO:1 펩타이드를 0.1~15%(w/w) 함유한 약학 조성물·염/용매화물 형태·흡수촉진제 조합 및 그 치료용도를 청구한다.
- 동일 조성물 패밀리의 **캐나다 대응(CA3202226A1, 153 청구항)**은 이번에 Google Patents로 전체 청구항을 확보했다(이전 파이프라인에서는 FPO 404로 미확보였음). FPO 대응본이 없어 ⚠️단일소스(GP)로 분류하나, US11939361B2와 동일 SEQ ID NO:1 조성물 계열임이 명확하다.
- **속(genus) 특허 패밀리**(출원 17/149,509 및 자매 출원): pre-grant 공개 **US20210261622A1**, 등록본 **US11845808B2**, 자매 **US12018057B2**. 이들은 단환 펩타이드 IL-23R 길항제의 Markush 속/종 청구항을 담는다. 이 중 **US12018057B2**는 GP↔FPO 10/10 완전일치 ✅, US11845808B2는 30개 중 4개 차이 ☑️, US20210261622A1은 (GP가 (canceled) 표기를 포함해 50개 비교 대상에서) 14개 차이 ☑️이다.
- **이전 파이프라인의 최대 공백 2건이 이번에 해소되었다:**
  - **WO2021146441A1** — Google Patents 기준 **전체 186 청구항** 확보(FPO는 167에서 잘려 168~186 누락이었음). 본 보고서는 GP 전문을 [VERBATIM]으로 싣는다.
  - **CA3202226A1** — Google Patents 기준 **153 청구항** 확보(FPO는 추출 실패였음).
- **잔여 공백(부록 B):** **JP2023145581A**(일본 조성물 대응)는 Google Patents `/en` 페이지에 청구항이 실리지 않아(claims=0) **⚠️미확보**이며 J-PlatPat(일본 특허청) 원문 확인이 필요하다.
- **권위 만료일(부록 C):** Google Patents anticipated expiration(출원일+20년, PTE 미반영) 기준 — US11939361B2 = **2041-11-19**, 속 패밀리(US20210261622/US11845808/US12018057) = **2041-01-14**, US12552836B2 = **2039-07-12**, US11041000B2 = **2040-07-09**, US10787490B2 및 PTG-200 계열(US9624268/US10023614/US10941183/US11884748) = **2035-07-15**, lipidated US12478617B2 = **2042-07-14**.
- **PTE 주의:** icotrokinra는 2026-03 FDA 승인 약물이므로, 조성물 특허 **US11939361B2**에는 Hatch-Waxman 특허존속기간연장(PTE, 최대 +5년)이 적용될 수 있다 → **실질 만료 ~2045년까지 가능**(권위 GP 값 2041-11-19은 PTE 미반영 base term).
- **오귀속 9건(부록 A):** Dell 광통신(WO2023212427A1), 다중날 칼(WO2023212432A1), Alector 항체 2건(WO2024026471A1·WO2024026472A1), Zealand Pharma IL-23R 펩타이드(WO2023099669A1 — 경쟁사), Medical Diagnostic Laboratories IL-23R 폴리펩타이드 2건(US9605027B2·USRE49026E1), 박테리아 종양침투 키메라 펩타이드(US11180535B2).

---


## 🔎 한눈에 보기 — 특허별 핵심 요약 (분석층, 원문 위에 부가)

> 아래는 각 특허가 **무엇을 청구/보호하는지** 한 줄로 본 것이다. 청구항 원문은 각 특허 섹션의 `[VERBATIM]`에 변형 없이 그대로 있다. 만료일은 Google Patents anticipated expiration(출원일+20년, PTE/PTA 미반영, WO는 해당없음).

| # | 특허번호 | 유형 | 무엇을 청구/보호하는가 (요지) | 독립항 | 검증 | 추정만료 |
|---|---|---|---|---|---|---|
| 1 | **US11939361B2** | formulation, composition, use | icotrokinra(SEQ ID NO:1) 또는 그 염/용매화물을 조성물의 약 0.1~15%(또는 0.1~20%)(w/w)로 함유하는 의약조성물(제형) 자체와 그 염증질환 치료방법을 청구 | 1,11 | ✅교차검증 | 2041-11-19 |
| 2 | **CA3202226A1** | formulation, composition, use | icotrokinra(SEQ ID NO:1)를 0.1~15%(w/w)로 함유하고 sodium caprate 흡수촉진제·내상/외상 구조·SMCC·장용코팅을 갖춘 경구 정제 조성물과 제조방법, 그리고 혈액·피부·연… | 1,20,66,67,68,76,77,80,81,94,95,104,109,118,123,132,137,146,151 | ⚠️단일소스(GP) | 2041-11-19 |
| 3 | **WO2021146441A1** | compound, composition, use | IL-23 수용체에 결합하는 단환(monocyclic) 펩타이드 저해제 자체를 Formula (I) Markush 구조로 청구하고(X4-X9 디설파이드/티오에터 고리화), 그 펩타이드 이량체, 의약조성물, IB… | 1,36,44,47,52,183 | ☑️부분교차검증(차이75) | PCT(term N/A) |
| 4 | **US20210261622A1** | compound | WO2021146441과 동일 계열의 단환 IL-23R 펩타이드 저해제를 Formula (I) Markush로 청구(공개 출원); X4-X9 디설파이드/티오에터 고리화 및 IL-23/IL-23R 결합 저해를 명시 | 1 | ☑️부분교차검증(차이14) | 2041-01-14 |
| 5 | **US11845808B2** | compound, use | icotrokinra(SEQ ID NO:1)를 포함하는 좁은 단환 펩타이드 화학식(Formula I: X3-Pen-N-T-X7-Lys(Ac)-Pen-X10-2Nal-X12-E-N-X15-Sarc, X15=3Pa… | 1,5 | ☑️부분교차검증(차이4) | 2041-01-14 |
| 6 | **US12018057B2** | compound, composition, use | Pen-Pen 디설파이드 고리화된 특정 IL-23R 펩타이드 화합물군(SEQ ID NO:3~137에서 열거된 개별 서열)을 청구하고, 그 의약조성물 및 IBD·UC·CD·건선·PsA 등 치료방법을 청구 | 1 | ✅교차검증 | 2041-01-14 |
| 7 | **US12552836B2** | compound, composition | 8잔기 코어 Formula (II)(Pen-X5-T-W(alkyl)-X8-Pen-Phe(아미노에톡시)-Nal)로 정의되는 단환 IL-23R 펩타이드 저해제 자체와 그 의약조성물(장용코팅 포함)을 청구 | 1 | ✅교차검증 | 2039-07-12 |
| 8 | **US11041000B2** | compound, composition | Formula (Z') 단환 IL-23R 펩타이드 저해제(X4=Pen, X5=Asn, X6=Thr, X7=alkyl 치환 Trp, X9=Pen, 두 Pen 간 디설파이드)와 그 의약조성물을 청구 | 1 | ☑️부분교차검증(차이9) | 2040-07-09 |
| 9 | **US10787490B2** | compound, use | PEG화·지질화(Palm/Octanyl/isoGlu 등) 변형을 포함하는 특정 IL-23R 펩타이드 저해제(SEQ ID NO:1115~1206 열거)를 청구하고, IBD(UC/CD) 치료방법을 청구 | 1 | ☑️부분교차검증(차이4) | 2035-07-15 |
| 10 | **US9624268B2** | compound, composition | IL-23R 단환 펩타이드 저해제를 20잔기 Formula Ir 및 Xa의 광범위 초기 Markush로 청구(X4-X9 고리화)하고, 다수 개별 SEQ 화합물과 의약조성물까지 청구(PTG-200 계열 기초 물질특허) | 1,11,19,24 | ⚠️단일소스(GP) | 2035-07-15 |
| 11 | **US10023614B2** | compound, composition | Formula (Xa)로 좁혀진 IL-23R 단환 펩타이드 저해제(X4=Pen, X6=Thr, X7=Trp, X8=Gln, X9=Pen 디설파이드)와 일부 이량체(DIG 링커) 화합물 및 그 의약조성물을 청구 | 1,21 | ⚠️단일소스(GP) | 2035-07-15 |
| 12 | **US10941183B2** | use, compound | X4=Abu·X9=Cys 티오에터 고리화 단환 IL-23R 펩타이드 저해제를 투여해 염증성 장질환(IBD)을 치료하는 방법을 청구(용도·치료방법 특허) | 1 | ⚠️단일소스(GP) | 2035-07-15 |
| 13 | **WO2016011208A1** | compound, composition, use | IL-23R 단환 펩타이드 저해제를 20잔기 Formula (Xa)의 매우 광범위한 1세대 Markush(X4-X9 고리화)로 청구하고, 펩타이드 이량체·의약조성물·IBD/건선 등 치료방법·DSS/TNBS 평가… | 1,36,44,47,52 | ⚠️단일소스(GP) | PCT(term N/A) |
| 14 | **US12478617B2** | compound, composition, use | 구조식 군에서 선택되는 특정 IL-23 수용체 저해제 화합물(claim 1) 자체와 그 의약조성물, IL-23/IL-23R 관련 질환·IBD·UC·CD·PsO·PsA 치료방법을 청구 | 1,24,25,26,27,28,29,30 | ✅교차검증 | 2042-07-14 |
| 15 | **US20240173309A1** | compound, composition, use | 구조식 군에서 선택되는 특정 IL-23 수용체 저해제 화합물(claim 23) 자체와 그 의약조성물, 그리고 IL-23/IL-23R 관련 질환·IBD·UC·CD·PsO·PsA 각각의 치료방법을 청구 | 23,46,47,48,49,50,51,52 | ✅교차검증 | 2042-07-14 |
| 16 | **WO2023288019A2** | compound, composition, use | Formula I~X의 광범위 Markush 및 Table 1·실시예로 정의되는 IL-23R 저해 펩타이드(7MeW 등 다양한 비천연 Trp 치환, AEF, THP, 3Pya, 지질/PEG 변형 포함)와 그 의… | 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,19 | ☑️부분교차검증(차이5) | PCT(term N/A) |
| 17 | **WO2024155552A1** | formulation, compound, use | 지질화(lipidated) IL-23R 펩타이드와 흡수촉진제를 함유하는 경구 제형(claim 1) 및 그 펩타이드 구조(Formula A/B, 단일·이중고리, 3Pya 고정, PEG/지질 치환)와 흡수촉진제 비… | 1,69,73,76 | ☑️부분교차검증(차이19) | PCT(term N/A) |
| 18 | **JP2023145581A** | formulation, composition, use | CA3202226과 동일 내용의 일본 출원으로, SEQ ID NO:1(icotrokinra)을 0.1~15%(w/w)로 함유하는 경구 제형(카프린산나트륨 흡수촉진제·SMCC·장용코팅)과 그 치료·IL-23R 억… | — | ⚠️부분(번호불확실) | 2043-07-24 |

**패밀리 큰 그림:** 이 패밀리는 Protagonist/Janssen 계열의 경구 IL-23 수용체 길항 펩타이드(최종 후보 icotrokinra = JNJ-77242113 = SEQ ID NO:1, Ac-[Pen]*-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]*-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3-Pal]-Sarc-NH2)를 여러 층으로 둘러싸 보호한다. (1) 물질층: 초기 광범위 Markush(WO2016011208 = PTG-200 세대, US9624268/US10023614)부터 단환(monocyclic) IL-23R 펩타이드 화학종을 청구하고, 이후 WO2021146441/US20210261622로 3-Pal·Sarc 등 C-말단 한정을 도입해 icotrokinra 구조군으로 좁혀 들어간다. (2) 화학종 확정층: US11845808은 icotrokinra(SEQ ID NO:1)를 포함하는 좁은 단환 화학식과 개별 SEQ를 직접 청구하고, US12552836·US11041000·US10787490·US12018057·US12478617·US20240173309은 특정 SEQ/구조 화합물군을 청구한다. (3) 조성물·제형층: US11939361·CA3202226·JP2023145581은 SEQ ID NO:1을 0.1~15%(w/w)로 함유하고 sodium caprate 흡수촉진제·SMCC·장용코팅을 갖춘 경구 정제 제형(내상/외상 구조)을 청구한다. (4) 용도·치료방법층: 위 물질·조성물을 IBD·UC·CD·건선(PsO)·건선성관절염(PsA) 치료, 그리고 혈액·피부·연골·활막·소화관 조직에서 IL-23R 차단 및 IL-17A/F·IL-22 생성 억제에 사용하는 방법을 청구한다. (5) 차세대 확장층: WO2023288019·WO2024155552는 지질화(lipidated)·이중고리·PEG화 변형 펩타이드와 그 경구 제형으로 권리범위를 확장한다. 종합하면 동일 분자를 물질→화학종→염/형태(아세테이트·무정형)→제형→용도→차세대 변형 순으로 다단계 중첩 보호하는 전형적 패밀리이다.

---

## 제1장. 진짜 icotrokinra 패밀리 — 티어별 정리

### 티어 1 — 조성물(Composition) 특허 (icotrokinra = SEQ ID NO:1 직접 권리, 최우선)

#### 1.1 US11939361B2 ✅교차검증 (GP↔FPO 16/16 완전일치, substantive_diff=0)

> **💡 핵심 요약** &nbsp;|&nbsp; **유형:** formulation(제형), composition(조성물), use·치료방법
> 
> **무엇을 청구하나:** icotrokinra(SEQ ID NO:1) 또는 그 염/용매화물을 조성물의 약 0.1~15%(또는 0.1~20%)(w/w)로 함유하는 의약조성물(제형) 자체와 그 염증질환 치료방법을 청구
> 
> **핵심 권리범위:** SEQ ID NO:1 함량 0.1~15%(w/w) 및 0.1~20%(w/w); 아세테이트 염·무정형(amorphous) 형태; 흡수촉진제 약 10~60%(w/w) 포함 옵션; 펩타이드 절대량 1~1000mg / 10~300mg / 25~150mg 등
> 
> **독립항:** 1, 11 &nbsp;|&nbsp; **적응증:** 염증성 질환(inflammatory disease) &nbsp;|&nbsp; **검증:** ✅교차검증 &nbsp;|&nbsp; **추정만료:** 2041-11-19


| 항목 | 내용 |
|---|---|
| 특허번호 | US11939361B2 (등록, B2) |
| 제목 | Compositions of peptide inhibitors of Interleukin-23 receptor |
| 출원번호 / 출원일 | 17/531,538 / 2021-11-19 |
| 우선일 | 2020-11-20 (US Provisional 63/116,568); 추가 63/275,222 (2021-11-03) |
| 등록일 | 2024-03-26 |
| 출원인/양수인 | Janssen Pharmaceutica NV; Protagonist Therapeutics, Inc. |
| 패밀리 | CA3202226A1, JP2023145581A (동일 제목 조성물 패밀리) |
| 권위 만료일 | **2041-11-19** (GP anticipated expiration; 출원일+20년, PTE 미반영) — FDA 승인 약물이므로 Hatch-Waxman PTE 최대 +5년 시 ~2045 가능 |
| 교차검증 | GP=16, FPO=16, both=16, agree=16, **substantive_diff=0** → ✅완전일치 |

**[ANALYSIS] (한국어)**

icotrokinra 권리의 **핵심(crown jewel)**. SEQ ID NO:1 펩타이드(또는 그 약학적으로 허용되는 염/용매화물)를 조성물 대비 약 0.1~15%(w/w) 함유하는 약학 조성물을 직접 청구한다(청구항 1). 종속항은 화학구조 한정·아세테이트 형태·무정형(amorphous) 형태(청구항 2~4), 함량 범위(1~1000mg, 10~300mg, 25~150mg; 청구항 5~7), 흡수촉진제 (absorption enhancer) 10~60%(w/w) 조합(청구항 8~9), 그리고 염증성 질환 치료방법(청구항 10, 16)으로 확장된다. 청구항 11~15는 0.1~**20%**(w/w) 범위의 또 다른 조성물 군이다(청구항 1의 15% 상한과 구별되는 별도 독립항).

**검증 의의:** 본 특허는 이번 2-소스 비교에서 GP와 FPO가 16개 청구항 전부 substantive diff 0으로 **완전일치**했다. 즉 어느 한 소스의 파싱 오류 가능성이 양쪽 독립 수집에서 상호 배제되어, 청구항 원문 신뢰도가 가장 높다. icotrokinra 물질 자체가 SEQ ID NO:1로 고정되므로 이 조성물 청구항은 약물의 시장 독점과 직결된다.

**[VERBATIM] — 출처: Google Patents (`work/05_gp_authoritative/US11939361B2.md`)**

```text
1. A pharmaceutical composition comprising: a peptide of SEQ ID NO: 1 or a pharmaceutically acceptable salt or solvate form thereof in an amount of from about 0.1% to about 15% (w/w) of the pharmaceutical composition; and one or more pharmaceutically acceptable excipients.

2. The pharmaceutical composition of claim 1, wherein the peptide of SEQ ID NO: 1 or a pharmaceutically acceptable salt or solvate form thereof, has the chemical structure: and wherein the peptide of SEQ ID NO: 1 or a pharmaceutically acceptable salt or solvate form thereof is a pharmaceutically acceptable salt form.

3. The pharmaceutical composition of claim 1, wherein the peptide of SEQ ID NO: 1 or a pharmaceutically acceptable salt or solvate form thereof is an acetate form.

4. The pharmaceutical composition of claim 3, wherein the acetate form is in an amorphous form.

5. The pharmaceutical composition of claim 1, wherein the amount of the peptide of SEQ ID NO: 1 or a pharmaceutically acceptable salt or solvate form thereof is from about 1 mg to about 1000 mg.

6. The pharmaceutical composition of claim 1, wherein the amount of the peptide of SEQ ID NO: 1 or a pharmaceutically acceptable salt or solvate form thereof is from about 10 mg to about 300 mg.

7. The pharmaceutical composition of claim 1, wherein the amount of the peptide of SEQ ID NO: 1 or a pharmaceutically acceptable salt or solvate form thereof is from about 25 mg to about 150 mg.

8. The pharmaceutical composition of claim 1, wherein the pharmaceutical composition further comprises an absorption enhancer.

9. The pharmaceutical composition of claim 8 comprising: a peptide of SEQ ID NO: 1 or a pharmaceutically acceptable salt or solvate form thereof in an amount of from about 0.1% to about 15% (w/w) of the pharmaceutical composition; an absorption enhancer in an amount from about 10% to about 60% (w/w); and one or more pharmaceutically acceptable excipients.

10. A method of treating an inflammatory disease in a subject comprising administering to the subject a therapeutically effective amount of a pharmaceutical composition of claim 1.

11. A pharmaceutical composition comprising: a peptide of SEQ ID NO: 1 or a pharmaceutically acceptable salt or solvate form thereof in an amount of from about 0.1% to about 20% (w/w) of the pharmaceutical composition; and one or more pharmaceutically acceptable excipients.

12. The pharmaceutical composition of claim 11, wherein the peptide of SEQ ID NO: 1 or a pharmaceutically acceptable salt or solvate form thereof, has the chemical structure: and wherein the peptide of SEQ ID NO: 1 or a pharmaceutically acceptable salt or solvate form thereof is a pharmaceutically acceptable salt form.

13. The pharmaceutical composition of claim 12, wherein the amount of the peptide of SEQ ID NO: 1 or a pharmaceutically acceptable salt or solvate form thereof is from about 1 mg to about 1000 mg.

14. The pharmaceutical composition of claim 13, wherein the amount of the peptide of SEQ ID NO: 1 or a pharmaceutically acceptable salt or solvate form thereof is from about 10 mg to about 500 mg.

15. The pharmaceutical composition of claim 14, wherein the amount of the peptide of SEQ ID NO: 1 or a pharmaceutically acceptable salt or solvate form thereof is from about 10 mg to about 300 mg.

16. A method of treating an inflammatory disease in a subject comprising administering to the subject a therapeutically effective amount of a pharmaceutical composition of claim 11.
```

---

#### 1.2 CA3202226A1 ⚠️단일소스(GP) — 공백 해소 (153 청구항 신규 확보)

> **💡 핵심 요약** &nbsp;|&nbsp; **유형:** formulation(제형), composition(조성물), use·치료방법
> 
> **무엇을 청구하나:** icotrokinra(SEQ ID NO:1)를 0.1~15%(w/w)로 함유하고 sodium caprate 흡수촉진제·내상/외상 구조·SMCC·장용코팅을 갖춘 경구 정제 조성물과 제조방법, 그리고 혈액·피부·연골·활막·소화관에서 IL-23R 차단 및 IL-17A/F·IL-22 억제 치료방법을 광범위 청구
> 
> **핵심 권리범위:** SEQ ID NO:1 0.1~15%(w/w), 아세테이트/무정형, 1.8% 또는 7.1% 등 구체 처방; sodium caprate 흡수촉진제 약 20~50%(w/w), 순도 ≥98%; 내상(internal phase)/외상(external phase) + SMCC HD90 + 서브코팅(PVA-PEG)/장용코팅; 경구 투여, 10/25/50mg 1일 1~2회 용량, IL-23R 및 IL-17A/F·IL-22 억제
> 
> **독립항:** 1, 20, 66, 67, 68, 76, 77, 80, 81, 94, 95, 104, 109, 118, 123, 132, 137, 146, 151 &nbsp;|&nbsp; **적응증:** IBD/크론병/궤양성대장염/건선/건선성관절염(중등도~중증) &nbsp;|&nbsp; **검증:** ⚠️단일소스(GP) &nbsp;|&nbsp; **추정만료:** 2041-11-19


| 항목 | 내용 |
|---|---|
| 특허번호 | CA3202226A1 (캐나다 공개, A1) |
| 제목 | Compositions of peptide inhibitors of interleukin-23 receptor |
| 출원일 / 공개일 | 2021-11-19 / 2022-05-27 |
| 우선일 | 확인불가 (CA 소스 미확인; US 자매 US11939361B2는 2020-11-20 우선) |
| 출원인/양수인 | Janssen Pharmaceutica NV; Protagonist Therapeutics, Inc. |
| 패밀리 | US11939361B2 (동일 조성물), JP2023145581A |
| 권위 만료일 | 추정 2041-11-19 (출원일+20년; PTA/PTE 미반영) |
| 교차검증 | GP=153, FPO=0(추출 실패) → ⚠️단일소스(GP). 이전 파이프라인 공백 해소. |

**[ANALYSIS] (한국어)**

이전 파이프라인에서 FPO가 404를 반환해 청구항 0건으로 **미확보**였던 캐나다 조성물 대응본을, 이번에 Google Patents에서 **전체 153 청구항**으로 확보했다. 청구항 1은 US11939361B2와 동일하게 **SEQ ID NO:1 펩타이드를 0.1~15%(w/w) 함유한 조성물**을 청구하여, 본 캐나다 출원이 icotrokinra 조성물 패밀리의 정규 구성원임을 원문으로 확인한다. 다만 캐나다 단일 소스(GP)만 확보되어 교차검증 등급은 ⚠️단일소스(GP)로 둔다. 153개 청구항은 분량이 크므로 전문을 아래 [VERBATIM]에 그대로 싣는다(화학구조식이 텍스트로 깨진 부분도 원문 보존).

**[VERBATIM] — 출처: Google Patents (`work/05_gp_authoritative/CA3202226A1.md`)**

```text
1. A composition comprising:a peptide of SEQ ID NO: 1 or a pharmaceutically acceptable salt or solvate form thereof in an amount of from about 0.1% to about 15% (w/w) of the composition; and one or more pharmaceutically acceptable excipients.

2. The composition of claim 1, wherein the peptide of SEQ ID NO: 1 or a pharmaceutically acceptable salt or solvate form thereof, has the chemical structure:HNHN La ,NH HHN, HNO = 0y)cS'sYyLo ,NH HNly H 00/ rsls 11 \ H

3. The composition of claim 1 or 2, wherein the peptide of SEQ ID NO: 1 or a pharmaceutically acceptable salt or solvate form thereof is an acetate form.

4. The composition of claim 3, wherein the acetate form of the peptide of SEQ ID NO: 1 or a pharmaceutically acceptable salt or solvate form thereof is in an amorphous form.

5. The composition of any one of claims 1 to 4, wherein the amount of the peptide of SEQ ID NO: 1 or a pharmaceutically acceptable salt or solvate form thereof is from about 1 mg to about 1000 mg.

6. The composition of any one of claims 1 to 5, wherein the amount of the peptide of SEQ ID NO: 1 or a pharmaceutically acceptable salt or solvate form thereof is from about 10 mg to about 300 mg.

7. The composition of any one of claims 1 to 6, wherein the amount of the peptide of SEQ ID NO: 1 or a pharmaceutically acceptable salt or solvate form thereof is from about 25 mg to about 150 mg.

8. The composition of any one of claims 1 to 7, wherein the amount of the peptide of SEQ ID NO: 1 or a pharmaceutically acceptable salt or solvate form thereof is from about 25 mg to about 100 mg.

9. The composition of any one of claims 1 to 7, wherein the amount of the peptide of SEQ ID NO: 1 or a pharmaceutically acceptable salt or solvate form thereof is about 25 mg.

10. The composition of any one of claims 1 to 7, wherein the amount of the peptide of SEQ ID NO: 1 or a pharmaceutically acceptable salt or solvate form thereof is about 100 mg.

11. The composition of any one of claims 1 to 7, wherein the amount of the peptide of SEQ ID NO: 1 or a pharmaceutically acceptable salt or solvate form thereof is about 150 mg.

12. The composition of any one of claims 1 to 11, wherein the composition further comprises microcrystalline cellulose.

13. The composition of claim 12, wherein the microcrystalline cellulose is in an amount of from about 1% to about 25% (w/w) of the composition.

14. The composition of any one of claims 1 to 13, wherein the composition further comprises a silicified microcrystalline cellulose.

15. The composition of claim 14, wherein the silicified microcrystalline cellulose is in an amount of from about 25% to about 60% (w/w) of the composition.

16. The composition of any one of claims 1 to 15, wherein the composition further comprises one or more of alpha cellulose, beta cellulose, gamma cellulose, starch, modified-starch, sorbitol, mannitol, lactose, dextrose, sucrose, dibasic calcium phosphate, tribasic calcium phosphate, or calcium carbonate.

17. The composition of any one of claims 1 to 16, wherein the composition further comprises sorbitol.

18. The composition of claim 17, wherein the sorbitol is in an amount of from about 5% to about 15% (w/w) of the composition.

19. The composition of any one of claims 1 to 18, wherein the composition further comprises an absorption enhancer.

20. A composition comprising:a peptide of SEQ ID NO: 1 or a pharmaceutically acceptable salt or solvate form thereof in an amount of from about 0.1% to about 15% (w/w) of the composition;an absorption enhancer in an amount from about 10% to about 60%(w/w); and one or more pharmaceutically acceptable excipients.

21. The composition of claim 19 or 20, wherein the absorption enhancer is sodium caprate, sodium caprylate, sodium palmitate, sodium stearate, sodium citrate, sodium salicylate, sodium salcaprozate (SNAC), a polyethylene glycol (PEG)-modified medium chain fatty acid triglyceride of capric and caprylic acid, sucrose laurate, or lauroyl-L-carnitine (LC).

22. The composition of claim 21, wherein the absorption enhancer is sodium caprate.

23. The composition of claim 21, wherein the absorption enhancer is sodium salcaprozate.

24. The composition of claim 21, wherein the absorption enhancer is a polyethylene glycol (PEG)-modified medium chain fatty acid triglyceride of capric and caprylic acid.

25. The composition of any one of claims 19 to 22 comprising:an internal phase comprising:the peptide of SEQ ID NO: 1 or a pharmaceutically acceptable salt or solvate form thereof in an amount of from about 0.1% to about 15% (w/w) of the composition, sodium caprate in an amount of from about 20% to about 45%(w/w) of the composition; and an external phase disposed over the internal phase, wherein the external phase comprises a microcrystalline cellulose.

26. The composition of claim 25, wherein the peptide of SEQ ID NO: 1 or a pharmaceutically acceptable salt or solvate form thereof is present in an amount of from about 1% to about 5% (w/w).

27. The composition of claim 25 or 26, wherein the peptide of SEQ ID NO: 1 or a pharmaceutically acceptable salt or solvate form thereof is present in an amount of about 1.8% (w/w).

28. The composition of any one of claims 25 to 27, wherein the peptide of SEQ ID NO: 1 or a pharmaceutically acceptable salt or solvate form thereof is present in an amount of from about 10 mg to about 50 mg.

29. The composition of any one of claims 25 to 28, wherein the sodium caprate is present in an amount of from about 30% to about 40% (w/w).

30. The composition of any one of claims 25 to 29, wherein the sodium caprate is present in an amount of about 35.7% (w/w).

31. The composition of any one of claims 25 to 30, wherein the sodium caprate has a purity of at least 98%.

32. The composition of any one of claims 25 to 31, wherein the peptide of SEQ ID NO: 1 or a pharmaceutically acceptable salt or solvate form thereof and the sodium caprate form a granulated mixture.

33. The composition of any one of claims 25 to 32, wherein the composition further comprises a disintegrant.

34. The composition of claim 33, wherein the disintegrant is in an amount of from about 1% to about 10% (w/w) of the composition.

35. The composition of any one of claims 25 to 34, wherein the composition further comprises a hydrophilic silica.

36. The composition of claim 35, wherein the hydrophilic silica is in an amount of from about 0.1% to about 1.5% (w/w) of the composition.

37. The composition of any one of claim 25 to 36, wherein the internal phase further comprises at least one of:a disintegrant in an amount from about 1% to about 10% (w/w) of the composition, a microcrystalline cellulose in an amount from about 1% to about 10% (w/w) of the composition, a hydrophilic silica in an amount from about 0.1% to about 1.5% (w/w) of the composition, or sorbitol in an amount from about 5% to about 15% (w/w) of the composition.

38. The composition of any one of claims 25 to 37, wherein the microcrystalline cellulose of the external phase comprises a silicified microcrystalline cellulose (SMCC).

39. The composition of claim 38, wherein the microcrystalline cellulose of the external phase is a silicified microcrystalline cellulose (SMCC).

40. The composition of claim 38 or 39, wherein the silicified microcrystalline cellulose is SMCC 50, SMCC SOLD, SMCC 90, SMCC HD90 or SMCC 9OLM.

41. The composition of any one of claims 38 to 40, wherein the silicified microcrystalline cellulose is present in an amount of from about 25% to about 45% (w/w) of the composition.

42. The composition of any one of claims 25 to 41, wherein the external phase further comprises at least one of:a glidant in an amount from about 0.1% to about 0.5% (w/w) of the composition, a disintegrant in an amount from about 1% to about 10% (w/w) of the composition, or a hydrophilic silica in an amount from about 0.1% to about 1.5% (w/w) of the composition.

43. The composition of any one of claims 1 to 42, wherein the composition is a tablet or capsule composition.

44. The composition of any one of claims 1 to 43, wherein the composition is a tablet composition.

45. The composition of claim 43 or 44, wherein the tablet composition comprises a unit dose size of from about 500 mg to about 2000 mg.

46. The composition of claim 44 or 45, wherein the tablet composition comprises a unit dose size of about 1400 mg.

47. The composition of claim 25, wherein: the internal phase comprises:the acetate form of the peptide of SEQ ID NO: 1 in an amount of about 1.8%(w/w), and sodium caprate in an amount of about 35.7% (w/w); and the external phase comprises:silicified microcrystalline cellulose HD90 in an amount of about 36.6% (w/w).

48. The composition of claim 47, wherein:the internal phase comprises:a granulated mixture of the acetate form of the peptide of SEQ ID NO: 1 in an amount of about 1.8% (w/w), and sodium caprate in an amount of about 35.7% (w/w);a microcrystalline cellulose in an amount of about 3.9% (w/w);sorbitol in an amount of about 10.7% (w/w);a disintegrant in an amount of about 5.0% (w/w); and a hydrophilic silica in an amount of about 0.5% (w/w); and the external phase comprises:a silicified microcrystalline cellulose in an amount of about 36.6% (w/w);a disintegrant in an amount of about 5.0% (w/w);a hydrophilic silica in an amount of about 0.5% (w/w); and a glidant in an amount of about 0.25% (w/w).

49. The composition of claim 48, wherein:the internal phase comprises:a granulated mixture of the acetate form of the peptide of SEQ ID NO: 1 in an amount of about 1.8% (w/w), and sodium caprate in an amount of about 35.7% (w/w);a microcrystalline cellulose in an amount of about 3.9% (w/w);sorbitol in an amount of about 10.7% (w/w);croscarmellose sodium in an amount of about 5.0% (w/w); and colloidal anhydrous silica in an amount of about 0.5% (w/w); and the external phase comprises:a silicified microcrystalline cellulose in an amount of about 36.6% (w/w);croscarmellose sodium in an amount of about 5.0% (w/w);colloidal anhydrous silica in an amount of about 0.5% (w/w); and magnesium stearate in an amount of about 0.25% (w/w).

50. The composition of claim 48, wherein:the internal phase comprises:a granulated mixture of the acetate form of the peptide of SEQ ID NO: 1 in an amount of about 1.8% (w/w), and sodium caprate in an amount of about 35.7% (w/w);Avicel PH101 in an amount of about 3.9% (w/w);sorbitol in an amount of about 10.7% (w/w);croscarmellose sodium in an amount of about 5.0% (w/w); and Aerosil 200 in an amount of about 0.5% (w/w); and the external phase comprises:SMCC HD90 in an amount of about 36.6% (w/w);croscarmellose sodium in an amount of about 5.0% (w/w);Aerosil 200 in an amount of about 0.5% (w/w); and magnesium stearate in an amount of about 0.25% (w/w).

51. The composition of claim 25, wherein:the internal phase comprises:the acetate form of peptide of SEQ ID NO: 1 in an amount of about 7.1%(w/w); and sodium caprate in an amount of about 35.7% (w/w); and the external phase comprises:silicified microcrystalline cellulose HD90 in an amount of about 30.75%(w/w).

52. The composition of claim 25, wherein the internal phase comprises:a granulated mixture of the acetate form of the peptide of SEQ ID NO: 1 in an amount of about 7.1% (w/w), and sodium caprate in an amount of about 35.7% (w/w);a microcrystalline cellulose in an amount of about 3.9% (w/w);sorbitol in an amount of about 10.7% (w/w);a disintegrant in an amount of about 5.0% (w/w);a hydrophilic silica in an amount of about 0.5% (w/w); and a glidant in an amount of about 0.25% (w/w); and the external phase comprises:a silicified microcrystalline cellulose in an amount of about 30.75% (w/w); a disintegrant in an amount of about 5.0% (w/w);a hydrophilic silica in an amount of about 0.5% (w/w); and a glidant in an amount of about 0.5% (w/w).

53. The composition of claim 52, wherein the internal phase comprises:a granulated mixture of the acetate form of the peptide of SEQ ID NO: 1 in an amount of about 7.1% (w/w), and sodium caprate in an amount of about 35.7% (w/w);Avicel PH101 in an amount of about 3.9% (w/w);sorbitol in an amount of about 10.7% (w/w);croscarmellose sodium in an amount of about 5.0% (w/w);Aerosil 200 in an amount of about 0.5% (w/w); and magnesium stearate in an amount of about 0.25% (w/w); and the external phase comprises:SMCC HD90 in an amount of about 30.75% (w/w);a croscarmellose sodium in an amount of about 5.0% (w/w);Aerosil in an amount of about 0.5% (w/w); and magnesium stearate in an amount of about 0.5% (w/w).

54. The composition of claim 25, wherein the internal phase comprises:a granulated mixture of the acetate form of the peptide of SEQ ID NO: 1 in an amount of about 7.1% (w/w), and sodium caprate in an amount of about 35.7% (w/w);microcrystalline cellulose in an amount of about 3.9% (w/w);sorbitol in an amount of about 10.7% (w/w);croscarmellose sodium in an amount of about 5.0% (w/w);colloidal anhydrous silica in an amount of about 0.5% (w/w); and magnesium stearate in an amount of about 0.25% (w/w); and the external phase comprises:silicified microcrystalline cellulose in an amount of about 31.0% (w/w);a croscarmellose sodium in an amount of about 5.0% (w/w); colloidal anhydrous silica in an amount of about 0.5% (w/w); and magnesium stearate in an amount of about 0.25% (w/w).

55. The composition of claim 25, wherein the internal phase comprises:a granulated mixture of the acetate form of the peptide of SEQ ID NO: 1 in an amount of about 10.7% (w/w), and sodium caprate in an amount of about 35.7% (w/w);microcrystalline cellulose in an amount of about 3.9% (w/w);sorbitol in an amount of about 10.7% (w/w);croscarmellose sodium in an amount of about 5.0% (w/w); and colloidal anhydrous silica in an amount of about 0.5% (w/w); and the external phase comprises:silicified microcrystalline cellulose in an amount of about 27.7% (w/w);a croscarmellose sodium in an amount of about 5.0% (w/w);colloidal anhydrous silica in an amount of about 0.5% (w/w); and magnesium stearate in an amount of about 0.25% (w/w).

56. The composition of claim 1, wherein the compostion comprises:the acetate form of peptide of SEQ ID NO: 1 in an amount of about 16.3% (w/w), and sodium caprate in an amount of about 50.0% (w/w).

57. The composition of claim 56, further comprising:a poly(ethylene glycol)-block-poly(propylene glycol)-block-poly(ethylene glycol) in an amount of about 6.0% (w/w);mannitol in an amount of about 15.2% (w/w);a disintegrant in an amount of about 10.0% (w/w);a hydrophilic silica in an amount of about 1.0% (w/w); and a glidant in an amount of about 1.5% (w/w).

58. The composition of claim 57, further comprising:Kolliphor P188 in an amount of about 6.0% (w/w); mannitol in an amount of about 15.2% (w/w); croscarmellose sodium in an amount of about 10.0% (w/w); Aerosil 200 in an amount of about 1.0% (w/w); and magnesium stearate in an amount of about 1.5% (w/w).

59. The composition of claim 1, wherein the internal phase comprises:the acetate form of peptide of SEQ ID NO: 1 in an amount of about 1.8%(w/w), and microcrystalline cellulose in an amount of about 21.3% (w/w);sorbitol in an amount of about 10.7% (w/w);croscarmellose sodium in an amount of about 2.5% (w/w);hydrophilic silica in an amount of about 0.5% (w/w); and magnesium stearate in an amount of about 0.25% (w/w); and the external phase comprises:silicified microcrystalline cellulose HD90 in an amount of about 59.6% (w/w);crocarmellose sodium in an amount of about 2.5% (w/w);hydrophilic silica in an amount of about 0.5% (w/w); and magnesium stearate in an amount of about 0.25% (w/w).

60. The composition of any one of claims 1 to 59, further comprising a subcoating of a PVA-PEG graft co-polymer disposed over the composition.

61. The composition of claim 60, wherein the subcoating is present in an amount from about 1% to about 10% (w/w).

62. The composition of claim 60 or 61, further comprising an enteric coating disposed over the subcoating.

63. The composition of claim 62, wherein the enteric coating is present in an amount from about 1% to about 15% (w/w).

64. The composition of any one of claims 1 to 63, wherein the composition has a bioavailability of at least about 1 to about 10% (w/w).

65. The composition of any one of claims 1 to 63, wherein the composition has a bioavailability in a range from about 10% to about 50% (w/w).

66. A composition comprising: a peptide of SEQ ID NO: 1 or a pharmaceutically acceptable salt or solvate form thereof; and a 50 mM pH 7.4 phosphate buffered aqueous solution.

67. A tablet made by the process of:granulating a mixture comprising:a peptide of SEQ ID NO: 1 or a pharmaceutically acceptable salt or solvate form thereof; and sodium caprate;adding to the granulated mixture:a microcrystalline cellulose;sorbitol;a disintegrant; and a hydrophilic silica, to form an internal phase;compressing an external phase over the internal phase, wherein the external phase comprises a silicified microcrystalline cellulose;applying a subcoating over the external phase; and applying an enteric coating over the subcoating to form a tablet.

68. A method comprising:granulating a mixture comprising:a peptide of SEQ ID NO: 1 or a pharmaceutically acceptable salt or solvate form thereof; and sodium caprate;adding to the granulated mixture:a microcrystalline cellulose;sorbitol;a disintegrant; and a hydrophilic silica, to form an internal phase;compressing an external phase over the internal phase, wherein the external phase comprises a silicified microcrystalline cellulose;applying a subcoating over the external phase; and applying an enteric coating over the subcoating to form a tablet.

69. A method of treating an inflammatory disease in a subject comprising administering to the subject a therapeutically effective amount of a composition according to any one of claims 1 to 66 or a tablet according to claim 67.

70. The method of claim 69, wherein the inflammatory disease is inflammatory bowel disease (IBD), Crohn's disease, ulcerative colitis, psoriasis, or psoriatic arthritis.

71. A method of treating an inflammatory bowel disease (IBD) in a subject in need thereof comprising administering to the subject a therapeutically effective amount of a composition according to any one of claims 1 to 66 or a tablet according to claim 67.

72. The method of claim 71, wherein the IBD is Crohn's disease or ulcerative colitis.

73. Use of a composition of any one of claims 1 to 66 or a tablet according to claim 67 in the manufacture of a medicament for treating an inflammatory bowel diseases (IBD).

74. A method of treating psoriasis or psoriatic arthritis in a subject in need thereof comprising administering to the subject a therapeutically effective amount of a composition according to any one of claims 1 to 66 or a tablet according to claim 67.

75. Use of a composition of any one of claims 1 to 66 or a tablet according to claim 67, in the manufacture of a medicament for treating psoriasis or psoriatic arthritis. 76 A method for IL-23 receptor inhibition for treating inflammatory diseases or disorders by delivering a systemically active peptide Ac-[Pen]*-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]*-Phe[4-(2-aminoethoxy)]-[2-Nal] - [THP]-E-N-[3-Pal]-Sarc-NH2 (*Pen-Pen form disulfide bond) (SEQ ID NO: 1):I HHN N HNOycS,sYyLo H 0 ,1,,'¨NH2 0 0<7,1 Nv_AN IRL,ANThrNH2 ; or a pharmaceutically acceptable salt or solvate form thereof to a patient in need thereof.

77. A method for IL-23 receptor inhibition for treating inflammatory diseases or disorders by delivering a pharmaceutical composition, which comprises:[a] a therapeutically effective amount of a systemically active peptide Ac-[Pen]*-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]*-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N43-Pal]-Sarc-NH2 (*Pen-Pen form disulfide bond) (SEQ ID NO: 1):*I HHN NH2N )2\) õ., Hrsr-O0,ecS,s 0 õNH HN-H 0 ,(NH2 0 001 N\AN 111,.).LN,..iNH.0 o I 0 ; or a pharmaceutically acceptable salt or solvate form thereof;[b] optionally with or without an absorption enhancer; and [c] at least one pharmaceutically acceptable excipient;to a patient in need thereof.

78. The method for IL-23 receptor inhibition for treating inflammatory diseases or disorders according to any one of claims 76 or 77, wherein the systemically active peptide or pharmaceutically acceptable salt thereof or pharmaceutical composition is orally administered.

79. The method for IL-23 receptor inhibition for treating inflammatory diseases or disorders according to any one of claims 76 or 77, wherein the systemically the active peptide compound or a pharmaceutically acceptable salt thereof or corresponding pharmaceutical composition thereof is or delivered directly via or to blood, blood circulation, tissue, skin or joints for the treatment of inflammatory diseases or disorders.

80. A method for systemically inhibiting or pharmacologically blocking:= IL-23 receptor;= IL-23 signalling through IL-23 receptor; or = IL-23 pathway, for treatment of inflammatory diseases or disorders, which comprises orally administering a therapeutically effective amount of a systemically active peptide Ac-[Pen]*-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]*-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3-Pal]-Sarc-NH2 (*Pen-Pen form disulfide bond) (SEQ ID NO: 1):*I HHN N7 0 r HN,õ, 0 101 HN 0 FINI) 1:).ezcS,s=Lo ,NH cal7N\AN kl...,..).LNThr.NH2 0 o HO ; or a pharmaceutically acceptable salt or solvate form thereof to a patient in need thereof.

81. A method for systemically inhibiting or pharmacologically blocking:= IL-23 receptor, = IL-23 signalling through IL-23 receptor; or = IL-23 pathway, for treatment of inflammatory diseases or disorders, which comprises orally administering a pharmaceutical composition, which comprises:[a] a therapeutically effective amount of a systemically active peptide Ac-[Pen]*-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]*-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N43-Pal]-Sarc-NH2 (*Pen-Pen form disulfide bond) (SEQ ID NO: 1): o *I HNHNH2N) H HI;ITOHNOs,sXrc3 õNH 0 ..õ(NH2 H HO oD<IN.1,1,N\AN II , or a pharmaceutically acceptable salt or solvate form thereof [b] optionally with or without an absorption enhancer; and [c] at least one pharmaceutically acceptable excipient to a patient in need thereof

82. The method for systemically inhibiting or pharmacologically blocking according to any one of claims 80 or 81, wherein the inflammatory diseases or disorders are psoriasis, psoriatic arthritis, inflammatory bowel disease, ulcerative colitis or Crohn's disease.

83. The method for systemically inhibiting or pharmacologically blocking according to claim 82, wherein the inflammatory diseases or disorders are characterized as moderate to severe in degree.

84. The method for systemically inhibiting or pharmacologically blocking according to any one of claims 80 or 81, which comprises administering the therapeutically effective amount of the systemically active peptide in a dose range from about 1 mg to about 1000 mg.

85. The method for systemically inhibiting or pharmacologically blocking: according to claim 84, which comprises administering the amount of the systemically active peptide in dose range from about 25 mg to about 100 mg.

86. The method for systemically inhibiting or pharmacologically blocking: according to any one of claims 83 to 85, which comprises administering the amount of the systemically active peptide in specific doses of 10 mg, 25 mg or 50 mg once daily or twice daily as needed.

87. The method for systemically inhibiting or pharmacologically blocking according to any one of claims 83 to 86, which comprises administering 10 mg once daily.

88. The method for systemically inhibiting or pharmacologically blocking according to any one of claims 83 to 86, which comprises administering 10 mg twice daily. 89 The method for systemically inhibiting or pharmacologically blocking according to any one of claims 83 to 86, which comprises administering 25 mg once daily. 90 The method for systemically inhibiting or pharmacologically blocking according to any one of claims 83 to 86, which comprises administering 25 mg twice daily. 91 The method for systemically inhibiting or pharmacologically blocking according to any one of claims 83 to 86, which comprises administering 50 mg once daily. 92 The method for systemically inhibiting or pharmacologically blocking according to any one of claims 83 to 86, which comprises administering 50 mg twice daily. 93 The method for systemically inhibiting or pharmacologically blocking according to any one of claims 80 to 92, wherein after the amount of the systemically active peptide is dosed 50 mg once or twice daily greater than 50 % inhibition over a hour period is observed. 94 A method for inhibition or blocking of IL-23 receptor in blood, blood circulation, tissue, skin or joints for treatment of inflammatory diseases or disorders, which comprises administering:an oral dose of therapeutically effective amount of a peptide Me)]-[Lys(Ac)]-[Pen]*-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3-Pal]-Sarc-(*Pen-Pen form disulfide bond) (SEQ ID NO: 1): FIN HN(10 H2N y ,1 1;) .,,NH 0 ..õ.(N H2 H Hoa,...7sULN , or a pharmaceutically acceptable salt or solvate form thereof. 95 A method for inhibition or blocking of IL-23 receptor in blood, blood circulation, tissue, skin or joints for treatment of inflammatory diseases or disorders, which comprises administering an oral dose of therapeutically effective amount of a pharmaceutical composition, which comprises:[a] a therapeutically effective amount of a systemically active peptide Ac-[Pen]*-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]*-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N43-Pal]-Sarc-NH2 (*Pen-Pen form disulfide bond) (SEQ ID NO: 1);FIN HN )*%\CO'.,,_NH HN w Os,sYyLo .,NH H 0 ,(NH2 ca7rsis H , or a pharmaceutically acceptable salt or solvate form thereof;[b] optionally with or without an absorption enhancer; and [c] at least one pharmaceutically acceptable excipient to a patient in need thereof. 96 The method for inhibition or blocking of IL-23 receptor in blood, blood circulation, tissue, skin or joints for treatment of inflammatory diseases or disorders according to anyone of claims 94 or 95, wherein inhibition or blocking IL-23 receptor (IL23R) occurs in tissues including and beyond the gastrointestinal tract 97 The method for inhibition or blocking of IL-23 receptor in blood, blood circulation, tissue, skin or joints for treatment of inflammatory diseases or disorders according to any one of claims 94 or 95, wherein inflammatory diseases or disorders are selected from psoriasis, psoriatic arthritis, inflammatory bowel disease, ulcerative colitis, or Crohn's disease. 98 The method for inhibition or blocking of IL-23 receptor in blood, blood circulation, tissue, skin or joints for treatment of inflammatory diseases or disorders according to claim 97, wherein inflammatory diseases or disorders are moderate to severe in degree. 99 The method for inhibition or blocking of IL-23 receptor in blood, blood circulation, tissue, skin or joints for treatment of inflammatory diseases or disorders according to anyone of claims 94 to 98, wherein systemic pharmacodynamic activity in blood is directly proportional to the systemic exposure in human subjects.

100. The method for inhibition or blocking of IL-23 receptor in blood, blood circulation, tissue, skin or joints for treatment of inflammatory diseases or disorders according to anyone of claims 94 to 98, wherein level of target blockade is predicted by IC50 value.

101. The method for inhibition or blocking of IL-23 receptor in blood, blood circulation, tissue, skin or joints for treatment of inflammatory diseases or disorders according to anyone of claims 94 to 98, wherein sufficient exposure of the systemically active peptide level is at least above ICso for 24 hours.

102. The method for inhibition or blocking of IL-23 receptor in blood, blood circulation, tissue, skin or joints for treatment of inflammatory diseases or disorders according to anyone of claims 94 to 98, wherein a level of target blockade is determined by ICso values in picomolar range.

103. The method for inhibition or blocking of IL-23 receptor in blood, blood circulation, tissue, skin or joints for treatment of inflammatory diseases or disorders according to anyone of claims 94 to 98, wherein systemic exposure is required for inhibitory activity in the blood.

104. A method for inhibiting IL-23 receptor in a tissue selected from blood, skin, cartilage, or synovial membrane comprising administering an oral dose of a therapeutically effective amount of a peptide [Lys(Ac)]-[Pen]*-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N43-Pal]-Sarc-NH2 (*Pen-Pen form disulfide bond) (SEQ ID NO: 1):HN HN OS,sYyL .,,NH 0a,N111.r>1 N\AN AN NH 2 0 o I A ; or a pharmaceutically acceptable salt or solvate form thereof to a patient in need thereof.

105. The method of claim 104, wherein the tissue is blood.

106. The method of claim 104, wherein the tissue is skin.

107. The method of claim 104, wherein the tissue is cartilage.

108. The method of claim 104, wherein the tissue is synovial membrane.

109. A method for inhibiting IL-23 receptor in a digestive tract tissue comprising administering an oral dose of a therapeutically effective amount of a peptide Ac-[Pen]*-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]*-Phe[4-(2-aminoethoxy)]-[2-Nal]-[TEIP]-E-N43-Pal]-Sarc-NH2 (*Pen-Pen form disulfide bond) (SEQ ID NO: 1): I HHN N H2N,i 1,1 Hr;ITO .,,NH rYìi 8 ca7tv.LN , or a pharmaceutically acceptable salt or solvate form thereof to a patient in need thereof.

110. The method of claim 109, wherein the tissue is selected from the group consisting of mouth, esophagus, stomach, small intestine, large intestine, duodenum, and anus.

111. The method of claim 109, wherein the tissue is mouth.

112. The method of claim 109, wherein the tissue is esophagus.

113. The method of claim 109, wherein the tissue is stomach.

114. The method of claim 109, wherein the tissue is small intestine.

115. The method of claim 109, wherein the tissue is large intestine.

116. The method of claim 109, wherein the tissue is duodenum.

117. The method of claim 109, wherein the tissue is anus.

118. A method inhibiting the production of IL-17A in a tissue selected from blood, skin, cartilage, or synovial membrane comprising administering an oral dose of a therapeutically effective amount of a peptide Ac-[Pen]*-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]*-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N43-Pal]-Sarc-NH2 (*Pen-Pen form disulfide bond) (SEQ ID NO: 1): HN HNN c4,-10 H2N y ,1 al 0 Oycs,sYyL0 .0NH HH0a7N\AN or a pharmaceutically acceptable salt or solvate form thereof to a patient in need thereof.

119. The method of claim 118, wherein the tissue is blood.

120. The method of claim 118, wherein the tissue is skin.

121. The method of claim 118, wherein the tissue is cartilage.

122. The method of claim 118, wherein the tissue is synovial membrane.

123. A method inhibiting the production of IL-17A in a digestive tract tissue comprising administering an oral dose of a therapeutically effective amount of a peptide Ac-[Pen]*-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]*-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3-Pal]-Sarc-NH2 (*Pen-Pen form disulfide bond) (SEQ ID NO: 1): FIN HN .===='"1] 7 0 9H HN o 0 0a7Ersil \AN H 0 H 0 g or a pharmaceutically acceptable salt or solvate form thereof to a patient in need thereof.

124. The method of claim 123, wherein the tissue is selected from the group consisting of mouth, esophagus, stomach, small intestine, large intestine, duodenum, and anus.

125. The method of claim 123, wherein the tissue is mouth.

126. The method of claim 123, wherein the tissue is esophagus.

127. The method of claim 123, wherein the tissue is stomach.

128. The method of claim 123, wherein the tissue is small intestine.

129. The method of claim 123, wherein the tissue is large intestine.

130. The method of claim 123, wherein the tissue is duodenum.

131. The method of claim 123, wherein the tissue is anus.

132. A method inhibiting the production of IL-17F in a tissue selected from blood, skin, cartilage, or synovial membrane comprising administering an oral dose of a therapeutically effective amount of a peptide Ac-[Pen]*-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]*-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N43-Pal]-Sarc-NH2 (*Pen-Pen form disulfide bond) (SEQ ID NO: 1):*I HHN NH2N 1,1 0 gHI H 1410 HN 0 HN ''')LNH2 OreLxS,sY11)0 o (NH2 0 091,1 ......H or a pharmaceutically acceptable salt or solvate form thereof to a patient in need thereof.

133. The method of claim 132, wherein the tissue is blood.

134. The method of claim 132, wherein the tissue is skin.

135. The method of claim 132, wherein the tissue is cartilage.

136. The method of claim 132, wherein the tissue is synovial membrane.

137. A method inhibiting the production of IL-17F in a digestive tract tissue comprising administering an oral dose of a therapeutically effective amount of a peptide Ac-[Pen]*-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]*-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3-Pal]-Sarc-NH2 (*Pen-Pen form disulfide bond) (SEQ ID NO: 1): HH2N1 "0 HIsl.õ.0 0 HN 0 HNrj OcS,s.L0 .0NH o HNH2 0 H0a71, N0 o I II or a pharmaceutically acceptable salt or solvate form thereof to a patient in need thereof.

138. The method of claim 137, wherein the tissue is selected from the group consisting of mouth, esophagus, stomach, small intestine, large intestine, duodenum, and anus.

139. The method of claim 137, wherein the tissue is mouth.

140. The method of claim 137, wherein the tissue is esophagus.

141. The method of claim 137, wherein the tissue is stomach.

142. The method of claim 137, wherein the tissue is small intestine.

143. The method of claim 137, wherein the tissue is large intestine.

144. The method of claim 137, wherein the tissue is duodenum.

145. The method of claim 137, wherein the tissue is anus.

146. A method inhibiting the production of IL-22 in a tissue selected from blood, skin, cartilage, or synovial membrane comprising administering an oral dose of a therapeutically effective amount of a peptide Ac-[Pen]*-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]*-Phe[4-(2-aminoethoxy)]-[2-Nal] - [TEIP]-E-N43-Pal]-Sarc-NE12 (*Pen-Pen form disulfide bond) (SEQ ID NO: 1): I HHN N H2N.o 1 I H HN'LO HNOS,sYyLo .,,NH r 0 H ca7N\AN or a pharmaceutically acceptable salt or solvate form thereof to a patient in need thereof.

147. The method of claim 146, wherein the tissue is blood.

148. The method of claim 146, wherein the tissue is skin.

149. The method of claim 146, wherein the tissue is cartilage.

150. The method of claim 146, wherein the tissue is synovial membrane.

151. A method inhibiting the production of IL-22 in a digestive tract tissue comprising administering an oral dose of a therapeutically effective amount of a peptide Ac-[Pen]*-N-T4W(7-Me)]-[Lys(Ac)]-[Pen]*-Phe[4-(2-aminoethoxy)]-[2-Nal] - [TEIP]-E-N-[3-Pal]-Sarc-NH2 (*Pen-Pen form disulfide bond) (SEQ ID NO: 1): I HN HN0 gH HN 0 HN ''')LNH2 C:oelxs,sYy(:) O ..õ(NH2 0 03,...17)1N ti 0 o g or a pharmaceutically acceptable salt or solvate form thereof to a patient in need thereof.

152. The method of claim 151, wherein the tissue is selected from the group consisting of mouth, esophagus, stomach, small intestine, large intestine, duodenum, and anus.

153. The method of claim 151, wherein the tissue is mouth.

154. The method of claim 151, wherein the tissue is esophagus.

155. The method of claim 151, wherein the tissue is stomach.

156. The method of claim 151, wherein the tissue is small intestine.

157. The method of claim 151, wherein the tissue is large intestine.

158. The method of claim 151, wherein the tissue is duodenum.

159. The method of claim 151, wherein the tissue is anus.

160. The method of any of claims 104 to 108, 118 to 122, 132 to 136, or 146 to wherein the oral dose is 10 mg to 25 mg.

161. The method of any of claims 109 to 117, 123 to 131, 137 to 145, or 151 to wherein the oral dose is 25 mg to 50 mg.

162. The method of claim 160, wherein the oral dose is 10 mg.

163. The method of claim 160, wherein the oral dose is 25 mg.

164. The method of claim 161, wherein the oral dose is 25 mg.

165. The method of claim 161, wherein the oral dose is 50 mg.
```

---

### 티어 2 — 속(Genus) / 단환 펩타이드 Markush 특허

#### 2.1 WO2021146441A1 ☑️부분교차검증 — 공백 해소 (전체 186 청구항)

> **💡 핵심 요약** &nbsp;|&nbsp; **유형:** compound·물질(peptide), composition(조성물), use·치료방법
> 
> **무엇을 청구하나:** IL-23 수용체에 결합하는 단환(monocyclic) 펩타이드 저해제 자체를 Formula (I) Markush 구조로 청구하고(X4-X9 디설파이드/티오에터 고리화), 그 펩타이드 이량체, 의약조성물, IBD·건선 등 치료방법 및 치료용도까지 포괄 청구
> 
> **핵심 권리범위:** X4/X9가 Pen·Cys·Abu 등으로 X4-X9 디설파이드 또는 티오에터 고리 형성; X15에 His/3Pal/4Pal/5Pyal 등, X16에 Sarc·(D)NMeTyr·absent 등 C-말단 한정; 특정 선행 화합물(Ac-[Pen]-N-T-W...-H-NH2 등)을 명시적으로 제외(proviso); IL-23의 IL-23R 결합 저해
> 
> **독립항:** 1, 36, 44, 47, 52, 183 &nbsp;|&nbsp; **적응증:** IBD/UC/CD/건선/건선성관절염 등 염증성 질환 &nbsp;|&nbsp; **검증:** ☑️부분교차검증(차이75) &nbsp;|&nbsp; **추정만료:** PCT(term N/A)


| 항목 | 내용 |
|---|---|
| 특허번호 | WO2021146441A1 (PCT 공개, A1) |
| 제목 | Peptide Inhibitors of Interleukin-23 Receptor and Their Use to Treat Inflammatory Diseases |
| 국제출원 / 공개 | PCT/US2021/013463, 국제출원일 2021-01-14 |
| 우선일 | 2020-01-15 (US Provisional 62/961,624) |
| 출원인/양수인 | Janssen Biotech, Inc.; Protagonist Therapeutics, Inc. |
| 패밀리 | US20210261622A1, US11845808B2, US12018057B2 (동일/자매 출원 17/149,509 계열) |
| 권위 만료일 | PCT 자체는 존속기간 만료 개념 **해당없음(N/A)**; 국내단계 진입국별 산정(미국 대응 = 2041-01-14) |
| 교차검증 | GP=186, FPO=167(168~186 잘림), both=167, agree=92, **substantive_diff=75** → ☑️부분교차검증 |

**[ANALYSIS] (한국어)**

프로그램의 **기초 PCT**. 이전 파이프라인에서 FPO가 청구항 167에서 잘려 **168~186번 19개가 누락**된 상태였으나, 이번에 Google Patents로 **전체 186 청구항**을 확보했다. 이로써 보고서상 최대 공백 중 하나가 해소되었다. GP↔FPO 비교에서 두 소스 공통 167개 중 substantive_diff가 75개로 크게 나타나는데, 이는 FPO의 OCR/파싱 잡음(공백·기호 깨짐, Markush 치환기 목록의 줄바꿈 차이)이 누적된 것으로, **권위 소스는 GP**이며 FPO 차이분은 원문 권리범위 변동이 아니라 추출 잡음으로 본다. 따라서 등급은 ☑️부분교차검증(차이 청구항 다수 = 공통 167개 중 75개; GP 단독 보유분 168~186은 FPO 부재)이며 본문 [VERBATIM]은 **GP 186 전문**을 사용한다.

청구항 1은 Formula (I) 단환 펩타이드 속(X3~X16 가변)을 정의하고, proviso로 특정 서열들을 제외(disclaimer)하는 복잡한 Markush 구조다. 후반부(180번대)는 조성물/치료용도 청구항으로 확장된다.

**[VERBATIM] — 출처: Google Patents (`work/05_gp_authoritative/WO2021146441A1.md`)**

```text
1. A monocyclic peptide inhibitor of an interleukin-23 receptor, or a pharmaceutically acceptable salt thereof, wherein the peptide inhibitor comprises an amino acid sequence of Formula (I): X3 -X4-X5 -X6-X7-X8-X9-X10-X11-X12-X13-X14-X15 -X16 (I) wherein X3 is absent or any amino acid; X4 is Abu, Cys, (D)Cys, alpha-MeCys, (D)Pen, Pen, or Pen(sulfoxide); X5 is Cit, Glu, Gly, substituted Gly, Leu, lie, beta-Ala, Ala, Lys, Asn, Pro, Ser, alpha-MeGln, alpha-MeLys, alpha-MeLeu, alpha-MeAsn, Lys(Ac), alpha-MeLys(Ac), Dab(Ac), Dap(Ac), homo-Lys(Ac), Gin, or Asp; X6 is Thr, Aib, Asp, Dab, Gly, Pro, Ser, alpha-MeGln, alpha-MeLys, alpha-MeLeu, alpha- MeAsn, alpha-MeThr, alpha-MeSer, or Val; X7 is unsubstituted Trp, or Trp substituted with cyano, halo, alkyl, haloalkyl, hydroxy, alkoxy, substituted or unsubstituted aryl, or substituted or unsubstituted heteroaryl; X8 is Gin, alpha-MeLys, alpha-MeLeu, alpha-MeLys(Ac), beta-homoGln, Cit, Glu, Phe, substituted Phe, Tyr, Asn, Thr, Val, Aib, alpha-MeGln, alpha-MeAsn, Lys(Ac), Dab(Ac), Dap(Ac), homo-Lys(Ac), 1-Nal, 2-Nal, Lys(b-Ala), Lys(Gly), Lys(Benzyl, Ac), Lys(butyl, Ac), Lys(isobutyl,Ac), Lys(propyl,Ac), or Trp; X9 is Abu, Cys, (D)Cys, alpha-MeCys, (D)Pen, Pen, or Pen(sulfoxide); X10 is Tyr, or substituted Tyr, unsubstituted Phe, or Phe substituted with halo, alkyl, haloalkyl, hydroxy, alkoxy, cyano, cycloalkyl, carboxy, carboxamido, 2-aminoethoxy, or 2- acetylaminoethoxy; and X11 is 2-Nal, Phe(2-Me), Phe(3-Me), Phe(4-Me), Phe(3,4-dimethoxy), 2Quin, 3Quin, 1-Nal, unsubstituted Trp, or Trp substituted with cyano, halo, alkyl, haloalkyl, hydroxy, or alkoxy; X12 is 4-amino-4-carboxy-tetrahydropyran (THP), Acvc, alpha-MeLys, alpha-MeLeu, alpha- MeArg, alpha-MePhe, alpha-MeLeu, alpha-MeLys, alpha-MeAsn, alpha-MeTyr, Ala, cyclohexylAla, Lys, or Aib; X13 is any amino acid; X14 is any amino acid; and i) X15 is any amino acid other than His, (D)His, substituted or unsubstituted His, 2Pal, 3Pal, or 4Pal; X16 is Sarc, aMeLeu, (D)NMeTyr, His, (D)Thr, bAla, Pro, or (D)Pro; and the peptide inhibitor is other than Ac-[Abu]-QTWQC-[Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-[Lys(Ac)]-NNPG-NH2; Ac- [Pen] -N-T - W - [Lys(Ac)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-N al] - [aMeLeu] - [Lys(Ac)]-NN-[Sarc]-NH2; Ac-[(D)Arg]-[Abu]-Q-T-[W(7-Me)]-[Lys(Ac)]-[Cys]-Phe[4-(2-aminoethoxy)]-[2-Nal]- [a-MeLys] - [Lys(Ac)] -N- [(D)Lys] - [Sarc] -NH2; or Ac-[Pen]-N-T-[W(7-Me)]-[Cit]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]- [Lys(Ac)] -N- [Aib] - [bA] -NH2; or ii) X15 is His, (D)His, substituted or unsubstituted His, 2Pal, 3Pal, 4Pal, 4TriazolAla, or 5Pyal; and X16 is absent, (D)aMeTyr, (D)NMeTyr or any amino acid other than THP, substituted or unsubstituted Phe, substituted or unsubstituted (D)Phe, substituted or unsubstituted His, substituted or unsubstituted (D)His, substituted or unsubstituted Trp, substituted or unsubstituted 2-Nal, or N-substituted Asp; and the compound is other than Ac- [Pen] -N-T - [ W(7 -Me)] - [Lys(Ac)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-Nal] - [a-MeLys] - [Ly s(Ac) ] -N-H-NH2 ; wherein 2Pal is 2-pyridyl substituted alanine, and 3Pal is 3-pyridyl substituted alanine, and 4Pal is 4-pyridyl substituted alanine 5Pyal is 5-pyrimidine substituted alanine:

2. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1, wherein X15 is any amino acid other than His, (D)His, or substituted or unsubstituted His, 2Pal, 3Pal, or 4Pal; X16 is Sarc, aMeLeu, (D)NMeTyr, His, (D)Thr, bAla, Pro, or (D)Pro; and the compound is other than Ac- [Abu] -QTWQC] - [Phe[4-(2-aminoethoxy)] - [2-Nal] - [THP] - [Lys(Ac)] -NNPG-NH2; Ac- [Pen] -N-T - W - [Lys(Ac)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-N al] - [aMeLeu] - [Lys(Ac)]-NN-[Sarc]-NH2; Ac-[(D)Arg]-[Abu]-Q-T-[W(7-Me)]-[Lys(Ac)]-[Cys]-Phe[4-(2-aminoethoxy)]-[2-Nal]- [a-MeLys] - [Lys(Ac)] -N- [(D)Lys] - [Sarc] -NH2; or Ac-[Pen]-N-T-[W(7-Me)]-[Cit]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]- [Lys(Ac)] -N- [Aib] - [bA] -NH2.

3. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1, wherein the peptide inhibitor comprises an amino acid sequence of Formula (la): X3-X4-X5 -X6-X7-X8-X9-X10-X11-X12-X13-X14-X15 -Sarc (la) wherein X4 and X9 form a disulfide bond or a thioether bond; X15 is any amino acid; and ; and the compound is other than Ac- [Pen] -N-T - W - [Lys(Ac)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-N al] - [aMeLeu] - [Lys(Ac)]-NN-[Sarc]-NH2; or Ac-[(D)Arg]-[Abu]-Q-T-[W(7-Me)]-[Lys(Ac)]-[Cys]-Phe[4-(2-aminoethoxy)]-[2-Nal]- [a-MeLys] - [Lys(Ac)] -N- [(D)Lys] - [Sarc] -NH2.

4. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1, wherein the peptide inhibitor comprises an amino acid sequence of Formula (lb): X3 -X4-X5 -X6-X7-X8-X9-X10-X11-X12-X13-X14-X15 -(D)NMeTyr (lb) wherein X4 and X9 form a disulfide bond or a thioether bond; X15 is any amino acid.

5. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1, wherein the peptide inhibitor comprises an amino acid sequence of Formula (Ic): X3-X4-X5 -X6-X7-X8-X9-X10-X11-X12-X13-X14- [Pal] -X16 (Ic) wherein Pal is 2Pal, 3Pal, or 4Pal; X16 is absent; wherein 2Pal is 2-pyridyl substituted alanine, and 3Pal is 3-pyridyl substituted alanine, and 4Pal is 4-pyridyl substituted alanine

6. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1, wherein the peptide inhibitor comprises an amino acid sequence of Formula (Id): X3 -X4-X5-X6-X7-X8-X9-X10-X11-X12-X13-X14- [His ' ] -X16 (Id) wherein His' is His or 3-MeHis; X16 is absent; and X4 and X9 form a disulfide bond or a thioether bond.

7. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1, wherein X15 is any amino acid; X16 is bA, aMe(D)Tyr, (D)NMeTyr, Sarc, Pro, or (D)Pro; and the peptide inhibitor is other than Ac-[Abu]-QTWQC-[Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-[Lys(Ac)]-NNPG-NH2; Ac- [Pen] -N-T - W - [Lys(Ac)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-N al] - [aMeLeu] - [Lys(Ac)]-NN-[Sarc]-NH2; Ac-[(D)Arg]-[Abu]-Q-T-[W(7-Me)]-[Lys(Ac)]-[Cys]-Phe[4-(2-aminoethoxy)]-[2-Nal]- [a-MeLys] - [Lys(Ac)] -N- [(D)Lys] - [Sarc] -NH2; or Ac-[Pen]-N-T-[W(7-Me)]-[Cit]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]- [Lys(Ac)] -N- [Aib] - [bA] -NH2.

8. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1 , wherein X15 is any amino acid; X16 is bA, aMe(D)Tyr, (D)NMeTyr, Sarc, Pro, or (D)Pro, and the compound is other than Ac- [Pen] -N-T - W - [Lys(Ac)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-N al] - [aMeLeu] - [Lys(Ac)]-NN-[Sarc]-NH2; or Ac-[(D)Arg]-[Abu]-Q-T-[W(7-Me)]-[Lys(Ac)]-[Cys]-Phe[4-(2-aminoethoxy)]-[2-Nal]- [a-MeLys] - [Lys(Ac)] -N- [(D)Lys] - [Sarc] -NH2.

9. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1 , wherein X15 is any amino acid; X16 is (D)NMeTyr, or Sarc; and the peptide inhibitor is other than Ac- [Pen] -N-T - W - [Lys(Ac)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-N al] - [aMeLeu] - [Lys(Ac)]-NN-[Sarc]-NH2; or Ac-[(D)Arg]-[Abu]-Q-T-[W(7-Me)]-[Lys(Ac)]-[Cys]-Phe[4-(2-aminoethoxy)]-[2-Nal]- [a-MeLys] - [Lys(Ac)] -N- [(D)Lys] - [Sarc] -NH2.

10. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1 , wherein X15 is 3 Quin, Asn, His, (D)His, (D)Leu, (D)Lys, 3 -Pal, 4-Pal, Phe, substituted Phe, (D)Thr, substituted Trp or (D)Val; X16 is (D)NMeTyr, or Sarc; and the peptide inhibitor is other than Ac- [Pen] -N-T - W - [Lys(Ac)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-N al] - [aMeLeu] - [Lys(Ac)]-NN-[Sarc]-NH2; or Ac-[(D)Arg]-[Abu]-Q-T-[W(7-Me)]-[Lys(Ac)]-[Cys]-Phe[4-(2-aminoethoxy)]-[2-Nal]- [a-MeLys] - [Lys(Ac)] -N- [(D)Lys] - [Sarc] -NH2.

11. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1 , wherein X16 is (D)NMeTyr.

12. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1 , wherein X16 is Sarc; and the peptide inhibitor is other than Ac- [Pen] -N-T - W - [Lys(Ac)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-N al] - [aMeLeu] - [Lys(Ac)]-NN-[Sarc]-NH2; or Ac-[(D)Arg]-[Abu]-Q-T-[W(7-Me)]-[Lys(Ac)]-[Cys]-Phe[4-(2-aminoethoxy)]-[2-Nal]- [a-MeLys] - [Lys(Ac)] -N- [(D)Lys] - [Sarc] -NH2.

13. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1 , wherein X15 is His, (D)Lys, 3-Pal, or 4-Pal; X16 is (D)NMeTyr, or Sarc; and the peptide inhibitor is other than Ac-[(D)Arg]-[Abu]-Q-T-[W(7-Me)]-[Lys(Ac)]-[Cys]-Phe[4-(2-aminoethoxy)]-[2-Nal]- [a-MeLys] - [Lys(Ac)] -N- [(D)Lys] - [Sarc] -NH2.

14. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1 , wherein X15 is Asn, His, (D), His, (D)Leu, (D)Lys, 3-Pal, substituted or unsubstituted Phe, (D)Thr, or (D)Val; X16 is (D)NMeTyr.

15. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1 , wherein X15 is 3Quin, Asn, His, (D)His, (D)Leu, (D)Lys, 3-Pal, 4-Pal, or substituted Trp; X16 is Sarc; and the peptide inhibitor is other than Ac- [Pen] -N-T - W - [Lys(Ac)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-N al] - [aMeLeu] - [Lys(Ac)]-NN-[Sarc]-NH2; or Ac-[(D)Arg]-[Abu]-Q-T-[W(7-Me)]-[Lys(Ac)]-[Cys]-Phe[4-(2-aminoethoxy)]-[2-Nal]- [a-MeLys] - [Lys(Ac)] -N- [(D)Lys] - [Sarc] -NH2.

16. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1, wherein X15 is (3-Me)His, 3-Pal, or 4-Pal; and X16 is absent, Sarc or (D)NMeTyr.

17. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1, wherein X15 is (3-Me)His or 3-Pal; and X16 is absent or Sarc.

18. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1 , wherein X15 is 3-Pal; and X16 is Sarc.

19. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1 , wherein X15 is Asn, His, (D)Lys, or 3-Pal; X16 is (D)NMeTyr, or Sarc; and the peptide inhibitor is other than Ac- [Pen] -N-T - W - [Lys(Ac)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-N al] - [aMeLeu] - [Lys(Ac)]-NN-[Sarc]-NH2; Ac-[(D)Arg]-[Abu]-Q-T-[W(7-Me)]-[Lys(Ac)]-[Cys]-Phe[4-(2-aminoethoxy)]-[2-Nal]- [a-MeLys] - [Lys(Ac)] -N- [(D)Lys] - [Sarc] -NH2.

20. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1 , wherein X15 is 5-Pyal, (D)His, (l-Me)His, (3-Me)His, 2-Pal or 3-Pal; and X16 is absent; and the peptide inhibitor is other than Ac- [Pen] -N-T - [ W(7 -Me)] - [Lys(Ac)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-Nal] - [a-MeLys] - [Lys(Ac)]-N-H-NH2.

21. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1 , wherein X15 is 5-Pyal, (l-Me)His, or (3-Me)His; and X16 is absent.

22. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1 , wherein X15 is 5-Pyal or (3-Me)His; and X16 is absent.

23. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1, wherein X15 is His, (D)His, or substituted or unsubstituted His, 2Pal, 3Pal, 4Pal, or 5Pyal; and X16 is absent, (D)aMeTyr, (D)NMeTyr or any amino acid other than THP, substituted or unsubstituted Phe, substituted or unsubstituted (D)Phe, substituted or unsubstituted His, substituted or unsubstituted (D)His, substituted or unsubstituted Trp, substituted or unsubstituted 2-Nal, orN-substituted Asp.

24. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 1-23, wherein X4 orX9 is independently Cys, (D)Cys, alpha-MeCys, (D)Pen, or Pen; and the bond between X4 and X9 is a disulfide bond.

25. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 1-23, wherein X4 is (D)Pen, Pen, or Pen(sulfoxide).

26. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 1-23, wherein X4 is Pen.

27. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 1-23, wherein X9 is Cys, (D)Cys, or alpha-MeCys.

28. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 1-3, wherein X9 is Pen or (D)Pen.

29. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 1-23, wherein X9 is Pen.

30. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 1-23, wherein X4 is Pen and X9 is Pen, and the bond is a disulfide bond.

31. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 1-23, wherein X4 or X9 is Abu; and the bond between X4 and X9 is a thioether bond.

32. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 1-23, wherein X4 is Abu.

33. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 1-27 or 31-32, wherein X9 is Cys, (D)Cys, or alpha-MeCys.

34. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 1-26 or 28-32, wherein X9 is Pen or (D)Pen.

35. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 1-26 or 28-32, wherein X9 is Pen.

36. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 1-27 or 31-33, wherein X9 is Cys.

37. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 1-24, 27-29, or 31-32, wherein X4 is Abu and X9 is Cys or Pen, and the bond is a thioether bond.

38. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 1-24, 27-29, or 31-32, wherein X4 is Abu and X9 is Cys, and the bond is a thioether bond.

39. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1, wherein the peptide inhibitor comprises an amino acid sequence of Formula (Ila), (lib), or (IIc): Pen-X5 -X6-X7-X8-Pen-X10-X11-X12-X13-X14-X15 -X16 (Ila), Abu-X5 -X6-X7-X8-Cys-X10-X11-X12-X13-X14-X15 -X16 (lib), or Abu-X5 -X6-X7-X8-Pen-X10-X11-X12-X13-X14-X15 -X16 (He), wherein X5-X8 and X10-X 14 are as described in claim 1; X15 is His, (D)His, or substituted or unsubstituted His, 2Pal, 3Pal, or 4Pal, and X16 is any amino acid; or X15 is any amino acid and X16 is Sarc; and the peptide inhibitor is cyclized via a Pen-Pen disulfide bond; or the peptide inhibitor is cyclized via a Abu-Cys or Abu-Pen thioether bond.

40. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 1-39, wherein X15 is 2Pal, 3Pal, or 4Pal, and X16 is any amino acid.

41. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 1-39, wherein X15 is His or 3MeHis; and X16 is any amino acid.

42. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 1-39, wherein X15 is any amino acid and X16 is Sarc.

43. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 1-39, wherein X15 is any amino acid and X16 is (D)NMeTyr.

44. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 1-43, wherein X5 is Asn, Ser, Gin, or Glu.

45. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 1-43, wherein X5 is Asn, or Gin.

46. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 1-43, wherein X5 is Asn.

47. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1, wherein the peptide inhibitor comprises an amino acid sequence of Formula (Ilia), (Illb), (IIIc), or (IIId): Pen- Asn-X6-X7-X8-Pen-X10-X11-X12-X13-X14- [Pal] -X16 (Ilia), Pen-Gln-X6-X7-X8-Pen-X10-X11-X12-X13-X14- [Pal] -X16 (Illb), Abu- Asn-X6-X7-X8-Cys-X10-X11-X12-X13-X14-[Pal]-X16 (IIIc), or Abu-Gln-X6-X7-X8-Pen-X10-X11-X12-X13-X14- [Pal] -X16 (IIId), wherein X6-X8 and X10-X 14 are as described in claim 1; Pal is 2Pal, 3Pal, or 4Pal; and X16 is any amino acid; wherein 2Pal is 2-pyridyl substituted alanine, and 3Pal is 3-pyridyl substituted alanine, and 4Pal is 4-pyridyl substituted alanine

48. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1, wherein the peptide inhibitor comprises an amino acid sequence of Formula (IVa), (IVb), (IVc), or (IV d), (IVe), (IVf), (IVg), or (IVh): Pen- Asn-X6-X7-X8-Pen-X10-X11-X12-X13-X14-X15 -Sarc (IVa), Pen-Gln-X6-X7-X8-Pen-X10-X11-X12-X13-X14-X15 -Sarc (IVb), Abu- Asn-X6-X7-X8-Cys-X 10-X 11-X12-X13-X14-X15-Sarc (IVc), Abu-Gln-X6-X7-X8-Pen-X10-Xl 1-X12-X13-X14-X15-Sarc (IVd), Pen- Asn-X6-X7-X8-Pen-X10-X11-X12-X13-X14-X15 -(D)NMeTyr (IVe), Pen-Gln-X6-X7-X8-Pen-X10-X11-X12-X13-X14-X15-(D)NMeTyr (IVf), Abu- Asn-X6-X7-X8-Cys-X10-X11-X12-X13-X14-X15-(D)NMeTyr (IVg), or Abu-Gln-X6-X7-X8-Pen-X10-X11-X12-X13-X14-X15 -(D)NMeTyr (IVh), wherein X6-X8 and X10-X 14 are as described in claim 1; X15 is any amino acid; and the peptide inhibitor is cyclized via a Pen-Pen disulfide bond; or a Abu-Cys or Abu-Pen thioether bond.

49. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 1-48, wherein X6 is Thr.

50. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1, wherein the peptide inhibitor comprises an amino acid sequence of Formula (Va), (Vb), (Vc), or (Vd): Pen- Asn-Thr-X7-X8-Pen-X10-X11-X12-X13-X14- [Pal] -X16 (Va), Pen-Gln-Thr-X7-X8-Pen-X10-X11-X12-X13-X14- [Pal] -X16 (Vb), Abu- Asn-Thr-X7-X8-Cys-X10-X11-X12-X13-X14- [Pal] -X16 (Vc), or Abu-Gln-Thr-X7-X8-Pen-X10-X11-X12-X13-X14- [Pal] -X16 (Vd), wherein X7-X8 and X10-X 14 are as described in claim 1; Pal is 2Pal, 3Pal, or 4Pal; and X16 is any amino acid; wherein 2Pal is 2-pyridyl substituted alanine, and 3Pal is 3-pyridyl substituted alanine, and 4Pal is 4-pyridyl substituted alanine

51. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1, wherein the peptide inhibitor comprises an amino acid sequence of Formula (Via), (VIb), (Vic), or (VId), (Vie), (Vlf), (VIg), or (VIh): Pen- Asn-Thr-X7-X8-Pen-X10-X11-X12-X13-X14-X15 - Sarc (Via), Pen-Gln-Thr-X7-X8-Pen-X10-X11-X12-X13-X14-X15 -Sarc (VIb), Abu- Asn-Thr-X7-X8-Cys-X10-X11-X12-X13-X14-X15 -Sarc (Vic), Abu-Gln-Thr-X7-X8-Pen-X10-X11-X12-X13-X14-X15 -Sarc (VId), Pen- Asn-Thr-X7-X8-Pen-X10-X11-X12-X13-X14-X15 -(D)NMeTyr (Vie), Pen-Gin- Thr-X7-X8-Pen-X10-X11-X12-X13-X14-X15-(D)NMeTyr (Vlf), Abu- Asn-Thr-X7-X8-Cys-X10-X11-X12-X13-X14-X15 -(D)NMeTyr (VIg) (SEQ ID NO:536), or Abu-Gln-Thr-X7-X8-Pen-X10-X11-X12-X13-X14-X15 -(D)NMeTyr (VIh), wherein X7-X8 and X10-X 14 are as described in claim 1; X15 is any amino acid; and the peptide inhibitor is cyclized via a Pen-Pen disulfide bond; or a Abu-Cys or Abu-Pen thioether bond.

52. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 1-51, wherein X8 is Gin, alpha- Me-Lys, alpha- MeLys(Ac), Lys(Ac), or Glu.

53. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 1-51, wherein X8 is Gin.

54. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 1-51, wherein X8 is Lys(Ac).

55. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1, wherein the peptide inhibitor comprises an amino acid sequence of Formula (Vila), (Vllb), (Vile), or (Vlld): Pen- Asn-Thr-X7-Gln-Pen-X10-X11-X12-X13-X14- [Pal] -X16 (Vila), Pen-Gln-Thr-X7-Gln-Pen-X10-X11-X12-X13-X14- [Pal] -X16 (Vllb), Abu- Asn-Thr-X7-Gln-Cys-X10-X11-X12-X13-X14- [Pal] -X16 (Vile) (SEQ ID NO: 448), or Abu-Gln-Thr-X7-Gln-Pen-X10-X11-X12-X13-X14- [Pal] -X16 (Vlld), wherein X7 and X10-X 14 are as described in claim 1; Pal is 2Pal, 3Pal, or 4Pal; and X16 is any amino acid; wherein 2Pal is 2-pyridyl substituted alanine, and 3Pal is 3-pyridyl substituted alanine, and 4Pal is 4-pyridyl substituted alanine

56. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1, wherein the peptide inhibitor comprises an amino acid sequence of Formula (Villa), (VllIb), (VIIIc), (VllId), (Vine), (Vlllf), (VllIg), or (VllIh): Pen- Asn-Thr-X7-Gln-Pen-X10-X11-X12-X13-X14-X15 -Sarc (Villa), Pen-Gln-Thr-X7-Gln-Pen-X10-X11-X12-X13-X14-X15 -Sarc (VllIb), Abu- Asn-Thr-X7-Gln-Cys-X 10-X 11-X12-X13-X14-X15-Sarc (VIIIc), Abu-Gln-Thr-X7-Gln-Pen-X10-X11-X12-X13-X14-X15 -Sarc (VllId), Pen- Asn-Thr-X7-Gln-Pen-X10-X11-X12-X13-X14-X15 -(D)NMeTyr (VllIe) (SEQ ID NO: 450), Pen-Gln-Thr-X7-Gln-Pen-X10-X11-X12-X13-X14-X15 -(D)NMeTyr (VllIf) (SEQ ID NO: 451), Abu- Asn-Thr-X7-Gln-Cys-X10-X11-X12-X13-X14-X15 -(D)NMeTyr (VllIg) (SEQ ID NO: 452), or Abu-Gln-Thr-X7-Gln-Pen-X10-X11-X12-X13-X14-X15 -(D)NMeTyr (VllIh) (SEQ ID NO: 453), wherein X7 and X10-X 14 are as described in claim 1; X15 is any amino acid; and the peptide inhibitor is cyclized via a Pen-Pen disulfide bond; or a Abu-Cys or Abu-Pen thioether bond.

57. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 1-56, wherein X10 is Phe, Phe[4-(2-aminoethoxy)], Phe[4-(2-acetylaminoethoxy)], or Phe(4-CONH2).

58. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 1-56, wherein X10 is Phe[4-(2-aminoethoxy)], or Phe[4-(2-acetylaminoethoxy)].

59. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 1-56, wherein X10 is Phe[4-(2-aminoethoxy)].

60. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1, wherein the peptide inhibitor comprises an amino acid sequence of Formula (IXa), (IXb), (IXc), or (IXd): Pen- Asn-Thr-X7- Gin-Pen- [F (4-2ae)] -X11-X12-X13-X14- [Pal] -X16 (IXa) (SEQ ID NO:454), Pen-Gln-Thr-X7-Gln-Pen- [F (4-2ae)] -X11-X12-X13-X14- [Pal] -X16 (IXb) (SEQ ID NO:455), Abu- Asn-Thr-X7-Gln-Cys- [F (4-2ae)] -X11-X12-X13-X14- [Pal] -X16 (IXc) (SEQ ID NO:456), or Abu-Gln-Thr-X7-Gln-Pen- [F (4-2ae)] -X11-X12-X13-X14- [Pal] -X16 (IXd) (SEQ ID NO:457), wherein X7, and X11-X14 are as described in claim 1; F(4-2-ae) is Phe[4-(2-aminoethoxy)]; Pal is 2Pal, 3Pal, or 4Pal; and X16 is any amino acid; wherein 2Pal is 2-pyridyl substituted alanine, and 3Pal is 3-pyridyl substituted alanine, and 4Pal is 4-pyridyl substituted alanine

61. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1, wherein the peptide inhibitor comprises an amino acid sequence of Formula (Xa), (Xb), (Xc), (Xd), (Xe), (Xf), (Xg), or (Xh): Pen Asn-Thr-X7-Gln-Pen- [F (4-2ae)] -X11-X12-X13-X14-X15- Sarc (Xa) (SEQ ID NO: 458), Pen-Gln-Thr-X7-Gln-Pen- [F (4-2ae)] -X11-X12-X13-X14-X15-Sarc (Xb) (SEQ ID NO: 459), Abu-Asn-Thr-X7-Gln-Cys- [F (4-2ae)] -X11-X12-X13-X14-X15-Sarc (Xc) (SEQ ID NO: 460), Abu-Gln-Thr-X7-Gln-Pen- [F (4-2ae)] -X11-X12-X13-X14-X15-Sarc (Xd) (SEQ ID NO:461, Pen-Asn-Thr-X7-Gln-Pen- [F (4-2ae)] -X 1 l-X12-X13-X14-X15-(D)NMeTyr (Xe) (SEQ ID NO:462), Pen-Gln-Thr-X7-Gln-Pen- [F (4-2ae)] -X11-X12-X13-X14-X15-(D)NMeTyr (Xf) (SEQ ID NO:463), Abu-Asn-Thr-X7-Gln-Cys- [F (4-2ae)] -X11-X12-X13-X14-X15-(D)NMeTyr (Xg) (SEQ ID NO:464), or Abu-Gln-Thr-X7-Gln-Pen- [F (4-2ae)] -X11-X12-X13-X14-X15-(D)NMeTyr (Xh) (SEQ ID NO:465), wherein X7, and X11-X14 are as described in claim 1; F(4-2-ae) is Phe[4-(2-aminoethoxy)]; X15 is any amino acid; and the peptide inhibitor is cyclized via a Pen-Pen disulfide bond; or a Abu- Cys or Abu-Pen thioether bond.

62. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 1-61, wherein X12 is 4-amino-4-carboxy-tetrahydropyran (THP), alpha- MeLys, alpha-MeLeu, Ala, cyclohexylAla, Lys, or Aib.

63. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 1-61, wherein X12 is 4-amino-4-carboxy-tetrahydropyran (THP), alpha- MeLys, or alpha-MeLeu.

64. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 1-61, wherein X12 is alpha-MeLeu.

65. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 1-61, wherein X12 is THP.

66. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 1-65, wherein X13 is Aib, Glu, Cit, Gin, Lys(Ac), alpha-MeArg, alpha-MeGlu, alpha-MeLeu, alpha-MeLys, alpha-Me-Asn, alpha-MeLys(Ac), Dab(Ac), Dap(Ac), homo- Lys(Ac), Lys, pegylated Lys, b-homoGlu, or Lys(Y2-Ac); wherein Y2 is an amino acid.

67. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 1-65, wherein X13 is Glu, Gin, Lys(Ac), or Lys.

68. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 1-65, wherein X13 is Lys(Ac), or Lys.

69. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 1-65, wherein X13 is Lys(Ac).

70. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 1-65, wherein X13 is Glu.

71. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1, wherein the peptide inhibitor comprises an amino acid sequence of Formula (XIa), (Xlb), (XIc), or (X1 d): Pen-Asn-Thr-X7-Gln-Pen-[F(4-2ae)]-X11-[α-MeLeu]-Lys(Ac)-X14-[Pal]-X16 (XIa) (SEQ ID NO:466), Pen-Gin- Thr-X7-Gln-Pen-[F(4-2ae)] -X1 l-[α-MeLeu]-Lys(Ac)-X14-[Pal]-X16 (Xlb) (SEQ ID NO:467), Abu-Asn-Thr-X7-Gln-Cys-[F(4-2ae)]-X11-[α-MeLeu]-Lys(Ac)-X14-[Pal]-X16 (XIc) (SEQ ID NO:468), or Abu-Gln-Thr-X7-Gln-Pen-[F(4-2ae)]-X11-[α-MeLeu]-Lys(Ac)-X14-[Pal]-X16 (Xld) (SEQ ID NO:469), wherein X7, X11, and X14, and X14 are as described in claim 1; F(4-2-ae) is Phe[4-(2- aminoethoxy)]; Pal is 2Pal, 3Pal, or 4Pal; and X16 is any amino acid; wherein 2Pal is 2-pyridyl substituted alanine, and 3Pal is 3-pyridyl substituted alanine, and 4Pal is 4-pyridyl substituted alanine

72. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1, wherein the peptide inhibitor comprises an amino acid sequence of Formula (Xlla), (Xllb), (XIIc), or (Xlld), (Xlle), (Xllf), (Xllg), or (Xllh): Pen- Asn-Thr-X7-Gln-Pen-[F(4-2ae)]-X11-[α-MeLeu]-Lys(Ac)-X14-X15-(D)NMeTyr (Xlla) (SEQ ID NO:470), Pen-Gln-Thr-X7-Gln-Pen-[F(4-2ae)]-X 11 - [α-MeLeu] -Lys(Ac)-X 14-X15-(D)NMeTyr (Xllb) (SEQ ID NO:471), Abu- Asn-Thr-X7-Gln-Cys-[F(4-2ae)]-X11-[α-MeLeu]-Lys(Ac)-X14-X15-(D)NMeTyr (XIIc) (SEQ ID NO:472), Abu-Gln-Thr-X7-Gln-Pen- [F (4-2ae)] -X 11 - [α-MeLeu] -Lys(Ac)-X 14-X15-(D)NMeTyr (Xlld) (SEQ ID NO:473), Pen- Asn-Thr-X7-Gln-Pen-[F(4-2ae)]-X11-[α-MeLeu]-Lys(Ac)-X14-X15-(D)NMeTyr (Xlle) (SEQ ID NO:474), Pen-Gln-Thr-X7-Gln-Pen- [F(4-2ae)] -X 11 - [α-MeLeu] -Lys(Ac)-X 14-X15-(D)NMeTyr (Xllf) (SEQ ID NO:475), Abu- Asn-Thr-X7-Gln-Cys-[F(4-2ae)]-X11-[α-MeLeu]-Lys(Ac)-X14-X15-(D)NMeTyr (XHg) (SEQ ID NO:476), or Abu-Gln-Thr-X7-Gln-Pen- [F (4-2ae)] -X 11 - [α-MeLeu] -Lys(Ac)-X 14-X15-(D)NMeTyr (Xllh) (SEQ ID NO:477), wherein X7, X11, and X14 are as described in claim 1; F(4-2-ae) is Phe[4-(2-aminoethoxy)]; X15 is any amino acid; and the peptide inhibitor is cyclized via a Pen-Pen disulfide bond; or a Abu-Cys or Abu-Pen thioether bond.

73. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 1-72, wherein X14 is Asn, 2-Nap, Aib, Arg, Cit, Asp, Phe, Gly, Lys, Leu, Ala, (D)Ala, beta-Ala, His, Thr, n-Leu, Gin, Ser, (D)Ser, Tic, Trp, alpha-MeGln, alpha-MeAsn, alpha-MeLys(Ac), Dab(Ac), Dap(Ac), homo-Lys(Ac), or Lys(Ac).

74. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 1-72, wherein X14 is Asn.

75. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1, wherein the peptide inhibitor comprises an amino acid sequence of Formula (XllIa), (XllIb), (XIIIc), or (XIII d): Pen- Asn-Thr-X7-Gln-Pen-[F(4-2ae)]-X11-[α-MeLeu]-Lys(Ac)-Asn-[Pal]-X16 (XllIa) (SEQ ID NO:478), Pen-Gln-Thr-X7-Gln-Pen-[F(4-2ae)]-X11-[α-MeLeu]-Lys(Ac)-Asn-[Pal]-X16 (XllIb) (SEQ ID NO:479), Abu- Asn-Thr-X7-Gln-Cys-[F(4-2ae)]-X11-[α-MeLeu]-Lys(Ac)-Asn-[Pal]-X16 (XIIIc) (SEQ ID NO:480), Abu-Gln-Thr-X7-Gln-Pen-[F(4-2ae)]-X11-[α-MeLeu]-Lys(Ac)-Asn-[Pal]-X16 (XllId) (SEQ ID NO:481), wherein X7 and X11 are as described in claim 1; F(4-2-ae) is Phe[4-(2-aminoethoxy)]; Pal is 2Pal, 3Pal, or 4Pal; and X16 is any amino acid; wherein 2Pal is 2-pyridyl substituted alanine, and 3Pal is 3-pyridyl substituted alanine, and 4Pal is 4-pyridyl substituted alanine

76. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1, wherein the peptide inhibitor comprises an amino acid sequence of Formula (XlVa), (XlVb), (XIVc), (XlVd), (XlVe), (XlVf), (XlVg), or (XlVh): Pen- Asn-Thr-X7-Gln-Pen-[F(4-2ae)]-X11-[α-MeLeu]-Lys(Ac)-Asn-X15-Sarc (XlVa) (SEQ ID NO:482), Pen-Gin- Thr-X7-Gln-Pen-[F(4-2ae)]-X11-[α-MeLeu]-Lys(Ac)-Asn-X15-Sarc (XlVb) (SEQ ID NO:483), Abu- Asn-Thr-X7-Gln-Cys-[F(4-2ae)]-X11-[α-MeLeu]-Lys(Ac)-Asn-X15-Sarc (XIVc) (SEQ ID NO:484), or Abu-Gln-Thr-X7-Gln-Pen-[F(4-2ae)]-X11-[α-MeLeu]-Lys(Ac)-Asn-X15-Sarc (XlVd) (SEQ ID NO:485), Pen- Asn-Thr-X7-Gln-Pen-[F(4-2ae)]-X11-[α-MeLeu]-Lys(Ac)-Asn-X15-(D)NMeTyr (XlVe) (SEQ ID NO:486), Pen-Gin- Thr-X7-Gln-Pen- [F (4-2ae)] -X 11 - [α-MeLeu] -Lys(Ac)-Asn-X15-(D)NMeTyr (XIV f) (SEQ ID NO:487), Abu- Asn-Thr-X7-Gln-Cys-[F(4-2ae)]-X11-[α-MeLeu]-Lys(Ac)-Asn-X15-(D)NMeTyr (XlVg) (SEQ ID NO:488), or Abu-Gln-Thr-X7-Gln-Pen- [F (4-2ae)] -X 11 - [α-MeLeu] -Lys(Ac)-Asn-X15-(D)NMeTyr (XlVh) (SEQ ID NO:489), wherein X7 and X11 are as described in claim 1; F(4-2-ae) is Phe[4-(2-aminoethoxy)]; X15 is any amino acid; and the peptide inhibitor is cyclized via a Pen-Pen disulfide bond; or a Abu-Cys or Abu-Pen thioether bond.

77. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 1-76, wherein X7 is Trp unsubstiuted or substituted with cyano, halo, alkyl, haloalkyl, hydroxy, alkoxy, phenyl, substituted phenyl, or thienyl; and X11 is as described in claim 1.

78. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 1-76, wherein X7 is Trp substituted with cyano, halo, alkyl, haloalkyl, hydroxy, alkoxy, phenyl, substituted phenyl, or thienyl; and the substitution is at 4-, 5-, 6- or 7- position.

79. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 1-76, wherein X7 is Trp substituted with cyano, F, Cl, Br, I, Me, Et, i-Pr, n-Pr, n- Bu, t-Bu, CPs, hydroxy, OMe, OEt; and the substitution is at 4-, 5-, 6- or 7- position.

80. The peptide inhibitor or pharmaceutically acceptable salt or solvate thereof of any one of claims 1-76, wherein X7 is Trp substituted with i) phenyl, unsubstituted or substituted with cyano, halo, alkyl, haloalkyl, aryl hydroxy, alkoxy, or haloalkoxy; or ii) thienyl.

81. The peptide inhibitor or pharmaceutically acceptable salt or solvate thereof of any one of claims 1-76, wherein X7 is Trp substituted with phenyl, unsubstituted or substituted with Me, Et, n-Pr, i-Pr, t-Bu, OMe, OEt, Cl, F, CF3, OCF3, phenyl, substituted phenyl, or amido.

82. The peptide inhibitor or pharmaceutically acceptable salt or solvate thereof of any one of claims 1-76, wherein X7 is Trp substituted with unsubstituted phenyl; or unsubstitued thienyl.

83. The peptide inhibitor or pharmaceutically acceptable salt or solvate thereof of any one of claims 1-76, wherein X7 is Trp substituted with 7-Ph

84. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 1-76, wherein X7 is Trp substituted with 5-F, 6-F, 7-F, 5- Cl, 6-Cl, 7-Cl, 5-Me, 6- Me, 7-Me, 5-OH, 6-OH, 7-OH, 5-OMe, 6-OMe, or 7-OMe.

85. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 1-76, wherein X7 is Trp substituted with 7-Me, 5-F, 7-F, 6-Cl, 6-Me, 4-OMe, 5- OMe, or 5-Br.

86. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 1-76, wherein X7 is Trp substituted with 7-Me, 6-Me, 4-OMe, or 6-Cl.

87. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 1-76, wherein X7 is Trp substituted with 7-Me or 7-Ph.

88. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 1-76, wherein X7 is Trp substituted with 7-Me.

89. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 1-76, wherein X7 is Trp substituted with 7-Ph.

90. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1, wherein the peptide inhibitor comprises an amino acid sequence of Formula (XVa), (XVb), (XVc), or (XVd): Pen- Asn-Thr-[W(7-Me)]-Gln-Pen-[F(4-2ae)]-X11-[α-MeLeu]-Lys(Ac)-Asn-[Pal]-X16 (XVa) (SEQ ID NO:490), Pen-Gln-Thr- [ W(7 -Me)] -Gin-Pen- [F (4-2ae)] -X 11 - [α-MeLeu] -Lys(Ac)- Asn- [Pal] -X16 (XVb) (SEQ ID NO:491), Abu- Asn-Thr-[W(7-Me)]-Gln-Cys-[F(4-2ae)]-Xl 1 - [α-MeLeu] -Lys(Ac)-Asn- [Pal] -X16 (XVc) (SEQ ID NO:492), or Abu-Gln-Thr- [ W(7 -Me)] -Gin-Pen- [F (4-2ae)] -X 11 - [α-MeLeu] -Lys(Ac)-Asn- [Pal] -X16 (XV d) (SEQ ID NO:493), wherein X11 is as described in claim 1; F(4-2-ae) is Phe[4-(2-aminoethoxy)]; Pal is 2Pal, 3Pal, or 4Pal; and X16 is any amino acid; and the peptide inhibitor is cyclized via a Pen-Pen disulfide bond; or a Abu-Cys or Abu-Pen thioether bond.

91. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1, wherein the peptide inhibitor comprises an amino acid sequence of Formula (XVIa), (XVIb), (XVIc), (XVId), (XVIe), (XVIf), (XVIg), or (XVIh): Pen- Asn-Thr-[W(7-Me)]-Gln-Pen-[F(4-2ae)]-X11-[α-MeLeu]-Lys(Ac)-Asn-X15-Sarc (XVIa) (SEQ ID NO:494), Pen-Gln-Thr-[W(7-Me)]-Gln-Pen-[F(4-2ae)]-X11-[α-MeLeu]-Lys(Ac)-Asn-X15-Sarc (XVIb) (SEQ ID NO:495), Abu- Asn-Thr-[W(7-Me)]-Gln-Cys-[F(4-2ae)]-X11-[α-MeLeu]-Lys(Ac)-Asn-X15-Sarc (XVIc) (SEQ ID NO:496), or Abu-Gln-Thr-[W(7-Me)]-Gln-Pen-[F(4-2ae)]-X11-[α-MeLeu]-Lys(Ac)-Asn-X15-Sarc (XVId) (SEQ ID NO:497), Pen- Asn-Thr- [W(7 -Me)] -Gin-Pen- [F (4-2ae)] -X 11 - [α-MeLeu] -Lys(Ac)-Asn-X15-(D)NMeTyr (XVIe) (SEQ ID NO:498), Pen-Gln-Thr-[W(7-Me)]-Gln-Pen-[F(4-2ae)]-X11-[α-MeLeu]-Lys(Ac)-Asn-X15-(D)NMeTyr (XVIf) (SEQ ID NO:499), Abu- Asn-Thr- [W(7 -Me)] -Gln-Cys- [F (4-2ae)] -X 11 - [α-MeLeu] -Lys(Ac)-Asn-X15-(D)NMeTyr (XVIg) (SEQ ID NO:500), or Abu-Gln-Thr-[W(7-Me)]-Gln-Pen-[F(4-2ae)]-X11-[α-MeLeu]-Lys(Ac)-Asn-X15-(D)NMeTyr (XVIh) (SEQ ID NO:501), wherein X11 is as described in claim 1; F(4-2-ae) is Phe[4-(2-aminoethoxy)]; X15 is any amino acid; and the peptide inhibitor is cyclized via a Pen-Pen disulfide bond; or a Abu-Cys or Abu- Pen thioether bond.

92. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 1-91, wherein X11 is 2-Nal, Phe(2-Me), Phe(3-Me), Phe(4-Me), Phe(3,4- dimethoxy), or 1-Nal.

93. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 1-91, wherein X11 is 2-Nal, or 1-Nal.

94. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 1-91, wherein X11 is 2-Nal.

95. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1, wherein the peptide inhibitor comprises an amino acid sequence of Formula (XVIIa), (XVIIb), (XVIIc), or (XVIId): Pen- Asn-Thr- [W(7-Me)] -Gin-Pen- [F (4-2ae)] - [2-Nal] - [α-MeLeu] -Lys(Ac)-Asn- [Pal] -X16 (XVIIa) (SEQ ID NO:502), Pen-Gin- Thr- [W(7 -Me)] -Gin-Pen- [F (4-2ae)] - [2-Nal] - [α-MeLeu] -Lys(Ac)-Asn- [Pal] -X16 (XVIIb) (SEQ ID NO:503), Abu- Asn-Thr- [W(7-Me)] -Gln-Cys- [F (4-2ae)] - [2-Nal] - [α-MeLeu] -Lys(Ac)- Asn- [Pal] -X16 (XVIIc) (SEQ ID NO:504), or Abu-Gln-Thr- [W (7 -Me)] -Gin-Pen- [F (4-2ae)] - [2-Nal] - [α-MeLeu] -Lys(Ac)-Asn- [Pal] -X16 (XVIId) (SEQ ID NO:505), wherein F(4-2-ae) is Phe[4-(2-aminoethoxy)]; Pal is 2Pal, 3Pal, or 4Pal; and X16 is any amino acid; and the peptide inhibitor is cyclized via a Pen-Pen disulfide bond; or a Abu-Cys or Abu- Pen thioether bond.

96. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1, wherein the peptide inhibitor comprises an amino acid sequence of Formula (XVIIIa), (XVIIIb), (XVIIIc), (XVIIId), (XVIIIe), (XVIIIf), (XVIIIg), or (XVIIIh): Pen- Asn-Thr-[W(7-Me)]-Gln-Pen-[F(4-2ae)]-[2-Nal]-[α-MeLeu]-Lys(Ac)-Asn-X15-Sarc (XVIIIa) (SEQ ID NO:506), Pen-Gln-Thr-[W(7-Me)]-Gln-Pen-[F(4-2ae)]-[2-Nal]-[α-MeLeu]-Lys(Ac)-Asn-X15-Sarc (XVIIIb), (SEQ ID NO: 507) Abu- Asn-Thr- [W(7-Me)] -Gln-Cys- [F (4-2ae)] - [2-Nal] - [α-MeLeu] -Lys(Ac)- Asn-X15-Sarc (XVIIIc) (SEQ ID NO:508), Abu-Gln-Thr-[W(7-Me)]-Gln-Pen-[F(4-2ae)]-[2-Nal]-[α-MeLeu]-Lys(Ac)-Asn-X15-Sarc (XVIIId) (SEQ ID NO:509), Pen- Asn-Thr-[W(7-Me)]-Gln-Pen-[F(4-2ae)]-[2-Nal]-[α-MeLeu]-Lys(Ac)-Asn-X15- (D)NMeTyr (XVIIIe) (SEQ ID NO:510), Pen-Gln-Thr- [ W(7 -Me)] -Gin-Pen- [F (4-2ae)] - [2-Nal] - [α-MeLeu] -Ly s(Ac)-Asn-X15- (D)NMeTyr (XVIIIf) (SEQ ID NO:511), Abu- Asn-Thr- [W (7 -Me)] -Gln-Cys- [F (4-2ae)] - [2-Nal] - [α-MeLeu] -Lys(Ac)-Asn-X15- (D)NMeTyr (XVIIIg) (SEQ ID NO:512), or Abu-Gln-Thr- [W(7 -Me)] -Gin-Pen- [F (4-2ae)] - [2-Nal] - [α-MeLeu] -Lys(Ac)- Asn-X15- (D)NMeTyr (XVIIIh) (SEQ ID NO:513), wherein F(4-2-ae) is Phe[4-(2-aminoethoxy)]; X15 is any amino acid; and the peptide inhibitor is cyclized via a Pen-Pen disulfide bond; or a Abu-Cys or Abu-Pen thioether bond.

97. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 1-96, wherein X15 is 2Pal, 3Pal, 4Pal, His, (D)His, Lys, (D)Lys, Leu, (D)Leu, 2Quin, or 3 Quin.

98. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 1-96, wherein X15 is 3Pal, 4Pal, His, (D)His, (D)Lys or (D)Leu.

99. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 1-96, wherein X15 is 3Pal, His, (D)Lys or (D)Leu.

100. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 1-96, wherein X15 is His.

101. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 1-96, wherein X15 is 3Pal.

102. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 1-101, wherein X16 is absent.

103. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 90-102, wherein W(7-Me) is replaced with W(7-Ph).

104. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 1-103, wherein the peptide inhibitor comprises the structure of Formula (Z): R1-X-R2 (Z) wherein R1 is a hydrogen, Ac, a C1-C6 alkyl, a C6-C12 aryl, a C6-C12aryl-C1-6alkyl, a C1-C20 alkanoyl, and including PEGylated versions alone or as spacers of any of the foregoing; X is the amino acid sequence of Formula (I), (la), (lb), (Ic), (Id), or any of Formula (Il)-(XVIIId); and R2 is OH, NH2 or N(H)Me.

105. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 104, wherein the peptide inhibitor comprises the structure of Formula (Z'): R1 -X3 -X4-X5 -X6-X7-X8-X9-X10-X11-X12-X13-X14-X15-X16-R2 (Z') wherein R1 is a hydrogen, Ac, a C1-C6 alkyl, a C6-C12 aryl, a C6-C12aryl-C1-6alkyl, a C1-C20 alkanoyl, and including PEGylated versions alone or as spacers of any of the foregoing; and R2 is OH, NH2 or N(H)Me.

106. The peptide inhibitor or pharmaceutically acceptable salt thereof claim 105, wherein X4 is (D)Pen, Pen, or Pen(sulfoxide).

107. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 105 to 106, wherein X4 is Pen.

108. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 105 to 107, wherein X9 is Pen or (D)Pen.

109. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 105 to 108, wherein X9 is Pen.

110. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 105 to 109, wherein X4 is Pen and X9 is Pen, and the bond is a disulfide bond.

111. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 105 to 110, wherein the peptide inhibitor comprises the structure of Formula (Z'): R1-X3 -Pen-X5 -X6-X7-X8-Pen-X10-X11-X12-X13-X14-X15 -X16-R2 (Z' -A) wherein the peptide inhibitor is cyclized via a Pen-Pen disulfide bond.

112. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 105 to 111, wherein X5 is Asn, Ser, Gin, or Glu.

113. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 105 to 112, wherein X5 is Asn.

114. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 105 to 113, wherein the peptide inhibitor comprises the structure of Formula (Z'): R1-X3-Pen-Asn-X6-X7-X8-Pen-X10-X11-X12-X13-X14-X15 -X16-R2 (Z' -B) wherein the peptide inhibitor is cyclized via a Pen-Pen disulfide bond.

115. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 105 to 114, wherein X6 is Thr.

116. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 105 to 115, wherein the peptide inhibitor comprises the structure of Formula (Z'): R1-X3-Pen-Asn-Thr-X7-X8-Pen-X10-X11-X12-X13-X14-X15 -X16-R2 (Z' -C) wherein the peptide inhibitor is cyclized via a Pen-Pen disulfide bond.

117. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 105 to 116, wherein X8 is Gin, alpha-Me-Lys, alpha-MeLys(Ac), Lys(Ac), or Glu.

118. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 105 to 117, wherein X8 is Lys(Ac).

119. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 105 to 118, wherein the peptide inhibitor comprises the structure of Formula (Z'): R1 -X3 -Pen-Asn-Thr-X7 -Lys(Ac)-Pen-X10-X11-X12-X13-X14-X15 -X16-R2 (Z' -D) wherein the peptide inhibitor is cyclized via a Pen-Pen disulfide bond.

120. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 105 to 119, wherein X10 is Phe, Phe[4-(2-aminoethoxy)], Phe[4-(2- acetylaminoethoxy)], or Phe(4-CONFl2).

121. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 105 to 120, wherein X10 is Phe[4-(2-aminoethoxy)], or Phe[4-(2- acetylaminoethoxy)] .

122. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 105 to 121, wherein X10 is Phe[4-(2-aminoethoxy)].

123. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 105 to 122, wherein the peptide inhibitor comprises the structure of Formula (Z'): R1-X3 -Pen-Asn-Thr-X7-Lys(Ac)-Pen- [F(4-2ae)] -X11-X12-X13-X14-X15-X16-R2 (Z'-E) (SEQ ID NO:514) wherein F(4-2-ae) is Phe[4-(2-aminoethoxy)], and the peptide inhibitor is cyclized via a Pen-Pen disulfide bond.

124. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 105 to 123, wherein X11 is 2-Nal, Phe(2-Me), Phe(3-Me), Phe(4-Me), Phe(3,4- dimethoxy), or 1-Nal.

125. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 105 to 124, wherein X11 is 2-Nal, or 1-Nal.

126. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 105 to 125, wherein X11 is 2-Nal.

127. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 105 to 126, wherein the peptide inhibitor comprises the structure of Formula (Z'): R7-X3 -Pen-Asn-Thr-X7 -Lys(Ac)-Pen- [F(4-2ae)] - [2-Nal] -X12-X13-X14-X15-X16-R2 (Z' -F) (SEQ ID NO:515) wherein F(4-2-ae) is Phe[4-(2-aminoethoxy)], and the peptide inhibitor is cyclized via a Pen-Pen disulfide bond.

128. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 105 to 127, wherein X12 is 4-amino-4-carboxy-tetrahydropyran (THP), alpha- MeLys, alpha-MeLeu, Ala, cyclohexylAla, Lys, or Aib.

129. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 105 to 128, wherein X12 is THP.

130. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 105 to 129, wherein the peptide inhibitor comprises the structure of Formula (Z'): R1-X3-Pen-Asn-Thr-X7-Lys(Ac)-Pen- [F(4-2ae)] - [2-Nal] -THP-X13-X14-X15-X16-R2 (Z' -G) (SEQ ID NO:516) wherein F(4-2-ae) is Phe[4-(2-aminoethoxy)], and the peptide inhibitor is cyclized via a Pen-Pen disulfide bond.

131. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 105 to 130, wherein X13 is Glu, Gin, Lys(Ac), or Lys.

132. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 105 to 131, wherein X13 is Glu.

133. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 105 to 132, wherein the peptide inhibitor comprises the structure of Formula (Z'): R1 -X3 -Pen- Asn-Thr-X7-Lys(Ac)-Pen- [F(4-2ae)] - [2-Nal] -THP-Glu-X 14-X15-X16-R2 (Z' -H) (SEQ ID NO:517) wherein F(4-2-ae) is Phe[4-(2-aminoethoxy)], and the peptide inhibitor is cyclized via a Pen-Pen disulfide bond.

134. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 105 to 133, wherein X14 is Asn.

135. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 105 to 134, wherein the peptide inhibitor comprises the structure of Formula (Z'): R1-X3 -Pen-Asn-Thr-X7 -Lys(Ac)-Pen- [F(4-2ae)] - [2-Nal] -THP-Glu-Asn-X15-X16-R2 (Z’-l) (SEQ ID NO:518) wherein F(4-2-ae) is Phe[4-(2-aminoethoxy)], and the peptide inhibitor is cyclized via a Pen-Pen disulfide bond.

136. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 105 to 135, wherein X7 is Trp or Trp substituted with alkyl, or phenyl; and the substitution is at the 4-, 5-, 6- or 7- position.

137. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 105 to 136, wherein X7 is Trp or Trp substituted with Me, Et, i-Pr, n-Pr, n-Bu, t- Bu, or phenyl; and the substitution is at the 4-, 5-, 6- or 7- position.

138. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 105 to 137, wherein X7 is Trp or Trp substituted with 5-Me, 6-Me, 7-Me, 5- phenyl, 6-phenyl or 7-Ph.

139. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 105 to 138, wherein X7 is Trp or Trp substituted with 7-Me, 6-Me, or 7-Ph.

140. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 105 to 139, wherein X7 is Trp or Trp substituted with 7-Me or 7-Ph.

141. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 105 to 140, wherein X7 is Trp substituted with 7-Me.

142. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 105 to 141, wherein the peptide inhibitor comprises the structure of Formula (Z'): R1-X3 -Pen-Asn-Thr- [W(7-Me)] -Lys(Ac)-Pen- [F(4-2ae)] - [2-Nal] -THP-Glu- Asn-X15-X16-R2 (Z'-J) wherein F(4-2-ae) is Phe[4-(2-aminoethoxy)], and the peptide inhibitor is cyclized via a Pen-Pen disulfide bond.

143. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 105 to 142, wherein X3 is absent or (D)Arg.

144. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 105 to 143, wherein X3 is absent.

145. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 105 to 143, wherein X3 is (D)Arg.

146. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 105 to 143, wherein the peptide inhibitor comprises the structure of Formula (Z'): R1-Pen-Asn-Thr- [W(7-Me)] -Lys(Ac)-Pen- [F(4-2ae)] - [2-Nal] -THP-Glu-Asn-X15-X16-R2 (Z' -K) wherein F(4-2-ae) is Phe[4-(2-aminoethoxy)], and the peptide inhibitor is cyclized via a Pen-Pen disulfide bond.

147. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 105, wherein X3 is absent or (D)Arg; X4 is Abu, Cys, (D)Cys, alpha-MeCys, or Pen; X5 is Ala, (allyl)Gly, lie, Leu, Asn, Nle, or Gin; X6 is Asp, or Thr; X7 is (7-methyl)Trp, (4-F)Trp, or Trp; X8 is Cit, Lys(Ac), Lys(Benzyl, Ac), Lys(butyl, Ac), Lys(isobutyl,Ac), Lys(propyl,Ac),Gln, 4- adamantyl-Phe, (4-AcNFI)Phe, or Tyr; X9 is Cys, alpha-MeCys, or Pen; X10 is Phe or substituted Phe, Tyr or substituted Tyr; X11 is 2-Nal; X12 is 4-amino-4-carboxy-tetrahydropyran (TFIP), Acpx, Acvc, alpha-MeLys, or alpha-MeLeu; X13 is alpha-methylGlu, Glu, or Lys(Ac); and X14 is Asn.

148. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 104 to 147, wherein R1 is H or C1-C20 alkanoyl.

149. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 104 to 148, wherein R1 is H or Ac.

150. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 104 to 149, wherein R1 is Ac.

151. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 104 to 150, wherein R2 is NH2 or N(FI)Me.

152. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 104 to 151, wherein R2 is NH2.

153. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 105 to 151, wherein R1 is Ac; X3 is absent or (D)Arg; X4 is Pen; X5 is Asn; X6 is Thr; X7 is Trp or (7-Me)Trp or (7-Ph)Trp; X8 is Lys(Ac); X9 is Pen; X10 is Phe(2-aminoethoxy); X11 is 2-Nal; X12 is 4-amino-4-carboxy-tetrahydropyran (THP); X13 is Gin; X14 is Asn; and R2 is NH2 or N(H)Me.

154. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 153, wherein R1 is Ac; X3 is absent; X4 is Pen; X5 is Asn; X6 is Thr; X7 is 7-methylTrp; X8 is Lys(Ac); X9 is Pen; X10 is Phe(2-aminoethoxy); X11 is 2-Nal; X12 is 4-amino-4-carboxy-tetrahydropyran (THP); X13 is Glu; X14 is Asn; and R2 is NH2 or N(H)Me.

155. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 105 to 154, wherein X15 is Aib, beta-Ala, (D)Phe, (D)Lys, (D)Leu, (D)Om, substituted (D)Phe, (D)Arg, (D)Val, (D)Tyr, Phe, Hph, Asn, 4-amino-4-carboxy-tetrahydropyran (THP), substituted Tyr, or Tyr; and XI 6 is beta-Ala, (D)NMeTyr, (D)Pro, NMeTyr, Pro, or Sarc.

156. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 105 to 154, wherein X15 is 3Pal, substituted 3Pal, 4Pal, 4-triazole-Ala, (D)His, His or substituted His; and XI 6 is absent, Aib, alpha- MePro, (D)Leu, (D)NMeTyr, (D)Pro, (D)Tyr, substituted Gly, MeLeu, MeNLe, Pro, Paf, 4-di-fluoro-Pro, Sarc, or Tyr.

157. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 105 to 154 or 156, wherein X15 is (D)His, substituted His, 2Pal, 3Pal, 4Pal, 4TriazolAla, or 5Pyal; and XI 6 is absent, (D)NMeTyr or Sarc.

158. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 105 to 154, 156 or 157, wherein X15 is (3-Me)His or 3Pal; and XI 6 is absent or Sarc.

159. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 105 to 154 or 156 to 158, wherein the peptide inhibitor comprises the structure of Formula (Z'): Ac-Pen-Asn-Thr- [W(7 -Me)] -Lys(Ac)-Pen- [F (4-2ae)] - [2-Nal] -THP-Glu-Asn- [3 -Pal] -X16-NH2 (Z'-L) wherein F(4-2-ae) is Phe[4-(2-aminoethoxy)], and the peptide inhibitor is cyclized via a Pen-Pen disulfide bond.

160. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 105 to 159, wherein the peptide inhibitor comprises the structure of Formula (Z'): Ac-Pen-Asn-Thr-[W(7-Me)]-Lys(Ac)-Pen-[F(4-2ae)]-[2-Nal]-THP-Glu-Asn-X15-Sarc-NH2 (Z'- M) wherein F(4-2-ae) is Phe[4-(2-aminoethoxy)], and the peptide inhibitor is cyclized via a Pen-Pen disulfide bond.

161. The peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 105 to 154 or 156 to 160, wherein X15 is 3Pal; and XI 6 is Sarc.

162. A peptide inhibitor of an interleukin-23 receptor, wherein the peptide inhibitor comprises or is any one of the amino acid sequence set forth in any of Table El A and Table E IB; or a pharmaceutically acceptable salt thereof.

163. The peptide inhibitor of claim 162, wherein the peptide inhibitor comprises or is any one of the amino acid sequence listed below: Ac-[(D)Arg]-[Abu]-Q-T-[W(7-Ph)]-[Lys(Ac)]-[Cys]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a- MeLys] - [Lys(Ac)] -N-dK- [Sarc] -NH2 (SEQ ID NO:l); Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [3 -Quin] - [a-MeLys] - [Lys(Ac)]-N-[(D)Leu)]-[Sarc]-NH2 (SEQ ID NO:2); Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [3 -Quin] - [THP] -E-N- [(D)Lys] - [Sarc] -NH2 (SEQ ID NO:3); Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [3 -Quin] - [a-MeLys] - [Lys(Ac)] -N- [(D)His] - [Sarc] -NH2 (SEQ ID NO:4); Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [3 -Quin] - [a-MeLys] - [Lys(Ac)] -N-H- [Sarc] -NH2 (SEQ ID NO:5); Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [3 -Quin] - [THP] -E-N- [(D)Leu)]-[Sarc]-NH2 (SEQ ID NO:6); Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [3 -Quin] - [a-MeLys] - [Lys(Ac)] -N- [(D)Lys] - [Sarc] -NH2 (SEQ ID NO:7); Ac- [(D)Arg] - [Abu] -Q-T - W-Q- [Cys] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [THP] -E-N-N- [(D)NMeTyr] -NH2 (SEQ ID NO: 8); Ac-[(D)Arg]-[Pen]-Q-T-W-Q-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-N- [(D)NMeTyr] -NH2 (SEQ ID NO: 9); Ac- [(D)Arg] - [Pen] -Q-T -W-Q- [Pen] -Phe [4-(2-aminoethoxy)] - [2-Nal] - [THP] - [aMeGlu] -N-F - [(D)NMeTyr] -NH2 (SEQ ID NO: 10); Ac- [Pen] -N-T - [W (7 -Ph)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [3 Quin] - [THP] -E-N- [(D)Lys] - [Sarc] -NH2 (SEQ ID NO:l 1); Ac- [Pen] -N-T - [W (7 -Ph)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [3 Quin] - [a-MeLys] - [Lys(Ac)] -N- [(D)Lys] - [Sarc] -NH2 (SEQ ID NO: 12); Ac- [Pen] -N-T - [W (7 -Ph)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [3 Quin] - [THP] -E-N- [(D)Leu] - [Sarc] -NH2 (SEQ ID NO: 13); Ac- [Pen] -N-T - [W (7 -Ph)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [3 Quin] - [a-MeLys] - [Lys(Ac)] -N- [(D)Leu] - [Sarc] -NH2 (SEQ ID NO: 14); Ac- [Pen] -N-T - [W (7 -Ph)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [3 Quin] - [THP] -E-N-H- [Sarc]-NH2 (SEQ ID NO: 15); Ac- [Pen] -N-T - [W (7 -Ph)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [3 Quin] - [a-MeLys] - [Lys(Ac)] -N-H- [Sarc] -NH2 (SEQ ID NO: 16); Ac- [Abu] -Q-T - [ W(7 -Me)] - [Lys(Ac)] - [Cys] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [a-MeLys] - [Lys(Ac)] -N- [(D)Lys] - [Sarc] -NH2 (SEQ ID NO: 17); Ac-[Abu]-Q-T-[W(7-Ph)]-[Lys(Ac)]-[Cys]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]- [Lys(Ac)] -N- [(D)Lys] - [Sarc] -NH2 (SEQ ID NO: 18); Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [a-MeLys] - [Lys(Ac)] -N- [(D)Leu] - [Sarc] -NH2 (SEQ ID NO:20); Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [a-MeLys] - [Lys(Ac)] -N- [(D)Lys] - [Sarc] -NH2 (SEQ ID NO:21); Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [THP] -E-N-H- [Sarc]-NH2 (SEQ ID NO:22); Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [a-MeLys] - [Lys(Ac)] -N-H- [Sarc] -NH2 (SEQ ID NO:23); Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [THP] -E-N- [(D)Leu] - [Sarc] -NH2 (SEQ ID NO:24); Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [a-MeLys] - [Lys(Ac)] -N- [(D)Leu] - [Sarc] -NH2 (SEQ ID NO:25); Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Gly)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-N al] - [THP] -E-N-H- [Sarc]-NH2 (SEQ ID NO:26); Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Gly)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-N al] - [a-MeLys] - [Lys(Ac)] -N-H- [Sarc] -NH2 (SEQ ID NO:27); Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Gly)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-N al] - [THP] -E-N- [(D)Leu] - [Sarc] -NH2 (SEQ ID NO:28); Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Gly)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-N al] - [a-MeLys] - [Lys(Ac)] -N- [(D)Leu] - [Sarc] -NH2 (SEQ ID NO:29); Ac-[Pen]-N-T-[W(7-Me)]-[Lys(bAla)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-H- [Sarc]-NH2 (SEQ ID NO:30); Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(bAla)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [a-MeLys] - [Lys(Ac)] -N-H- [Sarc] -NH2 (SEQ ID NOG 1); Ac-[Pen]-N-T-[W(7-Et)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-H- [Sarc]-NH2 (SEQ ID NO: 32); Ac- [Pen] -N-T - [W (7 -Et) ] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [a-MeLys] - [Lys(Ac)] -N-H- [Sarc] -NH2 (SEQ ID NO:33); Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [ W(7 -Et)] - [a-MeLys] - [Lys(Ac)] -N-H- [Sarc] -NH2 (SEQ ID NO:34); Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [ W(4-Me)] - [a-MeLys] - [Lys(Ac)] -N-H- [Sarc] -NH2 (SEQ ID NO:35); Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [ W(6-Me)] - [a-MeLys] - [Lys(Ac)] -N-H- [Sarc] -NH2 (SEQ ID NO:36); Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [ W(4-OMe)] - [a-MeLys] - [Lys(Ac)] -N-H- [Sarc] -NH2 (SEQ ID NO:37); Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [ W(7 -i-Pr)] - [a-MeLys] - [Lys(Ac)] -N-H- [Sarc] -NH2 (SEQ ID NO:38); Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [ W(7 -nPr)] - [a-MeLys] - [Lys(Ac)] -N-H- [Sarc] -NH2 (SEQ ID NO:39); Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [ W(7-OMe)] - [a-MeLys] - [Lys(Ac)] -N-H- [Sarc] -NH2 (SEQ ID NO:40); Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [ W(6-C1)] - [a-MeLys] - [Lys(Ac)] -N-H- [Sarc] -NH2 (SEQ ID NO:41); Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [ W(5 -OMe)] - [a-MeLys] - [Lys(Ac)] -N-H- [Sarc] -NH2 (SEQ ID NO:42); Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [ W(3 -MePh)] - [a-MeLys] - [Lys(Ac)] -N-H- [Sarc] -NH2 (SEQ ID NO:43); Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [ W(6-Ph)] - [a-MeLys] - [Lys(Ac)] -N-H- [Sarc] -NH2 (SEQ ID NO:44); Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [ W(6-Et)] - [a-MeLys] - [Lys(Ac)] -N-H- [Sarc] -NH2 (SEQ ID NO:45); Ac-[Pen]-N-T-[W(7-(2-FPh)]- [Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]- [Lys(Ac)] -N-H- [Sarc] -NH2 (SEQ ID NO:46); Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [a-MeLys] - [Lys(Ac)] -N- [(D)Leu] - [(D)NMeTyr] -NH2 (SEQ ID NO:47); Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [a-MeLys] - [Ly s(Ac) ] -N- [(D)Ly s] - [(D)NMeT yr] -NH2 (SEQ ID NO:48); Ac-[Pen]-N-T-[W(7-(2-OMePh)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]- [Lys(Ac)] -N-H- [Sarc] -NH2 (SEQ ID NO:49); Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [ W(7 -Ph)] - [a-MeLys] - [Lys(Ac)] -N-H- [Sarc] -NH2 (SEQ ID NO:50); Ac- [Pen] -N-T - [W (7 -Ph)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [a-MeLys] - [Lys(Ac)] -N-H- [Sarc] -NH2 (SEQ ID N0:51); Ac-[Pen]-N-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-H- [Sarc]-NH2 (SEQ ID NO: 52); Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [3 Quin] - [THP] -E-N-H- [Sarc]-NH2 (SEQ ID NO:53); Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [THP] -E- S-H- [Sarc]-NH2 (SEQ ID NO: 54); Ac-[Pen]-S-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-H- [Sarc]-NH2 (SEQ ID NO:55); Ac-[Pen]-S-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-S-H- [Sarc]-NH2 (SEQ ID NO:56); Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [THP] -E-N-H- [(D)NMeTyr] -NH2 (SEQ ID NO: 57); Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [a-MeLys] - [Ly s(Ac) ] -N-F - [(D)NMeT yr] -NH2 (SEQ ID NO:58); Ac-[Pen]-N-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-S-H- [Sarc]-NH2 (SEQ ID NO:59); Ac-[Pen]-S-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-H- [Sarc]-NH2 (SEQ ID NO: 60); Ac-[Pen]-S-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-S-H- [Sarc]-NH2 (SEQ ID NO:61); Ac-[Pen]-N-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-H- [(D)NMeTyr] -NH2 (SEQ ID NO: 62); Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [THP] -E- [(D)Asn] - H-[Sarc]-NH2 (SEQ ID NO:63); Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [THP] -E-G-H- [Sarc]-NH2 (SEQ ID NO: 64); Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [THP] -E- [h(Ser)] - H-[Sarc]-NH2 (SEQ ID NO:65); Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [THP] -E-N-H-P- NH2 (SEQ ID NO:66); Ac-[Pen]-N-T-[W(7-(2-Nal))]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-H- [Sarc]-NH2 (SEQ ID NO: 67); Ac-[Pen]-N-T-[W(7-3BiPh)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-H- [Sarc]-NH2 (SEQ ID NO: 68); Ac- [Pen] -N-T - [W (7-(Phenanthren-5 -yl))] - [Lys(Ac)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-Nal] - [THP] -E-N-H- [Sarc] -NH2 (SEQ ID NO:69); Ac- [Pen] -N-T - [W (7-(4-Anthracen-5 -yl))] - [Lys(Ac)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-Nal] - [THP] -E-N-H- [Sarc] -NH2 (SEQ ID NO:70); Ac-[Pen]-N-T-[W(7-(l-Nal))]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-H- [Sarc]-NH2 (SEQ ID NO:71); Ac-[Pen]-N-T-[W(7-(4BiPh))]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-H- [Sarc]-NH2 (SEQ ID NO: 72); Ac- [Pen] -N-T - [W (7-(3 ,5 -t-Bu-Ph))] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [THP] -E- N-H-[Sarc]-NH2 (SEQ ID NO:73); Ac- [Pen] -N-T- [W(7-Me)] - [Lys(Ac)] - [Pen] - [Phe(4-CONH2)] - [2-Nal] - [THP] -E-N-H- [Sarc] -NH2 (SEQ ID NO:74); Ac- [Pen] -N-T- [W(7-Me)] - [Lys(Ac)] - [Pen] - [Phe(4-OMe)] - [2-Nal] - [THP] -E-N-H- [Sarc] -NH2 (SEQ ID NO:75); Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [3 Quin] - [a-MeLys] - [Lys(Ac)] -N- [2Pal] -NH2 (SEQ ID NO:78); Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [a-MeLys] - [Lys(Ac)] -N- [2Pal] -NH2 (SEQ ID NO:79); Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [a-MeLys] - [Lys(Ac)] -N- [3Pal] -NH2 (SEQ ID NO:80); Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [THP] - [Lys(Ac)] - N-H-[Sarc]-NH2 (SEQ ID NO:81); Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [a-MeLys] - [Ly s(Ac) ] -N-H- [(D)NMeT yr] -NH2 (SEQ ID NO:82); Ac- [(D)Arg] - [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-Nal] - [a- MeLys] -E-N-H- [(D)NMeTyr]-NH2 (SEQ ID NO:83); Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [a-MeLys] - [Lys(Ac)]-N-Phe[4-aminomethyl]-[(D)NMeTyr]-NH2(SEQ ID NO:84); Ac- [Pen] -N-T - [W (7 -Me)] - [Cit] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-N al] - [aMeLeu] - [Lys(Ac)] -N- [(D)His]-NH2 (SEQ ID NO:85); Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [a-MeLys] - [Lys(Ac)]-N-[(D)His]-NH2 (SEQ ID NO:86); Ac- [(D)Arg] - [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-Nal] - [THP] -E- N- [(D)His] - [(D)NMeT yr] -NH2 (SEQ ID NO:87); Ac- [(D)Arg] - [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-Nal] - [THP] -E- N -N - [(D)NMeT yr] -NH2 (SEQ ID NO:88); Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [a-MeLys] - [Ly s(Ac) ] -N-N- [(D)NMeT yr] -NH2 (SEQ ID NO:89); Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [a-MeLys] - [Lys(Ac)] -N- [(D)V al] - [(D)NMeTyr] -NH2 (SEQ ID NO:90); Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [a-MeLys] - [Lys(Ac)] -N- [(D)Thr] - [(D)NMeTyr] -NH2 (SEQ ID NO:91); Ac- [(D)Arg] - [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-Nal] - [THP] -E- N-[(D)His]-NH2 (SEQ ID NO:92); Ac-[Abu]-N-T-[W(7-Ph)]-Q-[Cys]-Phe[4-(2-aminoethoxy)]-[3Quin]-[THP]-E-N-H-[Sarc]-NH2 (SEQ ID NO:93); Ac- [Abu] -N-T - [ W(7 -Me)] -Q- [Cys] -Phe [4-(2-aminoethoxy)] - [3 Quin] - [THP] -E-N-H- [Sarc] -NH2 (SEQ ID NO:94); Ac-[Abu]-N-T-[W(7-Ph)]-Q-[Cys]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N-H- [Sarc]-NH2 (SEQ ID NO:95); Ac-[Abu]-N-T-[W(7-Ph)]-Q-[Cys]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-H-[Sarc]-NH2 (SEQ ID NO:96); Ac-[Abu]-N-T-[W(7-Me)]-[Lys(Ac)]-[Cys]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]- [Lys(Ac)] -N-H- [Sarc] -NH2 (SEQ ID NO:97); Ac-[Abu]-N-T-[W(7-Ph)]-[Lys(Ac)]-[Cys]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-H- [Sarc]-NH2 (SEQ ID NO: 98); Ac-[Abu]-N-T-[W(7-Me)]-[Lys(Ac)]-[Cys]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-H- [Sarc]-NH2 (SEQ ID NO: 99); Ac-[(D)Arg]-[Abu]-S-T-[W(7-Me)]-Q-[Cys]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-H- [Sarc]-NH2 (SEQ ID NO: 100); Ac- [(D)Arg] - [Abu] -N-T - [ W(7 -Me)] -Q- [Cys] -Phe [4-(2-aminoethoxy)] - [2-Nal] - [THP] -E-N- [(D)Leu] - [Sarc] -NH2 (SEQ ID NO: 101); Ac-[(D)Arg]-[Abu]-N-T-[W(7-Me)]-[Cit]-[Cys]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-H- [Sarc]-NH2 (SEQ ID NO: 102); Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [a-MeLys] - [Lys(Ac)] -N- [3Pal] - [Sarc] -NH2 (SEQ ID NO: 103); Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]- [Sarc]-NH2 (SEQ ID NO: 104); Ac- [Pen] -N-T - [W (7 -Ph)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [a-MeLys] - [Lys(Ac)] -N- [3Pal] - [Sarc] -NH2 (SEQ ID NO: 105); Ac-[Pen]-N-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]- [Sarc]-NH2 (SEQ ID NO: 106); Ac- [Pen] -N-T - [W (7 -Me)] - [Cit] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-N al] - [THP] -E-N- [3Pal] - [Sarc]-NH2 (SEQ ID NO: 107); Ac-[Pen]-N-T-[W(7-Me)]-Q-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]-[Sarc]- NH2 (SEQ ID NO: 108); Ac-[Abu]-Q-T-[W(7-Me)]-Q-[Cys]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]-[Sarc]- NH2 (SEQ ID NO: 109); Ac- [Abu] -Q-T - [ W(7 -Me)] -Q- [Cys] -Phe [4-(2-aminoethoxy)] - [2-Nal] - [a-MeLys] - [Lys(Ac)] -N- [3Pal]-[Sarc]-NH2 (SEQ ID NOT 10); Ac-[Abu]-Q-T-[W(7-Me)]-[Cit]-[Cys]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]- [Sarc]-NH2 (SEQ ID NO: 111); Ac- [Abu] -Q-T - [ W(7 -Me)] - [Cit] - [Cys] -Phe [4-(2-aminoethoxy)] - [2-Nal] - [a-MeLys] - [Lys(Ac)] - N-[3Pal]-[Sarc]-NH2 (SEQ ID NO: 112); Ac- [Abu] -Q-T - [ W(7 -Me)] -Q- [Cys] -Phe [4-(2-aminoethoxy)] - [2-Nal] - [THP] -E-N- [3Pal] - [bA] - NH2 (SEQ ID NO: 113); Ac- [Abu] -Q-T - [ W(7 -Me)] -Q- [Cys] -Phe [4-(2-aminoethoxy)] - [2-Nal] - [THP] -E- S- [3 Pal] - [bA] - NH2 (SEQ ID NO: 114); Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [THP] -E-N- [4Pal] - [Sarc] -NH2 (SEQ ID NO: 115); Ac-[Pen]-N-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]- [bA]-NH2 (SEQ ID NO:l 16); Ac-[Pen]-N-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-[Lys(Ac)]-N- [3Pal]-[Sarc]-NH2 (SEQ ID NOT 17); Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [THP] -E-N- [3 Quin]- [Sarc] -NH2 (SEQ ID NO: 118); Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [THP] -E-N- [ 7 - Aza-tryptophan]-[Sarc]-NH2 (SEQ ID NO: 119); Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [a-MeLys] - [Lys(Ac)] -N- [3Pal] - [(D)NMeTyr] -NH2 (SEQ ID NO:120); Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]- [(D)NMeTyr] -NH2 (SEQ ID NO: 121); Ac-[Pen]-N-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]- [Lys(Ac)] -N- [3Pal] - [(D)NMeTyr] -NH2 (SEQ ID NO:122); Ac-[Pen]-N-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]- [(D)NMeTyr] -NH2 (SEQ ID NO: 123); Ac-[Pen]-S-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-S-[3Pal]- [Sarc]-NH2 (SEQ ID NO: 124); Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [THP] -E- S- [3Pal] - [Sarc]-NH2 (SEQ ID NO: 125); Ac-[Pen]-N-T-[W(7-Ph)]-[Cit]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]-[Sarc]- NH2 (SEQ ID NO: 126); Ac-[Pen]-N-T-[W(7-Ph)]-Q-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]-[Sarc]- NH2 (SEQ ID NO: 127); Ac- [Pen] -N-T - [W (7 -Ph)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [a-MeLys] - [Lys(Ac)]-N-[3Pal]-[bA]-NH2 (SEQ ID NOT30); Ac-[Pen]-N-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]- [bA]-NH2 (SEQ ID NO: 131); Ac-[Pen]-S-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]- [Sarc]-NH2 (SEQ ID NO: 132); Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [THP] - [Lys(Ac)] - N-[3Pal]-[Sarc]-NH2 (SEQ ID NO: 133); Ac-[Abu]-Q-T-[W(7-Ph)]-Q-[Cys]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]-[Sarc]- NH2 (SEQ ID NO: 134); Ac-[Abu]-Q-T-[W(7-Ph)]-Q-[Cys]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N- [3Pal]-[Sarc]-NH2 (SEQ ID NOT35); Ac-[Pen]-N-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-[Lys(Ac)]-N- [3Pal]-[Sarc]-NH2 (SEQ ID NOT36); Ac-[Pen]-N-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aceylaminoethoxy)]-[2-Nal]-[THP]- [Lys(Ac)] -N- [3Pal] - [Sarc] -NH2 (SEQ ID NO: 137); Ac- [Pen] -E-T- [W(7-Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [THP] - [Lys(Ac)] - N-[3Pal]-[Sarc]-NH2 (SEQ ID NO: 138); Ac-[Pen]-E-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-[Lys(Ac)]-N- [3Pal]-[Sarc]-NH2 (SEQ ID NO:139); Ac-[Abu]-Q-T-[W(7-Me)]-Q-[Cys]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]-[Sarc]- NH2 (SEQ ID NO: 140); Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [THP] - [Lys(Ac)] - N-[3Pal]-[Sarc]-NH2 (SEQ ID NO: 141); Ac- [Pen] -N-T - [W (7-(3 -carboxamidophenyl))] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2- Nal] - [THP] -E-N - [3Pal] - [Sarc] -NH2 (SEQ ID NO: 142); Ac-[Pen]-N-T-[W(7-pyrimidin-5-yl)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]- E-N- [3Pal]- [Sarc] -NH2 (SEQ ID NO: 143); Ac- [Pen] -N-T - [W (7 -imidazopyridinyl)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [THP] -E-N- [3Pal] - [Sarc] -NH2 (SEQ ID NO: 144); Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [NMe(Lys)] - [Lys(Ac)]-N-[His_3Me]-NH2 (SEQ ID NO: 145); Ac- [(D)Arg] - [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-Nal] - [THP] -E- N-[His_3Me]-NH2 (SEQ ID NO: 146); Ac-[Pen]-N-T-[W(7-(4Quin))]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N- [3Pal]-[Sarc]-NH2 (SEQ ID NO: 147); Ac-[Pen]-N-T-[(W(7-(3-pyrazol-l-yl))]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]- [THP] -E-N- [3Pal] - [Sarc] -NH2 (SEQ ID NO: 148); Ac-[Pen]-N-T-[(W(7-(5-Et))]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N- [3Pal]-[Sarc]-NH2 (SEQ ID NO: 149); Ac-[Pen]-N-T-[W(5-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]- [Sarc]-NH2 (SEQ ID NO: 150); Ac-[Pen]-N-T-[(W(7-(3-pyrazol-l-yl))]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]- [THP] -E-N- [3Pal] - [Sarc] -NH2 (SEQ ID NO: 151); Ac- [Pen] -N-T - [W (7 -indazol-5 -yl)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [THP] -E- N-[3Pal]-[Sarc]-NH2 (SEQ ID NO: 152); Ac-[Pen]-N-T-[W(4-F)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]- [Sarc]-NH2 (SEQ ID NO: 153); Ac-[Pen]-N-T-[W(5-CN)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]- [Sarc]-NH2 (SEQ ID NO: 154); Ac-[Pen]-N-T-[W(7-CN)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]- [Sarc]-NH2 (SEQ ID NO: 155); Ac-[Pen]-N-T-[W(4-OMe)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N- [3Pal]-[Sarc]-NH2 (SEQ ID NO:156); Ac-[Pen]-N-T-[W(4-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]- [Sarc]-NH2 (SEQ ID NO: 157); Ac-[Pen]-N-T-W-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]-[Sarc]- NH2 (SEQ ID NO: 158); Ac-[Pen]-N-T-W-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[Acvc]-E-N-[3Pal]-[Sarc]- NH2 (SEQ ID NO: 159, 285); Ac-[Pen]-N-T-[W(5-Ca)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]- [Sarc]-NH2 (SEQ ID NO: 160); Ac-[Pen]-N-T-[Trp_4Aza]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]- [Sarc]-NH2 (SEQ ID NO: 161); Ac-[Pen]-N-T-W-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]-[Sarc]- NH2 (SEQ ID NO: 162); Ac-[Pen]-N-T-W-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-[Lys(Ac)]-N-[3Pal]- [Sarc]-NH2 (SEQ ID NO: 163); Ac- [(D)Arg] - [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-Nal] - [THP] -E- N-[(5Pyal)]-NH2 (SEQ ID NO: 164); Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [a-Me-Lys] - [Lys(Ac)]-N-[(5Pyal)]-NH2 (SEQ ID NO:165); Ac- [(D)Arg] - [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-Nal] - [THP] -E- N-[(l-Me)His]-NH2 (SEQ ID NO: 166); Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [aMeLys] - [Lys(Ac)]-N-[(l-Me)His]-NH2 (SEQ ID NO: 167); or Ac- [Pen] -N -T - [ W(7 -Me] - [Lys(Ac)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-Nal] - [a-Me-Lys] - [Lys(Ac)] -N- [3Pal] - [(D)NMeTyr] -NH2 (SEQ ID NOT68); and wherein the peptide inhibitor is cyclized via a Pen-Pen disulfide bond; or via an Abu-C thioether bond; or a pharmaceutically acceptable salt thereof.

164. The peptide inhibitor of claim 163, wherein the peptide comprises or is: Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [a-MeLys] - [Lys(Ac)] -N- [3Pal] -NH2 (SEQ ID NO:80); Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]- [Sarc]-NH2 (SEQ ID NO: 104); Ac-[Pen]-N-T-[W(7-Me)]-Q-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]-[Sarc]- NH2 (SEQ ID NO: 108); Ac- [Abu] -Q-T - [ W(7 -Me)] -Q- [Cys] -Phe [4-(2-aminoethoxy)] - [2-Nal] - [a-MeLys] - [Lys(Ac)] -N- [3Pal] - [Sarc] -NH2 (SEQ ID NO:l 10); Ac- [Abu] -Q-T - [ W(7 -Me)] - [Cit] - [Cys] -Phe [4-(2-aminoethoxy)] - [2-Nal] - [a-MeLys] - [Lys(Ac)] - N-[3Pal]-[Sarc]-NH2 (SEQ ID NO: 112); Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [THP] -E-N- [3Quin]- [Sarc] -NH2 (SEQ ID NO:l 18); Ac-[Pen]-S-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-S-[3Pal]- [Sarc]-NH2 (SEQ ID NO: 124); or Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [THP] -E- S- [3Pal] - [Sarc]-NH2 (SEQ ID NO: 125); and wherein the peptide inhibitor is cyclized via a Pen-Pen disulfide bond; or via an Abu-C thioether bond; or a pharmaceutically acceptable salt thereof.

165. The peptide inhibitor of claim 163, wherein the peptide comprises or is: Ac- [Pen] -N-T - [W (7 -Ph)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [a-MeLys] - [Lys(Ac)] -N- [3Pal] - [Sarc] -NH2 (SEQ ID NO: 105); Ac-[Pen]-N-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]- [Sarc]-NH2(SEQ ID NO: 106); Ac-[Pen]-N-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-[Lys(Ac)]-N- [3Pal] - [Sarc] -NH2 (SEQ ID NO:l 17); Ac-[Pen]-N-T-[W(7-Ph)]-[Cit]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]-[Sarc]- NH2 (SEQ ID NO: 126); Ac-[Pen]-N-T-[W(7-Ph)]-Q-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]-[Sarc]- NH2 (SEQ ID NO: 127); Ac-[Abu]-Q-T-[W(7-Ph)]-Q-[Cys]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]-[Sarc]- NH2 (SEQ ID NO: 134); Ac-[Abu]-Q-T-[W(7-Ph)]-Q-[Cys]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N- [3Pal] - [Sarc] -NH2 (SEQ ID NOT35); Ac-[Pen]-N-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-[Lys(Ac)]-N- [3Pal] - [Sarc] -NH2 (SEQ ID NO:136); Ac-[Pen]-N-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aceylaminoethoxy)]-[2-Nal]-[THP]- [Lys(Ac)] -N- [3Pal] - [Sarc] -NH2 (SEQ ID NO: 137); or Ac-[Pen]-E-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-[Lys(Ac)]-N- [3Pal] - [Sarc] -NH2 (SEQ ID NO:139); and wherein the peptide inhibitor is cyclized via a Pen-Pen disulfide bond; or via an Abu-C thioether bond; or a pharmaceutically acceptable salt thereof.

166. The peptide inhibitor of claim 162, wherein the peptide inhibitor comprises or is any one of the amino acid sequence listed below: Ac- [(D)Arg] - [Pen] -N-T - [W (7 -Me)] - [Cit] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [aMeLeu] -E- N- [(D)Ly s] - [(D)NMeT yr] -NH2 (SEQ ID NO:201), Ac- [(D)Arg] - [Pen] -N-T - [W (7 -Me)] - [Cit] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [aMeLeu] -E- N- [(D)His] - [(D)NMeT yr] -NH2 (SEQ ID NO:202), Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [a-MeLys] - [Lys(Ac)] -N- [(D)Om] - [(D)NMeTyr] -NH2 (SEQ ID NO:203), Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [a-MeLys] - [Lys(Ac)] -N- [(D)Ser] - [(D)NMeTyr] -NH2 (SEQ ID NO:204), Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [a-MeLys] - [Ly s(Ac) ] -N - [(D)Phe] - [(D)NMeT yr] -NH2 (SEQ ID NO:205), Ac- [(D)Arg] - [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-Nal] - [THP] -E- N-H-[(D)Tyr] -NH2 (SEQ ID NO:206), Ac- [Pen] -N-T - [W (7 -Me)] - [(D)Tyr] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-Nal] - [a-MeLys] - [Ly s(Ac) ] -N- [(D)Ly s] - [(D)NMeT yr] -NH2 (SEQ ID NO:207), Ac- [(D)Arg] - [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-Nal] - [THP] -E- N-H-P-NH2 (SEQ ID NO:208), Ac- [(D)Arg] - [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-Nal] - [THP] -E- N-H- [(D)Pro] -NH2 (SEQ ID NO:209), Ac- [Pen] -N-T - [W (7 -Me)] - [Phe(4-CONH2)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-Nal] - [a-MeLys] - [Ly s(Ac) ] -N- [(D)Ly s] - [(D)NMeT yr] -NH2 (SEQ ID NO:210), Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [Acvc] -E-N- (D)Phe[4-NH2] - [Sarc] -NH2 (SEQ ID NO:211), Ac- [(D)Arg] - [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-Nal] - [THP] -E- N-H-NH2 (SEQ ID NO:212), Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [a-MeLys] - [Ly s(Ac) ] -N-H-N (H)Me (SEQ ID NO:213), Ac- [Pen] -N-T - [W (7 -Me)] - [Phe(4-NH(Ac))] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [a-MeLys] - [Ly s(Ac) ] -N- [(D)Ly s] - [(D)NMeT yr] -NH2 (SEQ ID NO:214), Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [a-MeLys] - [Ly s(Ac) ] -N- [(D)Tyr] - [(D)NMeT yr] -NH2 (SEQ ID NO:215), Ac- [Pen] -N-T - [W (7 -Me)] - [Cit] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-N al] - [aMeLeu] - [Lys(Ac)] -N- [(D)Lys] - [(D)NMeTyr] -NH2 (SEQ ID NO:216), Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [a-MeLys] - [Lys(Ac)] -N- [(D)His] - [(D)NMeTyr] -NH2 (SEQ ID NO:217), Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [a-MeLys] - [Ly s(Ac) ] -N - [bAla] - [(D)NMeTyr] -NH2 (SEQ ID NO:218), Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [a-MeLys] - [Ly s(Ac) ] -N - [bAla] - [(D)NMeTyr] -NH2 (SEQ ID NO:219), Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [a-MeLys] - [Ly s(Ac) ] -N - [bAla] - [(D)NMeTyr] -NH2 (SEQ ID NO:220), Ac- [(D)Arg] - [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-Nal] - [a- MeLys] -E-N-H-N(H)Me (SEQ ID NO:221), Ac- [(D)Arg] - [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-Nal] - [THP] -E- N-[THP]-P-NH2 (SEQ ID NO:222), Ac- [(D)Arg] - [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-Nal] - [THP] -E- N- [THP] - [(D)Pro] -NH2 (SEQ ID NO:223), Ac- [(D)Arg] - [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-Nal] - [Acvc] -E- N- [bAla] - [Sarc] -NH2 (SEQ ID NO:224), Ac- [(D)Arg] - [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-Nal] - [Acvc] -E- N- [(D) Val] - [Sarc] -NH2 (SEQ ID NO:225), Ac- [(D)Arg] - [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-Nal] - [Acvc] -E- N- [(D) Arg] - [Sarc] -NH2 (SEQ ID NO:226), Ac- [(D)Arg] - [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-Nal] - [Acvc] -E- N-[Hph]-[Sarc]-NH2 (SEQ ID NO:227), Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [Acvc] -E-N-Phe [4- NH2]-[Sarc]-NH2 (SEQ ID NO:228), Ac- [(D)Arg] - [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-Nal] - [Acvc] -E- N-Phe [4-NH2] - [Sarc] -NH2 (SEQ ID NO:229), Ac- [(D)Arg] - [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-Nal] - [Acvc] -E- N-F-[Sarc]-NH2 (SEQ ID NO:230), Ac- [(D)Arg] - [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-Nal] - [Acvc] -E- N- [THP] - [Sarc] -NH2 (SEQ ID NO:231), Ac- [(D)Arg] - [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-Nal] - [Acvc] -E- N- [(D)Leu] - [Sarc] -NH2 (SEQ ID NO:232), Ac-[(D)Arg]-[Cys]-N-T-[W(7-Me)]-[Lys(Ac)]-[aMeCys]-Phe[4-(2-aminoethoxy)]-[2-Nal]- [Acvc] -E-N-H- [Sarc] -NH2 (SEQ ID NO:233), Ac-[(D)Arg]-[Cys]-N-T-[W(7-Me)]-[Lys(Ac)]-[aMeCys]-Phe[4-(2-aminoethoxy)]-[2-Nal]- [Acvc] -E-N- [(D)Leu] - [Sarc] -NH2 (SEQ ID NO:234), Ac- [(D)Arg] - [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-Nal] - [Acvc] -E- N-[3Pal]-[Sarc]-NH2 (SEQ ID NO:235), Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [a-MeLys] - [Lys(Ac)]-N-[bAla]-[Sarc]-NH2 (SEQ ID NO:236), Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [a-MeLys] - [Lys(Ac)] -N- [(D)V al] - [Sarc] -NH2 (SEQ ID NO:237), Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [a-MeLys] - [Lys(Ac)] -N- [(D)Arg] - [Sarc] -NH2 (SEQ ID NO:238), Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [a-MeLys] - [Lys(Ac)] -N- [Hph] - [Sarc] -NH2 (SEQ ID NO:239), Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [a-MeLys] - [Ly s(Ac) ] -N- [(D)Tyr] - [Sarc] -NH2 (SEQ ID NO:240), Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [a-MeLys] - [Ly s(Ac) ] -N- [(D)Tyr] - [Sarc] -NH2 (SEQ ID NO:241), Ac- [(D)Arg] - [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-Nal] - [THP] -E- N-[4Pal]-NH2 (SEQ ID NO:242), Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [a-MeLys] - [Ly s(Ac) ] -N- [Phe(4- CF3 ) ] - [S arc] -NH2 (SEQ ID NO:243), Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [a-MeLys] - [Lys(Ac)]-N-Tyr_CHF2-[Sarc]-NH2 (SEQ ID NO:244), Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [a-MeLys] - [Lys(Ac)] -N- [THP] -P-NH2 (SEQ ID NO:245), Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [a-MeLys] - [Lys(Ac)] -N- [3Pal] - [(D)NMeTyr] -NH2 (SEQ ID NO:246), Ac- [(D)Arg] - [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-Nal] - [THP] -E- N-[3Pal]-[Sarc]-NH2 (SEQ ID NO:247), Ac- [(D)Arg] - [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-Nal] - [THP] -E- N-[4Pal]-[Sarc]-NH2 (SEQ ID NO:248), Ac- [(D)Arg] - [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-Nal] - [THP] -E- N-[Phe(2-aminomethyl)]-[Sarc]-NH2 (SEQ ID NO:249), Ac- [(D)Arg] - [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-Nal] - [THP] -E- N-[3Pal]-[Pro(4,4diF)]-NH2 (SEQ ID NO:250), Ac- [(D)Arg] - [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-Nal] - [THP] -E- N-[3Pal]-[aMePro]-NH2 (SEQ ID NO:251), Ac- [(D)Arg] - [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-Nal] - [THP] -E- N-[3Pal]-[Aib]-NH2 (SEQ ID NO:252), Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [a-MeLys] - [Lys(Ac)] -N- [His(3 -Me)] - [Sarc] -NH2 (SEQ ID NO:253), Ac- [(D)Arg] - [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-Nal] - [THP] -E- N- [His(3 -Me)] - [Sarc] -NH2 (SEQ ID NO:261), Ac- [(D)Arg] - [Pen] -N-T - W - [Lys(Ac)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-Nal] - [THP] -E-N- [His(3 -Me)] - [Sarc] -NH2 (SEQ ID NO:262), Ac- [(D)Arg] - [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-Nal] - [THP] -E- N-[3Pal]-[Sarc]-NH2 (SEQ ID NO:266), Ac- [(D)Arg] - [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-Nal] - [THP] -E- N-[3Pal]-N(H)Me (SEQ ID NO:267), [(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N- [3Pal] - [Sarc] -NH2 (SEQ ID NO:270), Ac- [(D)Arg] - [Pen] -N-T - W - [Lys(Ac)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-Nal] - [THP] -E-N- [3Pal] - [Sarc] -NH2 (SEQ ID NO:271), Pr-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]- Phe[4-(2-(N-propionylamino)ethoxy)]-[2- Nal] - [THP] -E-N - [3Pal] - [Sarc] -NH2 (SEQ ID NO:272), Ac- [(D)Arg] - [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe [4-(2-(N-(4-hydroxy-3 -methylphenyl) propionylamino) ethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]-[Sarc]-NH2 (SEQ ID NO:273), Ac- [(D)Arg] - [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-Nal] - [THP] -E- N- [3Pal(5 -Me)] - [Sarc] -NH2 (SEQ ID NO:276), Ac- [(D)Arg] - [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-Nal] - [THP] -E- N- [3 Pal(5 -NH2) ] - [S arc] -NH2 (SEQ ID NO:277), Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe[4-(2-aminoethoxy)] - [2-Nal] - [THP] -E-N- [His(3 - Me)]-N(H)Me (SEQ ID NO:278), Ac- [(D)Arg] - [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-Nal] - [THP] -E- N- [3 Pal] - [(D)NMeT yr] -NH2 (SEQ ID NO:279), Ac- [(D)Arg] - [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-Nal] - [THP] -E- N-[3Pal]-[Gly(N-cyclohexylmethyl)]-NH2 (SEQ ID NO:280), Ac- [(D)Arg] - [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-Nal] - [THP] -E- N-[3Pal]-[Gly(N-isobutyl)]-NH2 (SEQ ID NO:281), Ac- [(D)Arg] - [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-Nal] - [THP] -E- N-[3Pal(3-Me)]-NH2 (SEQ ID NO:282), Ac-[(D)Arg]-[aMeCys]-N-T-[W(7-Me)]-[Lys(Ac)]-[Cys]-Phe[4-(2-aminoethoxy)]-[2-Nal]- [THP] -E-N- [3Pal] - [Sarc] -NH2 (SEQ ID NO:283), Ac-[Pen]-N-T-W-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]-[Sarc]- NH2 (SEQ ID NO:284), Ac-[Pen]-N-T-W-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[Acvc]-E-N-[3Pal]-[Sarc]- NH2 (SEQ ID NO:285, 159), Ac- [Pen] -N-T- [W(7-Me)] - [Lys(Ac)] - [Pen] - [Phe(4-CONH2)] - [2-Nal] - [THP] -E-N- [3Pal] - [Sarc] - NH2 (SEQ ID NO:286), Ac- [Pen] - [Gly(Allyl)] -T- [W(7-Me)] - [Lys(Ac)] - [Pen] - [Tyr(O-Allyl)] - [2-Nal] - [THP] - [Lys(Ac)] - N-[3Pal]-[Sarc]-NH2 (SEQ ID NO:287), Ac- [Pen] - [Gly(Allyl)] -D- [W(7-Me)] - [Lys(Ac)] - [Pen] - [Tyr(O-Allyl)] - [2-Nal] - [THP] - [Lys(Ac)] - N-[3Pal]-[Sarc]-NH2 (SEQ ID NO:288), Ac- [Pen] - [Gly(Allyl)] -T-(W(4-F)] - [Lys(Ac)] - [Pen] - [Tyr(O-Allyl)] - [2-Nal] - [THP] - [Lys(Ac)] -N- [3Pal] - [Sarc] -NH2 (SEQ ID NO:289), Ac-[Pen]-N-D-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]- [Sarc]-NH2 (SEQ ID NO:290), Ac-[Pen]-L-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]- [Sarc]-NH2 (SEQ ID NO:291), Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] - [Phe(4-CONH2)] - [2-Nal] - [a-MeLys] - [Lys(Ac)] -N- [3Pal] - [Sarc] -NH2 (SEQ ID NO:299), Ac- [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -F - [2-Nal] - [THP] - [Lys(Ac)] -N- [3Pal] - [Sarc] -NH2 (SEQ ID NO:308), Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-[(D)Tyr]-[2-Nal]-[THP]-[Lys(Ac)]-N-[3Pal]-[Sarc]- NH2 (SEQ ID NO:309), Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-[Phe(4-OMe)]-[2-Nal]-[THP]-[Lys(Ac)]-N-[3Pal]- [Sarc]-NH2 (SEQ ID NO:310), Ac- [Pen] -N-T- [W(7-Me)] - [Lys(Ac)] - [Pen] - [Phe(4-CONH2)] - [2-Nal] - [THP] - [Lys(Ac)]-N- [3 Pal] - [Sarc] -NH2 (SEQ ID NO:311), Ac-[Pen]-N-T-[W(7-Me)]-[Lys(N-acetyl-N-propyl)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]- [THP] -E-N- [3Pal] - [Sarc] -NH2 (SEQ ID NO:332), Ac-[Pen]-N-T-[W(7-Me)]-[Lys(N-acetyl-N-butyl)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]- [THP] -E-N- [3Pal] - [Sarc] -NH2 (SEQ ID NO:333), Ac-[Pen]-N-T-[W(7-Me)]-[Lys(N-acetyl-N-isobutyl)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]- [THP] -E-N- [3Pal] - [Sarc] -NH2 (SEQ ID NO:334), Ac-[Pen]-N-T-[W(7-Me)]-[Lys(N-acetyl-N-benzyl)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]- [THP] -E-N- [3Pal] - [Sarc] -NH2 (SEQ ID NO:335), Ac-[Pen]-L-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-[Phe(4-CONH2)]-[2-Nal]-[aMeLeu]-E-N-[3Pal]- [Sarc]-NH2 (SEQ ID NO:339), Ac-[Pen]-L-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-[Phe(4-OMe)]-[2-Nal]-[aMeLeu]-E-N-[3Pal]-[Sarc]- NH2 (SEQ ID NO: 347), or Ac-[Abu]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]- [Sarc]-NH2 (SEQ ID NO:373), and wherein the peptide inhibitor is cyclized via a Pen-Pen disulfide bond; or via an Abu-C thioether bond; or a pharmaceutically acceptable salt thereof.

167. The peptide inhibitor of claim 163 or 166, wherein the peptide is Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]- [Sarc]-NH2 (SEQ ID NO: 104), Ac-[Pen]-N-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]- [Sarc]-NH2 (SEQ ID NO: 106), Ac-[Pen]-N-T-W-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]-[Sarc]- NH2 (SEQ ID NOS:158, 162, 284), Ac- [(D)Arg] - [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-Nal] - [THP] -E- N-[3Pal]-[Sarc]-NH2 (SEQ ID NOs:247, 266), Ac- [(D)Arg] - [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-Nal] - [THP] -E- N- [His(3 -Me)] - [Sarc] -NH2 (SEQ ID NO:261), or Ac- [(D)Arg] - [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-Nal] - [THP] -E- N-[3Pal]-N(H)Me (SEQ ID NO:267), wherein the peptide inhibitor is cyclized via a Pen-Pen disulfide bond, or a pharmaceutically acceptable salt thereof.

168. The peptide inhibitor of claim 167, wherein the peptide is Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]- [Sarc]-NH2 (SEQ ID NO: 104), wherein the peptide inhibitor is cyclized via a Pen-Pen disulfide bond, or a pharmaceutically acceptable salt thereof.

169. The peptide inhibitor of claim 167, wherein the peptide is Ac-[Pen]-N-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]- [Sarc]-NH2 (SEQ ID NO: 106), wherein the peptide inhibitor is cyclized via a Pen-Pen disulfide bond, or a pharmaceutically acceptable salt thereof.

170. The peptide inhibitor of claim 167, wherein the peptide is Ac-[Pen]-N-T-W-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]-[Sarc]- NH2 (SEQ ID NOs:158, 162, 284), wherein the peptide inhibitor is cyclized via a Pen-Pen disulfide bond, or a pharmaceutically acceptable salt thereof.

171. The peptide inhibitor of claim 167, wherein the peptide is Ac- [(D)Arg] - [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-Nal] - [THP] -E- N-[3Pal]-[Sarc]-NH2 SEQ ID NOs:247, 266), wherein the peptide inhibitor is cyclized via a Pen-Pen disulfide bond, or a pharmaceutically acceptable salt thereof.

172. The peptide inhibitor of claim 167, wherein the peptide is Ac- [(D)Arg] - [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-Nal] - [THP] -E- N-[His(3-Me)]-[Sarc]-NH2 (SEQ ID NO:261), wherein the peptide inhibitor is cyclized via a Pen-Pen disulfide bond, or a pharmaceutically acceptable salt thereof.

173. The peptide inhibitor of claim 167, wherein the peptide is Ac- [(D)Arg] - [Pen] -N-T - [W (7 -Me)] - [Lys(Ac)] - [Pen] -Phe [4-(2-aminoethoxy)] - [2-Nal] - [THP] -E- N-[3Pal]-N(H)Me (SEQ ID NO:267), wherein the peptide inhibitor is cyclized via a Pen-Pen disulfide bond, or a pharmaceutically acceptable salt thereof.

174. A polynucleotide comprising a sequence encoding the peptide inhibitor of any one of claims 1-173.

175. A vector comprising the polynucleotide of claim 174.

176. A pharmaceutical composition comprising the peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 1-173, and a pharmaceutically acceptable carrier, excipient, or diluent.

177. The pharmaceutical composition of claim 176, further comprising an enteric coating.

178. The pharmaceutical composition of claim 177, wherein the enteric coating protects and releases the pharmaceutical composition within a subject's lower gastrointestinal system.

179. A method for treating an Inflammatory Bowel Disease (IBD), ulcerative colitis, Crohn's disease, Celiac disease ( nontropical Sprue), enteropathy associated with seronegative arthropathies, microscopic colitis, collagenous colitis, eosinophilic gastroenteritis, colitis associated with radio- or chemo-therapy, colitis associated with disorders of innate immunity as in leukocyte adhesion deficiency- 1 , chronic granulomatous disease, glycogen storage disease type lb, Hermansky-Pudlak syndrome, Chediak- Higashi syndrome, and Wiskott- Aldrich Syndrome, pouchitis resulting after proctocolectomy and ileoanal anastomosis, gastrointestinal cancer, pancreatitis, insulin-dependent diabetes mellitus, mastitis, cholecystitis, cholangitis, pericholangitis, chronic bronchitis, chronic sinusitis, asthma, psoriasis, psoriatic arthritis, or graft versus host disease in a subject, comprising providing to the subject an effective amount of the peptide inhibitor or peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 1-173, or the pharmaceutical composition of any one of claims 176-178.

180. The method of claim 179, wherein the pharmaceutical composition is provided to the subject by an oral, parenteral, intravenous, peritoneal, intradermal, subcutaneous, intramuscular, intrathecal, inhalation, vaporization, nebulization, sublingual, buccal, parenteral, rectal, intraocular, inhalation, topically, vaginal, or topical route of administration.

181. The method of claim 179 for treating Inflammatory Bowel Disease (IBD), ulcerative colitis, or Crohn's disease, wherein the pharmaceutical composition is provided to the subject orally.

182. The method of claim 179 for treating psoriasis, wherein the pharmaceutical composition is provided to the subject orally, topically, parenterally, intravenously, subcutaneously, peritonealy, or intravenously.

183. The peptide inhibitor or peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 1-173, or the pharmaceutical composition of any one of claims 176-178, for use in the treatment of an Inflammatory Bowel Disease (IBD), ulcerative colitis, Crohn's disease, Celiac disease ( nontropical Sprue), enteropathy associated with seronegative arthropathies, microscopic colitis, collagenous colitis, eosinophilic gastroenteritis, colitis associated with radio- or chemo-therapy, colitis associated with disorders of innate immunity as in leukocyte adhesion deficiency- 1, chronic granulomatous disease, glycogen storage disease type lb, Hermansky-Pudlak syndrome, Chediak-Higashi syndrome, and Wiskott-Aldrich Syndrome, pouchitis resulting after proctocolectomy and ileoanal anastomosis, gastrointestinal cancer, pancreatitis, insulin-dependent diabetes mellitus, mastitis, cholecystitis, cholangitis, pericholangitis, chronic bronchitis, chronic sinusitis, asthma, psoriasis, psoriatic arthritis, or graft versus host disease in a subject, comprising providing to the subject an effective amount of the peptide inhibitor or peptide inhibitor or pharmaceutically acceptable salt thereof of any one of claims 1-173, or the pharmaceutical composition of any one of claims 176-178.

184. The composition for use according to claim 183, wherein the pharmaceutical composition is provided to the subject by an oral, parenteral, intravenous, peritoneal, intradermal, subcutaneous, intramuscular, intrathecal, inhalation, vaporization, nebulization, sublingual, buccal, parenteral, rectal, intraocular, inhalation, topically, vaginal, or topical route of administration.

185. The composition for use according to claim 183 for treating Inflammatory Bowel Disease (IBD), ulcerative colitis, or Crohn's disease, wherein the pharmaceutical composition is provided to the subject orally.

186. The composition for use according to claim 183 for treating psoriasis, wherein the pharmaceutical composition is provided to the subject orally, topically, parenterally, intravenously, subcutaneously, peritonealy, or intravenously.
```

---

#### 2.2 US20210261622A1 ☑️부분교차검증 (차이 14개)

> **💡 핵심 요약** &nbsp;|&nbsp; **유형:** compound·물질(peptide)
> 
> **무엇을 청구하나:** WO2021146441과 동일 계열의 단환 IL-23R 펩타이드 저해제를 Formula (I) Markush로 청구(공개 출원); X4-X9 디설파이드/티오에터 고리화 및 IL-23/IL-23R 결합 저해를 명시
> 
> **핵심 권리범위:** X4-X9 디설파이드 또는 티오에터 결합으로 고리화; Formula (Z') 하위구조에서 R1=H/Ac, X11=2-Nal, X14=Asn 등 한정; 특정 선행 화합물 proviso 제외; IL-23의 IL-23R 결합 저해 기능 한정
> 
> **독립항:** 1 &nbsp;|&nbsp; **적응증:** — &nbsp;|&nbsp; **검증:** ☑️부분교차검증(차이14) &nbsp;|&nbsp; **추정만료:** 2041-01-14


| 항목 | 내용 |
|---|---|
| 특허번호 | US20210261622A1 (pre-grant 공개, A1) |
| 제목 | Peptide Inhibitors of Interleukin-23 Receptor and Their Use to Treat Inflammatory Diseases |
| 출원번호 / 출원일 | 17/149,509 / 2021-01-14 |
| 우선일 | 2020-01-15 (US Provisional 62/961,624) |
| 공개일 | 2021-08-26 |
| 출원인/양수인 | Janssen Biotech, Inc.; Protagonist Therapeutics, Inc. |
| 패밀리 | WO2021146441A1 (PCT), US11845808B2 (동일 출원의 등록본) |
| 권위 만료일 | **2041-01-14** (GP anticipated expiration; 출원일+20년, PTE 미반영) |
| 교차검증 | GP=50, FPO=50, both=50, agree=36, **substantive_diff=14** → ☑️부분교차검증 |

**[ANALYSIS] (한국어)**

WO2021146441A1과 동일 출원(17/149,509)의 미국 pre-grant 공개본. GP 청구항 본문에는 `(canceled)` 표기(예: `2.-104. (canceled)`, `106.-110. (canceled)` 등)가 그대로 남아 있어 실제 심사 중 다수 청구항이 삭제·재번호되었음을 보여준다. GP↔FPO 50개 비교에서 36개 일치, 14개 차이로 ☑️부분교차검증. 차이는 Markush 치환기 목록의 파싱 잡음이 주된 원인이며 권위 소스는 GP다. 청구항 1의 Formula (I)과 proviso 구조는 PCT(WO) 및 등록본 US11845808B2와 동일 계열이다.

**[VERBATIM] — 출처: Google Patents (`work/05_gp_authoritative/US20210261622A1.md`)**

```text
1. A monocyclic peptide inhibitor of an interleukin-23 receptor; or a pharmaceutically acceptable salt thereof; wherein the monocyclic peptide inhibitor of the interleukin-23 receptor comprises an amino acid sequence of Formula (I): X3-X4-X5-X6-X7-X8-X9-X10-X11-X12-X13-X14-X15-X16  (I) wherein; X3 is absent or any amino acid; X4 is Abu, Cys, (D)Cys, alpha-MeCys, (D)Pen, Pen, or Pen(sulfoxide); X5 is Cit, Glu, Gly, substituted Gly, Leu, lie, beta-Ala, Ala, Lys, Asn, Pro, Ser, alpha-MeGln, alpha-MeLys, alpha-MeLeu, alpha-MeAsn, Lys(Ac), alpha-MeLys(Ac), Dab(Ac), Dap(Ac), homo-Lys(Ac), Gin, or Asp; X6 is Thr, Aib, Asp, Dab, Gly, Pro, Ser, alpha-MeGln, alpha-MeLys, alpha-MeLeu, alpha-MeAsn, alpha-MeThr, alpha-MeSer, or Val; X7 is unsubstituted Trp, or Trp substituted with cyano, halo, alkyl, haloalkyl, hydroxy, alkoxy, substituted or unsubstituted aryl, or substituted or unsubstituted heteroaryl; X8 is Gin, alpha-MeLys, alpha-MeLeu, alpha-MeLys(Ac), beta-homoGln, Cit, Glu, Phe, substituted Phe, Tyr, Asn, Thr, Val, Aib, alpha-MeGln, alpha-MeAsn, Lys(Ac), Dab(Ac), Dap(Ac), homo-Lys(Ac), 1-Nal, 2-Nal, Lys(b-Ala), Lys(Gly), Lys(Benzyl, Ac), Lys(butyl, Ac), Lys(isobutyl,Ac), Lys(propyl,Ac), or Trp; X9 is Abu, Cys, (D)Cys, alpha-MeCys, (D)Pen, Pen, or Pen(sulfoxide); X10 is Tyr, or substituted Tyr, unsubstituted Phe, or Phe substituted with halo, alkyl, haloalkyl, hydroxy, alkoxy, cyano, cycloalkyl, carboxy, carboxamido, 2-aminoethoxy, or 2-acetylaminoethoxy; X11 is 2-Nal, Phe(2-Me), Phe(3-Me), Phe(4-Me), Phe(3,4-dimethoxy), 2Quin, 3Quin, 1-Nal, unsubstituted Trp, or Trp substituted with cyano, halo, alkyl, haloalkyl, hydroxy, or alkoxy; X12 is 4-amino-4-carboxy-tetrahydropyran (THP), Acvc, alpha-MeLys, alpha-MeLeu, alpha-MeArg, alpha-MePhe, alpha-MeLeu, alpha-MeLys, alpha-MeAsn, alpha-MeTyr, Ala, cyclohexylAla, Lys, or Aib; X13 is any amino acid; X14 is any amino acid; and i) X15 is any amino acid other than His, (D)His, substituted or unsubstituted His, 2Pal, 3Pal, or 4Pal; X16 is Sarc, aMeLeu, (D)NMeTyr, His, (D)Thr, bAla, Pro, or (D)Pro; and provided that the monocyclic peptide inhibitor is other than: Ac-[Abu]-QTWQC-[Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-[Lys(Ac)]-NNPG-NH2; Ac-[Pen]-N-T-W-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[aMeLeu]-[Lys(Ac)]-NN-[Sarc]-NH2; Ac-[(D) Arg]-[Abu]-Q-T-[W(7-Me)]-[Lys(Ac)]-[Cys]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N-[(D)Lys]-[Sarc]-NH2; or Ac-[Pen]-N-T-[W(7-Me)]-[Cit]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys (Ac)]-N-[Aib]-[bA]-NH2; or ii) X15 is His, (D)His, substituted or unsubstituted His, 2Pal, 3Pal, 4Pal, 4TriazolAla, or 5Pyal; and X16 is absent, (D)aMeTyr, (D)NMeTyr or any amino acid other than THP, substituted or unsubstituted Phe, substituted or unsubstituted (D)Phe, substituted or unsubstituted His, substituted or unsubstituted (D)His, substituted or unsubstituted Trp, substituted or unsubstituted 2-Nal, or N-substituted Asp; and provided that the monocyclic peptide inhibitor is other than: Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N—H—NH2; wherein; 2Pal is 2-pyridyl substituted alanine; 3Pal is 3-pyridyl substituted alanine; 4Pal is 4-pyridyl substituted alanine; 5Pyal is 5-pyrimidine substituted alanine; wherein X4 and X9 form a disulfide bond or a thioether bond; and wherein the peptide inhibitor of the interleukin-23 receptor inhibits the binding of an interleukin-23 (IL-23) to an IL-23 receptor. 2.-104. (canceled)

105. The monocyclic peptide inhibitor of interleukin-23 receptor or pharmaceutically acceptable salt thereof of claim 1, wherein the monocyclic peptide inhibitor comprises the structure of Formula (Z′): R1-X3-X4-X5-X6-X7-X8-X9-X10-X11-X12-X13-X14-X15-X16-R2  (Z′) wherein R1 is a hydrogen, or Ac; X3 is absent or (D)Arg; X4 is Abu, Cys, (D)Cys, alpha-MeCys, or Pen; X5 is Ala, (allyl)Gly, Ile, Leu, Asn, Nle, or Gln; X6 is Asp, or Thr; X7 is (7-methyl)Trp, (4-F)Trp, or Trp; X8 is Cit Lys(Ac)-Lys(Benzyl, Ac), Lys(butyl, Ac), Lys(isobutyl,Ac), Lys(propyl,Ac), Gln, 4-adamantyl-Phe, (4-AcNH)Phe, or Tyr; X9 is Cys, alpha-MeCys, or Pen; X10 is Phe, substituted Phe, Tyr, or substituted Tyr; X11 is 2-Nal; X13 is alpha-methylGlu, Glu, or Lys(Ac); and X14 is Asn; and R2 is OH, NH2 or N(H)Me. 106.-110. (canceled)

111. The monocyclic peptide inhibitor of an interleukin-23 receptor of claim 105 or pharmaceutically acceptable salt thereof, wherein the monocyclic peptide inhibitor comprises the structure of Formula (Z′): R1-X3-Pen-X5-X6-X7-X8-Pen-X10-X11-X12-X13-X14-X15-X16-R2  (Z′-A) wherein; the monocyclic peptide inhibitor of an interleukin-23 is cyclized via a Pen-Pen disulfide bond. 112.-113. (canceled)

114. The monocyclic peptide inhibitor of an interleukin-23 receptor or pharmaceutically acceptable salt thereof of claim 105, wherein the monocyclic peptide inhibitor comprises the structure of Formula (Z′): R1-X3-Pen-Asn-X6-X7-X8-Pen-X10-X11-X12-X13-X14-X15-X16-R2  (Z′-B) wherein: the monocyclic peptide inhibitor of an interleukin-23 is cyclized via a Pen-Pen disulfide bond.

115. (canceled)

116. The monocyclic peptide inhibitor of an interleukin-23 receptor of claim 15 or pharmaceutically acceptable salt thereof, wherein the monocyclic peptide inhibitor comprises the structure of Formula (Z′): R1-X3-Pen-Asn-Thr-X7-X8-Pen-X10-X11-X12-X13-X14-X15-X16-R2  (Z′-C) wherein: the peptide inhibitor is cyclized via a Pen-Pen disulfide bond. 117.-118. (canceled)

119. The monocyclic peptide inhibitor of an interleukin-23 receptor of claim 105 or pharmaceutically acceptable salt thereof wherein the monocyclic peptide inhibitor comprises the structure of Formula (Z′): R1-X3-Pen-Asn-Thr-X7-Lys(Ac)-Pen-X10-X11-X12-X13-X14-X15-X16-R2  (Z′-D) wherein; the monocyclic peptide inhibitor of an interleukin-23 receptor is cyclized via a Pen-Pen disulfide bond.

120. The monocyclic peptide inhibitor or pharmaceutically acceptable salt thereof of claim 105, wherein X10 is Phe, Phe[4-(2-aminoethoxy)], Phe[4-(2-acetylaminoethoxy)], or Phe(4-CONH2). 121.-122. (canceled)

123. The monocyclic peptide inhibitor of an interleukin-23 of claim 105 or pharmaceutically acceptable salt thereof, wherein the monocyclic peptide inhibitor comprises the structure of Formula (Z′): (SEQ ID NO: 514) R1-X3-Pen-Asn-Thr-X7-Lys(Ac)-Pen-[F(4-2ae)]-X11- X12-X13-X14-X15-X16-R2 (Z′-E) wherein: F(4-2-ae) is Phe[4-(2-aminoethoxy)]; and the monocyclic peptide inhibitor of an interleukin-23 receptor is cyclized via a Pen-Pen disulfide bond. 124.-126. (canceled)

127. The monocyclic peptide inhibitor of an interleukin-23 receptor of claim 105 or pharmaceutically acceptable salt thereof, wherein monocyclic peptide inhibitor comprises the structure of Formula (Z′): (SEQ ID NO: 515) R1-X3-Pen-Asn-Thr-X7-Lys(Ac)-Pen-[F(4-2ae)]-[2- Nal]-X12-X13-X14-X15-X16-R2 (Z′-F) wherein: F(4-2-ae) is Phe[4-(2-aminoethoxy)]; and the monocyclic peptide inhibitor of an interleukin-23 receptor is cyclized via a Pen-Pen disulfide bond. 128.-129. (canceled)

130. The monocyclic peptide inhibitor of an interleukin-23 receptor of claim 105 or pharmaceutically acceptable salt thereof, wherein the monocyclic peptide inhibitor comprises the structure of Formula (Z′): (SEQ ID NO: 516) R1-X3-Pen-Asn-Thr-X7-Lys(Ac)-Pen-[F(4-2ae)]-[2- Nal]-THP-X13-X14-X15-X16-R2 (Z′-G) wherein; F(4-2-ae) is Phe[4-(2-aminoethoxy)]; and the monocyclic peptide inhibitor of an interleukin-23 receptor is cyclized via a Pen-Pen disulfide bond. 131.-132. (canceled)

133. The monocyclic peptide inhibitor of an interleukin-23 receptor of claim 105 or pharmaceutically acceptable salt thereof, wherein the monocyclic peptide inhibitor comprises the structure of Formula (Z′): (SEQ ID NO: 517) R1-X3-Pen-Asn-Thr-X7-Lys(Ac)-Pen-[F(4-2ae)]-[2- Nal]-THP-G1u-X14-X15-X16-R2 (Z′-H) wherein: F(4-2-ae) is Phe[4-(2-aminoethoxy)]; and the peptide inhibitor is cyclized via a Pen-Pen disulfide bond.

134. (canceled)

135. The monocyclic peptide inhibitor of an interleukin-23 receptor of claim 105 or pharmaceutically acceptable salt thereof, wherein the monocyclic peptide inhibitor comprises the structure of Formula (Z′): (SEQ ID NO: 518) R1-X3-Pen-Asn-Thr-X7-Lys(Ac)-Pen-[F(4-2ae)]-[2- Nal]-THP-G1u-Asn-X15-X16-R2 (Z′-I) wherein: F(4-2-ae) is Phe[4-(2-aminoethoxy)]; and the peptide inhibitor is cyclized via a Pen-Pen disulfide bond. 136.-141. (canceled)

142. The monocyclic peptide inhibitor of an interleukin-23 receptor of claim 105 or pharmaceutically acceptable salt thereof, whereinthe monocyclic peptide inhibitor comprises the structure of Formula (Z′): R1-X3-Pen-Asn-Thr-[W(7-Me)]-Lys(Ac)-Pen-[F(4-2ae)]-[2-Nal]-THP-Glu-Asn-X15-X16-R2  (Z′-J) wherein; F(4-2-ac) is Phe[4-(2-aminoethoxy)]; and the peptide inhibitor is cyclized via a Pen-Pen disulfide bond.

143. (canceled)

144. The monocyclic peptide inhibitor of an interleukin-23 receptor of claim 105 or pharmaceutically acceptable salt thereof, wherein X3 is absent.

145. The monocyclic peptide inhibitor of an interleukin-23 receptor of claim 105 or pharmaceutically acceptable salt thereof, wherein X3 is (D)Arg.

146. The monocyclic peptide inhibitor of an interleukin-23 receptor of claim 105 or pharmaceutically acceptable salt thereof, wherein the monocyclic peptide inhibitor comprises the structure of Formula (Z′): R1-Pen-Asn-Thr-[W(7-Me)]-Lys(Ac)-Pen-[F(4-2ae)]-[2-Nal]-THP-Glu-Asn-X15-X16-R2  (Z′-K) wherein: F(4-2-ae) is Phe[4-(2-aminoethoxy)]; and the peptide inhibitor is cyclized via a Pen-Pen disulfide bond. 147.-149. (canceled)

150. The monocyclic peptide inhibitor of an interleukin-23 receptor of claim 105 or pharmaceutically acceptable salt thereof, wherein R1 is Ac.

151. The monocyclic peptide inhibitor of an interleukin-23 receptor of claim 105 or pharmaceutically acceptable salt thereof, wherein R2 is NH2 or N(H)Me.

152. The monocyclic peptide inhibitor of an interleukin-23 receptor of claim 105 or pharmaceutically acceptable salt thereof, wherein R2 is NH2.

153. The monocyclic peptide inhibitor of an interleukin-23 receptor of claim 105 or pharmaceutically acceptable salt thereof, wherein: R1 is Ac; X3 is absent or (D)Arg; X4 is Pen; X5 is Asn; X6 is Thr; X7 is Trp; X8 is Lys(Ac); X9 is Pen; X10 is Phe(2-aminoethoxy); X11 is 2-Nal; X12 is 4-amino-4-carboxy-tetrahydropyran (THP); X13 is Gin; X14 is Asn; and R2 is NH2 or N(H)Me.

154. The monocyclic peptide inhibitor of an interleukin-23 receptor of claim 105 or pharmaceutically acceptable salt thereof, wherein; R1 is Ac; X3 is absent; X4 is Pen; X5 is Asn; X6 is Thr; X7 is 7-methylTrp; X8 is Lys(Ac); X9 is Pen; X10 is Phe(2-aminoethoxy); X11 is 2-Nal; X12 is 4-amino-4-carboxy-tetrahydropyran (THP); X13 is Glu; X14 is Asn; and R2 is NH2 or N(H)Me.

155. The monocyclic peptide inhibitor of an interleukin-23 receptor of claim 105 or pharmaceutically acceptable salt thereof, wherein: X15 is Aib, beta-Ala, (D)Phe, (D)Lys, (D)Leu, (D)Orn, substituted (D)Phe, (D)Arg, (D)Val, (D)Tyr, Phe, Hph, Asn, 4-amino-4-carboxy-tetrahydropyran (THP), substituted Tyr, or Tyr; and X16 is beta-Ala, (D)NMeTyr, (D)Pro, NMeTyr, Pro, or Sarc.

156. The monocyclic peptide inhibitor of an interleukin-23 receptor of claim 105 or pharmaceutically acceptable salt thereof, wherein; X15 is 3Pal, substituted 3Pal, 4Pal, 4-triazole-Ala, (D)His, His or substituted His; and X16 is absent, Aib, alpha-MePro, (D)Leu, (D)NMeTyr, (D)Pro, (D)Tyr, substituted Gly, MeLeu, MeNLe, Pro, Paf, 4-di-fluoro-Pro, Sarc, or Tyr.

157. The monocyclic peptide inhibitor of an interleukin-23 receptor of claim 105 or pharmaceutically acceptable salt thereof, wherein; X15 is (D)His, substituted His, 2Pal, 3Pal, 4Pal, 4TriazolAla, or 5Pyal; and X16 is absent, (D)NMeTyr or Sarc.

158. The monocyclic peptide inhibitor of an interleukin-23 receptor of claim 105 or pharmaceutically acceptable salt thereof, wherein: X15 is (3-Me)His or 3Pal; and X16 is absent or Sarc.

159. The monocyclic peptide inhibitor of an interleukin-23 receptor of claim 105 or pharmaceutically acceptable salt thereof, wherein the monocyclic peptide inhibitor comprises the structure of Formula (Z′): Ac-Pen-Asn-Thr-[W(7-Me)]-Lys(Ac)-Pen-[F(4-2ae)]-[2-Nal]-THP-Glu-Asn-[3-Pal]-X16-NH2  (Z′-L) wherein; F(4-2-ae) is Phe[4-(2-aminoethoxy; and the peptide inhibitor is cyclized via a Pen-Pen disulfide bond.

160. The monocyclic peptide inhibitor of an interleukin-23 receptor of claim 105 or pharmaceutically acceptable salt thereof, wherein the monocyclic peptide inhibitor comprises the structure of Formula (Z′): Ac-Pen-Asn-Thr-[W(7-Me)]-Lys(Ac)-Pen-[F(4-2ae)]-[2-Nal]-THP-Glu-Asn-X15-Sarc-NH2  (Z′-M) wherein: F(4-2-ae) is Phe[4-(2-aminoethoxy)]; and the peptide inhibitor is cyclized via a Pen-Pen disulfide bond.

161. The monocyclic peptide inhibitor of an interleukin-23 receptor of claim 160 or pharmaceutically acceptable salt thereof, wherein X15 is 3Pal; and X16 is Sarc.

162. A monocyclic peptide inhibitor of an interleukin-23 receptor of an interleukin-23 receptor, wherein the monocyclic peptide inhibitor is: (SEQ ID NO: 1) Ac-[(D)Arg]-[Abu]-Q-T-[W(7-Ph)]-[Lys(Ac)]-[Cys]- Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]- [Lys(Ac)]-N-dK-[Sarc]-NH2; (SEQ ID NO: 2) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[3-Quin]-[a-MeLys]-[Lys(Ac)]-N- [(D)Leu]-[Sarc]-NH2; (SEQ ID NO: 3) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[3-Quin]-[THP]-E-N-(D)Lys]-[Sarc]- NH2; (SEQ ID NO: 4) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[3-Quin]-[a-MeLys]-[Lys(Ac)]-N- [(D)His]-[Sarc]-NH2; (SEQ ID NO: 5) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[3-Quin]-[a-MeLys]-[Lys(Ac)]-N- H-[Sarc]-NH2; (SEQ ID NO: 6) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[3-Quin]-[THP]-E-N-[(D)Leu]- [Sarc]-NH2; (SEQ ID NO: 7) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[3-Quin]-[a-MeLys]-[Lys(Ac)]-N- [(D)Lys]-[Sarc]-NH2; (SEQ ID NO: 8) Ac-[(D)Arg]-[Abu]-Q-T-W-Q-[Cys]-Phe[4-(2-amino- ethoxy)]-[2-Nal]-[THP]-E-N-N-[(D)NMeTyr]-NH2; (SEQ ID NO: 9) Ac-[(D)Arg]-[Pen]-Q-T-W-Q-[Pen]-Phe[4-(2-amino- ethoxy)]-[2-Nal]-[THP]-E-N-N-[(D)NMeTyr]-NH2; (SEQ ID NO: 10) Ac-[(D)Arg]-[Pen]-Q-T-W-Q-[Pen]-Phe[4-(2-amino- ethoxy)]-[2-Nal]-[THP]-[aMeGlu]-N-F-[(D)NMeTyr]- NH2; (SEQ ID NO: 11) Ac-[Pen]-N-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[3-Quin]-[THP]-E-N-(D)Lys]-[Sarc]- NH2; (SEQ ID NO: 12) Ac-[Pen]-N-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[3-Quin]-[a-MeLys]-[Lys(Ac)]-N- [(D)Lys]-[Sarc]-NH2; (SEQ ID NO: 13) Ac-[Pen]-N-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[3-Quin]-[THP]-E-N-(D)Leu]-[Sarc]- NH2; (SEQ ID NO: 14) Ac-[Pen]-N-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[3-Quin]-[a-MeLys]-[Lys(Ac)]-N- [(D)Leu]-[Sarc]-NH2; (SEQ ID NO: 15) Ac-[Pen]-N-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[3-Quin]-[THP]-E-N-H-[Sarc]-NH2; (SEQ ID NO: 16) Ac-[Pen]-N-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[3-Quin]-[a-MeLys]-[Lys(Ac)]-N- H-[Sarc]-NH2; (SEQ ID NO: 17) Ac-[Abu]-Q-T-[W(7-Me)]-[Lys(Ac)]-[Cys]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N- [(D)Lys]-[Sarc]-NH2; (SEQ ID NO: 18) Ac-[Abu]-Q-T-[W(7-Ph)]-[Lys(Ac)]-[Cys]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N- [(D)Lys]-[Sarc]-NH2; (SEQ ID NO: 19) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N- [(D)Leu]-[NMeLeu]-NH2; (SEQ ID NO: 20) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N- [(D)Leu]-[Sarc]-NH2; (SEQ ID NO: 21) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N- [(D)Lys]-[Sarc]-NH2; (SEQ ID NO: 22) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-E-N-H-[Sarc]-NH2; (SEQ ID NO: 23) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N-H- [Sarc]-NH2; (SEQ ID NO: 24) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-E-N-(D)Leu]-[Sarc]- NH2; (SEQ ID NO: 25) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N- [(D)Leu]-[Sarc]-NH2; (SEQ ID NO: 26) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Gly)]-[Pen]-Phe[4- (2-aminoethoxy)]-[2-Nal]-[THP]-E-N-H-[Sarc]- NH2; (SEQ ID NO: 27) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Gly)]-[Pen]-Phe[4- (2-aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N- H-[Sarc]-NH2; (SEQ ID NO: 28) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Gly)]-[Pen]-Phe[4- (2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[(D)Leu]- [Sarc]-NH2; (SEQ ID NO: 29) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Gly)]-[Pen]-Phe[4- (2-aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N- [(D)Leu]-[Sarc]-NH2; (SEQ ID NO: 30) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(bAla)]-[Pen]-Phe[4- (2-aminoethoxy)]-[2-Nal]-[THP]-E-N-H-[Sarc]- NH2; (SEQ ID NO: 31) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(bAla)]-[Pen]-Phe[4- (2-aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N- H-[Sarc]-NH2; (SEQ ID NO: 32) Ac-[Pen]-N-T-[W(7-Et)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-E-N-H-[Sarc]-NH2; (SEQ ID NO: 33) Ac-[Pen]-N-T-[W(7-Et)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N-H- [Sarc]-NH2; (SEQ ID NO: 34) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[W(7-Et)]-[a-MeLys]-[Lys(Ac)]-N-H- [Sarc]-NH2; (SEQ ID NO: 35) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[W(4-Me)]-[a-MeLys]-[Lys(Ac)]-N-H- [Sarc]-NH2; (SEQ ID NO: 36) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[W(6-Me)]-[a-MeLys]-[Lys(Ac)]-N-H- [Sarc]-NH2; (SEQ ID NO: 37) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[W(4-OMe)]-[a-MeLys]-[Lys(Ac)]-N- H-[Sarc]-NH2; (SEQ ID NO: 38) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[W(7-i-Pr)]-[a-MeLys]-[Lys(Ac)]-N- H-[Sarc]-NH2; (SEQ ID NO: 39) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[W(7-nPr)]-[a-MeLys]-[Lys(Ac)]-N- H-[Sarc]-NH2; (SEQ ID NO: 40) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[W(7-OMe)]-[a-MeLys]-[Lys(Ac)]-N- H-[Sarc]-NH2; (SEQ ID NO: 41) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[W(6-Cl)]-[a-MeLys]-[Lys(Ac)]-N-H- [Sarc]-NH2; (SEQ ID NO: 42) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[W(5-OMe)]-[a-MeLys]-[Lys(Ac)]-N- H-[Sarc]-NH2; (SEQ ID NO: 43) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[W(3-MePh)]-[a-MeLys]-[Lys(Ac)]-N- H-[Sarc]-NH2; (SEQ ID NO: 44) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[W(6-Ph)]-[a-MeLys]-[Lys(Ac)]-N-H- [Sarc]-NH2; (SEQ ID NO: 45) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[W(6-Et)]-[a-MeLys]-[Lys(Ac)]-N-H- [Sarc]-NH2; (SEQ ID NO: 46) Ac-[Pen]-N-T-[W(7-(2-Fph)]-[Lys(Ac)]-[Pen]-Phe [4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]- N-H-[Sarc]-NH2; (SEQ ID NO: 47) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N- [(D)Leu]-[(D)NMeTyr]-NH2; (SEQ ID NO: 48) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N- [(D)Lys]-[(D)NMeTyr]-NH2; (SEQ ID NO: 49) Ac-[Pen]-N-T-[W(7-(2-OMePh)]-[Lys(Ac)]-[Pen]-Phe [4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]- N-H-[Sarc]-NH2; (SEQ ID NO: 50) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[W(7-Ph)]-[a-MeLys]-[Lys(Ac)]-N-H- [Sarc]-NH2; (SEQ ID NO: 51) Ac-[Pen]-N-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N-H- [Sarc]-NH2; (SEQ ID NO: 52) Ac-[Pen]-N-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-E-N-H-[Sarc]-NH2; (SEQ ID NO: 53) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[3Quin]-[THP]-E-N-H-[Sarc]-NH2; (SEQ ID NO: 54) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-E-S-H-[Sarc]-NH2; (SEQ ID NO: 55) Ac-[Pen]-S-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-E-N-H-[Sarc]-NH2; (SEQ ID NO: 56) Ac-[Pen]-S-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-E-S-H-[Sarc]-NH2; (SEQ ID NO: 57) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-E-N-H-[(D)NMeTyr]- NH2; (SEQ ID NO: 58) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLys]-N-F-[(D)NMeTyr]- NH2; (SEQ ID NO: 59) Ac-[Pen]-N-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-E-S-H-[Sarc]-NH2; (SEQ ID NO: 60) Ac-[Pen]-S-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-E-N-H-[Sarc]-NH2; (SEQ ID NO: 61) Ac-[Pen]-S-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-E-S-H-[Sarc]-NH2; (SEQ ID NO: 62) Ac-[Pen]-N-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-E-N-H-[(D)NMeTyr]- NH2; (SEQ ID NO: 63) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-E-[(D)Asn]-H-{Sarc]- NH2; (SEQ ID NO: 64) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-E-G-H-[Sarc]-NH2; (SEQ ID NO: 65) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-E-[h(Ser)-H-[Sarc]- NH2; (SEQ ID NO: 66) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-E-N-H-P-NH2; (SEQ ID NO: 67) Ac-[Pen]-N-T-[W(7-(2-Nal))]-[Lys(Ac)]-[Pen]-Phe [4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-H-[Sarc]- NH2; (SEQ ID NO: 68) Ac-[Pen]-N-T-[W(7-3BiPh)]-[Lys(Ac)]-[Pen]-Phe[4- (2-aminoethoxy)]-[2-Nal]-[THP]-E-N-H-[Sarc]-NH2; (SEQ ID NO: 69) Ac-[Pen]-N-T-[W(7-(Phenanthren-5-yl)]-[Lys(Ac)]- [Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N- H-[Sarc]-NH2; (SEQ ID NO: 70) Ac-[Pen]-N-T-[W(7-(4-Anthracen-5-yl)]-[Lys(Ac)]- [Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N- H-[Sarc]-NH2; (SEQ ID NO: 71) Ac-[Pen]-N-T-[W(7-(1-Nal)))]-[Lys(Ac)]-[Pen]-Phe [4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-H-[Sarc]- NH2; (SEQ ID NO: 72) Ac-[Pen]-N-T-[W(7-4BiPh))]-[Lys(Ac)]-[Pen]-Phe [4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-H-[Sarc]- NH2; (SEQ ID NO: 73) Ac-[Pen]-N-T-[W(3:5-t-Bu-Ph))]-[Lys(Ac)]-[Pen]- Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-H- [Sarc]-NH2; (SEQ ID NO: 74) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4- CONH2)]-[2-Nal]-[THP]-E-N-H-[Sarc]-NH2; (SEQ ID NO: 75) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[(4- OMe)]-[2-Nal]-[THP]-E-N-H-[Sarc]-NH2; (SEQ ID NO: 78) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[3Quin]-[a-MeLys]-[Lys(Ac)]-N- [2Pal]-NH2; (SEQ ID NO: 79) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N- [2Pal]-NH2; (SEQ ID NO: 80) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N- [3Pal]-NH2; (SEQ ID NO: 81) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-[Lys(Ac)]-N-H- [Sarc]-NH2; (SEQ ID NO: 82) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N-H- [(D)NMeTyr]-NH2; (SEQ ID NO: 83) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]- Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]-E-N-H- [(D)NMeTyr]-NH2; (SEQ ID NO: 84) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)-N-Phe- [4-aminomethyl]-[(D)NMeTyr]-NH2; (SEQ ID NO: 85) Ac-[Pen]-N-T-[W(7-Me)]-[Cit]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLeu]-[Lys(Ac)-N- [(D)His]-NH2; (SEQ ID NO: 86) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)-N- [(D)His]-NH2; (SEQ ID NO: 87) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]- Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N- [(D)His]-[(D)NMeTyr]-NH2; (SEQ ID NO: 88) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]- Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-N- [(D)NMeTyr]-NH2; (SEQ ID NO: 89) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N-N- [(D)NMeTyr]-NH2; (SEQ ID NO: 90) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N- [(D)Val]-[(D)NMeTyr]-NH2; (SEQ ID NO: 91) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N- [(D)Thr]-[(D)NMeTyr]-NH2; (SEQ ID NO: 92) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]- Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N- [(D)His]-NH2; (SEQ ID NO: 93) Ac-[Abu]-N-T-[W(7-Ph]-Q-[Cys]-Phe[4-(2-amino- ethoxy)]-[3Quin]-[THP]-[Lys(Ac)]-E-N-H-[Sarc]- NH2; (SEQ ID NO: 94) Ac-[Abu]-N-T-[W(7-Me]-Q-[Cys]-Phe[4-(2-amino- ethoxy)]-[3Quin]-[THP]-[Lys(Ac)]-E-N-H-[Sarc]- NH2; (SEQ ID NO: 95) Ac-[Abu]-N-T-[W(7-Ph]-Q-[Cys]-Phe[4-(2-amino- ethoxy)]-[2Nal]-[a-MeLys]-[Lys(Ac)]-N-H- [Sarc]-NH2; (SEQ ID NO: 96) Ac-[Abu]-N-T-[W(7-Ph]-Q-[Cys]-Phe[4-(2-amino- ethoxy)]-[2Nal]-[THP]-E-N-H-[Sarc]-NH2; (SEQ ID NO: 97) Ac-[Abu]-N-T-[W(7-Me]-[Lys(Ac)]-[Cys]-Phe[4-(2- aminoethoxy)]-[2Nal]-[a-MeLys]-[Lys(Ac)]-N-H- [Sarc]-NH2; (SEQ ID NO: 98) Ac-[Abu]-N-T-[W(7-Ph]-[Lys(Ac)]-[Cys]-Phe[4-(2- aminoethoxy)]-[2Nal]-[THP]-E-N-H-[Sarc]-NH2; (SEQ ID NO: 99) Ac-[Abu]-N-T-[W(7-Me]-[Lys(Ac)]-[Cys]-Phe[4-(2- aminoethoxy)]-[2Nal]-[THP]-E-N-H-[Sarc]-NH2; (SEQ ID NO: 100) Ac-[(D)Arg]-[Abu]-S-T-[W(7-Me)]-Q-[Cys]-Phe[4- (2-aminoethoxy)]-[2-Nal]-[THP]-E-N-H-[Sarc]- NH2; (SEQ ID NO: 101) Ac-[(D)Arg]-[Abu]-N-T-[W(7-Me)]-Q-[Cys]-Phe[4- (2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[(D)Leu]- [Sarc]-NH2; (SEQ ID NO: 102) Ac-[(D)Arg]-[Abu]-N-T-[W(7-Me)]-[Cit]-[Cys]-Phe [4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-H-[Sarc]- NH2; (SEQ ID NO: 103) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N- [3Pal]-[Sarc]-NH2; (SEQ ID NO: 104) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]-[Sarc]- NH2; (SEQ ID NO: 105) Ac-[Pen]-N-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N- [3Pal]-[Sarc]-NH2; (SEQ ID NO: 106) Ac-[Pen]-N-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]-[Sarc]- NH2; (SEQ ID NO: 107) Ac-[Pen]-N-T-[W(7-Me)]-[Cit]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]-[Sarc]- NH2; (SEQ ID NO: 108) Ac-[Pen]-N-T-[W(7-Me)]-Q-[Pen]-Phe[4-(2-amino- ethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]-[Sarc]-NH2; (SEQ ID NO: 109) Ac-[Abu]-Q-T-[W(7-Me)]-Q-[Cys]-Phe[4-(2-amino- ethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]-[Sarc]-NH2; (SEQ ID NO: 110) Ac-[Abu]-Q-T-[W(7-Me)]-Q-[Cys]-Phe[4-(2-amino- ethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N-[3Pal]- [Sarc]-NH2; (SEQ ID NO: 111) Ac-[Abu]-Q-T-[W(7-Me)]-[Cit]-[Cys]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]-[Sarc]- NH2; (SEQ ID NO: 112) Ac-[Abu]-Q-T-[W(7-Me)]-[Cit]-[Cys]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N- [3Pal]-[Sarc]-NH2; (SEQ ID NO: 113) Ac-[Abu]-Q-T-[W(7-Me)]-Q-[Cys]-Phe[4-(2-amino- ethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]-[bA]-NH2; (SEQ ID NO: 114) Ac-[Abu]-Q-T-[W(7-Me)]-Q-[Cys]-Phe[4-(2-amino- ethoxy)]-[2-Nal]-[THP]-E-S-[3Pal]-[bA]-NH2; (SEQ ID NO: 115) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-E-N-[4Pal]-[Sarc]- NH2; (SEQ ID NO: 116) Ac-[Pen]-N-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]-[bA]-NH2; (SEQ ID NO: 117) Ac-[Pen]-N-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-[Lys(Ac)]-N-[3Pal]- [Sarc]-NH2; (SEQ ID NO: 118) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Quin]-[Sarc]- NH2; (SEQ ID NO: 119) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-E-N-[7-Aza-trypto- phan]-[Sarc]-NH2; (SEQ ID NO: 120) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N- [3Pal]-[(D)NMeTyr]-NH2; (SEQ ID NO: 121) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]- [(D)NMeTyr]-NH2; (SEQ ID NO: 122) Ac-[Pen]-N-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N- [3Pal]-[(D)NMeTyr]-NH2; (SEQ ID NO: 123) Ac-[Pen]-N-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]- [(D)NMeTyr]-NH2; (SEQ ID NO: 124) Ac-[Pen]-S-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-E-S-[3Pal]-[Sarc]- NH2; (SEQ ID NO: 125) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-E-S-[3Pal]-[Sarc]- NH2; (SEQ ID NO: 126) Ac-[Pen]-N-T-[W(7-Ph)]-[Cit]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]-[Sarc]- NH2; (SEQ ID NO: 127) Ac-[Pen]-N-T-[W(7-Ph)]-Q-[Pen]-Phe[4-(2-amino- ethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]-[Sarc]-NH2; (SEQ ID NO: 130) Ac-[Pen]-N-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N- [3Pal]-[bA]-NH2; (SEQ ID NO: 131) Ac-[Pen]-N-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]-[bA]-NH2; (SEQ ID NO: 132) Ac-[Pen]-S-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]-[Sarc]- NH2; (SEQ ID NO: 133) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-[Lys(Ac)]-N-[3Pal]- [Sarc]-NH2; (SEQ ID NO: 134) Ac-[Abu]-Q-T-[W(7-Ph)]-Q-[Cys]-Phe[4-(2-amino- ethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]-[Sarc]-NH2; (SEQ ID NO: 135) Ac-[Abu]-Q-T-[W(7-Ph)]-Q-[Cys]-Phe[4-(2-amino- ethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N-[3Pal]- [Sarc]-NH2; (SEQ ID NO: 136) Ac-[Pen]-N-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-[Lys(Ac)]-N-[3Pal]- [Sarc]-NH2; (SEQ ID NO: 137) Ac-[Pen]-N-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aceylaminoethoxy)]-[2-Nal]-[THP]-[Lys(Ac)]-N- [3Pal]-[Sarc]-NH2; (SEQ ID NO: 138) Ac-[Pen]-E-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-[Lys(Ac)]-N-[3Pal]- [Sarc]-NH2; (SEQ ID NO: 139) Ac-[Pen]-E-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-[Lys(Ac)]-N-[3Pal]- [Sarc]-NH2; (SEQ ID NO: 140) Ac-[Abu]-Q-T-[W(7-Me)]-Q-[Cys]-Phe[4-(2-amino- ethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]-[Sarc]-NH2; (SEQ ID NO: 141) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-[Lys(Ac)]-N-[3Pal]- [Sarc]-NH2; (SEQ ID NO: 142) Ac-[Pen]-N-T-[W(7-(3-carboxamidophenyl))]- [Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]- [THP]-E-N-[3Pal]-[Sarc]-NH2; (SEQ ID NO: 143) Ac-[Pen]-N-T-[W(7-pyrimidin-5-yl]-[Lys(Ac)]- [Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N- [3Pal]-[Sarc]-NH2; (SEQ ID NO: 144) Ac-[Pen]-N-T-[W(7-imidazopyridinyl]-[Lys(Ac)]- [Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N- [3Pal]-[Sarc]-NH2; (SEQ ID NO: 145) Ac-[Pen]-N-T-[W(7-Me]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[NMe(Lys)]-[Lys(Ac)]-N- [His_3Me]-NH2; (SEQ ID NO: 146) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me]-[Lys(Ac)]-[Pen]- Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N- [His_3Me]-NH2; (SEQ ID NO: 147) Ac-[Pen]-N-T-[W(7-(4Quin))]-[Lys(Ac)]-[Pen]- Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]- [Sarc]-NH2; (SEQ ID NO: 148) Ac-[Pen]-N-T-[W(7-(3-pyrazol-1-yl))]-[Lys(Ac)]- [Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N- [3Pal]-[Sarc]-NH2; (SEQ ID NO: 149) Ac-[Pen]-N-T-[W(7-(5-Et)]-[Lys(Ac)]-[Pen]-Phe[4- (2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]- [Sarc]-NH2; (SEQ ID NO: 150) Ac-[Pen]-N-T-[W(5-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]-[Sarc]- NH2; (SEQ ID NO: 151) Ac-[Pen]-N-T-[W(7-(3-pyrazol-1-yl))]-[Lys(Ac)]- [Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N- [3Pal]-[Sarc]-NH2; (SEQ ID NO: 152) Ac-[Pen]-N-T-[W(7-indazol-5-yl)]-[Lys(Ac)]- [Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N- [3Pal]-[Sarc]-NH2; (SEQ ID NO: 153) Ac-[Pen]-N-T-[W(4-F)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]-[Sarc]- NH2; (SEQ ID NO: 154) Ac-[Pen]-N-T-[W(5-CN)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]-[Sarc]- NH2; (SEQ ID NO: 155) Ac-[Pen]-N-T-[W(7-CN)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]-[Sarc]- NH2; (SEQ ID NO: 156) Ac-[Pen]-N-T-[W(4-Ome)]-[Lys(Ac)]-[Pen]-Phe[4- (2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]- [Sarc]-NH2; (SEQ ID NO: 157) Ac-[Pen]-N-T-[W(4-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]-[Sarc]- NH2; (SEQ ID NO: 158) Ac-[Pen]-N-T-W-[Lys(Ac)]-[Pen]-Phe[4-(2-amino- ethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]-[Sarc]-NH2; (SEQ ID NO: 159) Ac-[Pen]-N-T-W-[Lys(Ac)]-[Pen]-Phe[4-(2-amino- ethoxy)]-[2-Nal]-[Acvc]-E-N-[3Pal]-[Sarc]-NH2; (SEQ ID NO: 160) Ac-[Pen]-N-T-[W(5-Ca)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]-[Sarc]- NH2; (SEQ ID NO: 161) Ac-[Pen]-N-T-[Trp_4Aza]]-[Lys(Ac)]-[Pen]-Phe[4- (2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]- [Sarc]-NH2; (SEQ ID NO: 162) Ac-[Pen]-N-T-W-[Lys(Ac)]-[Pen]-Phe[4-(2-amino- ethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]-[Sarc]-NH2; (SEQ ID NO: 163) Ac-[Pen]-N-T-W-[Lys(Ac)]-[Pen]-Phe[4-(2-amino- ethoxy)]-[2-Nal]-[THP]-[Lys(Ac)]-N-[3Pal]- [Sarc]-NH2; (SEQ ID NO: 164) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]- Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N- [5Pyal]-NH2; (SEQ ID NO: 165) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N- [5Pyal]-NH2; (SEQ ID NO: 166) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]- Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N- [(1-Me)His]-NH2; (SEQ ID NO: 167) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N- [(1-Me)His]-NH2; (SEQ ID NO: 168) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N- [3Pal]-[(D)NMeTyr]-NH2; (SEQ ID NO: 169) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N- [Aib]-[(D)Thr]-NH2; (SEQ ID NO: 170) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-E-N-H-[(D)Pro]-NH2; (SEQ ID NO: 201) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Cit]-[Pen]-Phe [4-(2-aminoethoxy)]-[2-Nal]-[aMeLeu]-E-N- [(D)Lys]-[(D)NMeTyr]-NH2; (SEQ ID NO: 202) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Cit]-[Pen]-Phe [4-(2-aminoethoxy)]-[2-Nal]-[aMeLeu]-E-N- ((D)His]-[(D)NMeTyr]-NH2; (SEQ ID NO: 203) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N- ((D)Orn]-[(D)NMeTyr]-NH2; (SEQ ID NO: 204) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N- [(D)Ser]-[(D)NMeTyr]-NH2; (SEQ ID NO: 205) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N- ((D)Phe]-[(D)NMeTyr]-NH2; (SEQ ID NO: 206) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]- Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-H- [(D)Tyr]-NH2; (SEQ ID NO: 207) Ac-[Pen]-N-T-[W(7-Me)]-[(D)Tyr]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N- [(D)Lys]-[(D)NMeTyr]-NH2; (SEQ ID NO: 208) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]- Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-H-P- NH2; (SEQ ID NO: 209) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]- Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-H- [(D)Pro]-NH2; (SEQ ID NO: 210) Ac-[Pen]-N-T-[W(7-Me)]-[Phe(4-CONH2)]-[Pen]-Phe [4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]- N-[(D)Lys]-[(D)NMeTyr]-NH2; (SEQ ID NO: 211) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4- (2-aminoethoxy)]-[2-Nal]-[Acvc]-E-N-(D)Phe[4- NH2]-[Sarc]-NH2; (SEQ ID NO: 212) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac))]- [Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N- H-NH2; (SEQ ID NO: 213) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4- (2-aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N- H-N(H)Me; (SEQ ID NO: 214) Ac-[Pen]-N-T-[W(7-Me)]-[Phe(4-NH(Ac)))]-[Pen]- Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]- [Lys(Ac)]-N-[(D)Lys]-[(D)NMeTyr]-NH2; (SEQ ID NO: 215) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N- [(D)Lys]-[(D)NMeTyr]-NH2; (SEQ ID NO: 216) Ac-[Pen]-N-T-[W(7-Me)]-[Cit]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLeu]-[Lys(Ac)]-N- [(D)His]-[(D)NMeTyr]-NH2; (SEQ ID NO: 217) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N- [(D)His]-[(D)NMeTyr]-NH2; (SEQ ID NO: 218) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N- [bAla]-[(D)NMeTyr]-NH2; (SEQ ID NO: 219) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N- [bAla]-[(D)NMeTyr]-NH2; (SEQ ID NO: 220) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N- [bAla]-[(D)NMeTyr]-NH2; (SEQ ID NO: 221) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]- Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]-E-N-H- N(H)Me; (SEQ ID NO: 222) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]- Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[THP]- P-NH2; (SEQ ID NO: 223) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]- Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[THP]- [(D)Pro]-NH2; (SEQ ID NO: 224) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]- Phe[4-(2-aminoethoxy)]-[2-Nal]-[Acvc]-E-N- [bAla]-[Sarc]-NH2; (SEQ ID NO: 225) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]- Phe[4-(2-aminoethoxy)]-[2-Nal]-[Acvc]-E-N- [(D)Val]-[Sarc]-NH2; (SEQ ID NO: 226) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]- Phe[4-(2-aminoethoxy)]-[2-Nal]-[Acvc]-E-N- [(D)Arg]-[Sarc]-NH2; (SEQ ID NO: 227) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]- Phe[4-(2-aminoethoxy)]-[2-Nal]-[Acvc]-E-N- [Hph]-[Sarc]-NH2; (SEQ ID NO: 228) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[Acvc]-E-N-Phe[4-NH2]- [Sarc]-NH2; (SEQ ID NO: 229) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]- Phe[4-(2-aminoethoxy)]-[2-Nal]-[Acvc]-E-N-Phe[4- NH2]-[Sarc]-NH2; (SEQ ID NO: 230) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]- Phe[4-(2-aminoethoxy)]-[2-Nal]-[Acvc]-E-N-F- [Sarc]-NH2; (SEQ ID NO: 231) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]- Phe[4-(2-aminoethoxy)]-[2-Nal]-[Acvc]-E-N-[THP]- [Sarc]-NH2; (SEQ ID NO: 232) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]- Phe[4-(2-aminoethoxy)]-[2-Nal]-[Acvc]-E-N- [(D)Leu]-[Sarc]-NH2; (SEQ ID NO: 233) Ac-[(D)Arg]-[Cys]-N-T-[W(7-Me)]-[Lys(Ac)]- [aMeCys]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[Acvc]- E-N-H-[Sarc]-NH2; (SEQ ID NO: 234) Ac-[(D)Arg]-[Cys]-N-T-[W(7-Me)]-[Lys(Ac)]- [aMeCys]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[Acvc]- E-N-[(D)Leu]-[Sarc]-NH2; (SEQ ID NO: 235) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]- Phe[4-(2-aminoethoxy)]-[2-Nal]-[Acvc]-E-N- [3Pal]-[Sarc]-NH2; (SEQ ID NO: 236) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N- [bAla]-[Sarc]-NH2; (SEQ ID NO: 237) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N- [(D)Val]-[Sarc]-NH2; (SEQ ID NO: 238) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N- [(D)Arg]-[Sarc]-NH2; (SEQ ID NO: 239) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N- [Hph]-[Sarc]-NH2; (SEQ ID NO: 240) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N- [(D)Tyr]-[Sarc]-NH2; (SEQ ID NO: 241) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N- [(D)Tyr]-[Sarc]-NH2; (SEQ ID NO: 242) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]- Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[4Pal]- [Sarc]-NH2; (SEQ ID NO: 243) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N- [Phe(4-CF3)]-[Sarc]-NH2; (SEQ ID NO: 244) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N- Tyr_CHF2-[Sarc]-NH2; (SEQ ID NO: 245) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N- [THP]-P-[Sarc]-NH2; (SEQ ID NO: 246) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N- [3Pal]-[(D)NMeTyr]-NH2; (SEQ ID NO: 247) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]- Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]- [Sarc]-NH2; (SEQ ID NO: 248) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]- Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[4Pal]- [Sarc]-NH2; (SEQ ID NO: 249) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]- Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[Phe(2- aminomethyl]-[Sarc]-NH2; (SEQ ID NO: 250) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]- Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]- [Pro(4;4diF)]-NH2; (SEQ ID NO: 251) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]- Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]- [aMePro]-NH2; (SEQ ID NO: 252) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]- Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]- [Aib]-NH2; (SEQ ID NO: 253) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N- [His(3-Me)]-[Sarc]-NH2; (SEQ ID NO: 261) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]- Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[His(3- Me)]-[Sarc]-NH2; (SEQ ID NO: 262) Ac-[(D)Arg]-[Pen]-N-T-W-[Lys(Ac)]-[Pen]-Phe[4- (2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[His(3-Me)]- [Sarc]-NH2; (SEQ ID NO: 266) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]- Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]- [Sarc]-NH2; (SEQ ID NO: 267) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]- Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]- N(H)Me; (SEQ ID NO: 270) [(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe [4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]- [Sarc]-NH2; (SEQ ID NO: 271) Ac-[(D)Arg]-[Pen]-N-T-W-[Lys(Ac)]-[Pen]-Phe[4- (2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]- [Sarc]-NH2; (SEQ ID NO: 272) Pr-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]- Phe[4-(2-(N-propionylamino)ethoxy)]-[2-Nal]- [THP]-E-N-[3Pal]-[Sarc]-NH2; (SEQ ID NO: 273) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]- Phe[4-(2-(N-(4-hydroxy-3-methylphenyl)propionyl- amino)ethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]-[Sarc]- NH2; (SEQ ID NO: 274) [N3_Acid]-[(D)Arg]-[Pen]-N-T-[W(7-Me)]- [Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]- [THP]-E-N-[3Pal]-[Sarc]-NH2; (SEQ ID NO: 275) [FPrpTriazoleMe_Acid]-[(D)Arg]-[Pen]-N-T-[W(7- Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2- Nal]-[THP]-E-N-[3Pal]-[Sarc]-NH2; (SEQ ID NO: 276) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]- Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N- [3Pal(5-Me)]-[Sarc]-NH2; (SEQ ID NO: 277) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]- Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N- [3Pal(5-NH2)]-[Sarc]-NH2; (SEQ ID NO: 278) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-E-N-[His(3-Me)]- N(H)Me; (SEQ ID NO: 279) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]- Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]- [(D)NMeTyr]-NH2; (SEQ ID NO: 280) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]- Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]- [Gly(N-cyclohexylmethyl)]-NH2; (SEQ ID NO: 281) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]- Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]- [Gly(N-isobutyl)]-NH2; (SEQ ID NO: 282) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]- Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N- [3Pal(3-Me)]-NH2; (SEQ ID NO: 283) Ac-[(D)Arg]-[aMeCys]-N-T-[W(7-Me)]-[Lys(Ac)]- [Cys]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N- [3Pal]-[Sarc]-NH2; (SEQ ID NO: 284) Ac-[Pen]-N-T-W-[Lys(Ac)]-[Pen]-Phe[4-(2-amino- ethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]-[Sarc]-NH2; (SEQ ID NO: 285) Ac-[Pen]-N-T-W-[Lys(Ac)]-[Pen]-Phe[4-(2-amino- ethoxy)]-[2-Nal]-[Acvc]-E-N-[3Pal]-[Sarc]-NH2; (SEQ ID NO: 286) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-[Phe(4- CONH2)]-[2-Nal]-[THP]-E-N-[3Pal]-[Sarc]-NH2; (SEQ ID NO: 287) Ac-[Pen]-[Gly(Allyl)]-T-[W(7-Me)]-[Lys(Ac)]- [Pen]-[Tyr(O-Allyl)]-[2-Nal]-[THP]-[Lys(Ac)]-N- [3Pal]-[Sarc]-NH2; (SEQ ID NO: 288) Ac-[Pen]-[Gly(Allyl)]-D-[W(7-Me)]-[Lys(Ac)]- [Pen]-[Tyr(O-Allyl)]-[2-Nal]-[THP]-[Lys(Ac)]-N- [3Pal]-[Sarc]-NH2; (SEQ ID NO: 289) Ac-[Pen]-[Gly(Allyl)]-T-[W(4-F)]-[Lys(Ac)]- [Pen]-[Tyr(O-Allyl)]-[2-Nal]-[THP]-[Lys(Ac)]-N- [3Pal]-[Sarc]-NH2; (SEQ ID NO: 290) Ac-[Pen]-N-D-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]-[Sarc]- NH2; (SEQ ID NO: 291) Ac-[Pen]-L-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]-[Sarc]- NH2; (SEQ ID NO: 299) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-[Phe(4- CONH2)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N-[3Pal]- [Sarc]-NH2; (SEQ ID NO: 308) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-F-[2- Nal]-[THP]-[Lys(Ac)]-N-[3Pal]-[Sarc]-NH2; (SEQ ID NO: 309) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-[(D)Tyr]- [2-Nal]-[THP]-[Lys(Ac)]-N-[3Pal]-[Sarc]-NH2; (SEQ ID NO: 310) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-[Phe(4- Ome)]-[2-Nal]-[THP]-[Lys(Ac)]-N-[3Pal]-[Sarc]- NH2; (SEQ ID NO: 311) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-[Phe(4- CONH2)]-[2-Nal]-[THP]-[Lys(Ac)]-N-[3Pal]-[Sarc]- NH2; (SEQ ID NO: 332) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(N-acetyl-N-propyl)]- [Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N- [3Pal]-[Sarc]-NH2; (SEQ ID NO: 333) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(N-acetyl-N-butyl)]- [Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N- [3Pal]-[Sarc]-NH2; (SEQ ID NO: 334) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(N-acetyl-N-isobut- yl)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]- E-N-[3Pal]-[Sarc]-NH2; (SEQ ID NO: 335) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(N-acetyl-N-benzyl)]- [Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N- [3Pal]-[Sarc]-NH2; (SEQ ID NO: 339) Ac-[Pen]-L-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-[Phe(4- CONH2)]-[2-Nal]-[aMeLeu]-E-N-[3Pal]-[Sarc]-NH2; (SEQ ID NO: 347) Ac-[Pen]-L-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-[Phe(4- OMe)]-[2-Nal]-[aMeLeu]-E-N-[3Pal]-[Sarc]-NH2; (SEQ ID NO: 373) Ac-[Abu]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]-[Sarc]- NH2; or a pharmaceutically acceptable salt thereof.

163. The monocyclic peptide inhibitor of an interleukin-23 receptor of claim 162, wherein the monocyclic peptide inhibitor is: (SEQ ID NO: 1) Ac-[(D)Arg]-[Abu]-Q-T-[W(7-Ph)]-[Lys(Ac)]-[Cys]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a- MeLys]-[Lys(Ac)]-N-dK4Sarc]-NH2; (SEQ ID NO: 2) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[3-Quin]-[a-MeLys]- [Lys(Ac)]-N-[(D)Leu)]-[Sarc]-NH2; (SEQ ID NO: 3) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[3-Quin]-[THP]-E-N- [(D)Lys]-[Sarc]-NH2; (SEQ ID NO: 4) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[3-Quin]-[a-MeLys]- [Lys(Ac)]-N-[(D)His]-[Sarc]-NH2; (SEQ ID NO: 5) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[3-Quin]-[a-MeLys]- [Lys(Ac)]-N-H-[Sarc]-NH2; (SEQ ID NO: 6) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[3-Quin]-[THP]-E-N- [(D)Leu)]-[Sarc]-NH2; (SEQ ID NO: 7) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[3-Quin]-[a-MeLys]- [Lys(Ac)]-N-[(D)Lys]-[Sarc]-NH2; (SEQ ID NO: 8) Ac-[(D)Arg]-[Abu]-Q-T-W-Q-[Cys]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-N- [(D)NMeTyr]-NH2; (SEQ ID NO: 9) Ac-[(D)Arg]-[Pen]-Q-T-W-Q-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-N- [(D)NMeTyr]-NH2; (SEQ ID NO: 10) Ac-[(D)Arg]-[Pen]-Q-T-W-Q-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-[aMeGlu]-N-F- [(D)NMeTyr]-NH2; (SEQ ID NO: 11) Ac-[Pen]-N-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[3Quin]-[THP]-E-N- [(D)Lys]-[Sarc]-NH2; (SEQ ID NO: 12) Ac-[Pen]-N-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[3Quin]-[a-MeLys]- [Lys(Ac)]-N-[(D)Lys]-[Sarc]-NH2; (SEQ ID NO: 13) Ac-[Pen]-N-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[3Quin]-[THP]-E-N- [(D)Leu]-[Sarc]-NH2; (SEQ ID NO: 14) Ac-[Pen]-N-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[3Quin]-[a-MeLys]- [Lys(Ac)]-N-[(D)Leu]-[Sarc]-NH2; (SEQ ID NO: 15) Ac-[Pen]-N-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[3Quin]-[THP]-E-N-H- [Sarc]-NH2; (SEQ ID NO: 16) Ac-[Pen]-N-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[3Quin]-[a-MeLys]- [Lys(Ac)]-N-H-[Sarc]-NH2; (SEQ ID NO: 17) Ac-[Abu]-Q-T-[W(7-Me)]-[Lys(Ac)]-[Cys]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]- [Lys(Ac)]-N-[(D)Lys]-[Sarc]-NH2; (SEQ ID NO: 18) Ac-[Abu]-Q-T-[W(7-Ph)]-[Lys(Ac)]-[Cys]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]- [Lys(Ac)]-N-[(D)Lys]-[Sarc]-NH2; (SEQ ID NO: 20) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]- [Lys(Ac)]-N-[(D)Leu]-[Sarc]-NH2; (SEQ ID NO: 21) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]- [Lys(Ac)]-N-[(D)Lys]-[Sarc]-NH2; (SEQ ID NO: 22) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-H- [Sarc]-NH2; (SEQ ID NO: 23) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]- [Lys(Ac)]-N-H-[Sarc]-NH2; (SEQ ID NO: 24) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N- [(D)Leu]-[Sarc]-NH2; (SEQ ID NO: 25) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]- [Lys(Ac)]-N-[(D)Leu]-[Sarc]-NH2; (SEQ ID NO: 26) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Gly)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-H- [Sarc]-NH2; (SEQ ID NO: 27) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Gly)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]- [Lys(Ac)]-N-H-[Sarc]-NH2; (SEQ ID NO: 28) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Gly)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N- [(D)Leu]-[Sarc]-NH2; (SEQ ID NO: 29) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Gly)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]- [Lys(Ac)]-N-[(D)Leu]-[Sarc]-NH2; (SEQ ID NO: 30) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(bAla)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N- H-[Sarc]-NH2; (SEQ ID NO: 31) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(bAla)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]- [Lys(Ac)]-N-H-[Sarc]-NH2; (SEQ ID NO: 32) Ac-[Pen]-N-T-[W(7-Et)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-H- [Sarc]-NH2; (SEQ ID NO: 33) Ac-[Pen]-N-T-[W(7-Et)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]- [Lys(Ac)]-N-H-[Sarc]-NH2; (SEQ ID NO: 34) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[W(7-Et)]-[a-MeLys]- [Lys(Ac)]-N-H-[Sarc]-NH2; (SEQ ID NO: 35) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[W(4-Me)]-[a-MeLys]- [Lys(Ac)]-N-H-[Sarc]-NH2; (SEQ ID NO: 36) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[W(6-Me)]-[a-MeLys]- [Lys(Ac)]-N-H-[Sarc]-NH2; (SEQ ID NO: 37) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[W(4-OMe)]-[a- MeLys]-[Lys(Ac)]-N-H-[Sarc]-NH2; (SEQ ID NO: 38) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[W(7-i-Pr)]-[a-MeLys]- [Lys(Ac)]-N-H-[Sarc]-NH2; (SEQ ID NO: 39) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[W(7-nPr)]-[a-MeLys]- [Lys(Ac)]-N-H-[Sarc]-NH2; (SEQ ID NO: 40) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[W(7-OMe)]-[a- MeLys]-[Lys(Ac)]-N-H-[Sarc]-NH2; (SEQ ID NO: 41) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[W(6-Cl)]-[a-MeLys]- [Lys(Ac)]-N-H-[Sarc]-NH2; (SEQ ID NO: 42) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[W(5-OMe)]-[a- MeLys]-[Lys(Ac)]-N-H-[Sarc]-NH2; (SEQ ID NO: 43) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[W(3-MePh)]-[a- MeLys]-[Lys(Ac)]-N-H-[Sarc]-NH2; (SEQ ID NO: 44) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[W(6-Ph)]-[a-MeLys]- [Lys(Ac)]-N-H-[Sarc]-NH2; (SEQ ID NO: 45) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[W(6-Et]-[a-MeLys]- [Lys(Ac)]-N-H-[Sarc]-NH2; (SEQ ID NO: 46) Ac-[Pen]-N-T-[W(7-(2-FPh)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]- [Lys(Ac)]-N-H-[Sarc]-NH2; (SEQ ID NO: 47) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]- [Lys(Ac)]-N-[(D)Leu]-[(D)NMeTyr]-NH2; (SEQ ID NO: 48) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]- [Lys(Ac)]-N-[(D)Lys]-[(D)NMeTyr]-NH2; (SEQ ID NO: 49) Ac-[Pen]-N-T-[W(7-(2-OMePh)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a- MeLys]-[Lys(Ac)]-N-H-[Sarc]-NH2; (SEQ ID NO: 50) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[W(7-Ph)]-[a-MeLys]- [Lys(Ac)]-N-H-[Sarc]-NH2; (SEQ ID NO: 51) Ac-[Pen]-N-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]- [Lys(Ac)]-N-H-[Sarc]-NH2; (SEQ ID NO: 52) Ac-[Pen]-N-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-H- [Sarc]-NH2; (SEQ ID NO: 53) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[3Quin]-[THP]-E-N-H- [Sarc]-NH2; (SEQ ID NO: 54) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-S-H- [Sarc]-NH2; (SEQ ID NO: 55) Ac-[Pen]-S-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-H- [Sarc]-NH2; (SEQ ID NO: 56) Ac-[Pen]-S-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-S-H- [Sarc]-NH2; (SEQ ID NO: 57) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-H- [(D)NMeTyr]-NH2; (SEQ ID NO: 58) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]- [Lys(Ac)]-N-F-[(D)NMeTyr]-NH2; (SEQ ID NO: 59) Ac-[Pen]-N-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-S-H- [Sarc]-NH2; (SEQ ID NO: 60) Ac-[Pen]-S-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-H- [Sarc]-NH2; (SEQ ID NO: 61) Ac-[Pen]-S-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-S-H- [Sarc]-NH2; (SEQ ID NO: 62) Ac-[Pen]-N-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-H- [(D)NMeTyr]-NH2; (SEQ ID NO: 63) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E- [(D)Asn]-H-[Sarc]-NH2; (SEQ ID NO: 64) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-G-H- [Sarc]-NH2; (SEQ ID NO: 65) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E- [h(Ser)]-H-[Sarc]-NH2; (SEQ ID NO: 66) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-H- P-NH2; (SEQ ID NO: 67) Ac-[Pen]-N-T-[W(7-(2-Nal))]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N- H-[Sarc]-NH2; (SEQ ID NO: 68) Ac-[Pen]-N-T-[W(7-3BiPh)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N- H-[Sarc]-NH2; (SEQ ID NO: 69) Ac-[Pen]-N-T[W(7-(Phenanthren-5-yl))]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]- [THP]E-N-H-[Sarc]-NH2; (SEQ ID NO: 70) Ac-[Pen]-N-T-[W(7-(4-Anthracen-5-yl))]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]- [THP]-E-N-H-[Sarc]-NH2; (SEQ ID NO: 71) Ac-[Pen]-N-T-[W(7-(1-Nal))]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]42-Nal]-[THP]-E-N- H-[Sarc]-NH2; (SEQ ID NO: 72) Ac-[Pen]-N-T-[W(7-(4BiPh))]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E- N-H-[Sarc]-NH2; (SEQ ID NO: 73) Ac-[Pen]-N-T-[W(7-(3,5-t-Bu-Ph))]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]- [THP]E-N-H-[Sarc]-NH2; (SEQ ID NO: 74) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-[Phe(4-CONH2)]-[2-Nal]-[THP]-E-N-H-[Sarc]- NH2; (SEQ ID NO: 75) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-[Phe(4-OMe)]-[2-Nal]-[THP]-E-N-H-[Sarc]-NH2; (SEQ ID NO: 78) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[3Quin]-[a-MeLys]- [Lys(Ac)]-N-[2Pal]-NH2; (SEQ ID NO: 79) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]- [Lys(Ac)]-N-[2Pal]-NH2; (SEQ ID NO: 80) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]- [Lys(Ac)]-N-[3Pal]-NH2; (SEQ ID NO: 81) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]- [Lys(Ac)]-N-H-[Sarc]-NH2; (SEQ ID NO: 82) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]- [Lys(Ac)]-N-H-[(D)NMeTyr]-NH2; (SEQ ID NO: 83) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a- MeLys]-E-N-H-[(D)NMeTyr]-NH2; (SEQ ID NO: 84) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]- [Lys(Ac)]-N-Phe[4-aminomethyl]-[(D)NMeTyr]-NH2; (SEQ ID NO: 85) Ac-[Pen]-N-T-[W(7-Me)]-[Cit]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[aMeLeu]-[Lys(Ac)]- N-[(D)His]-NH2; (SEQ ID NO: 86) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]- [Lys(Ac)]-N-[(D)His]-NH2; (SEQ ID NO: 87) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]- [THP]-E-N-[(D)His]-[(D)NMeTyr]-NH2; (SEQ ID NO: 88) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]- [THP]-E-N-N-[(D)NMeTyr]-NH2; (SEQ ID NO: 89) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]- [Lys(Ac)]-N-N-[(D)NMeTyr]-NH2; (SEQ ID NO: 90) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]- [Lys(Ac)]-N-[(D)Val]-[(D)NMeTyr]-NH2; (SEQ ID NO: 91) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]- [Lys(Ac)]-N-[(D)Thr]-[(D)NMeTyr]-NH2; (SEQ ID NO: 92) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]- [THP]-E-N-[(D)His]-NH2; (SEQ ID NO: 93) Ac-[Abu]-N-T-[W(7-Ph)]-Q-[Cys]-Phe[4-(2-aminoethoxy)]-[3Quin]-[THP]-E-N-H-[Sarc]- NH2; (SEQ ID NO: 94) Ac-[Abu]-N-T-[W(7-Me)]-Q-[Cys]-Phe[4-(2-aminoethoxy)]-[3 Quin]-[THP]-E-N-H-[Sarc]- NH2; (SEQ ID NO: 95) Ac-[Abu]N-T-[W(7-Ph)]-Q-[Cys]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]- N-H-[Sarc]-NH2; (SEQ ID NO: 96) Ac-[Abu]N-T-[W(7-Ph)]-Q-[Cys]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]E-N-H-[Sarc]- NH2; (SEQ ID NO: 97) Ac-[Abu]-N-T-[W(7-Me)]-[Lys(Ac)]-[Cys]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]- [Lys(Ac)]-N-H-[Sarc]-NH2; (SEQ ID NO: 98) Ac-[Abu]-N-T-[W(7-Ph)]-[Lys(Ac)]-[Cys]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-H- [Sarc]-NH2; (SEQ ID NO: 99) Ac-[Abu]-N-T-[W(7-Me)]-[Lys(Ac)]-[Cys]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-H- [Sarc]-NH2; (SEQ ID NO: 100) Ac-[(D)Arg]-[Abu]-S-T-[W(7-Me)]-Q-[Cys]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N- H-[Sarc]-NH2; (SEQ ID NO: 101) Ac-[(D)Arg]-[Abu]-N-T-[W(7-Me)]-Q-[Cys]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N- [(D)Leu]-[Sarc]-NH2; (SEQ ID NO: 102) Ac-[(D)Arg]-[Abu]-N-T-[W(7-Me)]-[Cit]-[Cys]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E- N-H-[Sarc]-NH2; (SEQ ID NO: 103) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]- [Lys(Ac)]-N-[3Pal]-[Sarc]-NH2; (SEQ ID NO: 104) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N- [3Pal]-[Sarc]-NH2; (SEQ ID NO: 105) Ac-[Pen]-N-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]- [Lys(Ac)]-N-[3Pal]-[Sarc]-NH2; (SEQ ID NO: 106) Ac-[Pen]-N-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N- [3Pal]-[Sarc]-NH2; (SEQ ID NO: 107) Ac-[Pen]-N-T-[W(7-Me)]-[Cit]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]- [Sarc]-NH2; (SEQ ID NO: 108) Ac-[Pen]-N-T-[W(7-Me)]-Q-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]- [Sarc]-NH2; (SEQ ID NO: 109) Ac-[Abu]-Q-T-[W(7-Me)]-Q-[Cys]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]- [Sarc]-NH2; (SEQ ID NO: 110) Ac-[Abu]-Q-T-[W(7-Me)]-Q-[Cys]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]- N-[3Pal]-[Sarc]-NH2; (SEQ ID NO: 111) Ac-[Abu]-Q-T-[W(7-Me)]-[Cit]-[Cys]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]- [Sarc]-NH2; (SEQ ID NO: 112) Ac-[Abu]-Q-T-[W(7-Me)]-[Cit]-[Cys]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]- [Lys(Ac)]-N-[3Pal]-[Sarc]-NH2; (SEQ ID NO: 113) Ac-[Abu]-Q-T-[W(7-Me)]-Q-[Cys]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]- [bA]-NH2; (SEQ ID NO: 114) Ac-[Abu]-Q-T-[W(7-Me)]-Q-[Cys]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-S-[3Pal]- [bA]-NH2; (SEQ ID NO: 115) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N- [4Pal]-[Sarc]-NH2; (SEQ ID NO: 116) Ac-[Pen]-N-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N- [3Pal]-[bA]-NH2; (SEQ ID NO: 117) Ac-[Pen]-N-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]- [Lys(Ac)]-N-[3Pal]-[Sarc]-NH2; (SEQ ID NO: 118) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N- [3Quin]-[Sarc]-NH2; (SEQ ID NO: 119) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[7- Aza-tryptophan]-[Sarc]-NH2; (SEQ ID NO: 120) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]- [Lys(Ac)]-N-[3Pal]-[(D)NMeTyr]-NH2; (SEQ ID NO: 121) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N- [3Pal]-[(D)NMeTyr]-NH2; (SEQ ID NO: 122) Ac-[Pen]-N-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]- [Lys(Ac)]-N-[3Pal]-[(D)NMeTyr]-NH2; (SEQ ID NO: 123) Ac-[Pen]-N-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N- [3Pal]-[(D)NMeTyr]-NH2; (SEQ ID NO: 124) Ac-[Pen]-S-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-S- [3Pal]-[Sarc]-NH2; (SEQ ID NO: 125) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-S- [3Pal]-[Sarc]-NH2; (SEQ ID NO: 126) Ac-[Pen]-N-T-[W(7-Ph)]-[Cit]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]- [Sarc]-NH2; (SEQ ID NO: 127) Ac-[Pen]-N-T-[W(7-Ph)]-Q-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]- [Sarc]-NH2; (SEQ ID NO: 130) Ac-[Pen]-N-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]- [Lys(Ac)]-N-[3Pal]-[bA]-NH2; (SEQ ID NO: 131) Ac-[Pen]-N-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N- [3Pal]-[bA]-NH2; (SEQ ID NO: 132) Ac-[Pen]-S-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N- [3Pal]-[Sarc]-NH2; (SEQ ID NO: 133) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]- [Lys(Ac)]-N-[3Pal]-[Sarc]-NH2; (SEQ ID NO: 134) Ac-[Abu]-Q-T-[W(7-Ph)]-Q-[Cys]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]- [Sarc]-NH2; (SEQ ID NO: 135) Ac-[Abu]-Q-T-[W(7-Ph)]-Q-[Cys]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]- N-[3Pal]-[Sarc]-NH2; (SEQ ID NO: 136) Ac-[Pen]-N-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]- [Lys(Ac)]-N-[3Pal]-[Sarc]-NH2; (SEQ ID NO: 137) Ac-[Pen]-N-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aceylaminoethoxy)]-[2-Nal]-[THP]- [Lys(Ac)]-N-[3Pal]-Sarc]-NH2; (SEQ ID NO: 138) Ac-[Pen]-E-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]- [Lys(Ac)]-N-[3Pal]-[Sarc]-NH2; (SEQ ID NO: 139) Ac-[Pen]-E-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]- [Lys(Ac)]-N-[3 Pal]-[Sarc]-NH2; (SEQ ID NO: 140) Ac-[Abu]Q-T-[W(7-Me)]-Q-[Cys]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]- [Sarc]-NH2; (SEQ ID NO: 141) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]- [Lys(Ac)]-N-[3Pal]-[Sarc]-NH2; (SEQ ID NO: 142) Ac-[Pen]-N-T-[W(7-(3-carboxamidopheny1))]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2- Nal]-[THP]-E-N-[3Pal]-[Sarc]-NH2; (SEQ ID NO: 143) Ac-[Pen]-N-T-[W(7-pyrimidin-5-yl)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]- [THP]-E-N-[3Pal]-[Sarc]-NH2; (SEQ ID NO: 144) Ac-[Pen]-N-T-[W(7-imidazopyridinyl)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]- [THP]-E-N-[3Pal]-[Sarc]-NH2; (SEQ ID NO: 145) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[NMe(Lys)]- [Lys(Ac)]-N-[His_3Me]-NH2; (SEQ ID NO: 146) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]- [THP]-E-N-[His_3Me]-NH2; (SEQ ID NO: 147) Ac-[Pen]-N-T-[W(7-(4Quin))]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E- N-[3Pal]-[Sarc]-NH2; (SEQ ID NO: 148) Ac-[Pen]-N-T-[(W(7-(3-pyrazol-l-yl))]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]- [THP]-E-N-[3Pal]-[Sarc]-NH2; (SEQ ID NO: 149) Ac-[Pen]-N-T-[(W(7-(5-Et))]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N- [3Pal]-[Sarc]-NH2; (SEQ ID NO: 150) Ac-[Pen]-N-T-[W(5-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N- [3Pal]-[Sarc]-NH2; (SEQ ID NO: 151) Ac-[Pen]-N-T-[(W(7-(3-pyrazol-l-yl))-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]- [THP]-E-N-[3Pal]-[Sarc]-NH2; (SEQ ID NO: 152) Ac-[Pen]-N-T-[W(7-indazol-5-yl)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]- E-N-[3Pal]-[Sarc]-NH2; (SEQ ID NO: 153) Ac-[Pen]-N-T-[W(4-F)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N- [3Pal]-[Sarc]-NH2; (SEQ ID NO: 154) Ac-[Pen]-N-T-[W(5-CN)]-[Lys(Ac)]-[Pen]-Phe[4-(2-arninoethoxy)]-[2-Nal]-[THP]-E-N- [3Pal]-[Sarc]-NH2; (SEQ ID NO: 155) Ac-[Pen]-N-T-[W(7-CN)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N- [3Pal]-[Sarc]-NH2; (SEQ ID NO: 156) Ac-[Pen]-N-T-[W(4-OMe)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N- [3Pal]-[Sarc]-NH2; (SEQ ID NO: 157) Ac-[Pen]-N-T-[W(4-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N- [3Pal]-[Sarc]-NH2; (SEQ ID NO: 158) Ac-[Pen]-N-T-W-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]- [Sarc]-NH2; (SEQ ID NO: 159, 285) Ac-[Pen]-N-T-W-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[Acvc]-E-N-[3Pal]- [Sarc]-NH2; (SEQ ID NO: 160) Ac-[Pen]-N-T-[W(5-Ca)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N- [3Pal]-[Sarc]-NH2; (SEQ ID NO: 161) Ac-[Pen]-N-T-[Trp_4Aza]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N- [3Pal]-[Sarc]-NH2; (SEQ ID NO: 162) Ac-[Pen]-N-T-W-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]- [Sarc]-NH2; (SEQ ID NO: 163) Ac-[Pen]-N-T-W-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-[Lys(Ac)]-N- [3Pal]-[Sarc]-NH2; (SEQ ID NO: 164) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]- [THP]-E-N-[(5Pyal)]-NH2; (SEQ ID NO: 165) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-Me-Lys]- [Lys(Ac)]-N-[(5Pyal)]-NH2; (SEQ ID NO: 166) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]- [THP]-E-N-[(1-Me)His]-NH2; (SEQ ID NO: 167) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[aMeLys]- [Lys(Ac)]-N-[(1-Me)His]-NH2; or (SEQ ID NO: 168) Ac-[Pen]-N-T-[W(7-Me]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-Me-Lys]- [Lys(Ac)]-N-[3Pal]-[(D)NMeTyr]-NH2; and wherein: the monocyclic peptide inhibitor of an interleukin-23 receptor is cyclized via a Pen-Pen disulfide bond; or via an Abu-C thioether bond; or a pharmaceutically acceptable salt thereof.

164. The monocyclic peptide inhibitor of an interleukin-23 receptor of claim 162, wherein the monocyclic peptide is: (SEQ ID NO: 80) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]- [Lys(Ac)]-N-[3Pal]-NH2; (SEQ ID NO: 104) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N- [3Pal]-[Sarc]-NH2; (SEQ ID NO: 108) Ac-[Pen]-N-T-[W(7-Me)]-Q-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]- [Sarc]-NH2; (SEQ ID NO: 110) Ac-[Abu]-Q-T-[W(7-Me)]-Q-[Cys]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]- N-[3Pal]-[Sarc]-NH2; (SEQ ID NO: 112) Ac-[Abu]-Q-T-[W(7-Me)]-[Cit]-[Cys]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]- [Lys(Ac)]-N-[3Pal]-[Sarc]-NH2; (SEQ ID NO: 118) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N- [3Quin]-[Sarc]-NH2; (SEQ ID NO: 124) Ac-[Pen]-S-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-S- [3Pal]-[Sarc]-NH2; or (SEQ ID NO: 125) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-S- [3Pal]-[Sarc]-NH2; wherein: the monocyclic peptide inhibitor of an interleukin-23 receptor is cyclized via a Pen-Pen disulfide bond: or via an Abu-C thioether bond; or a pharmaceutically acceptable salt thereof.

165. The monocyclic peptide inhibitor of an interleukin-23 receptor of claim 164, wherein the monocyclic peptide inhibitor is: (SEQ ID NO: 105) Ac-[Pen]-N-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]- [Lys(Ac)]-N-[3Pal]-[Sarc]-NH2; (SEQ ID NO: 106) Ac-[Pen]-N-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N- [3Pal]-[Sarc]-NH2; (SEQ ID NO: 117) Ac-[Pen]-N-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]- [Lys(Ac)]-N-[3Pal]-[Sarc]-NH2; (SEQ ID NO: 126) Ac-[Pen]-N-T-[W(7-Ph)]-[Cit]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]- [Sarc]-NH2; (SEQ ID NO: 127) Ac-[Pen]-N-T-[W(7-Ph)]-Q-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]- [Sarc]-NH2; (SEQ ID NO: 134) Ac-[Abu]-Q-T-[W(7-Ph)]-Q-[Cys]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]- [Sarc]-NH2; (SEQ ID NO: 135) Ac-[Abu]-Q-T-[W(7-Ph)]-Q-[Cys]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]- N-[3Pal]-[Sarc]-NH2; (SEQ ID NO: 136) Ac-[Pen]-N-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]- [Lys(Ac)]-N-[3Pal]-[Sarc]-NH2; (SEQ ID NO: 137) Ac-[Pen]-N-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aceylaminoethoxy)]-[2-Nal]-[THP]- [Lys(Ac)]-N-[3Pal]-[Sarc]-NH2; or (SEQ ID NO: 139) Ac-[Pen]-E-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]- [Lys(Ac)]-N-[3Pal]-[Sarc]-NH2; and wherein: the monocyclic peptide inhibitor of an interleukin-23 receptor is cyclized via a Pen-Pen disulfide bond; or via an Abu-C thioether bond; or a pharmaceutically acceptable salt thereof.

166. The monocyclic peptide inhibitor of an interleukin-23 receptor of claim 162, wherein the monocyclic peptide inhibitor is: (SEQ ID NO: 201) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Cit]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[aMeLeu]- E-N-[(D)Lys]-[(D)NMeTyr]-NH2; (SEQ ID NO: 202) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Cit]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[aMeLeu]- E-N-[(D)His]-[(D)NMeTyr]-NH2; (SEQ ID NO: 203) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]- [Lys(Ac)]-N-[(D)Orn]-[(D)NMeTyr]-NH2; (SEQ ID NO: 204) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]- [Lys(Ac)]-N-[(D)Ser]-[(D)NMeTyr]-NH2; (SEQ ID NO: 205) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]- [Lys(Ac)]-N-[(D)Phe]-[(D)NMeTyr]-NH2; (SEQ ID NO: 206) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]- [THP]-E-N-H-[(D)Tyr]-NH2; (SEQ ID NO: 207) Ac-[Pen]-N-T-[W(7-Me)]-[(D)Tyr]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]- [Lys(Ac)]-N-[(D)Lys]-[(D)NMeTyr]-NH2; (SEQ ID NO: 208) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]- [THP]-E-N-H-P-NH2; (SEQ ID NO: 209) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]- [THP]-E-N-H-[(D)Pro]-NH2; (SEQ ID NO: 210) Ac-[Pen]-N-T-[W(7-Me)]-[Phe(4-CONH2)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a- MeLys]-[Lys(Ac)]-N-[(D)Lys]-[(D)NMeTyr]-NH2; (SEQ ID NO: 211) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[Acvc]-E-N- (D)Phe[4-NH2]-[Sarc]-NH2; (SEQ ID NO: 212) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]- [THP]-E-N-H-NH2; (SEQ ID NO: 213) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]- [Lys(Ac)]-N-H-N(H)Me; (SEQ ID NO: 214) Ac-[Pen]-N-T-[W(7-Me)]-[Phe(4-NH(Ac))]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a- MeLys]-[Lys(Ac)]-N-[(D)Lys]-[(D)NMeTyr]-NH2; (SEQ ID NO: 215) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]- [Lys(Ac)]-N-[(D)Tyr]-[(D)NMeTyr]-NH2; (SEQ ID NO: 216) Ac-[Pen]-N-T-[W(7-Me)]-[Cit]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[aMeLeu]-[Lys(Ac)]- N-[(D)Lys]-[(D)NMeTyr]-NH2; (SEQ ID NO: 217) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]- [Lys(Ac)]-N-[(D)His]-[(D)NMeTyr]-NH2; (SEQ ID NO: 218) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]- [Lys(Ac)]-N-[bAla]-[(D)NMeTyr]-NH2; (SEQ ID NO: 2l9) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]- [Lys(Ac)]-N-[bAla]-[(D)NMeTyr]-NH2; (SEQ ID NO: 220) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]- [Lys(Ac)]-N-[bAla]-[(D)NMeTyr]-NH2; (SEQ ID NO: 221) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4 -(2-aminoethoxy)]-[2-Nal]-[a- MeLys]-E-N-H-N(H)Me; (SEQ ID NO: 222) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4 -(2-aminoethoxy)]-[2-Nal]- [THP]-E-N-[THP]-P-NH2; (SEQ ID NO: 223) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4 -(2-aminoethoxy)]-[2-Nal]- [THP]-E-N-[THP]-[(D)Pro]-NH2; (SEQ ID NO: 224) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4 -(2-aminoethoxy)]-[2-Nal]- [Acvc]-E-N-[bAla]-[Sarc]-NH2; (SEQ ID NO: 225) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4 -(2-aminoethoxy)]-[2-Nal]- [Acvc]-E-N-[(D)Val]-[Sarc]-NH2; (SEQ ID NO: 226) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4 -(2-aminoethoxy)]-[2-Nal]- [Acvc]-E-N-[(D)Arg]-[Sarc]-NH2; (SEQ ID NO: 227) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4 -(2-aminoethoxy)]-[2-Nal]- [Acvc]-E-N-[Hph]-[Sarc]-NH2; (SEQ ID NO: 228) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[Acvc]-E-N- Phe[4-NH2]-[Sarc]-NH2; (SEQ ID NO: 229) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4 -(2-aminoethoxy)]-[2-Nal]- [Acvc]-E-N-Phe[4-NH2]-[Sarc]-NH2;  (SEQ ID NO: 230) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4 -(2-aminoethoxy)]-[2-Nal]- [Acvc]-E-N-F-[Sarc]-NH2; (SEQ ID NO: 231) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4 -(2-aminoethoxy)]-[2-Nal]- [Acvc]-E-N-[THP]-[Sarc]-NH2; (SEQ ID NO: 232) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4 -(2-aminoethoxy)]-[2-Nal]- [Acvc]-E-N-[(D)Leu]-[Sarc]-NH2; (SEQ ID NO: 233) Ac-[(D)Arg]-[Cys]-N-T-[W(7-Me)]-[Lys(Ac)]-[aMeCys]-Phe[4-(2-aminoethoxy)]-[2-Nal]- [Acvc]-E-N-H-[Sarc]-NH2; (SEQ ID NO: 234) Ac-[(D)Arg]-[Cys]-N-T-[W(7-Me)]-[Lys(Ac)]-[aMeCys]-Phe[4-(2-aminoethoxy)]-[2-Nal]- [Acvc]-E-N-[(D)Leu]-[Sarc]-NH2; (SEQ ID NO: 235) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]- [Acvc]-E-N-[3Pal]-[Sarc]-NH2; (SEQ ID NO: 236) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]- [Lys(Ac)]-N-[bAla]-[Sarc]-NH2; (SEQ ID NO: 237) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]- [Lys(Ac)]-N-[(D)Val]-[Sarc]-NH2; (SEQ ID NO: 238) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]- [Lys(Ac)]-N-[(D)Arg]-[Sarc]-NH2; (SEQ ID NO: 239) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]- [Lys(Ac)]-N-[Hph]-[Sarc]-NH2; (SEQ ID NO: 240) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]- [Lys(Ac)]-N-[(D)Tyr]-[Sarc]-NH2; (SEQ ID NO: 241) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]- [Lys(Ac)]-N-[(D)Tyr]-[Sarc]-NH2; (SEQ ID NO: 242) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]- [THP]-E-N-[4Pal]-NH2; (SEQ ID NO: 243) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]- [Lys(Ac)]-N-[Phe(4-CF3)]-[Sarc]-NH2; (SEQ ID NO: 244) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]- [Lys(Ac)]-N-Tyr_CHF2-[Sarc]-NH2; (SEQ ID NO: 245) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]- [Lys(Ac)]-N-[THP]-P-NH2; (SEQ ID NO: 246) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]- [Lys(Ac)]-N-[3Pal]-[(D)NMeTyr]-NH2; (SEQ ID NO: 247) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]- [THP]-E-N-[3Pal]-[Sarc]-NH2; (SEQ ID NO: 248) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]- [THP]-E-N-[4Pal]-[Sarc]-NH2; (SEQ ID NO: 249) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]- [THP]-E-N-[Phe(2-aminomethyl)]-[Sarc]-NH2; (SEQ ID NO: 250) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]- [THP]-E-N-[3Pal]-[Pro(4,4diF)]-NH2; (SEQ ID NO: 251) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]- [THP]-E-N-[3Pal]-[aMePro]-NH2; (SEQ ID NO: 252) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]- [THP]-E-N-[3Pal]-[Aib]-NH2; (SEQ ID NO: 253) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]- [Lys(Ac)]-N-[His(3-Me)]-[Sarc]-NH2; (SEQ ID NO: 261) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]- [THP]-E-N-[His(3-Me)]-[Sarc]-NH2; (SEQ ID NO: 262) Ac-[(D)Arg]-[Pen]-N-T-W-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N- [His(3-Me)]-[Sarc]-NH2; (SEQ ID NO: 266) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]- [THP]-E-N-[3Pal]-[Sarc]-NH2; (SEQ ID NO: 267) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]- [THP]-E-N-[3Pal]-N(H)Me; (SEQ ID NO: 270) [(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E- N-[3Pal]-[Sarc]-NH2; (SEQ ID NO: 271) Ac-[(D)Arg]-[Pen]-N-T-W-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N- [3Pal]-[Sarc]-NH2;  (SEQ ID NO: 272) Pr-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]- Phe[4-(2-(N-propionylamino)ethoxy)]- [2-Nal]-[THP]-E-N-[3Pal]-[Sarc]-NH2; (SEQ ID NO: 273) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-(N-(4-hydroxy-3- methylphenyl)propionylamino)ethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]-[Sarc]-NH2; (SEQ ID NO: 276) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]- [THP]-E-N-[3Pal(5-Me)]-[Sarc]-NH2; (SEQ ID NO: 277) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]- [THP]-E-N-[3Pal(5-NH2)]-[Sarc]-NH2; (SEQ ID NO: 278) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N- [His(3-Me)]-N(H)Me; (SEQ ID NO: 279) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]- [THP]-E-N-[3Pal]-[(D)NMeTyr]-NH2; (SEQ ID NO: 280) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]- [THP]-E-N-[3Pal]-[Gly(N-cyclohexylmethyl)]-NH2; (SEQ ID NO: 281) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]- [THP]-E-N-[3Pal]-[Gly(N-isobutyl)]-NH2; (SEQ ID NO: 282) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]- [THP]-E-N-[3Pal(3-Me)]-NH2; (SEQ ID NO: 283) Ac-[(D)Arg]-[aMeCys]-N-T-[W(7-Me)]-[Lys(Ac)]-[Cys]-Phe[4-(2-aminoethoxy)]-[2-Nal]- [THP]-E-N-[3Pal]-[Sarc]-NH2; (SEQ ID NO: 284) Ac-[Pen]-N-T-W-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]- [Sarc]-NH2; (SEQ ID NO: 285, 159) Ac-[Pen]-N-T-W-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[Acvc]-E-N-[3Pal]- [Sarc]-NH2; (SEQ ID NO: 286) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-[Phe(4-CONH2)]-[2-Nal]-[THP]-E-N-[3Pal]- [Sarc]-NH2; (SEQ ID NO: 287) Ac-[Pen]-[Gly(Allyl)]-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-[Tyr(O-Allyl)]-[2-Nal]-[THP]- [Lys(Ac)]-N-[3Pal]-[Sarc]-NH2; (SEQ ID NO: 288) Ac-[Pen]-[Gly(Allyl)]-D-[W(7-Me)]-[Lys(Ac)]-[Pen]-[Tyr(O-Allyl)]-[2-Nal]-[THP]- [Lys(Ac)]-N-[3Pal]-[Sarc]-NH2; (SEQ ID NO: 289) Ac-[Pen]-[Gly(Allyl)]-T-(W(4-F)]-[Lys(Ac)]-[Pen]-[Tyr(O-Allyl)]-[2-Nal]-[THP]- [Lys(Ac)]-N-[3Pal]-[Sarc]-NH2; (SEQ ID NO: 290) Ac-[Pen]-N-D-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N- [3Pal]-[Sarc]-NH2; (SEQ ID NO: 291) Ac-[Pen]-L-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N- [3Pal]-[Sarc]-NH2; (SEQ ID NO: 299) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-[Phe(4-CONH2)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]- N-[3Pal]-[Sarc]-NH2; (SEQ ID NO: 308) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-F-[2-Nal]-[THP]-[Lys(Ac)]-N-[3Pal]-[Sarc]-NH2; (SEQ ID NO: 309) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-[(D)Tyr]-[2-Nal]-[THP]-[Lys(Ac)]-N-[3Pal]- [Sarc]-NH2; (SEQ ID NO: 310) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-[Phe(4-OMe)]-[2-Nal]-[THP]-[Lys(Ac)]-N- [3Pal]-[Sarc]-NH2; (SEQ ID NO: 311) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-[Phe(4-CONH2)]-[2-Nal]-[THP]-[Lys(Ac)]-N- [3Pal]-[Sarc]-NH2; (SEQ ID NO: 332) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(N-acetyl-N-propyl)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]- [THP]-E-N-[3Pal]-[Sarc]-NH2; (SEQ ID NO: 333) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(N-acetyl-N-butyl)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]- [THP]-E-N-[3Pal]-[Sarc]-NH2; (SEQ ID NO: 334) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(N-acetyl-N-isobutyl)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2- Nal]-[THP]E-N-[3Pal]-[Sarc]-NH2; (SEQ ID NO: 335) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(N-acetyl-N-benzyl)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]- [THP]-E-N-[3Pal]-[Sarc]-NH2; (SEQ ID NO: 339) Ac-[Pen]-L-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-[Phe(4-CONH2)]-[2-Nal]-[aMeLeu]-E-N-[3Pal]- [Sarc]-NH2; (SEQ ID NO: 347) Ac-[Pen]-L-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-[Phe(4-OMe)]-[2-Nal]-[aMeLeu]-E-N-[3Pal]- [Sarc]-NH2; or (SEQ ID NO: 373) Ac-[Abu]N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N- [3Pal]-[Sarc]-NH2; wherein; the monocyclic peptide inhibitor of an interleukin-23 receptor is cyclized via a Pen-Pen disulfide bond; or via an Abu-C thioether bond; or a pharmaceutically acceptable salt thereof.

167. The monocyclic peptide inhibitor of an interleukin-23 receptor of claim 164, wherein the monocyclic peptide inhibitor is: (SEQ ID NO: 104) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N- [3Pal]-[Sarc]-NH2; (SEQ ID NO: 106) Ac-[Pen]-N-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N- [3Pal]-[Sarc]-NH2; (SEQ ID NOs: 158, 162, 284) Ac-[Pen]-N-T-W-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]- [Sarc]-NH2; (SEQ ID NOs: 247, 266) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]- [THP]-E-N-[3Pal]-[Sarc]-NH2; (SEQ ID NO: 261) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]- [THP]-E-N-[His(3-Me)]-[Sarc]-NH2; or (SEQ ID NO: 267) Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]- [THP]-E-N-[3Pal]-N(H)Me; wherein: the monocyclic peptide inhibitor of an interleukin-23 receptor is cyclized via a Pen-Pen disulfide bond; or a pharmaceutically acceptable salt thereof.

168. The monocyclic peptide inhibitor of an interleukin-23 receptor of claim 167, wherein the monocyclic peptide inhibitor is: Ac-[Pen]-N-T-[W (7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-N al]-[THP]-E-N-[3Pal]-[Sarc]-NH2 (SEQ ID NO:104) having this structure: wherein: the monocyclic peptide inhibitor of an interleukin-23 receptor is cyclized via a Pen-Pen disulfide bond; or a pharmaceutically acceptable salt thereof.

169. The monocyclic peptide inhibitor of an interleukin-23 receptor of claim 167, wherein the monocyclic peptide inhibitor is: Ac-[Pen]-N-T-[W(7-Ph)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3 Pal]-[Sarc]-NH2 (SEQ ID NO:106) having this structure: wherein: the monocyclic peptide inhibitor of an interleukin-23 receptor is cyclized via a Pen-Pen disulfide bond, or a pharmaceutically acceptable salt thereof.

170. The monocyclic peptide inhibitor of an interleukin-23 receptor of claim 167, wherein the monocyclic peptide inhibitor is: Ac-[Pen]-N-T-W-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3 Pal]-[Sarc]-NH2 (SEQ ID NOs:158, 162, 284) having this structure: wherein: the monocyclic peptide inhibitor of an interleukin-23 receptor is cyclized via a Pen-Pen disulfide bond; or a pharmaceutically acceptable salt thereof.

171. The monocyclic peptide inhibitor of an interleukin-23 receptor of claim 167, wherein the monocyclic peptide inhibitor is Ac-[(D) Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]-[Sarc]-NH2 SEQ ID NOs:247, 266), wherein; the monocyclic peptide inhibitor of an interleukin-23 receptor is cyclized via a Pen-Pen disulfide bond; or pharmaceutically acceptable salt thereof.

172. The monocyclic peptide inhibitor of an interleukin-23 receptor of claim 167, wherein the monocyclic peptide inhibitor is: Ac-[(D) Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[His(3-Me)]-[Sarc]-NH2 (SEQ ID NO:261) having this structure: wherein: the monocyclic peptide inhibitor of an interleukin-23 receptor is cyclized via a Pen-Pen disulfide bond; or a pharmaceutically acceptable salt thereof.

173. The monocyclic peptide inhibitor of an interleukin-23 receptor of claim 167, wherein the monocyclic peptide is: Ac-[(D) Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]-N(H)Me (SEQ ID NO:267); wherein: the monocyclic peptide inhibitor of an interleukin-23 receptor is cyclized via a Pen-Pen disulfide bond; or a pharmaceutically acceptable salt thereof.

174. A polynucleotide comprising a sequence encoding the monocyclic peptide inhibitor of an interleukin-23 receptor of claim 1 or a pharmaceutically acceptable salt thereof.

175. A vector comprising the polynucleotide of claim 174.

176. A pharmaceutical composition comprising the monocyclic peptide inhibitor of an interleukin-23 receptor or pharmaceutically acceptable salt thereof of claim 1, and a pharmaceutically acceptable carrier, excipient, or diluent. 177.-178. (canceled)

179. A method for treating an Inflammatory Bowel Disease (IBD), ulcerative colitis, Crohn's disease, Celiac disease (nontropical Sprue), enteropathy associated with seronegative arthropathies, microscopic colitis, collagenous colitis, eosinophilic gastroenteritis, colitis associated with radio- or chemo-therapy, colitis associated with disorders of innate immunity as in leukocyte adhesion deficiency-1, chronic granulomatous disease, glycogen storage disease type 1b, Hermansky-Pudlak Syndrome, Chediak-Higashi Syndrome, and Wiskott-Aldrich Syndrome, pouchitis resulting after proctocolectomy and ileoanal anastomosis, gastrointestinal cancer, pancreatitis, insulin-dependent diabetes mellitus, mastitis, cholecystitis, cholangitis, pericholangitis, chronic bronchitis, chronic sinusitis, asthma, psoriasis, psoriatic arthritis, or graft versus host disease in a subject, comprising administering an effective amount of the monocyclic peptide inhibitor according to claim 1 or pharmaceutically acceptable salt thereof to a subject or patient in need thereof.

180. The method of claim 179, wherein the pharmaceutical composition is administered to the subject or patient in need thereof by an oral, parenteral, intravenous, peritoneal, intradermal, subcutaneous, intramuscular, intrathecal, inhalation, vaporization, nebulization, sublingual, buccal, parenteral, rectal, intraocular, inhalation, topically, vaginal, or topical route of administration.

181. A method for treating Inflammatory Bowel Disease (IBD), ulcerative colitis, Crohn's Disease (CD), psoriasis or psoriatic arthritis, which comprises administering an effective amount of: the monocyclic peptide inhibitor of an interleukin-23 receptor of claim 1 or pharmaceutically acceptable salt thereof; to a subject or patient in need thereof.

182. The method of claim 179 for treating psoriasis, wherein the pharmaceutical composition is adminstered to the subject orally, topically, parenterally, intravenously, subcutaneously, peritoneally, or intravenously. 183.-186. (canceled)
```

---

#### 2.3 US11845808B2 ☑️부분교차검증 (차이 4개)

> **💡 핵심 요약** &nbsp;|&nbsp; **유형:** compound·물질(peptide), use·치료방법
> 
> **무엇을 청구하나:** icotrokinra(SEQ ID NO:1)를 포함하는 좁은 단환 펩타이드 화학식(Formula I: X3-Pen-N-T-X7-Lys(Ac)-Pen-X10-2Nal-X12-E-N-X15-Sarc, X15=3Pal)과 개별 SEQ(104/158/247) 화합물 자체를 청구하고, 이를 이용한 IBD·UC·CD·PsO·PsA 경구 치료방법까지 청구
> 
> **핵심 권리범위:** X10=Phe[4-(2-aminoethoxy)], X12=THP, X15=3Pal 고정; Pen-Pen 디설파이드 고리화; X7=Trp/W(7-Me)/W(7-Ph); 경구·설하·국소 등 투여경로 및 plaque psoriasis 한정
> 
> **독립항:** 1, 5 &nbsp;|&nbsp; **적응증:** IBD/UC/CD/건선(plaque PsO 포함)/건선성관절염 &nbsp;|&nbsp; **검증:** ☑️부분교차검증(차이4) &nbsp;|&nbsp; **추정만료:** 2041-01-14


| 항목 | 내용 |
|---|---|
| 특허번호 | US11845808B2 (등록, B2) |
| 제목 | Peptide inhibitors of interleukin-23 receptor and their use to treat inflammatory diseases |
| 출원번호 / 출원일 | 17/149,509 / 2021-01-14 |
| 우선일 | 2020-01-15 (US Provisional 62/961,624) |
| 등록일 | 2023-12-19 |
| 출원인/양수인 | Janssen Biotech, Inc.; Protagonist Therapeutics, Inc. |
| 패밀리 | US20210261622A1 (동일 출원 공개본), WO2021146441A1 (PCT) |
| 권위 만료일 | **2041-01-14** (GP anticipated expiration; 출원일+20년, PTE 미반영) |
| 교차검증 | GP=30, FPO=30, both=30, agree=26, **substantive_diff=4** → ☑️부분교차검증 |

**[ANALYSIS] (한국어)**

출원 17/149,509의 **등록본**. 청구항 1은 Formula (I) **단환(monocyclic) 펩타이드**를 명시적으로 한정(X3-Pen-N-T-X7-Lys(Ac)-Pen-X10-2Nal-X12-E-N-X15-Sarc)하고, X7=Trp/W(7-Me)/W(7-Ph), X10=Phe(4-(2-aminoethoxy)), X12=THP, X15=3Pal로 좁힌다 — icotrokinra 화학형(monocyclic, Pen-Pen 이황화 가교)과 직접 부합한다. 청구항 5는 SEQ ID NO:104/158/247 서열군을, 청구항 12 이하는 IL-23/IL-23R 관련 질환(IBD/UC/CD/PsO/PsA) 치료방법 및 경구 등 투여경로를 청구한다. GP↔FPO 30개 중 26개 일치, 4개 차이로 ☑️부분교차검증이며 권위 소스는 GP.

**[VERBATIM] — 출처: Google Patents (`work/05_gp_authoritative/US11845808B2.md`)**

```text
1. A monocyclic peptide, comprising the amino acid sequence of Formula (I): X3-Pen-N-T-X7-Lys(Ac)-Pen-X10-2Nal-X12-E-N—X15-Sarc  (I) wherein: X3 is absent or any amino acid; X7 is Trp, 7-methyl tryptophan (W(7-Me)), or 7 phenyl tryptophan (W(7-Ph)); X10 is Phe(4-(2-aminoethoxy)); X12 is 4-amino-4-carboxy-tetrahydropyran (THP); and X15 is 3-pyridyl substituted alanine (3Pal); or a pharmaceutically acceptable salt thereof; wherein the monocyclic peptide is cyclized via a Pen-Pen disulfide bond.

2. The monocyclic peptide of claim 1, comprising the amino acid sequence of Formula (Z′): R1-X3-Pen-N-T-X7-Lys(Ac)-Pen-X10-2Nal-X12-E-N-3Pal-Sarc-R2  (Z′) wherein: R1 is hydrogen or Ac; X3 is absent or (D)Arg; X7 is Trp, W(7-Ph), or W(7-Me); X10 is Phe(4-(2-aminoethoxy)); X12 is THP; and R2 is NH2; or a pharmaceutically acceptable salt thereof.

3. The monocyclic peptide of claim 2, wherein R1 is Ac; or a pharmaceutically acceptable salt thereof.

4. The monocyclic peptide of claim 2, wherein: R1 is Ac; X3 is absent; and X7 is W(7-Ph); or a pharmaceutically acceptable salt thereof.

5. A monocyclic peptide comprising the amino acid sequence selected from the group consisting of: Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-[Phe(4-(2-aminoethoxy))]-[2-Nal]-[THP]-E-N-[3Pal]-[Sarc]-NH2 (SEQ ID NO:104); Ac-[Pen]-N-T-W-[Lys(Ac)]-[Pen]-[Phe(4-(2-aminoethoxy))]-[2-Nal]-[THP]-E-N-[3Pal]-[Sarc]-NH2 (SEQ ID NO:158); and Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]-[Sarc]-NH2 (SEQ ID NO:247); or a pharmaceutically acceptable salt thereof; wherein the monocyclic peptide is cyclized via a Pen-Pen disulfide bond.

6. The monocyclic peptide of claim 5, wherein the monocyclic peptide has the structure: a pharmaceutically acceptable salt thereof.

7. The monocyclic peptide of claim 5, wherein the monocyclic peptide has the structure: a pharmaceutically acceptable salt thereof.

8. The monocyclic peptide of claim 5, wherein the peptide comprises the amino acid sequence of: Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-[Phe(4-(2-aminoethoxy))]-[2-Nal]-[THP]-E-N-[3Pal]-[Sarc]-NH2 (SEQ ID NO:247), and wherein the monocyclic peptide is cyclized via a Pen-Pen disulfide bond; or a pharmaceutically acceptable salt thereof.

9. The monocyclic peptide of claim 5, wherein the monocyclic peptide has the structure:

10. The monocyclic peptide of claim 5, wherein the monocyclic peptide has the structure:

11. The monocyclic peptide of claim 5, wherein the peptide comprises the amino acid sequence of: Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-[Phe(4-(2-aminoethoxy))]-[2-Nal]-[THP]-E-N-[3Pal]-[Sarc]-NH2 (SEQ ID NO:247), and wherein the monocyclic peptide is cyclized via a Pen-Pen disulfide bond.

12. A method for treating a disease or disorder associated with Interleukin 23 (IL-23) or Interleukin 23 Receptor (IL-23R) in a patient in need thereof, comprising administering to the patient an effective amount of the monocyclic peptide or pharmaceutically acceptable salt thereof of claim 5, wherein the disease or disorder is inflammatory bowel disease (IBD), ulcerative colitis (UC), Crohn's disease (CD), psoriasis (PsO), or psoriatic arthritis (PsA).

13. The method of claim 12, wherein the disease or disorder is psoriasis (PsO).

14. The method of claim 12, wherein the disease or disorder is psoriatic arthritis (PsA).

15. The method of claim 12, wherein the disease or disorder is inflammatory bowel disease (IBD).

16. The method of claim 12, wherein the monocyclic peptide or the pharmaceutically acceptable salt thereof is administered to the patient in need thereof via an oral, parenteral, intravenous, peritoneal, intradermal, subcutaneous, intramuscular, intrathecal, inhalation, vaporization, nebulization, sublingual, buccal, parenteral, rectal, intraocular, inhalation, topically, vaginal, or topical, route of administration.

17. The method of claim 16, wherein the monocyclic peptide or pharmaceutically acceptable salt thereof is administered to the patient in need thereof via an oral, sublingual, buccal, or topical route of administration.

18. The method of claim 13, wherein the psoriasis (PsO) is plaque psoriasis.

19. A method for treating a disease or disorder associated with Interleukin 23 (IL-23) or Interleukin 23 Receptor (IL-23R) in a patient in need thereof, comprising administering to the patient an effective amount of the monocyclic peptide or pharmaceutically acceptable salt thereof of claim 6, wherein the disease or disorder is inflammatory bowel disease (IBD), ulcerative colitis (UC), Crohn's disease (CD), psoriasis (PsO), or psoriatic arthritis (PsA).

20. The method of claim 19, wherein the disease or disorder is psoriasis (PsO).

21. The method of claim 19, wherein the disease or disorder is psoriatic arthritis (PsA).

22. The method of claim 19, wherein the disease or disorder is inflammatory bowel disease (IBD).

23. The method of claim 19, wherein the monocyclic peptide or the pharmaceutically acceptable salt is administered to the patient in need thereof via an oral, parenteral, intravenous, peritoneal, intradermal, subcutaneous, intramuscular, intrathecal, inhalation, vaporization, nebulization, sublingual, buccal, parenteral, rectal, intraocular, inhalation, topically, vaginal, or topical, route of administration.

24. The method of claim 23, wherein the monocyclic peptide or pharmaceutically acceptable salt thereof is administered to the patient in need thereof via an oral, sublingual, buccal, or topical route of administration.

25. The method of claim 19, wherein the disease or disorder is Ulcerative colitis (UC).

26. The method of claim 19, wherein the disease or disorder is Crohn's Disease (CD).

27. A method for treating a disease or disorder associated with Interleukin 23 (IL-23) or Interleukin 23 Receptor (IL-23R) in a patient in need thereof, comprising administering to the patient an effective amount of the monocyclic peptide or pharmaceutically acceptable salt thereof of claim 7, wherein the disease or disorder is inflammatory bowel disease (IBD), ulcerative colitis (UC), Crohn's disease (CD), psoriasis (PsO), or psoriatic arthritis (PsA).

28. A method for treating a disease or disorder associated with Interleukin 23 (IL-23) or Interleukin 23 Receptor (IL-23R) in a patient in need thereof, comprising administering to the patient an effective amount of the monocyclic peptide or pharmaceutically acceptable salt thereof of claim 8, wherein the disease or disorder is inflammatory bowel disease (IBD), ulcerative colitis (UC), Crohn's disease (CD), psoriasis (PsO), or psoriatic arthritis (PsA).

29. The method of claim 19, wherein the monocyclic peptide or the pharmaceutically acceptable salt thereof is administered to the patient in need thereof via an oral route of administration.

30. The method of claim 20, wherein the psoriasis (PsO) is plaque psoriasis.
```

---

#### 2.4 US12018057B2 ✅교차검증 (10/10 완전일치)

> **💡 핵심 요약** &nbsp;|&nbsp; **유형:** compound·물질(peptide), composition(조성물), use·치료방법
> 
> **무엇을 청구하나:** Pen-Pen 디설파이드 고리화된 특정 IL-23R 펩타이드 화합물군(SEQ ID NO:3~137에서 열거된 개별 서열)을 청구하고, 그 의약조성물 및 IBD·UC·CD·건선·PsA 등 치료방법을 청구
> 
> **핵심 권리범위:** 열거된 개별 SEQ(예: SEQ ID NO:105 Ac-[(D)Arg]-[Pen]-N-T-W-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[THP]-NH2) 한정; Pen-Pen 디설파이드 고리화; N-말단 캡(Ac/Propionic acid/Pentanoic acid 등) 및 C-말단 변형(THP/alpha-MePhe 등); 약학적으로 허용되는 염 포함
> 
> **독립항:** 1 &nbsp;|&nbsp; **적응증:** IBD/UC/CD/건선/건선성관절염 등 다수 염증질환 &nbsp;|&nbsp; **검증:** ✅교차검증 &nbsp;|&nbsp; **추정만료:** 2041-01-14


| 항목 | 내용 |
|---|---|
| 특허번호 | US12018057B2 (등록, B2) |
| 제목 | Peptide inhibitors of interleukin-23 receptor and their use to treat inflammatory diseases |
| 출원번호 / 출원일 | 17/149,544 / 2021-01-14 |
| 우선일 | 2020-01-15 (US Provisional 62/961,618) |
| 등록일 | 2024-06-25 |
| 출원인/양수인 | Janssen Biotech, Inc.; Protagonist Therapeutics, Inc. |
| 패밀리 | US20210261622A1 / US11845808B2 (자매 출원 17/149,509), WO2021146441A1 |
| 권위 만료일 | **2041-01-14** (GP anticipated expiration; 출원일+20년, PTE 미반영) |
| 교차검증 | GP=10, FPO=10, both=10, agree=10, **substantive_diff=0** → ✅완전일치 |

**[ANALYSIS] (한국어)**

자매 출원(17/149,544)의 등록본으로, **GP↔FPO 10/10 완전일치** ✅교차검증을 통과했다. 청구항 1은 다수 SEQ ID NO(3~137)의 구체 서열들을 'or'로 나열한 종(species) 군 청구항이며, Pen-Pen 이황화 가교로 환화된다. 청구항 2는 SEQ ID NO:105 단일 종, 청구항 3~4는 조성물, 청구항 5~10은 IBD/UC/CD/PsO/PsA 치료방법이다. 완전일치 + 구체 서열 청구라는 점에서 권리 신뢰도가 높은 종 특허다.

**[VERBATIM] — 출처: Google Patents (`work/05_gp_authoritative/US12018057B2.md`)**

```text
1. A peptide that is: (SEQ ID NO: 3) [Propionic_acid]-[(D)Arg]-[Pen]-Q-T-W-Q-[Pen]- Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N- [alpha-MePhe]-NH2; (SEQ ID NO: 4) [Propionic_acid]-[(D)Arg]-[Pen]-Q-T-W-Q-[Pen]- [Phe(4-OMe)]-[2-Nal]-[THP]-E-N-[THP]-NH2; (SEQ ID NO: 5) [3,3,3-Trifluoropropionic acid]-[(D)Arg]-[Pen]- Q-T-W-Q-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]- [THP]-E-N-[THP]-NH2; SEQ ID NO: 6) [Propionic_acid]-[(D)Arg]-[Pen]-Q-T-W-Q-[Pen]- Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]- [Lys(COCF3)]-N-[THP]-NH2; (SEQ ID NO: 7) [Propionic_acid]-[(D)Arg]-[Pen]-Q-T-W-Q-[Pen]- Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]- [Lys(COtBu)]-N-[THP]-NH2; (SEQ ID NO: 8) [Propionic_acid]-[(D)Arg]-[Pen]-Q-T-W-Q-[Pen]- Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N- [N-Me-beta-Ala]-NH2; (SEQ ID NO: 9) [Pentanoic acid]-[(D)Arg]-[Pen]-Q-T-W-Q-[Pen]- Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N- [THP]-NH2; (SEQ ID NO: 10) [Propionic_acid]-[(D)Arg]-[Pen]-Q-T-W-Q-[Pen]- Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N- [THP]-NH2; (SEQ ID NO: 13) Ac-[(D)Arg]-[Pen]-Q-T-W-Q-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-E-N-[THP]-NH2; (SEQ ID NO: 14) Ac-[(D)Arg]-[Pen]-Q-T-W-Q-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-E-N-[N-Me-beta- Ala]-NH2; (SEQ ID NO: 15) pr-[(D)Arg]-[Pen]-Q-T-W-Q-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-Q-N-[THP]-NH2; (SEQ ID NO: 18) [(D)Arg]-[Pen]-Q-T-W-Q-[Pen]-[Phe(4-OMe)]- [2-Nal]-[THP]-E-N-[THP]-NH2; (SEQ ID NO: 26) pr-[(D)Arg]-[Pen]-Q-T-W-Q-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-[Lys(COtBu)]- N-F-NH2; (SEQ ID NO: 33) pr-[(D)Arg]-[Pen]-Q-T-W-Q-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-[Lys(CO2Allyl)]- N-F-NH2; (SEQ ID NO: 51) Ac-[(D)Arg]-[Pen]-Q-T-W-Q-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-[Lys(COcPr)]- N-[THP]-NH2; (SEQ ID NO: 52) Ac-[(D)Arg]-[Pen]-Q-T-W-Q-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-[Lys(COPr)]- N-[THP]-NH2; (SEQ ID NO: 53) Ac-[(D)Arg]-[Pen]-Q-T-W-Q-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-[Lys(Ac)]-N-F-NH2; (SEQ ID NO: 54) Ac-[(D)Arg]-[Pen]-Q-T-W-Q-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-[Lys(COEt)]- N-F-NH2; (SEQ ID NO: 55) Ac-[(D)Arg]-[Pen]-Q-T-W-Q-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-[Lys(COcPr)]- N-F-NH2; (SEQ ID NO: 56) Ac-[(D)Arg]-[Pen]-Q-T-W-Q-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-[Lys(Ac)]- N-[THP]-NH2; (SEQ ID NO: 57) Ac-[(D)Arg]-[Pen]-Q-T-W-Q-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-[Lys(COEt)]- N-[THP]-NH2; (SEQ ID NO: 58) Ac-[(D)Arg]-[Pen]-Q-T-W-Q-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-[Lys(COPr)]- N-F-NH2; (SEQ ID NO 59) Ac-[(D)Arg]-[Pen]-Q-T-W-Q-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-[Lys(COPent)]- N-F-NH2; (SEQ ID NO: 60) Ac-[(D)Arg]-[Pen]-Q-T-W-Q-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-[Lys(COCF3)- N-F-NH2; (SEQ ID NO: 61) Ac-[(D)Arg]-[Pen]-Q-T-W-Q-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-[Lys(COiPr)]- N-F-NH2; (SEQ ID NO: 105) Ac-[(D)Arg]-[Pen]-N-T-W-[Lys(Ac)]-[Pen]- Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E- N-[THP]-NH2; (SEQ ID NO: 106) Ac-[(D)Arg]-[Pen]-N-T-W-[Lys(Ac)]-[Pen]- Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E- N-[alpha-MePhe]-NH2; (SEQ ID NO: 125) Ac-[(D)Arg]-[Pen]-Q-T-W-Q-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-E-N-[(N- Ph)Asn]-NH2; (SEQ ID NO: 126) Ac-[(D)Arg]-[Pen]-Q-T-W-Q-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-E-N-[(N-(2- aminophenyl))Asn]-NH2; (SEQ ID NO: 127) Ac-[(D)Arg]-[Pen]-Q-T-W-Q-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-E-N-[(N- Pip)Asn]-NH2; (SEQ ID NO: 128) Ac-[(D)Arg]-[Pen]-Q-T-W-Q-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-E-N-[(N- Pyr)Asn]-NH2; (SEQ ID NO: 129) Ac-[(D)Arg]-[Pen]-Q-T-W-Q-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-E-N-[(N-(4- aminophenyl))Asn]-NH2; (SEQ ID NO: 130) Ac-[(D)Arg]-[Pen]-Q-T-W-Q-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-E-N-[(N-(3- aminophenyl))Asn]-NH2; (SEQ ID NO: 131) Ac-[(D)Arg]-[Pen]-Q-T-W-Q-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-E-N-[(N-(4- Pyz))Asn]-NH2; (SEQ ID NO: 132) Ac-[(D)Arg]-[Pen]-Q-T-W-Q-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-E-N-[(N-(5- indolyl)Asn]-NH2; (SEQ ID NO: 133) Ac-[(D)Arg]-[Pen]-Q-T-W-Q-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-E-N-[(N-(3- Pyz))Asn]-NH2; (SEQ ID NO: 134) pr-[(D)Arg]-[Pen]-Q-T-W-Q-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-THP]-E-N-[THP]-NH2; (SEQ ID NO: 135) pr-[(D)Arg]-[Pen]-Q-T-W-Q-[Pen]-Phe[(alpha- Me)-4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N- [THP]-NH2; (SEQ ID NO: 136) Ac-[(D)Arg]-[Pen]-Q-T-W-Q-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-E-N-[(N- propylamido)Asn]-NH2; or (SEQ ID NO: 137) Ac-[(D)Arg]-[Pen]-Q-T-W-Q-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[THP]-E-N-[(N- (imidazol-2-yl)methyl)Asn]-NH2; wherein the peptide is cyclized via a Pen-Pen disulfide bond; or a pharmaceutically acceptable salt thereof.

2. The peptide of claim 1, wherein said peptide is Ac-[(D)Arg]-[Pen]-N-T-W-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[THP]—NH2 (SEQ ID NO:105) or a pharmaceutically acceptable salt thereof.

3. A pharmaceutical composition comprising the peptide or a pharmaceutically acceptable salt thereof of claim 1 and a pharmaceutically acceptable carrier, excipient, or diluent.

4. The pharmaceutical composition of claim 3, wherein said peptide is Ac-[(D)Arg]-[Pen]-N-T-W-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[THP]—NH2 (SEQ ID NO:105) or a pharmaceutically acceptable salt thereof.

5. A method for treating an Inflammatory Bowel Disease (IBD), ulcerative colitis, Crohn's disease, Celiac disease (nontropical Sprue), enteropathy associated with seronegative arthropathies, microscopic colitis, collagenous colitis, eosinophilic gastroenteritis, colitis associated with radio- or chemo-therapy, colitis associated with disorders of innate immunity as in leukocyte adhesion deficiency-1, chronic granulomatous disease, glycogen storage disease type 1b, Hermansky-Pudlak syndrome, Chediak-Higashi syndrome, and Wiskott-Aldrich Syndrome, pouchitis resulting after proctocolectomy and ileoanal anastomosis, gastrointestinal cancer, pancreatitis, insulin-dependent diabetes mellitus, mastitis, cholecystitis, cholangitis, pericholangitis, chronic bronchitis, chronic sinusitis, asthma, psoriasis, psoriatic arthritis, or graft versus host disease in a subject in need thereof, comprising administering an effective amount of the peptide or a pharmaceutically acceptable salt thereof of claim 1 to the subject.

6. The method of claim 5, wherein the method is for treating an Inflammatory Bowel Disease (IBD).

7. The method of claim 5, wherein the method is for treating ulcerative colitis.

8. The method of claim 5, wherein the method is for treating Crohn's disease.

9. The method of claim 5, wherein the method is for treating psoriasis.

10. The method of claim 5, wherein the method is for treating psoriatic arthritis.
```

---

#### 2.5 US12552836B2 ✅교차검증 (21/21 완전일치)

> **💡 핵심 요약** &nbsp;|&nbsp; **유형:** compound·물질(peptide), composition(조성물)
> 
> **무엇을 청구하나:** 8잔기 코어 Formula (II)(Pen-X5-T-W(alkyl)-X8-Pen-Phe(아미노에톡시)-Nal)로 정의되는 단환 IL-23R 펩타이드 저해제 자체와 그 의약조성물(장용코팅 포함)을 청구
> 
> **핵심 권리범위:** X7=alkyl 치환 Trp(W(7-Me)/W(7-Et)/W(7-n-Pr) 등), X4=X9=Pen 고리화; X10=Phe[4-(2-aminoethoxy)], X11=2-Nal/1-Nal; 지질·중합체 콘주게이트(Palm, PEG, isoGlu-Palm 등) 선택적 포함; 장용코팅(enteric coating) 제형 한정
> 
> **독립항:** 1 &nbsp;|&nbsp; **적응증:** — &nbsp;|&nbsp; **검증:** ✅교차검증 &nbsp;|&nbsp; **추정만료:** 2039-07-12


| 항목 | 내용 |
|---|---|
| 특허번호 | US12552836B2 (등록, B2) |
| 제목 | Peptide inhibitors of interleukin-23 receptor and their use to treat inflammatory diseases |
| 출원번호 / 출원일 | 17/549,579 / 2021-12-13 (US App 16/510,118의 계속출원) |
| 우선일 | 2018-07-12 (US Provisional 62/697,218); 추가 62/872,477 (2019-07-10) |
| 등록일 | 2026-02-17 |
| 출원인/양수인 | Protagonist Therapeutics, Inc. |
| 권위 만료일 | **2039-07-12** (GP anticipated expiration; 출원일+20년, PTE 미반영) |
| 교차검증 | GP=21, FPO=21, both=21, agree=21, **substantive_diff=0** → ✅완전일치 |

**[ANALYSIS] (한국어)**

**GP↔FPO 21/21 완전일치** ✅교차검증. 청구항 1은 Formula (II) 단환 펩타이드(X4=Pen, X5=Asn/Gln, X6=Thr, X7=알킬치환 Trp, X8=Gln/αMeLys류, X9=Pen, X10=2-아미노에톡시 치환 Phe, X11=2-Nal/1-Nal; X4-X9 환화)를 정의하며, IL-23↔IL-23R 결합 저해를 기능 한정한다. 종속항은 구체 서열(SEQ ID NO:6, 242~285 등), 지질/PEG 콘쥬게이트, 장용코팅(enteric coating, 청구항 21) 등으로 확장된다. 우선일 2018-07-12로 본 패밀리 내에서 비교적 이른 우선권을 갖는다.

**[VERBATIM] — 출처: Google Patents (`work/05_gp_authoritative/US12552836B2.md`)**

```text
1. A peptide inhibitor or pharmaceutically acceptable salt or solvate thereof, wherein the peptide inhibitor comprises the amino acid sequence of Formula (II): X4-X5-X6-X7-X8-X9-X10-X11  (II) wherein X4 is Pen; X5 is Asn, or Gln; X6 is Thr; X7 is Trp substituted with alkyl; X8 is Gln, alpha-Me-Lys, alpha-MeLys(Ac), or Lys(Ac); X9 is Pen; X10 is Phe substituted with 2-aminoethoxy, or 2-acetylaminoethoxy; and X11 is 2-Nal, or 1-Nal; wherein the peptide inhibitor is cyclized via a bond between X4 and X9, and wherein the peptide inhibitor inhibits the binding of an interleukin-23 (IL-23) to an IL-23 receptor.

2. The peptide inhibitor or pharmaceutically acceptable salt or solvate thereof of claim 1, wherein X5 is Asn.

3. The peptide inhibitor or pharmaceutically acceptable salt or solvate thereof of claim 1, wherein X8 is Gln or Lys(Ac).

4. The peptide inhibitor or pharmaceutically acceptable salt or solvate thereof of claim 1, wherein X8 is alpha-Me-Lys, or alpha-MeLys(Ac).

5. The peptide inhibitor or pharmaceutically acceptable salt or solvate thereof of claim 1, wherein X10 is Phe[4-(2-aminoethoxy)].

6. The peptide inhibitor or pharmaceutically acceptable salt or solvate thereof of claim 1, wherein X7 is Trp substituted with methyl, ethyl, n-propyl, or isopropyl.

7. The peptide inhibitor or pharmaceutically acceptable salt or solvate thereof of claim 1, wherein X11 is 2-Nal.

8. The peptide inhibitor or pharmaceutically acceptable salt or solvate thereof of claim 1, wherein the peptide inhibitor comprises the structure of Formula (Z): R1—X—R2  (Z) or a pharmaceutically acceptable salt or solvate thereof, wherein R1 is a bond, hydrogen, Ac, a C1-C6 alkyl, a C6-C12 aryl, a C6-C12aryl-C1-6alkyl, a C1-C20 alkanoyl, and including PEGylated versions alone or as spacers of any of the foregoing; X is the amino acid sequence of Formula (II) and R2 is OH or NH2.

9. The peptide inhibitor or pharmaceutically acceptable salt or solvate thereof of claim 1, further comprising a conjugated chemical substituent selected from a lipophilic substituent or a polymeric moiety.

10. The peptide inhibitor or pharmaceutically acceptable salt or solvate thereof of claim 9, wherein the conjugated chemical substituent is Ac, Palm, gamaGlu-Palm, isoGlu-Palm, PEG with a molecular weight of 400 Da to 40,000 Da, PEG2-Ac, PEG4-isoGlu-Palm, (PEG)5-Palm, succinic acid, glutaric acid, pyroglutaric acid, benzoic acid, IVA, octanoic acid, 1,4 diaminobutane, isobutyl, or biotin.

11. The peptide inhibitor of claim 1, wherein the peptide inhibitor is selected from the group consisting of: (SEQ ID NO: 242) Ac-[Pen]-NT-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[α-MeLys]-[Lys(Ac)]-N- [BA]-NH2; (SEQ ID NO: 245) Ac-[Pen]-NT-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[α-MeLys]-[Lys(Ac)]-N- [(D)Leu]-NH2; (SEQ ID NO: 248) Ac-[Pen]-NT-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[α-MeLys]-[Lys(Ac)]-N-H- NH2; (SEQ ID NO: 249) Ac-[Pen]-NT-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[α-MeLys]-[Lys(Ac)]-N- [Cit]-NH2; (SEQ ID NO: 251) Ac-[Pen]-NT-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[α-MeLys]-[Lys(Ac)]-N- [(D)Val]-NH2; (SEQ ID NO: 252) Ac-[Pen]-NT-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[α-MeLys]-[Lys(Ac)]-N- [(D)Lys]-NH2; (SEQ ID NO: 258) Ac-[Pen]-NT-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[α-MeLys]-[Lys(Ac)]-N- [(D)Phe]-NH2; (SEQ ID NO: 284) Ac-[Pen]-N-T-[W(7-Et)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[α-MeLys]-[Lys(Ac)]-N- [(D)Leu]-NH2; and (SEQ ID NO: 285) Ac-[Pen]-N-T-[W(7-n-Pr)]-[Lys(Ac)]-[Pen]-Phe[4- (2-aminoethoxy)]-[2-Nal]-[[α-MeLys]-[Lys(Ac)]-N- [(D)Leu]-NH2; or a pharmaceutically acceptable salt or solvate thereof; wherein the peptide inhibitor is cyclized via a Pen-Pen disulfide bond.

12. The peptide inhibitor or pharmaceutically acceptable salt or solvate thereof of claim 1, wherein the bond between X4 and X9 is a disulfide bond.

13. The peptide inhibitor or pharmaceutically acceptable salt or solvate thereof of claim 1, wherein X7 is Trp substituted with alkyl at 4-, 6-, or 7-position.

14. The peptide inhibitor or pharmaceutically acceptable salt or solvate thereof of claim 1, wherein X7 is W(1-Me), W(4-Me), W(6-Me), W(6-Et), W(7-Me), W(7-Et), W(7-n-Pr), or W(7-i-Pr).

15. The peptide inhibitor of claim 1, or pharmaceutically acceptable salt or solvate thereof, wherein: X4 is Pen; X5 is Asn; X6 is Thr; X7 is Trp substituted with alkyl; X8 is Gln, or Lys(Ac); X9 is Pen; X10 is Phe[4-(2-aminoethoxy)]; and X11 is 2-Nal; wherein the peptide inhibitor is cyclized via a bond between X4 and X9, and wherein the peptide inhibitor inhibits the binding of an interleukin-23 (IL-23) to an IL-23 receptor.

16. The peptide inhibitor of claim 15, or pharmaceutically acceptable salt or solvate thereof, wherein the peptide inhibitor is: Ac-[Pen]-NT-[W(7-Me)]-Gln-[Pen]-[Phe[4-(2-aminoethoxy)]-[2-Nal]-[α-MeLeu]-[Lys(Ac)]—NN—NH2 (SEQ ID NO: 6); Ac-[Pen]-N-T-[W(7-Et)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]—N—[(D)Leu]-NH2 (SEQ ID NO: 284); or Ac-[Pen]-N-T-[W(7-n-Pr)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]—N—[(D)Leu]-NH2 (SEQ ID NO: 285); wherein the peptide inhibitor is cyclized via a Pen-Pen disulfide bond.

17. The peptide inhibitor of claim 1, or pharmaceutically acceptable salt or solvate thereof, wherein the peptide inhibitor is: Ac-[Pen]-NT-[W(7-Me)]-Gln-[Pen]-[Phe[4-(2-aminoethoxy)]-[2-Nal]-[α-MeLeu]-[Lys(Ac)]—NN—NH2 (SEQ ID NO: 6), wherein the peptide inhibitor is cyclized via a Pen-Pen disulfide bond.

18. The peptide inhibitor of claim 1, or pharmaceutically acceptable salt or solvate thereof, wherein the peptide inhibitor is: Ac-[Pen]-N-T-[W(7-Et)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]—N—[(D)Leu]-NH2 (SEQ ID NO: 284), wherein the peptide inhibitor is cyclized via a Pen-Pen disulfide bond.

19. The peptide inhibitor of claim 1, or pharmaceutically acceptable salt or solvate thereof, wherein the peptide inhibitor is: Ac-[Pen]-N-T-[W(7-n-Pr)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]—N—[(D)Leu]-NH2 (SEQ ID NO: 285), wherein the peptide inhibitor is cyclized via a Pen-Pen disulfide bond.

20. A pharmaceutical composition comprising the peptide inhibitor or pharmaceutically acceptable salt or solvate thereof of claim 1, and a pharmaceutically acceptble carrier, excipient, or diluent.

21. The pharmaceutical composition of claim 20, further comprising an enteric coating.
```

---

#### 2.6 US11041000B2 ☑️부분교차검증 (차이 9개)

> **💡 핵심 요약** &nbsp;|&nbsp; **유형:** compound·물질(peptide), composition(조성물)
> 
> **무엇을 청구하나:** Formula (Z') 단환 IL-23R 펩타이드 저해제(X4=Pen, X5=Asn, X6=Thr, X7=alkyl 치환 Trp, X9=Pen, 두 Pen 간 디설파이드)와 그 의약조성물을 청구
> 
> **핵심 권리범위:** X4=Pen·X9=Pen 간 디설파이드 고리화 고정; X7=alkyl 치환 Trp(1-/2-/7-위치), X8=Gln/Lys(Ac) 등; X10=Phe[4-(2-aminoethoxy)] 등, X11=2-Nal 등; R1=Ac, IL-23의 IL-23R 결합 저해
> 
> **독립항:** 1 &nbsp;|&nbsp; **적응증:** — &nbsp;|&nbsp; **검증:** ☑️부분교차검증(차이9) &nbsp;|&nbsp; **추정만료:** 2040-07-09


| 항목 | 내용 |
|---|---|
| 특허번호 | US11041000B2 (등록, B2) |
| 제목 | Peptide inhibitors of interleukin-23 receptor and their use to treat inflammatory diseases |
| 출원번호 / 출원일 | 17/001,428 / 2020-08-24 |
| 우선일 | 2019-07-10 (US Provisional 62/872,477); PCT/US2020/041409 (2020-07-09) |
| 등록일 | 2021-06-22 |
| 출원인/양수인 | Protagonist Therapeutics, Inc. |
| 권위 만료일 | **2040-07-09** (GP anticipated expiration; 출원일+20년, PTE 미반영) |
| 교차검증 | GP=26, FPO=26, both=26, agree=17, **substantive_diff=9** → ☑️부분교차검증 |

**[ANALYSIS] (한국어)**

Formula (Z′) 단환 펩타이드(X4~X15 가변, R1/R2 말단기)를 청구하는 속 특허. 청구항 15·25는 SEQ ID NO:201/227/242/245/249/252/267/284/285 등 구체 서열군을 나열한다. 주의: GP 원문에서 청구항 16~23, 26은 화학구조식이 텍스트로 렌더링되지 않아 본문이 `...the peptide inhibitor is:` 에서 끝나는 **빈 구조 청구항**으로 보존되어 있다(원문 그대로). GP↔FPO 26개 중 17개 일치, 9개 차이로 ☑️부분교차검증이며 권위 소스는 GP.

**[VERBATIM] — 출처: Google Patents (`work/05_gp_authoritative/US11041000B2.md`)**

```text
1. A peptide inhibitor according to Formula (Z′): R1-X4-X5-X6-X7-X8-X9-X10-X11-X12-X13-X14-X15-R2  (Z′) or a pharmaceutically acceptable salt thereof, wherein X4 is Pen; X5 is Asn; X6 is Thr; X7 is Trp substituted with alkyl; X8 is Gln, alpha-MeLys, alpha-MeLeu, alpha-MeLys(Ac), beta-homoGln, Cit, Glu, Phe, Asn, Thr, Val, Aib, alpha-MeGln, alpha-MeAsn, Lys(Ac), Dab(Ac), Dap(Ac), homo-Lys(Ac), 1-Nal, 2-Nal, or Trp; X9 is Pen; X10 is unsubstituted Phe, or Phe substituted with halo, alkyl, haloalkyl, hydroxy, alkoxy, carboxy, carboxamido, 2-aminoethoxy, or 2-acetylaminoethoxy; X11 is 2-Nal, Phe(2-Me), Phe(3-Me), Phe(4-Me), Phe(3,4-dimethoxy), 1-Nal, unsubstituted Trp, or Trp substituted with cyano, halo, alkyl, haloalkyl, hydroxy, or alkoxy; X12 is 4-amino-4-carboxy-tetrahydropyran (THP), alpha-MeLys, alpha-MeLeu, alpha-MeArg, alpha-MePhe, alpha-MeLeu, alpha-MeLys, alpha-MeAsn, alpha-MeTyr, Ala, cyclohexylAla, Lys, or Aib; X13 is Aib, Glu, Cit, Gln, Lys(Ac), alpha-MeArg, alpha-MeGlu, alpha-MeLeu, alpha-MeLys, alpha-Me-Asn, alpha-MeLys(Ac), Dab(Ac), Dap(Ac), homo-Lys(Ac), Lys, pegylated Lys, b-homoGlu, or Lys(Y2-Ac), wherein Y2 is an amino acid; X14 is Asn, 2-Nap, Aib, Arg, Cit, Asp, Phe, Gly, Lys, Leu, Ala, (D)Ala, beta-Ala, His, Thr, n-Leu, Gln, Ser, (D)Ser, Tic, Trp, alpha-MeGln, alpha-MeAsn, alpha-MeLys(Ac), Dab(Ac), Dap(Ac), homo-Lys(Ac), or Lys(Ac); X15 is Leu, (D)Leu, beta-Ala, Cit, or (D)Lys; R1 is hydrogen, a C1-C6 alkyl, a C6-C12 aryl, a C6-C12aryl-C1-C6alkyl, or a C1-C20 alkanoyl; and R2 is OH or NH2; wherein the peptide inhibitor or pharmaceutically acceptable salt or solvate thereof comprises a disulfide bond between two Pen residues; and wherein the peptide inhibitor or pharmaceutically acceptable salt thereof inhibits the binding of an interleukin-23 (IL-23) to an IL-23 receptor.

2. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1, wherein X7 is Trp substituted with alkyl, and the substitution is at a 1-, 2-, or 7-position.

3. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 2, wherein X7 is Trp substituted with 1-Me, 2-Me, or 7-Me.

4. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 2, wherein X8 is Gln, alpha-Me-Lys, alpha-MeLys(Ac), or Glu.

5. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 2, wherein X8 is Gln.

6. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 2, wherein X8 is Gln, Cit, alpha-MeLys, alpha-MeLeu, Aib, or Lys(Ac).

7. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 2, wherein X8 is Lys(Ac).

8. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 2, wherein X10 is Phe, Phe[4-(2-aminoethoxy)], Phe[4-(2-acetylaminoethoxy)], or Phe(4-CONH2).

9. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 2, wherein X10 is Phe[4-(2-aminoethoxy)], or Phe[4-(2-acetylaminoethoxy)].

10. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 2, wherein X11 is Trp substituted with cyano, halo, alkyl, haloalkyl, hydroxy, or alkoxy.

11. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 2, wherein X11 is 2-Nal, Phe(2-Me), Phe(3-Me), Phe(4-Me), Phe(3,4-dimethoxy), or 1-Nal.

12. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 2, wherein X11 is 2-Nal or 1-Nal.

13. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 2, wherein X11 is 2-Nal.

14. The peptide inhibitor or pharmaceutically acceptable salt thereof claim 1, wherein R1 is Ac.

15. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1, wherein the peptide inhibitor is: (SEQ ID NO: 201) Ac-[Pen]-N-T-[W(7-Me)]-Q-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLeu]-[Lys(Ac)]-N-[bA]- NH2; (SEQ ID NO: 227) Ac-[Pen]-N-T-[W(7-Me)]-[Cit]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLeu]-[Lys(Ac)]-N-[bA]- NH2; (SEQ ID NO: 242) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N-[bA]- NH2; (SEQ ID NO: 245) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N- [(D)Leu]-NH2; (SEQ ID NO: 249) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N-[Cit]- NH2; (SEQ ID NO: 252) Ac-[Pen]-N--T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N- [(D)Lys]-NH2; (SEQ ID NO: 267) Ac-[Pen]-NT-[W(7-Me)]-Q-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N-[bA]- NH2; or (SEQ ID NO: 284) Ac-[Pen]-N-T-[W(7-Et]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N- [(D)Leu]-NH2, or (SEQ ID NO: 285) Ac-[Pen]-N-T-[W(7-n-Pr]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N- [(D)Leu]-NH2.

16. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1, wherein the peptide inhibitor is:

17. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1, wherein the peptide inhibitor is:

18. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1, wherein the peptide inhibitor is:

19. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1, wherein the peptide inhibitor is:

20. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1, wherein the peptide inhibitor is

21. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1, wherein the peptide inhibitor is:

22. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1, wherein the peptide inhibitor is:

23. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1, wherein the peptide inhibitor is:

24. A pharmaceutical composition comprising the peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1, and a pharmaceutically acceptable carrier, excipient, or diluent.

25. The pharmaceutical composition of claim 24, wherein the peptide inhibitor is: (SEQ ID NO: 201) Ac-[Pen]-N-T-[W(7-Me)]-Q-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLeu]-[Lys(Ac)]-N-[bA]- NH2; (SEQ ID NO: 227) Ac-[Pen]-N-T-[W(7-Me)]-[Cit]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLeu]-[Lys(Ac)]-N-[bA]- NH2; (SEQ ID NO: 242) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N-[bA]- NH2; (SEQ ID NO: 245) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N- [(D)Leu]-NH2; (SEQ ID NO: 249) Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N- [Cit]-NH2; (SEQ ID NO: 252) Ac-[Pen]-N--T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N- [(D)Lys]-NH2; (SEQ ID NO: 267) Ac-[Pen]-NT-[W(7-Me)]-Q-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N-[bA]- NH2; (SEQ ID NO: 284) Ac-[Pen]-N-T-[W(7-Et]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N- [(D)Leu]-NH2; or (Seq. ID. No. 285) Ac-[Pen]-N-T-[W(7-n-Pr)]-[Lys(Ac)]-[Pen]-Phe[4-(2- aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N- [(D)Leu]-NH2.

26. The pharmaceutical composition of claim 24, wherein the peptide inhibitor is:
```

---

### 티어 3 — 초기 세대(PTG-200 계열) 경구 IL-23R 펩타이드 (icotrokinra 이전)

> 아래 4건(+PCT)은 우선일 2014-07-17의 PTG-200 계열로 icotrokinra 특정 조성물보다 앞서지만, 동일 Protagonist 경구 IL-23R 펩타이드 골격(scaffold)에 속한다. 모두 **GP 단독**(FPO 미수집)이라 ⚠️단일소스(GP)다.

#### 3.1 US10787490B2 ☑️부분교차검증 (차이 4개)

> **💡 핵심 요약** &nbsp;|&nbsp; **유형:** compound·물질(peptide), use·치료방법
> 
> **무엇을 청구하나:** PEG화·지질화(Palm/Octanyl/isoGlu 등) 변형을 포함하는 특정 IL-23R 펩타이드 저해제(SEQ ID NO:1115~1206 열거)를 청구하고, IBD(UC/CD) 치료방법을 청구
> 
> **핵심 권리범위:** 열거된 개별 SEQ 화합물 한정, Pen-Pen 디설파이드 고리화; Palm/Octanyl/PEG4-isoGlu 등 지질·PEG 콘주게이트 포함; Phe[4-(2-aminoethoxy)]·2-Nal·Aib·Lys(Ac) 코어; IBD(특히 UC·Crohn's) 치료
> 
> **독립항:** 1 &nbsp;|&nbsp; **적응증:** 염증성 장질환(IBD)/궤양성대장염/크론병 &nbsp;|&nbsp; **검증:** ☑️부분교차검증(차이4) &nbsp;|&nbsp; **추정만료:** 2035-07-15


| 항목 | 내용 |
|---|---|
| 특허번호 | US10787490B2 (등록, B2) |
| 제목 | Peptide inhibitors of interleukin-23 receptor and their use to treat inflammatory diseases |
| 출원번호 / 출원일 | 15/745,371 / 2016-07-15 (PCT/US2016/042680 국내단계; 14/800,627의 CIP) |
| 우선일 | 2015-07-15 (PCT/US2015/040658); 추가 62/264,820, 62/281,123 |
| 등록일 | 2020-09-29 |
| 출원인/양수인 | Protagonist Therapeutics, Inc. |
| 권위 만료일 | **2035-07-15** (GP anticipated expiration; 출원일+20년, PTE 미반영) |
| 교차검증 | GP=18, FPO=18, both=18, agree=14, **substantive_diff=4** → ☑️부분교차검증 |

**[ANALYSIS] (한국어)**

청구항 1은 SEQ ID NO:1115~1206의 **지질화/PEG화 종 서열군**을 나열한다(Palm, isoGlu, PEG4, Octanyl 등 콘쥬게이트 포함) — 후대 lipidated 패밀리(WO2023288019A2 등)의 화학적 전조에 해당한다. 종속항은 단일 종, 조성물, IBD/UC/CD 치료방법이다. GP↔FPO 18개 중 14개 일치, 4개 차이로 ☑️부분교차검증. 우선일 2015이므로 만료 2035-07-15로 본 코퍼스 내 가장 이른 축에 든다.

**[VERBATIM] — 출처: Google Patents (`work/05_gp_authoritative/US10787490B2.md`)**

```text
1. A peptide inhibitor of an interleukin-23 receptor, or a pharmaceutically acceptable salt thereof, wherein the peptide inhibitor is: (SEQ ID NO: 1115) [Palm]-[isoGlu]-[PEG4]-[Pen]-NTWQ-[Pen]-[Phe[4-(2- aminoethoxy)]-[2-Nal]-[Aib]-[Lys(Ac)]-NN-NH2; (SEQ ID NO: 1116) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2-Nal]- [Aib]-[Lys(PEG4-isoGlu-Palm)]-NN-NH2; (SEQ ID NO: 1117) Ac-[Pen]-QTWQ-[Pen]-Phe(4-CONH2)-[2-Nal]-[a- MeLys(Ac)]-[Lys(Ac)]-NN-NH2; (SEQ ID NO: 1118) [Octanyl]-[IsoGlu]-[PEG4]-[Pen]-NTWQ-[Pen]-[Phe[4- (2-aminoethoxy)]-[2-Nal]-[Aib]-[Lys(Ac)]-NN-NH2; (SEQ ID NO: 1119) [Octanyl]-[PEG4]-[Pen]-NTWQ-[Pen]-[Phe[4-(2- aminoethoxy)]-[2-Nal]-[Aib]-[Lys(Ac)]-NN-NH2; (SEQ ID NO: 1120) [Palm]-[PEG4]-[Pen]-NTWQ-[Pen]-[Phe[4-(2- aminoethoxy)]-[2-Nal]-[Aib]-[Lys(Ac)]-NN-NH2; (SEQ ID NO: 1121) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-(2- Nal]-[Aib]-[Lys(PEG4-Octanyl)]-NN-NH2; (SEQ ID NO: 1122) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-(2- Nal]-[Aib]-[Lys(PEG4-Palm)]-NN-NH2; (SEQ ID NO: 1123) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)-(PEG4-Palm)]-(2-Nal]-[Aib]- [Lys(Ac)]NN-NH2; (SEQ ID NO: 1124) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)-(PEG4- Lauryl)]-[2-Nal]-[Aib]-[Lys(Ac)]-NN-NH2; (SEQ ID NO: 1125) Ac-[Pen]-QTWQ-[Pen]-Phe(4-CONH2)-[2-Nal]-[a- MeLys(PEG4-Palm)-[Lys(Ac)]-NN-NH2; (SEQ ID NO: 1126) Ac-[Pen]-QTWQ-[Pen]-Phe(4-CONH2)-[2-Nal]-[a- MeLys(PEG4-Lauryl)]-[Lys(Ac)]-NN-NH2; (SEQ ID NO: 1127) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)-(PEG4- IsoGlu-Palm)]-[2-Nal]-[Aib]-[Lys(Ac)]-NN-NH2; (SEQ ID NO: 1128) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)-(PEG4- IsoGLu-Lauryl)]-[2-Nal]-[Aib]-[Lys(Ac)]-NN-NH2; (SEQ ID NO: 1129) Ac-[Pen]-QTWQ-[Pen]-Phe(4-CONH2)-[2-Nal]-[a- MeLys(PEG4-IsoGlu-Palm)]-[Lys(Ac)]-NN-NH2; (SEQ ID NO: 1130) Ac-[Pen]-QTWQ-[Pen]-Phe(4-CONH2)-[2-Nal]-a-Me- K(PEG4-IsoGlu-Lauryl)]-[Lys(Ac)]-NN-NH2; (SEQ ID NO: 1131) Ac-[Pen]-QTWQ-[Pen]-Phe(4-CONH2)-[2-Nal]-[a- MeLys(IVA)]-[Lys(Ac)]-NN-NH2; (SEQ ID NO: 1132) Ac-[Pen]-QTWQ-[Pen]-Phe(4-CONH2)-[2-Nal]-[a- MeLys(Biotin)]-[Lys(Ac)]-NN-NH2; (SEQ ID NO: 1133) Ac-[Pen]-QTWQ-[Pen]-Phe(4-CONH2)-[2-Nal]-[a- MeLys(Octanyl)]-[Lys(Ac)]-NN-NH2; (SEQ ID NO: 1134) Ac-[Pen]-[Lys(IVA)]-TWQ-[Pen]-[Phe[4-(2- aminoethoxy)]-[2-Nal]-[Aib]-[Lys(Ac)]-NN-NH2; (SEQ ID NO: 1135) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2- Nal]-[Aib]-[Lys(Ac)]-[Lys(IVA)]-N-NH2; (SEQ ID NO: 1136) Ac-[Pen]-[Lys(Biotin)]-TWQ-[Pen]-[Phe[4-(2- aminoethoxy)]-[2-Nal]-[Aib]-[Lys(Ac)]-NN-NH2; (SEQ ID NO: 1137) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2- Nal]-[Aib]-[Lys(Ac)]-[Lys(Biotin)]-N-NH2; (SEQ ID NO: 1138) Ac-[Pen]-[Lys(Octanyl)]-TWQ-[Pen]-[Phe[4-(2- aminoethoxy)]-[2-Nal]-[Aib]-[Lys(Ac)]-NN-NH2; (SEQ ID NO: 1139) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2- Nal]-[Aib]-[Lys(Ac)]-[Lys(octanyl)]-N-NH2; (SEQ ID NO: 1140) Ac-[Pen]-[Lys(Palm)]-TWQ-[Pen]-[Phe[4-(2- aminoethoxy)]-[2-Nal]--[Aib]-[Lys(Ac)]-NN-NH2; (SEQ ID NO: 1141) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2- Nal]-[Aib]-[Lys(Ac)]-Lys(Palm)]-N-NH2; (SEQ ID NO: 1142) Ac-[Pen]-[Lys(PEG8)]-TWQ-[Pen]-[Phe[4-(2- aminoethoxy)]-[2-Nal]--[Aib]-[Lys(Ac)]-NN-NH2; (SEQ ID NO: 1143) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2- Nal]-[Aib]-[Lys(Ac)]-[Lys(PEG8)]-N-NH2; (SEQ ID NO: 1144) Ac-[Pen]-K(Peg11-Palm)TWQ-[Pen]-[Phe[4-(2- aminoethoxy)]-[2-Nal]-[Aib]-[Lys(Ac)]-NN-NH2; (SEQ ID NO: 1145) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2- Nal]-[Aib]-[Lys(Ac)]-[Lys(Peg11-palm)]-N-NH2; (SEQ ID NO: 1146) Ac-[Pen]-[Cit]-TW-[Cit]-[Pen]-[Phe[4-(2- aminoethoxy)]-[2-Nal]--[Aib]-[Lys(Ac)]-NN-NH2; (SEQ ID NO: 1147) Ac-[Pen]-[Lys(Ac)]-TW-[Cit]-[Pen]-[Phe[4-(2- aminoethoxy)]-[2-Nal]-[Aib]-[Lys(Ac)]-NN-NH2; (SEQ ID NO: 1148) Ac-[Pen]-NT-[Phe(3,4-OCH3)2]-Q-[Pen]-[Phe[4-(2- aminoethoxy)]-[2-Nal]-[Aib]-[Lys(Ac)]-NN-NH2; (SEQ ID NO: 1149) Ac-[Pen]-NT-[Phe(2,4-CH3)2]-Q-[Pen]-[Phe[4-(2- aminoethoxy)]-[2-Nal]-[Aib]-[Lys(Ac)]-NN-NH2; (SEQ ID NO: 1150) Ac-[Pen]-NT-[Phe(3-CH3)]-Q-[Pen]-[Phe[4-(2- aminoethoxy)]-[2-Nal]-[Aib]-[Lys(Ac)]-NN-NH2; (SEQ ID NO: 1151) Ac-[Pen]-NT-[Phe(4-CH3)]-Q-[Pen]-[Phe[4-(2-amino- ethoxy)]-[2-Nal]-[Aib]-[Lys(Ac)]-NN-NH2; (SEQ ID NO: 1152) Ac[(D)Arg]-[Pen]-NTWQ-[Pen]-[Phe[4-(2-amino- ethoxy)]-[2-Nal]-[Aib]-[Lys(Ac)]-N-[bAla]-NH2; (SEQ ID NO: 1153) Ac-[(D)Tyr]-[Pen]-NTWQ-[Pen]-[Phe[4-(2- aminoethoxy)]-[2-Nal]-[Aib]-[Lys(Ac)]-N-[bAla]-NH2; (SEQ ID NO: 1154) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2- Nal]-[Aib]-[Lys(Ac)]-QN-NH2; (SEQ ID NO: 1155) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2- Nal]-[Aib]-[Lys(Ac)]-[Lys(Ac)]-N-NH2; (SEQ ID NO: 1156) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2- Nal]-[Aib]-[Lys(Ac)]-N-[Lys(Ac)]-NH2; (SEQ ID NO: 1157) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2-Nal]-[Aib]-[Lys(Ac)]-QQ-NH2; (SEQ ID NO: 1158) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2- Nal]-[Aib]-[Lys(Ac)]-Q-[bAla]-NH2; (SEQ ID NO: 1159) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2-Nal]-[Aib]-[Lys(Ac)]-N-[Cit]-NH2; (SEQ ID NO: 1160) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2- Nal]-[Aib]-(Lys(Ac)]-[Cit]-NNH2; (SEQ ID NO: 1161) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2- Nal]-[Aib]-(Lys(Ac)]-[Cit]-Q-NH2; (SEQ ID NO: 1162) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2- Nal]-[Aib]-(Lys(Ac)]-[Cit]-[Lys(Ac)]-NH2; (SEQ ID NO: 1163) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2- Nal]-[Aib]-[Lys(Ac)]-[Lys(Ac)]-[Cit]-NH2; (SEQ ID NO: 1164) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2- Nal]-[Aib]-QN-[bAla]-NH2; (SEQ ID NO: 1165) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2- Nal]-[Aib]-E-[Cit]-Q-NH2; (SEQ ID NO: 1166) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2- Nal]-[Aib]-CitNCitNH2; (SEQ ID NO: 1167) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2- Nal]-[Aib]-[Cit]-Q-[Cit]-NH2; (SEQ ID NO: 1168) Ac-[Pen]-[Cit]-TWQ-[Pen]-[Phe[4-(2-aminoethoxy)]- [2-Nal]-[Aib]-[Lys(Ac)]-NN-NH2; (SEQ ID NO: 1169) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2- Nal]-[Aib]-[Lys(Ac)]-NN-NH2; (SEQ ID NO: 1170) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2- Nal]-[Aib]-QNN-NH2; (SEQ ID NO: 1171) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2- Nal]-[Aib]-ENQ-NH2; (SEQ ID NO: 1172) Ac-[Pen]-GPWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2- Nal]-[Aib]-[Lys(Ac)]-NN-NH2; (SEQ ID NO: 1173) Ac-[Pen]-PGWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2- Nal]-[Aib]-[Lys(Ac)]-NN-NH2; (SEQ ID NO: 1174) Ac-[Pen]-NTWN-[Pen]-[Phe[4-(2-aminoethoxy)]-[2- Nal]-[Aib]-[Lys(Ac)]-NN-NH2; (SEQ ID NO: 1175) Ac-[Pen]-NSWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2- Nal]-[Aib]-[Lys(Ac)]-NN-NH2; (SEQ ID NO: 1176) Ac-[Pen]-N-[Aib]-WQ-[Pen]-[Phe[4-(2-aminoethoxy)]- [2-Nal]-[Aib]-[Lys(Ac)]-NN-NH2; (SEQ ID NO: 1177) Ac-[Pen]-NTW-[Aib]-[Pen]-[Phe[4-(2-aminoethoxy)]- [2-Nal]-[Aib]-[Lys(Ac)]N-[Aib]-NH2; (SEQ ID NO: 1178) Ac-[Pen]-QTW-[Lys(Ac)]-[Pen]-[Phe[4-(2- aminoethoxy)]-[2-Nal]-[Aib]-[Lys(Ac)]-NN-NH2; (SEQ ID NO: 1179) Ac-[Pen]-[Lys(Ac)]-TWQ-[Pen]-(Phe[4-(2- aminoethoxy)]-[2-Nal]-[Aib]-[Lys(Ac)]NNNH2; (SEQ ID NO: 1180) Ac-[Pen]-QVWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2- Nal]-[Aib]-[Lys(Ac)]-NN-NH2; (SEQ ID NO: 1181) Ac-[Pen]-NT-[2-Nal]-Q-[Pen]-[Phe[4-(2- aminoethoxy)]-[2-Nal]-[Aib]-[Lys(Ac)]-NN-NH2; (SEQ ID NO: 1182) Ac-[Pen]-NT-[1-Nal]-Q-[Pen]-[Phe[4-(2- aminoethoxy)]-[2-Nal]-[Aib]-[Lys(Ac)]-NN-NH2; (SEQ ID NO: 1183) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2- Nal]-[a-MeLeu]-[Lys(Ac)]-NN-NH2; (SEQ ID NO: 1184) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2- Nal]-[a-MeLys]-[Lys(Ac)]-NN-NH2; (SEQ ID NO: 1185) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2- Nal]-(4-amino-4-carboxy-tetrahydropyran]- [Lys(Ac)]-NN-NH2; (SEQ ID NO: 1186) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2- Nal]-[a-MeLeu]-[Lys(Ac)]-N-[bAla]-NH2; (SEQ ID NO: 1187) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2- Nal]-[a-MeLys]-[Lys(Ac)]-N-[bAla]-NH2; (SEQ ID NO: 1188) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2- Nal]-(4-amino-4-carboxy-tetrahydropyran]- [Lys(Ac)]-N-[bAla]-NH2; (SEQ ID NO: 1189) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2- Nal]-[Aib]-[Lys(Ac)]-LN-NH2; (SEQ ID NO: 1190) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2- Nal]-[Aib]-[Lys(Ac)]-GN-NH2; (SEQ ID NO: 1191) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2- Nal]-[Aib]-[Lys(Ac)]-SN-NH2; (SEQ ID NO: 1192) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2- Nal]-[Aib]-[Lys(Ac)]-[Aib]-N-NH2; (SEQ ID NO: 1193) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2- Nal]-[Aib]-[Lys(Ac)]-FN-NH2; (SEQ ID NO: 1194) Ac-[Pen]-NTW-[Cit]-[Pen]-[Phe[4-(2-aminoethoxy)]- (2-Nal]-[Aib]-[Lys(Ac)]-NN-NH2; (SEQ ID NO: 1195) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2- Nal]-[Aib]-(Lys(Ac)]-[Tic]-[bAla]-NH2; (SEQ ID NO: 1196) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2- Nal]-[Aib]-]Lys(Ac)]-[nLeu]-[bAla]-NH2; (SEQ ID NO: 1197) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2- Nal]-[Aib]-[Lys(Ac)]-G-[bAla]-NH2; (SEQ ID NO: 1198) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2- Nal]-[Aib]-[Lys(Ac)]-R-[bAla]-NH2; (SEQ ID NO: 1199) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2- Nal]-[Aib]-[Lys(Ac)]-W-[bAla]-NH2; (SEQ ID NO: 1200) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2- Nal]-[Aib]-[Lys(Ac)]-S-[bAla]-NH2; (SEQ ID NO: 1201) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2- Nal]-[Aib]-[Lys(Ac)]-L-[bAla]-NH2; (SEQ ID NO: 1202) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2- Nal]-[Aib]-[Lys(Ac)]-[AIB]-[bAla]-NH2; (SEQ ID NO: 1203) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2- Nal]-[Aib]-[Lys(Ac)]-(N-MeAla[-[bAla]-NH2; (SEQ ID NO: 1204) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2- Nal]-[Aib]-[Lys(Ac)]-[2-Nap]-[bAla]-NH2; (SEQ ID NO: 1205) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2- Nal]-[Aib]-[Lys(Ac)]-F-[bAla]-NH2; or (SEQ ID NO: 1206) Ac-[(D)Arg]-[Pen]-NTWQ-[Pen]-[Phe[4-(2- aminoethoxy)]-[2-Nal]-[4-amino-4- carboxy-tetrahydropyran]-[Lys(Ac)]-NN-NH2. wherein the peptide inhibitor is cyclized via a disulfide bond between Pen and Pen; and wherein 2-Nal is L-2-napthylalanine, α-MeLys is alpha-methyl-L-Lysine, α-MeLeu is alpha-methyl-L-Leucine, and Aib is 2-aminoisobutyric acid.

2. The peptide inhibitor or pharmaceutically acceptable salt thereof according to claim 1, wherein the peptide inhibitor is: (SEQ ID NO: 1178) Ac-[Pen]-QTW-[Lys(Ac)]-[Pen]-[Phe[4-(2-aminoethoxy)]-[2-Nal]-[Aib]-[Lys(Ac)]-NN-NH2; (SEQ ID NO: 1183) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2-Nal]-[α-MeLeu]-[Lys(Ac)]-NN-NH2; (SEQ ID NO: 1186) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2-Nal]-[α-MeLeu]-[Lys(Ac)]-N-[βAla+-NH2; (SEQ ID NO: 1187) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2-Nal]-[α-MeLys]-[Lys(Ac)]-N-[βAla]-NH2; (SEQ ID NO: 1188) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2-Nal]-[4-amino-4-carboxy-tetrahydropyran]- [Lys(Ac)]-N-[βAla]-NH2; (SEQ ID NO: 1191) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2-Nal]-[Aib]-[Lys(Ac)]-SN-NH2; (SEQ ID NO: 1193) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2-Nal]-[Aib]-[Lys(Ac)]-FN-NH2; (SEQ ID NO: 1194) Ac-[Pen]-NTW-[Cit]-[Pen]-[Phe[4-(2-aminoethoxy)]-[2-Nal]-[Aib]-[Lys(Ac)]-NN-NH2; (SEQ ID NO: 1197) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2-Nal]-[Aib]-[Lys(Ac)]-G-[βAla]-NH2; (SEQ ID NO: 1198) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2-Nal]-[Aib]-[Lys(Ac)]-R-[βAla]-NH2; (SEQ ID NO: 1200) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2-Nal]-[Aib]-[Lys(Ac)]-S-[βAla]-NH2; (SEQ ID NO: 1204) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2-Nal]-[Aib]-[Lys(Ac)]-[2-Nap]-[βAla]-NH2; or (SEQ ID NO: 1205) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2-Nal]-[Aib]-[Lys(Ac)]-F-[βAla]-NH2.

3. The peptide inhibitor or pharmaceutically acceptable salt thereof according to claim 1, wherein the peptide inhibitor is: (SEQ ID NO: 1178) Ac-[Pen]-QTW-[Lys(Ac)]-[Pen]-[Phe[4-(2- aminoethoxy)]-[2-Nal]-[Aib]-[Lys(Ac)]-NN-NH2.

4. The peptide inhibitor or pharmaceutically acceptable salt thereof according to claim 1, wherein the peptide inhibitor is: (SEQ ID NO: 1183) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2- Nal]-[α-MeLeu]-[Lys(Ac)]-NN-NH2.

5. The peptide inhibitor or pharmaceutically acceptable salt thereof according to claim 1, wherein the peptide inhibitor is: (SEQ ID NO: 1186) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]- [2-Nal]-[α-MeLeu]-[Lys(Ac)]-N-[βAla]-NH2.

6. The peptide inhibitor or pharmaceutically acceptable salt thereof according to claim 1, wherein the peptide inhibitor is: (SEQ ID NO: 1194) Ac-[Pen]-NTW-[Cit]-[Pen]-[Phe[4-(2-aminoethoxy)]- [2-Nal]-[Aib]-[Lys(Ac)]-NN-NH2.

7. The peptide inhibitor or pharmaceutically acceptable salt thereof according to claim 1, wherein the peptide inhibitor is: (SEQ ID NO: 1200) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]- [2-Nal]--[Aib]-[Lys(Ac)]-S-[βAla]-NH2.

8. The peptide inhibitor or pharmaceutically acceptable salt thereof according to claim 1, wherein the peptide inhibitor is: (SEQ ID NO: 1204) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2- Nal]-[Aib]-[Lys(Ac)]-[2-Nap]-[βAla]-NH2.

9. The peptide inhibitor or pharmaceutically acceptable salt thereof according to claim 1, wherein the peptide inhibitor is: (SEQ ID NO: 1205) Ac-[Pen]-NTWQ-[Pen]-[Phe]4-(2-aminoethoxy)]-[2- Nal]-[Aib]-[Lys(Ac)]-F-[βAla]-NH2.

10. A method for treating an Inflammatory Bowel Disease (IBD) in a subject, comprising administering to the subject an effective amount of the peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1.

11. The method of claim 10, wherein the IBD is ulcerative colitis or Crohn's disease.

12. The method of claim 10, wherein the peptide inhibitor is: (SEQ ID NO: 1178) Ac-[Pen]-QTW-[Lys(Ac)]-[Pen]-[Phe[4-(2- aminoethoxy)]-[2-Nal]-[Aib]-[Lys(Ac)]-NN-NH2.

13. The method of claim 10, wherein the peptide inhibitor is: (SEQ ID NO: 1183) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2- Nal]-[α-MeLeu]-[Lys(Ac)]-NN-NH2.

14. The method of claim 10, wherein the peptide inhibitor is: (SEQ ID NO: 1186) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2- Nal]-[α-MeLeu]-[Lys(Ac)]-N-[βAla]-NH2.

15. The method of claim 10, wherein the peptide inhibitor is: (SEQ ID NO: 1194) Ac-[Pen]-NTW-[Cit]-[Pen]-[Phe[4-(2-aminoethoxy)]- [2-Nal]-[Aib]-[Lys(Ac)]-NN-NH2.

16. The method of claim 10, wherein the peptide inhibitor is: (SEQ ID NO: 1200) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2- Nal]-[Aib]-[Lys(Ac)]-S-[βAla]-NH2.

17. The method of claim 10, wherein the peptide inhibitor is: (SEQ ID NO: 1204) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2- Nal]-[Aib]-[Lys(Ac)]-[2-Nap]-[βAla]-NH2.

18. The method of claim 10, wherein the peptide inhibitor is: (SEQ ID NO: 1205) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2-  Nal]-[Aib]-[Lys(Ac)]-F-[βAla]-NH2.
```

---

#### 3.2 US9624268B2 ⚠️단일소스(GP)

> **💡 핵심 요약** &nbsp;|&nbsp; **유형:** compound·물질(peptide), composition(조성물)
> 
> **무엇을 청구하나:** IL-23R 단환 펩타이드 저해제를 20잔기 Formula Ir 및 Xa의 광범위 초기 Markush로 청구(X4-X9 고리화)하고, 다수 개별 SEQ 화합물과 의약조성물까지 청구(PTG-200 계열 기초 물질특허)
> 
> **핵심 권리범위:** 20위치(X1~X20) 광범위 Markush, X4-X9 디설파이드/티오에터/락탐/트리아졸 등 고리화; X4=X9=Pen 디설파이드 또는 Abu-Cys 티오에터 하위군; 다수 개별 SEQ(예: SEQ ID NO:283/285/602/632 등) 한정; Phe[4-(2-aminoethoxy)]·2-Nal·THP·Lys(Ac) 등 코어 잔기
> 
> **독립항:** 1, 11, 19, 24 &nbsp;|&nbsp; **적응증:** — &nbsp;|&nbsp; **검증:** ⚠️단일소스(GP) &nbsp;|&nbsp; **추정만료:** 2035-07-15


| 항목 | 내용 |
|---|---|
| 특허번호 | US9624268B2 (등록, B2) |
| 제목 | Oral peptide inhibitors of interleukin-23 receptor and their use to treat inflammatory bowel diseases |
| 출원번호 / 출원일 | 14/800,627 / 2015-07-15 |
| 우선일 | 2014-07-17 (US Provisional 62/025,899); 추가 62/119,685, 62/119,688 |
| 등록일 | 2017-04-18 |
| 출원인/양수인 | Protagonist Therapeutics, Inc. |
| 패밀리 | WO2016011208A1 (PCT), US10023614B2, US10941183B2, US11884748B2 |
| 권위 만료일 | **2035-07-15** (GP anticipated expiration; 출원일+20년, PTE 미반영) |
| 교차검증 | GP=24, FPO=0(미수집) → ⚠️단일소스(GP) |

**[ANALYSIS] (한국어)**

PTG-200 계열의 **기초 미국 특허**(icotrokinra 이전 세대). 청구항 1은 Formula Ir(X1~X20, 광범위 가변)의 대형 Markush 속이며, X4/X9는 Pen/Cys 등 환화 가능 잔기다. 청구항 5·9는 다수 SEQ ID NO 종 서열을 나열하고, 청구항 24는 조성물이다. FPO 미수집이라 ⚠️단일소스(GP).

**[VERBATIM] — 출처: Google Patents (`work/05_gp_authoritative/US9624268B2.md`)**

```text
1. A peptide inhibitor of an interleukin-23 receptor, or a pharmaceutically acceptable salt or solvate thereof, wherein the peptide inhibitor comprises the amino acid sequence of Formula Ir: X1-X2-X3-X4-X5-X6-X7-X8-X9-X10-X11-X12-X13-X14-X15-X16-X17-X18-X19-X20  (Ir) wherein X1 is any amino acid or absent; X2 is any amino acid or absent; X3 is any amino acid or absent; X4 is Cys, Pen, hCys, D-Pen, D-Cys, D-hCys, Met, Glu, Asp, Lys, Orn, Dap, Dab, D-Dap, D-Dab, D-Asp, D-Glu, D-Lys, Sec, 2-chloromethylbenzoic acid, mercapto-propanoic acid, mercapto-butyric acid, 2-chloro-acetic acid, 3-choro-propanoic acid, 4-chloro-butyric acid, 3-chloro-isobutyric acid, Abu, β-azido-Ala-OH, propargylglycine, 2-(3′-butenyl)glycine, 2-allylglycine, 2-(3′-butenyl)glycine, 2-(4′-pentenyl)glycine, 2-(5′-hexenyl)glycine, or absent; X5 is any amino acid; X6 is any amino acid; X7 is Trp, Glu, Gly, Ile, Asn, Pro, Arg, Thr or OctGly, or a corresponding α-methyl amino acid form of any of the foregoing; X8 is any amino acid; X9 is Cys, Pen, hCys, D-Pen, D-Cys, D-hCys, Glu, Lys, Orn, Dap, Dab, D-Dap, D-Dab, D-Asp, D-Glu, D-Lys, Asp, Leu, Val, Phe, Ser, Sec, Abu, β-azido-Ala-OH, propargylglycine, 2-2-allylglycine, 2-(3′-butenyl)glycine, 2-(4′-pentenyl)glycine, Ala, hCys, Met, MeCys, (D)Tyr or 2-(5′-hexenyl)glycine; X10 is Tyr, Phe(4-OMe), 1-Nal, 2-Nal, Aic, α-MePhe, Bip, (D)Cys, Cha, DMT, (D)Tyr, Glu, His, hPhe(3,4-dimethoxy), hTyr, N-Me-Tyr, Trp, Phe(4-CONH2), Phe(4-phenoxy), Thr, Tic, Tyr(3-tBu), Phe(4-tBu), Phe(4-CN), Phe(4-Br), Phe(4-NH2), Phe(4-F), Phe(3,5-F2), Phe(4-CH2CO2H), Phe(penta-F), Phe(3,4-Cl2), Phe(4-CF3), Bip, Cha, 4-PyridylAlanine, βhTyr, OctGly, Phe(4-N3), Phe(4-Br), Phe[4-(2-aminoethoxy)], Phe, a Phe analog, or a Tyr analog, or a corresponding α-methyl amino acid form of any of the foregoing; X11 is 2-Nal, 1-Nal, 2,4-dimethylPhe, Bip, Phe(3,4-Cl2), Phe (3,4-F2), Phe(4-CO2H), βhPhe(4-F), α-Me-Trp, 4-phenylcyclohexyl, Phe(4-CF3), Phe(3,4-OMe2), α-MePhe, βhPhe, βhTyr, βhTrp, Nva(5-phenyl), Phe, His, hPhe, Tic, Tqa, Trp, Tyr, Phe(4-OMe), Phe(4-Me), Trp(2,5,7-tri-tert-Butyl), Phe(4-Oallyl), Tyr(3-tBu), Phe(4-tBu), Phe(4-guanidino, Phe(4-OBzl), Octgly, Glu(Bzl), 4-Phenylbenzylalanine, Phe[4-(2-aminoethoxy)], 5-Hydroxy-Trp, 6-Chloro-Trp, N-MeTrp, 1,2,3,4-tetrahydro-norharman, Phe(4-CONH2), Phe(3,4-Dimethoxy), Phe(2,3-Cl2), Phe(2,3-F2), Phe(4-F), 4-phenylcyclohexylalanine or Bip, or a corresponding α-methyl amino acid form of any of the foregoing; X12 is His, Phe, Arg, N-Me-His, Val, Cav, Cpa, Leu, Cit, hLeu, 3-Pal, t-butyl-Ala, α-MeLys, D-Ala, (D)Asn, (D)Asp, (D)Leu, (D)Phe, (D)Tyr, Aib, α-MeLeu, α-MeOrn, β-Aib, β-Ala, βhAla, βhArg, βhLeu, βhVal, β-spiro-pip, Glu, hArg, Ile, Lys, N-MeLeu, N-MeArg, Ogl, Orn, Pro, Gln, Ser, Thr, Tle, t-butyl-Gly, 4-amino-4-carboxy-tetrahydropyran (THP), Achc Acpc, Acbc, Acvc, Agp, Aib, α-DiethylGly, α-MeLys(Ac), α-MeOrn, α-MeSer, α-MeVal, Cha, Cit, Cpa, (D)Asn, Glu, hArg, or Lys, or a corresponding α-methyl amino acid form of any of the foregoing; X13 is Thr, Sarc, Glu, Phe, Arg, Leu, Asn, Cit, Lys, Arg, Orn, Val, βhAla, Lys(Ac), (D)Asn, (D)Leu, (D)Phe, (D)Thr, Ala, α-MeLeu, Aib, β-Ala, β-Glu, βhLeu, βhVal, β-spiro-pip, Cha, Chg, Asp, Dab, Dap, α-DiethylGly, hLeu, Asn, Ogl, Pro, Gln, Ser, β-spiro-pip, Thr, Tba, Tle or Aib, or a corresponding α-methyl amino acid form of any of the foregoing; X14 is Phe, Tyr, Glu, Gly, His, Lys, Leu, Met, Asn, Lys(Ac), Dap(Ac), Asp, Pro, Gln, Arg, Ser, Thr, Tic or βhPhe, or a corresponding α-methyl amino acid form of any of the foregoing; X15 is Gly, Ser, Thr, Gln, Ala, (D)Ala, (D)Asn, (D)Asp, (D)Leu, (D)Phe, (D)Thr, Aea, Asp, Asn, Glu, Phe, Gly, Lys, Leu, Pro, Arg, β-Ala, or Sarc, or a corresponding α-methyl amino acid form of any of the foregoing; X16 is any amino acid or absent; X17 is any amino acid or absent; X18 is any amino acid or absent; X19 is any amino acid or absent; and X20 is any amino acid or absent, wherein the peptide inhibitor is cyclized via a bond between X4 and X9, and wherein the peptide inhibitor inhibits the binding of an interleukin-23 (IL-23) to an IL-23 receptor.

2. The peptide inhibitor of claim 1, wherein the bond between X4 and X9 is a disulfide bond, a thioether bond, a lactam bond, a triazole ring, a selenoether bond, a diselenide bond, or an olefin bond.

3. The peptide inhibitor of claim 1, wherein X4 is Pen and X9 is Pen, and the bond is a disulfide bond.

4. The peptide inhibitor of claim 3, wherein X7 is Trp; X10 is Phe, Tyr, a Phe analog, or a Tyr analog; X11 is Trp, 1-Nal or 2-Nal; and X12 is Aib, α-Me-Lys, α-Me-Val, α-Me-Leu; Achc, Acvc, Acpc, or 4-amino-4-carboxy-tetrahydropyran (THP).

5. The peptide inhibitor of claim 4, wherein the peptide inhibitor comprises any of the following amino acid sequences: (SEQ ID NO: 282) Ac-[Pen]-Q-T-W-Q-[Pen]-[Phe(4-OMe)]-[2-Nal]-[α-Me- Lys]-ENG-NH2; (SEQ ID NO: 283) Ac-[Pen]-N-T-W-Q-[Pen]-[Phe[4-(2-aminoethoxy)]]- [2-Nal]-[Aib]-[Lys(Ac)]-NN-NH2; (SEQ ID NO: 285) Ac-[Pen]-Q-T-W-Q-[Pen]-[Phe[4-(2-aminoethoxy)]]- [2-Nal]-[α-MeLeu]-[Lys(Ac)]-NN-NH2; (SEQ ID NO: 668) Ac-[Pen]-QTWQ-[Pen]-[Phe(4-CONH2)]-[2-Nal]- [α-MeLys]-[Lys(Ac)]-NN-NH2; (SEQ ID NO: 603) Ac-[Pen]-Q-T-W-Q-[Pen]-[Phe[4-(2-aminoethoxy)]]- [2-Nal]-[α-MeLeu]-QNN-NH2; (SEQ ID NO: 286) Ac-[Pen]-Q-T-W-Q-[Pen]-[Phe(4-CONH2)]-[2-Nal]- [α-MeLys]-[Lys(Ac)]-NN-NH2; (SEQ ID NO: 598) Ac-[Pen]-QTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]]- [2-Nal]-[α-MeLys]-[Lys(Ac)]-NG-NH2; (SEQ ID NO: 1034) Ac-[Pen]-QTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]]- [2-Nal]-[α-MeLys]-[Lys(Ac)]-NN-NH2; (SEQ ID NO: 601) Ac-[Pen]-QTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]]- [2-Nal]-[α-MeLys]-ENA-NH2; (SEQ ID NO: 602) Ac-[Pen]-QTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]]- [2-Nal]-[α-MeLeu]-[Lys(Ac)]-NN-NH2; (SEQ ID NO: 603) Ac-[Pen]-QTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]]- [2-Nal]-[α-MeLeu]-QNN-NH2; (SEQ ID NO: 604) Ac-[Pen]-QTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]]- [2-Nal]-[Aib]-ENN-NH2; (SEQ ID NO: 605) Ac-[Pen]-QTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]]- [2-Nal]-Aib-[Lys(Ac)]-NN-NH2; (SEQ ID NO: 606) Ac-[Pen]-QTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]]- [2-Nal]-[Aib]-[Lys(Ac)]-NQ-NH2; (SEQ ID NO: 613) Ac-[Pen]-QTWQ-[Pen]-[Phe[4-(2-acetylaminoethoxy)]]- [2-Nal]-[α-MeLeu]-[Lys(Ac)]-NN-NH2; (SEQ ID NO: 614) Ac-[Pen]-QTWQ-[Pen]-[Phe[4-(2-acetylaminoethoxy)]]- [2-Nal]-[α-MeLeu]-QNN-NH2; (SEQ ID NO: 639) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]]- [2-Nal]-[Aib]-[Lys(Ac)]-N-[βAla]-NH2; (SEQ ID NO: 641) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]]- [2-Nal]-[hLeu]-[Lys(Ac)]-N-[βAla]-NH2; (SEQ ID NO: 616) Ac-[Pen]-QTWQ-[Pen]-[Phe[4-(2-acetylaminoethoxy)]]- [2-Nal]-[Aib]-[Lys(Ac)]-NN-NH2; (SEQ ID NO: 632) Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]]- [2-Nal]-[Aib]-[Lys(Ac)]-NN-NH2; (SEQ ID NO: 617) Ac-[Pen]-QTWQ-[Pen]-[Phe[4-(2-acetylaminoethoxy)]]- [2-Nal]-[Aib]-[Lys(Ac)]-NQ-NH2; or (SEQ ID NO: 623) Ac-[Pen]-QTWQ-[Pen]-[Phe(4-OMe]-[2-Nal]-[Aib]- [Lys(Ac)]-NQ-NH2, wherein the peptide inhibitor comprises a disulfide bond between the two Pen amino acids.

6. The peptide inhibitor of claim 1, wherein X4 is Abu, 2-chloromethylbenzoic acid, mercapto-propanoic acid, mercapto-butyric acid, 2-chloro-acetic acid, 3-chloro-propanoic acid, 4-chloro-butyric acid, 3-chloro-isobutyric acid; X9 is Abu, Cys, Pen, hCys, D-Pen, D-Cys, or D-hCys, and and the bond between X4 and X9 is a thioether bond.

7. The peptide inhibitor of claim 6, wherein (a) X4 is Abu and X9 is Cys; or (b) X4 is Cys and X9 is Abu; wherein the peptide inhibitor is cyclized via a thioether bond between X4 and X9.

8. The peptide inhibitor of claim 6, wherein X7 is Trp; X10 is Phe, Tyr, a Phe analog, or a Tyr analog; X11 is Trp, 1-Nal or 2-Nal; and X12 is α-Me-Lys, α-Me-Leu, α-Me-Ser, α-Me-Val, Achc, Acvc, Acpc, Acbc or 4-amino-4-carboxy-tetrahydropyran.

9. The peptide inhibitor of claim 8, wherein the peptide inhibitor comprises any of the following amino acid sequences: (SEQ ID NO: 430) Ac-Cyclo-[[Abu]-QTWQC]]-[Phe(4-OMe)]-[2-Nal]- [α-MeLys]-E-N-G; (SEQ ID NO: 431) Ac-Cyclo-[[Abu]-QTWQC]]-[Phe(4-OMe)]-[2-Nal]- [α-MeOrn]-ENG-NH2; (SEQ ID NO: 432) Ac-Cyclo-[[Abu]-QTWQC]]-[Phe(4-CO2H)]-[2-Nal]- [α-MeLys]-[Lys(Ac)]-NG-NH2; (SEQ ID NO: 433) Ac-Cyclo-[[Abu]-QTWQC]]-[Phe(4-OMe)]-[2-Nal]- [α-MeLys]-[Lys(Ac)]-NG-NH2; (SEQ ID NO: 434) Ac-Cyclo-[[Abu]-QTWQC]]-[Phe(4-CONH2)]-[2-Nal]- [α-MeLys]-[Lys(Ac)]NG-NH2; (SEQ ID NO: 435) Ac-Cyclo-[[Abu]-QTWQC]]-[Phe(4-OMe)]-[2-Nal]- [α-MeLys]-[Lys(Ac)]-NA-NH2; (SEQ ID NO: 436) Ac-Cyclo-[[Abu]-QTWQC]]-[Phe(4-OMe)]-[2-Nal]- [α-MeLys]-[Lys(Ac)]-NAE-NH2; (SEQ ID NO: 437) Ac-Cyclo-[[Abu]-QTWQC]]-[Phe[4-(2-aminoethoxy)]]- [2-Nal]-[α-MeLys]-ENG-NH2; (SEQ ID NO: 438) Ac-Cyclo-[[Abu]-QTWQC]]-[Phe[4-(2-aminoethoxy)]]-W- [α-MeLys]-E-N-G; (SEQ ID NO: 439) Ac-Cyclo-[[Abu]-QTWQC]]-[Phe[4-(2-aminoethoxy)]]- [2-Nal]-[α-MeLys]-DNG-NH2; (SEQ ID NO: 440) Ac-Cyclo-[[Abu]-QTWQC]]-[Phe[4-(2-aminoethoxy)]]- [2-Nal]-[α-MeLys]-[Lys(succinic acid)]-NG-NH2; (SEQ ID NO: 441) Ac-Cyclo-[[Abu]-QTWQC]]-[Phe[4-(2-aminoethoxy)]]- [2-Nal]-[α-MeLys]-[Lys(glutaric acid)]-NG-NH2; (SEQ ID NO: 442) Ac-Cyclo-[[Abu]-QTWQC]]-[Phe[4-(2-aminoethoxy)]]- [2-Nal]-[α-MeLys]-[Lys(pyroglutamic acid)]-NG-NH2; (SEQ ID NO: 443) Ac-Cyclo-[[Abu]-QTWQC]]-[Phe[4-(2-aminoethoxy)]]- [2-Nal]-[α-MeLys]-[Lys(isovaleric acid)]-NG-NH2; (SEQ ID NO: 444) Ac-Cyclo-[[Abu]-QTWQC]]-[Phe[4-(2-aminoethoxy)]]- [2-Nal]-[α-MeLys]-[Lys(Ac)]-NG-[(D)Lys]-NH2; (SEQ ID NO: 445) Ac-Cyclo-[[Abu]-QTWQC]]-[Phe[4-(2-aminoethoxy)]]- [2-Nal]-[α-MeLys]-[Lys(Ac)]-NG-[AEA]-NH2; (SEQ ID NO: 446) Ac-Cyclo-[[Abu]-QTWQC]]-[Phe[4-(2-aminoethoxy)]]- [2-Nal]-[Aib]-QNG-NH2; (SEQ ID NO: 447) Ac-Cyclo-[[Abu]-QTWQC]]-[Phe[4-(2-aminoethoxy)]]- [2-Nal]-[Aib]-[Lys(Ac)]-NA-NH2; (SEQ ID NO: 448) Ac-Cyclo-[[Abu]-QTWQC]]-[Phe[4-(2-aminoethoxy)]]- [2-Nal]-[Aib]-KNG-NH2; (SEQ ID NO: 449) Ac-Cyclo-[[Abu]-QTWQC]]-[Phe[4-(2-aminoethoxy)]]- [2-Nal]-[α-MeLys]-[Lys(Ac)]-NG-NH2; (SEQ ID NO: 656) Ac-Cyclo-[[Abu]-QTWQC]]-[Phe[4-(2-(acetyl- aminoethoxy)]]-[2-Nal]-[α-MeLys(Ac)]- [Lys(Ac)]-NG-NH2; (SEQ ID NO: 657) Ac-Cyclo-[[Abu]-QTWQC-[Phe[4-(2-(acetyl- aminoethoxy)]]-[2-Nal]-[α-MeLys(Ac)]-ENG-NH2; (SEQ ID NO: 658) Ac-Cyclo-[[Abu]-QTWQC]]-[Phe[4-(2-aminoethoxy)]]- [2-Nal]-[4-amino-4-carboxy-tetrahydropyran]-ENN- NH2; (SEQ ID NO: 659) Ac-Cyclo-[[Abu]-QTWQQ]]-[Phe[4-(2-aminoethoxy)]]- [2-Nal]-[α-MeLys]-ENQ-NH2; (SEQ ID NO: 912) Ac-Cyclo-[[Abu]-QTWQC]-[Phe[4-(2-aminoethoxy)]]- [2-Nal]-[α-MeLys]-ENN-NH2; (SEQ ID NO: 660) Ac-Cyclo-[[Abu]-QTWQC]]-[Phe[4-(2-aminoethoxy)]]- [2-Nal]-[α-MeVal]-[Lys(Ac)]-NG-NH2; (SEQ ID NO: 661) Ac-Cyclo-[[Abu]-QTWQC]]-[Phe[4-(2-aminoethoxy)]]- [2-Nal]-[hLeu]-[Lys(Ac)]-N-[βAla]-NH2; (SEQ ID NO: 662) Ac-Cyclo-[[Abu]-QTWQC]]-[Phe[4-(2-(acetyl- aminoethoxy)]]-[2-Nal]-[α-MeLys(Ac)]-ENQ-NH2; (SEQ ID NO: 663) Ac-Cyclo-[[Abu]-QTWQC]]-[Phe[4-(2-(acetyl- aminoethoxy)]]-[2-Nal]-[α-MeLys(Ac)]-ENN-NH2; (SEQ ID NO: 664) Ac-Cyclo-[[Abu]-QTWQC]]-[Phe[4-(2-aminoethoxy)]]- [2-Nal]-[α-MeLeu]-ENN-NH2; (SEQ ID NO: 665) Ac-Cyclo-[[Abu]-QTWQC]]-[Phe[4-(2-aminoethoxy)]]- [2-Nal]-[α-MeLeu)-[Cit]-NN-NH2; (SEQ ID NO: 766) Ac-Cyclo-[[Abu]-QTWQC]]-[Phe[4-(2-aminoethoxy)]]- [2-Nal]-[α-MeLeu]-[Lys(Ac)]-NN-NH2; (SEQ ID NO: 767) Ac-Cyclo-[[Abu]-QTWQC]]-[-Phe[4-(2-aminoethoxy)]]- [2-Nal]-[Aib]-[Lys(Ac)]-NG-NH2; (SEQ ID NO: 965) Ac-E-Cyclo-[[Abu]-QTWQC]-[Phe[4-(2-aminoethoxy)]]- [2-Nal]-[α-MeLys]-ENN-NH3; (SEQ ID NO: 966) Ac-(D)Glu-[Cyclo-[[Abu]-QTWQC]-[Phe[4-(2- aminoethoxy)]]-[2-Nal]-[α-MeLys]-ENN-NH2; (SEQ ID NO: 967) Ac-Arg-Cyclo-[[Abu]-QTWQC]-[Phe[4-(2- aminoethoxy)]]-[2-Nal]-[α-MeLys]-ENN-NH2; (SEQ ID NO: 1041) Ac-[(D)Arg-Cyclo-[[Abu]-QTWQC]-[Phe[4-(2- aminoethoxy)]]-[2-Nal]-[α-MeLys]-ENN-NH2; (SEQ ID NO: 969) Ac-F-Cyclo-[[Abu]-QTWQC]]-[Phe[4-(2-aminoethoxy)]]- [2-Nal]-[α-MeLys]-ENN-NH2; (SEQ ID NO: 970) Ac-[(D)Phe]-Cyclo-[[Abu]-QTWQC]-[Phe[4-(2- aminoethoxy)]]-[2-Nal]-[α-MeLys]-ENN-NH2; (SEQ ID NO: 971) Ac-[2-Nal]-Cyclo-[[Abu]-QTWQC]-[Phe[4-(2- aminoethoxy)]]-[2-Nal]-[α-MeLys]-ENN-NH2; (SEQ ID NO: 973) Ac-Leu-Cyclo-[[Abu]-QTWQC]-[Phe[4-(2- aminoethoxy)]]-[2-Nal]-[α-MeLys]-ENN-NH2; (SEQ ID NO: 1042) Ac-[(D)Gln]-Cyclo-[[Abu]-QTWQC]-[Phe[4-(2- aminoethoxy)]]-[2-Nal]-[α-MeLys]-ENN-NH2; (SEQ ID NO: 842) Ac-Cyclo-[[Abu]-QTWQC]-[Phe[4-(2-aminoethoxy)]]- [2-Nal]-[α-MeLeu]-ENG-NH2; (SEQ ID NO: 972) Ac-T-Cyclo-[[Abu]-QTWQC]-[Phe[4-(2-aminoethoxy)]]- [2-Nal]-[α-MeLys]-ENN-NH2; (SEQ ID NO: 752) Ac-Cyclo-[[Abu]-QTWQC]]-[Phe[4-(2-aminoethoxy)]]- [2-Nal]-[α-MeLeu]-QN-[βAla]-NH2; (SEQ ID NO: 753) Ac-Cyclo-[[Abu]-QTWQC]]-[Phe[4-(2-aminoethoxy)]]- [2-Nal]-[Acbc]-ENN-NH2; (SEQ ID NO: 754) Ac-Cyclo-[[Abu]-QTWQC]]-[Phe[4-(2-aminoethoxy)]]- [2-Nal]-[Achc]-ENN-NH2; (SEQ ID NO: 755) Ac-Cyclo-[[Abu]-QTWQC]]-[Phe[4-(2-aminoethoxy)]]- [2-Nal]-[Acvc]-ENN-NH2; (SEQ ID NO: 979) Ac-Cyclo-[[Abu]-QTWQC]-[Phe[4-(2-aminoethoxy)]]- [2-Nal]-[4-amino-4-carboxy-piperidine]-ENN-NH2; (SEQ ID NO: 993) Ac-[(D)Arg]-Cyclo-[[Abu]-QTWQC]-[Phe[4-(2- aminoethoxy)]]-[2-Nal]-[4-amino-4-carboxy- tetrahydropyran]-ENN-NH2; or (SEQ ID NO: 980) Ac-Cyclo-[[Abu]-QTWQC]-[Phe[4-(2-aminoethoxy)]]- [2-Nal]-[4-amino-4-carboxy-tetrahydropyran]-ENN- NH2, wherein the peptide inhibitor comprises a thioether bond between the Abu and the C.

10. The peptide inhibitor of claim 1, wherein the peptide inhibitor comprises the structure of Formula I: R1-X—R2  (I) or a pharmaceutically acceptable salt or solvate thereof, wherein R1 is a bond, hydrogen, a C1-C6 alkyl, a C6-C12 aryl, a C6-C12 aryl, a C1-C6 alkyl, a C1-C20 alkanoyl, and including PEGylated versions alone or as spacers of any of the foregoing; X is the amino acid sequence; and R2 is OH or NH2.

11. A peptide inhibitor of an interleukin-23 receptor, or a pharmaceutically acceptable salt or solvate thereof, wherein the peptide inhibitor comprises the amino acid sequence of Formula Xa: X1-X2-X3-X4-X5-X6-X7-X8-X9-X10-X11-X12-X13-X14-X15-X16-X17-X18-X19-X20  (Xa) wherein X1 is any amino acid or absent; X2 is any amino acid or absent; X3 is any amino acid or absent; X4 is Pen, Cys or homo-Cys; X5 is any amino acid; X6 is any amino acid; X7 is Trp, Bip, Gln, His, Glu(Bzl), 4-Phenylbenzylalanine, Tic, Phe[4-(2-aminoethoxy)], Phe(3,4-Cl2), Phe(4-OMe), 5-Hydroxy-Trp, 6-Chloro-Trp, N-MeTrp, α-Me-Trp, 1,2,3,4-tetrahydro-norharman, Phe(4-CO2H), Phe(4-CONH2), Phe(3,4-Dimethoxy), Phe(4-CF3), Phe(4-tBu), ββ-diPheAla, Glu, Gly, Ile, Asn, Pro, Arg, Thr or Octgly, or a corresponding α-methyl amino acid form of any of the foregoing; X8 is any amino acid; X9 is Pen, Cys or hCys; X10 is 1-Nal, 2-Nal, Aic, Bip, (D)Cys, Cha, DMT, (D)Tyr, Glu, Phe, His, Trp, Thr, Tic, Tyr, 4-pyridylAla, Octgly, a Phe analog or a Tyr analog, or a corresponding α-methyl amino acid form of any of the foregoing; X11 is 2-Nal, 1-Nal, 2,4-dimethylPhe, Bip, Phe(3,4-Cl2), Phe (3,4-F2), Phe(4-CO2H), βhPhe(4-F), α-Me-Trp, 4-phenylcyclohexyl, Phe(4-CF3), α-MePhe, βhPhe, βhTyr, βhTrp, Nva(5-phenyl), Phe, His, hPhe, Tic, Tqa, Trp, Tyr, Phe(4-OMe), Phe(4-Me), Trp(2,5,7-tri-tert-Butyl), Phe(4-Oallyl), Tyr(3-tBu), Phe(4-tBu), Phe(4-guanidino, Phe(4-OBzl), Octgly, Glu(Bzl), 4-Phenylbenzylalanine, Phe[4-(2-aminoethoxy)], 5-Hydroxy-Trp, 6-Chloro-Trp, N-MeTrp, 1,2,3,4-tetrahydro-norharman, Phe(4-CONH2), Phe(3,4-OMe2) Phe(2,3-Cl2), Phe(2,3-F2), Phe(4-F), 4-phenylcyclohexylalanine or Bip, or a corresponding α-methyl amino acid form of any of the foregoing; X12 is α-MeLys, α-MeOrn, α-MeLeu, α-MeVal, 4-amino-4-carboxy-tetrahydropyran, Achc Acpc, Acbc, Acvc, MeLeu, Aib, (D)Ala, (D)Asn, (D)Leu, (D)Asp, (D)Phe, (D)Thr, 3-Pal, Aib, β-Ala, βhGlu, βhAla, βhLeu, βhVal, β-spiro-pip, Cha, Chg, Asp, Dab, Dap, α-diethylGly, Glu, Phe, hLeu, hArg, hLeu, Ile, Lys, Leu, Asn, N-MeLeu, N-MeArg, Ogl, Orn, Pro, Gln, Arg, Ser, Thr or Tle, or a corresponding α-methyl amino acid form of any of the foregoing; X13 is Lys(Ac), (D)Asn, (D)Leu, (D)Thr, (D)Phe, Ala, Aib, α-MeLeu, β-Ala, βhGlu, βhAla, βhLeu, βhVal, β-spiro-pip, Cha, Chg, Asp, Lys, Arg, Orn, Dab, Dap, α-diethylGly, Glu, Phe, hLeu, Lys, Leu, Asn, Ogl, Pro, Gln, Asp, Arg, Ser, spiro-pip, Thr, Tba, Tlc, Val or Tyr, or a corresponding α-methyl amino acid form of any of the foregoing; X14 is Asn, Glu, Phe, Gly, His, Lys, Leu, Met, Asn, Pro, Gln, Arg, Ser, Thr, Tic or Tyr, Lys(Ac), Orn or a corresponding α-methyl amino acid form of any of the foregoing; X15 is Gly, (D)Ala, (D)Asn, (D)Asp, Asn, (D)Leu, (D)Phe, (D)Thr, Ala, Asn, Ser, AEA, Asp, Glu, Phe, Gly, Lys, Leu, Pro, Gln, Arg or Ser, β-Ala, Arg or a corresponding α-methyl amino acid form of any of the foregoing; X16 is absent, Gly, Ala, Asp, Ser, Pro, Asn or Thr, or a corresponding α-methyl amino acid form of any of the foregoing; X17 is absent, Glu, Ser, Gly or Gln, or a corresponding α-methyl amino acid form of any of the foregoing; X18 is absent or any amino acid; X19 is absent or any amino acid; and X20 is absent or any amino acid, wherein the peptide inhibitor comprises a disulfide bond between X4 and X9.

12. The peptide inhibitor of claim 11, wherein both X4 and X9 are Pen.

13. The peptide inhibitor of claim 11, wherein X18 is (D)-Lys.

14. The peptide inhibitor of claim 11, comprising one or more, two or more, three or more, or four of the following: X5 is Arg, Asn, Gln, Dap, Orn; X6 is Thr or Ser; and X8 is Gln, Val, Phe, Glu, Lys.

15. The peptide inhibitor of claim 11, comprising one or more, two or more, three or more, four or more, five or more, six or more, or seven of the following: X10 is Tyr or a Phe analog; X11 is Trp, 2-Nal, 1-Nal, Phe(4-OAllyl), Tyr(3-tBu), Phe(4-tBu), Phe(4-guanidino), Phe(Bzl) or Phe(4-Me), 5-Hydroxy-Trp, 6-Chloro-Trp, N-MeTrp, α-MeTrp or 1,2,3,4-tetrahydro-norharman; X12 is Arg, α-MeLys α-MeLeu, Aib or α-MeOrn; X13 is Lys, Glu or Lys(Ac); X14 is Phe or Asn; X15 is Asn, Gly, Ser, or βAla; and X16 is absent.

16. The peptide inhibitor of claim 15, wherein X4 and X9 are Pen; X5 is Gln; X6 is Thr; X7 is Trp; X8 is Gln; X10 is Tyr or a Phe analog; X11 is Trp, 2-Nal or 1-Nal; X12 is Arg, αMeLys or α-MeOrn; X13 is Lys, Glu or Lys(Ac); X14 is Phe or Asn; X15 is Gly; and X16 is absent.

17. The peptide inhibitor of claim 11, wherein the Phe analog is Phe(3,4-F2), Phe(3,4-Cl2), Phe(3-Me), Phe[4-(2-aminoethoxy)], Phe[4-(2-(acetyl-aminoethoxy)], Phe(4-Br), Phe(4-CONH2), Phe(4-Cl), Phe(4-CN), Phe(4-guanidino), Phe(4-Me), Phe(4-NH2), Phe(4-N3), Phe(4-OMe), or Phe(4-OBzl).

18. The peptide inhibitor of claim 15, wherein the Phe analog is Phe(4-OBzl), Phe(4-OMe), Phe(4-CONH2), Phe(3,4-Cl2), Phe(4-tBu), Phe(4-NH2), Phe(4-Br), Phe(4-CN), Phe(4-CO2H), Phe(4-(2aminoethoxy)) or Phe(4-guanidino).

19. A peptide inhibitor of an interleukin-23 receptor, or a pharmaceutically acceptable salt or solvate thereof, wherein the peptide inhibitor comprises the amino acid sequence of Formula Xa: X1-X2-X3-X4-X5-X6-X7-X8-X9-X10-X11-X12-X13-X14-X15-X16-X17-X18-X19-X20  (Xa) wherein X1 is any amino acid or absent; X2 is any amino acid or absent; X3 is any amino acid or absent; X4 is Abu, Pen, or Cys; X5 is any amino acid or absent; X6 is any amino acid or absent; X7 is Trp, Bip, Gln, His, Glu(Bzl), 4-Phenylbenzylalanine, Tic, Phe[4-(2-aminoethoxy)], Phe(3,4-Cl2), Phe(4-OMe), 5-Hydroxy-Trp, 6-Chloro-Trp, N-MeTrp, α-MeTrp, 1,2,3,4-tetrahydro-norharman, Phe(4-CO2H), Phe(4-CONH2), Phe(3,4-Dimethoxy), Phe(4-CF3), ββ-diPheAla, Phe(4-tBu), Glu, Gly, Ile, Asn, Pro, Arg, Thr or Octgly, or a corresponding α-methyl amino acid form of any of the foregoing; X8 is any amino acid or absent; X9 is Abu, Pen, or Cys; X10 is 1-Nal, 2-Nal, Aic, Bip, (D)Cys, Cha, DMT, (D)Tyr, Glu, Phe, His, Trp, Thr, Tic, Tyr, 4-pyridylAla, Octgly a Phe analog or a Tyr analog, or a corresponding α-methyl amino acid form of any of the foregoing; X11 is 2-Nal, 1-Nal, 2,4-dimethylPhe, Bip, 4-phenylcyclohexyl, Glu(Bzl), 4-Phenylbenzylalanine, Tic, Phe[4-(2-aminoethoxy)], Phe(3,4-Cl2), Phe(3,4-F2), βhPhe(4-F), Phe(4-OMe), 5-Hydroxy-Trp, 6-Chloro-Trp, N-MeTrp, α-MeTrp, 1,2,3,4-tetrahydro-norharman, Phe(4-CO2H), Phe(4-CONH2), Phe(3,4-Dimethoxy), Phe(4-CF3), Phe(2,3-Cl2), Phe(2,3-F2), Phe(4-F), 4-phenylcyclohexylalanine, α-MePhe, βhPhe, βhTyr, βhTrp, Bip, Nva(5-phenyl), Phe, His, hPhe, Tqa, Trp, Tyr, Phe(4-Me), Trp(2,5,7-tri-tertButyl), Phe(4-OAllyl), Tyr(3-tBu), Phe(4-tBu), Phe(4-guanidino), Phe(4-OBzl), or Octgly, or a corresponding α-methyl amino acid form of any of the foregoing; X12 is α-MeLys, α-MeOrn, α-MeLeu, MeLeu, Aib, Achc, Acvc, Acpc, 4 amino-4-carboxy-tetrahydropyran (THP), (D)Ala, (D)Asn, (D)Leu, (D)Asp, (D)Phe, (D)Thr, 3-Pal, Aib, β-Ala, βhGlu, βhAla, βhLeu, βhVal, β-spiro-pip, Cha, Chg, Asp, Dab, Dap, α-DiethylGly, Glu, Phe, hLeu, hArg, hLeu, Ile, Lys, Leu, Asn, N-MeLeu, N-MeArg, Ogl, Orn, Pro, Gln, Arg, Ser, Thr or Tle, or a corresponding α-methyl amino acid form of any of the foregoing; X13 is Lys(Ac), (D)Asn, (D)Leu, (D)Thr, (D)Phe, Ala, Aib, α-MeLeu, βAla, βhGlu, βhAla, βhLeu, βhVal, β-spiro-pip, Cha, Chg, Asp, Arg, Orn, Dab, Dap, α-DiethylGly, Glu, Phe, hLeu, Lys, Leu, Asn, Ogl, Pro, Gln, Asp, Arg, Ser, spiro-pip, Thr, Tba, Tlc, Val or Tyr, or a corresponding α-methyl amino acid form of any of the foregoing; X14 is Asn, Glu, Phe, Gly, His, Lys, Leu, Met, Asn, Pro, Gln, Arg, Ser, Thr, Tic or Tyr, or a corresponding α-methyl amino acid form of any of the foregoing; X15 is Gly, (D)Ala, (D)Asn, (D)Asp, Asn, (D)Leu, (D)Phe, (D)Thr, Ala, (2-aminoethoxy)acetic acid (AEA), Asp, Glu, Phe, Gly, Lys, Leu, Pro, Gln, Arg or Ser, or a corresponding α-methyl amino acid form of any of the foregoing; X16 is absent, Gly, Ala, Asp, Ser, Pro, Asn or Thr, or a corresponding α-methyl amino acid form of any of the foregoing; and X17 is absent, Glu, Ser, Gly or Gln, or a corresponding α-methyl amino acid form of any of the foregoing, wherein the peptide inhibitor is cyclized via an intramolecular bond between X4 and X9.

20. The peptide inhibitor of claim 19, wherein X4 or X9 is Abu.

21. The peptide inhibitor of claim 19, comprising one or more, two or more, or three of the following: X5 is Arg, Gln, Dap or Orn; X6 is Thr or Ser; and X8 is Gln, Val, Phe, Glu or Lys.

22. The peptide inhibitor of claim 19, comprising one or more, two or more, three or more, four or more, five or more, six or more, or seven of the following: X10 is Tyr; or a Phe analog; X11 is Trp, 2-Nal, 1-Nal, Phe(4-OAllyl), Tyr(3-tBu), Phe(4-tBu), Phe(4-guanidino), Phe(4-OMe), 5-Hydroxy-Trp, 6-Chloro-Trp, N-MeTrp, α-MeTrp or 1,2,3,4-tetrahydro-norharman; X12 is Arg, hLeu, (D)Asn, Aib, α-MeLys, α-MeLeu, α-MeOrn, Achc, Acvc, Acpc, Acpc, or THP; X13 is Lys, Glu or Lys(Ac); X14 is Phe or Asn; X15 is Gly, Ser, Asn, or Ala; and X16 is absent.

23. The peptide inhibitor of claim 22, wherein the Phe analog is Phe(4-OBzl), Phe(4-OMe), Phe(4-CONH2), Phe(3,4-Cl2), Phe(4-tBu), Phe(4-NH2), Phe(4-Br), Phe(4-CN), Phe(4-CO2H), Phe(4-(2aminoethoxy)) or Phe(4-guanadino).

24. A pharmaceutical composition comprising the peptide inhibitor of any one of claims 1, 2-5, 6-11, 12-16, 19 or 10-20, and a pharmaceutically acceptable carrier, excipient, or diluent.
```

---

#### 3.3 US10023614B2 ⚠️단일소스(GP)

> **💡 핵심 요약** &nbsp;|&nbsp; **유형:** compound·물질(peptide), composition(조성물)
> 
> **무엇을 청구하나:** Formula (Xa)로 좁혀진 IL-23R 단환 펩타이드 저해제(X4=Pen, X6=Thr, X7=Trp, X8=Gln, X9=Pen 디설파이드)와 일부 이량체(DIG 링커) 화합물 및 그 의약조성물을 청구
> 
> **핵심 권리범위:** X4=Pen·X9=Pen 디설파이드 고리화 고정, X6=Thr·X7=Trp·X8=Gln; X10=2-Nal/Phe analog/Tyr, X11=1-/2-Nal 등; 개별 SEQ(예: SEQ ID NO:602/632/639/666/668) 및 DiGlycolic acid(DIG) 링커 이량체; N-말단 Acetyl·C-말단 NH2
> 
> **독립항:** 1, 21 &nbsp;|&nbsp; **적응증:** — &nbsp;|&nbsp; **검증:** ⚠️단일소스(GP) &nbsp;|&nbsp; **추정만료:** 2035-07-15


| 항목 | 내용 |
|---|---|
| 특허번호 | US10023614B2 (등록, B2) |
| 제목 | Oral peptide inhibitors of interleukin-23 receptor and their use to treat inflammatory bowel diseases |
| 출원번호 / 출원일 | 15/831,100 / 2017-12-04 (15/442,229의 계속, 14/800,627 분할 계열) |
| 우선일 | 2014-07-17 (US Provisional 62/025,899) |
| 등록일 | 2018-07-17 |
| 출원인/양수인 | Protagonist Therapeutics, Inc. |
| 발명자 | Bhandari, Bourne, Smythe (성만 표면화) |
| 권위 만료일 | **2035-07-15** (GP anticipated expiration; 출원일+20년, PTE 미반영) |
| 교차검증 | GP=21, FPO=0(미수집) → ⚠️단일소스(GP) |

**[ANALYSIS] (한국어)**

US9624268B2의 계속 계열. 청구항 1은 Formula (Xa) 단환 펩타이드(X4-X9 이황화 환화)를 정의하고 잔기 정의·약어(2-Nal, Pen, Dap 등)를 본문에 명시한다. 청구항 13~16·20은 **DiGlycolic acid(DIG) 링커로 연결된 이량체(dimer)** 형태를 청구하는 점이 특징이다. FPO 미수집이라 ⚠️단일소스(GP).

**[VERBATIM] — 출처: Google Patents (`work/05_gp_authoritative/US10023614B2.md`)**

```text
1. A peptide inhibitor of an interleukin-23 receptor, or a pharmaceutically acceptable salt thereof, comprising an amino acid sequence consisting of Formula (Xa): X1-X2-X3-X4-X5-X6-X7-X8-X9-X10-X11-X12-X13-X14-X15-X16-X17-X18-X19-X20  (Xa), wherein X1 is absent; X2 is absent; X3 is Glu, (D)Glu, Arg, (D)Arg, Phe, (D)Phe, 2-Nal, Thr, Leu, (D)Gln, or absent; X4 is Pen; X5 is Dap, Dap(Ac), Gly, Lys, Gln, Arg, Ser, Thr, or Asn; X6 is Thr; X7 is Trp; X8 is Gln; X9 is Pen; X10 is 2-Nal, a Phe analog, Tyr, or a Tyr analog; X11 is 1-Nal, 2-Nal, Phe(3,4-dimethoxy), or Phe(3,4-Cl2); X12 is Acpc, Acbc, Acvc, Achc, Aib, α-DiethylGly, α-MeLys, α-MeLys(Ac), α-MeLeu, α-MeOrn, α-MeSer, α-MeVal, Cha, Cit, hLeu, Lys, Leu, Arg, or 4-amino-4-carboxy-tetrahydropyran; X13 is Cit, Asp, Glu, Lys, Lys(Ac), Asn, or Gln; X14 is Dab(Ac), Dap(Ac), His, Lys(Ac), Asn, Gln, or Tyr; X15 is Ala, betaAla, Gly, Asn, Gln, or Ser; X16 is any amino acid or absent; X17 is any amino acid or absent; X18 is any amino acid or absent; X19 is any amino acid or absent; and X20 is any amino acid or absent, wherein the peptide inhibitor is cyclized via a disulfide bond between X4 and X9 of the amino acid sequence, and wherein 2-Nal is L-2-Naphthylalanine, Pen is L-Penicillamine, Dap is L-Diaminopropionic acid, Dap(Ac) is L-Diaminopropionic acid(Ac), 1-Nal is L-1-Naphthylalanine, Acpc is 1-aminocyclopropylcarboxylic acid, Acbc is 1-aminocyclobutanecarboxylic acid, Acvc is 1-aminocyclopentanecarboxylic acid, Achc is 1-aminocyclohexanecarboxylic acid, Aib is 2-aminoisobutyric acid, α-MeLys is alpha-methyl-L-Lysine, α-MeLys(Ac) is alpha-methyl-L-Lysine(Ac), α-MeLeu is alpha-methyl-L-Leucine, α-MeOrn is alpha-methyl-L-Ornathine, α-MeSer is alpha-methyl-L-Serine, α-MeVal is alpha-methyl-L-Valine, Cha is Cyclohexyl-L-alanine, Cit is L-Citrulline, hLeu is L-homoLeucine, Dab(Ac) is L-Diaminobutyric acid(Ac), and betaAla is Beta-alanine.

2. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1, wherein the peptide inhibitor comprises an N-terminal Acetyl group.

3. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1, wherein the peptide inhibitor comprises a C-terminal NH2 group.

4. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1, wherein X10 is a Phe analog.

5. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 4, wherein X10 is Phe(4-OMe), Phe(4-CONH2), Phe[4-(2-acetylaminoethoxy) or Phe[4-(2-aminoethoxy)].

6. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1, wherein X11 is 2-Nal.

7. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1, wherein the peptide inhibitor or pharmaceutically acceptable salt thereof is: Ac-[Pen]-QTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2-Nal]-[α-MeLeu]-[Lys(Ac)]-NN-NH2 (SEQ ID NO:602) or a pharmaceutically acceptable salt thereof, wherein the peptide inhibitor is cyclized via a disulfide bond between the Pens.

8. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1, wherein the peptide inhibitor or pharmaceutically acceptable salt thereof is: Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2-Nal]-[Aib]-[Lys(Ac)]-NN-NH2 (SEQ ID NO:632) or a pharmaceutically acceptable salt thereof, wherein the peptide inhibitor is cyclized via a disulfide bond between the Pens.

9. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1, wherein the peptide inhibitor or pharmaceutically acceptable salt thereof is: Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2-Nal]-[Aib]-[Lys(Ac)]-N-[betaAla]-NH2 (SEQ ID NO:639) or a pharmaceutically acceptable salt thereof, wherein the peptide inhibitor is cyclized via a disulfide bond between the Pens.

10. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1, wherein the peptide inhibitor or pharmaceutically acceptable salt thereof is: Ac-[Pen]-QTWQ-[Pen]-[Phe(4-OMe)]-[2-Nal]-[α-MeLys]-[Lys(Ac)]-NN-NH2 (SEQ ID NO:666) or a pharmaceutically acceptable salt thereof, wherein the peptide inhibitor is cyclized via a disulfide bond between the Pens.

11. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1, wherein the peptide inhibitor or pharmaceutically acceptable salt thereof is: Ac-[Pen]-QTWQ-[Pen]-[Phe(4-CONH2)]-[2-Nal]-[α-MeLys]-[Lys(Ac)]-NN-NH2 (SEQ ID NO:668) or a pharmaceutically acceptable salt thereof, wherein the peptide inhibitor is cyclized via a disulfide bond between the Pens.

12. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1, wherein the peptide inhibitor or pharmaceutically acceptable salt thereof is: Ac-[Pen]-QTWQ-[Pen]-[Phe(4-CONH2)]-[2-Nal]-[α-MeVal]-[Lys(Ac)]-NN-NH2 (SEQ ID NO:669) or a pharmaceutically acceptable salt thereof, wherein the peptide inhibitor is cyclized via a disulfide bond between the Pens.

13. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1, wherein the peptide inhibitor or pharmaceutically acceptable salt thereof is a dimer of two peptide monomers: Ac-[Pen]-QTWQ-[Pen]-[Phe[4-(2-acetylaminoethoxy)]-[2-Nal]-[α-MeVal]-KNN-NH2 (SEQ ID NO:530), or a pharmaceutically acceptable salt thereof, wherein each of the peptide monomers is cyclized via a disulfide bond between the Pens, and wherein the peptide monomers are linked by a DiGlycolic acid (DIG) linker.

14. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1, wherein the peptide inhibitor or pharmaceutically acceptable salt thereof is a dimer of two peptide monomers: Ac-[Pen]-QTWQ [Pen]-[Phe[4-(2-acetylaminoethoxy)]-[2-Nal]-K-[Lys(Ac)]-NN-NH2 (SEQ ID NO:531), or a pharmaceutically acceptable salt thereof, wherein each of the peptide monomers is cyclized via a disulfide bond between the Pens, and wherein the peptide monomers are linked by a DiGlycolic acid (DIG) linker.

15. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1, wherein the peptide inhibitor or pharmaceutically acceptable salt thereof is a dimer of two peptide monomers: Ac-[Pen]-QTWQ-[Pen]-[Phe(4-OMe)]-[2-Nal]-[α-MeLys]-[Lys(Ac)]-NN-NH2 (SEQ ID NO:532), or a pharmaceutically acceptable salt thereof, wherein each of the peptide monomers is cyclized via a disulfide bond between the Pens, and wherein the peptide monomers are linked by a DiGlycolic acid (DIG) linker.

16. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1, wherein the peptide inhibitor or pharmaceutically acceptable salt thereof is a dimer of two peptide monomers: Ac-[Pen]-QTWQ-[Pen]-[Phe(4-CONH2)]-[2-Nal]-[α-MeLys]-[Lys(Ac)]-NN-NH2 (SEQ ID NO:534), or a pharmaceutically acceptable salt thereof, wherein each of the peptide monomers is cyclized via a disulfide bond between the Pens, and wherein the peptide monomers are linked by a DiGlycolic acid (DIG) linker.

17. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1, wherein the peptide inhibitor or pharmaceutically acceptable salt thereof is: Ac-[(D)Phe]-[Pen]-NTWQ[Pen]-[Phe(4-OMe)]-[2-Nal]-[4-amino-4-carboxy-tetrahydropyran]-[Cit]-NN-NH2 (SEQ ID NO: 1048) or a pharmaceutically acceptable salt thereof, wherein the peptide inhibitor is cyclized via a disulfide bond between the Pens.

18. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1, wherein the peptide inhibitor or pharmaceutically acceptable salt thereof is: Ac-[(D)Phe]-[Pen]-NTWQ[Pen]-[Phe(4-OMe)]-[2-Nal]-[Achc]-ENN-NH2 (SEQ ID NO:1049) or a pharmaceutically acceptable salt thereof, wherein the peptide inhibitor is cyclized via a disulfide bond between the Pens.

19. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1, wherein the peptide inhibitor or pharmaceutically acceptable salt thereof is: Ac-[Pen]-NTWQ[Pen]-[Phe(CONH2)]-[2-Nal]-[Aib]-[Lys(Ac)]-NN-NH2 (SEQ ID NO: 1050) or a pharmaceutically acceptable salt thereof, wherein the peptide inhibitor is cyclized via a disulfide bond between the Pens.

20. The peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1, wherein the peptide inhibitor or pharmaceutically acceptable salt thereof is a dimer of two peptide monomers: Ac-[Pen]-NTWQ-[Pen]-[Phe(4-CONH2)]-[2-Nal]-[Aib]-KNN-NH2 (SEQ ID NO:535), or a pharmaceutically acceptable salt thereof, wherein each of the peptide monomers is cyclized via a disulfide bond between the Pens, and wherein the peptide monomers are linked by a DiGlycolic acid (DIG) linker.

21. A pharmaceutical composition comprising the peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1.
```

---

#### 3.4 US10941183B2 ⚠️단일소스(GP)

> **💡 핵심 요약** &nbsp;|&nbsp; **유형:** use·치료방법, compound·물질(peptide)
> 
> **무엇을 청구하나:** X4=Abu·X9=Cys 티오에터 고리화 단환 IL-23R 펩타이드 저해제를 투여해 염증성 장질환(IBD)을 치료하는 방법을 청구(용도·치료방법 특허)
> 
> **핵심 권리범위:** X4=Abu·X9=Cys 간 티오에터 고리화(QTWQC 코어); X10=Phe analog, X11=2-Nal, X12=alpha-Me-Lys/THP 등; 개별 SEQ(예: SEQ ID NO:912/980/993 등) 한정, 경구 투여; IBD = UC/Crohn's/pouchitis 치료
> 
> **독립항:** 1 &nbsp;|&nbsp; **적응증:** 염증성 장질환(IBD)/궤양성대장염/크론병/pouchitis &nbsp;|&nbsp; **검증:** ⚠️단일소스(GP) &nbsp;|&nbsp; **추정만료:** 2035-07-15


| 항목 | 내용 |
|---|---|
| 특허번호 | US10941183B2 (등록, B2) |
| 제목 | Oral peptide inhibitors of interleukin-23 receptor and their use to treat inflammatory bowel diseases |
| 출원번호 / 출원일 | 16/217,864 / 2018-12-12 |
| 우선일 | 2014-07-17 (US Provisional 62/025,899) |
| 등록일 | 2021-03-09 |
| 출원인/양수인 | Protagonist Therapeutics, Inc. |
| 권위 만료일 | **2035-07-15** (GP anticipated expiration; 출원일+20년, PTE 미반영) |
| 교차검증 | GP=20, FPO=0(미수집) → ⚠️단일소스(GP) |

**[ANALYSIS] (한국어)**

**방법(method) 청구항** 중심. 청구항 1은 Formula (Xa)에서 X4=Abu, X9=Cys, **X4-X9 티오에터(thioether) 가교**로 환화된 펩타이드를 IBD 치료에 투여하는 방법이다(앞선 이황화 가교 특허들과 가교 화학이 구별됨). 종속항은 구체 SEQ 서열·경구투여·UC/CD/pouchitis 한정이다. FPO 미수집이라 ⚠️단일소스(GP).

**[VERBATIM] — 출처: Google Patents (`work/05_gp_authoritative/US10941183B2.md`)**

```text
1. A method of treating an inflammatory bowel disease (IBD) in a subject, comprising administering to the subject an effective amount of a peptide inhibitor of an interleukin-23 receptor, or a pharmaceutically acceptable salt thereof, wherein the peptide inhibitor comprises an amino acid sequence consisting of Formula (Xa): X1-X2-X3-X4-X5-X6-X7-X8-X9-X10-X11-X12-X13-X14-X15-X16-X17-X18-X19-X20  (Xa), wherein X1 is any amino acid or absent; X2 is any amino acid or absent; X3 is any amino acid or absent; X4 is Abu; X5 is Gln; X6 is Thr; X7 is Trp; X8 is Gln; X9 is Cys; X10 is Phe, Tyr, a Phe analog, or a Tyr analog; X11 is 1-Nal, 2-Nal, Phe(3,4-dimethoxy), or Phe(3,4-Cl2); X12 is α-Me-Lys, α-Me-Leu, α-Me-Ser, α-Me-Val, Achc, Acvc, Acpc, Acbc, Aib, or 4-amino-4-carboxy-tetrahydropyran; X13 is any amino acid; X14 is any amino acid; X15 is any amino acid, X16 is any amino acid or absent; X17 is any amino acid or absent; X18 is any amino acid or absent; X19 is any amino acid or absent; and X20 is any amino acid or absent, wherein the peptide inhibitor is cyclized via a thioether bond between X4 and X9, and wherein 1-Nal is L-1-napthylalanine, 2-Nal is L-2-napthylalanine, Abu is 2-aminobutyric acid, α-Me-Lys is alpha-methyl-L-Lysine, α-Me-Leu is alpha-methyl-L-Leucine, α-Me-Ser is alpha-methyl-L-Serine, α-Me-Val is alpha-methyl-L-Valine, Achc is 1-aminocyclohexanecarboxylic acid, Acvc is 1-aminocyclopentanecarboxylic acid, Acpc is 1-aminocyclopropylcarboxylic acid, Acbc is 1-aminocyclobutanecarboxylic acid, and Aib is 2-aminoisobutyric acid.

2. The method of claim 1, wherein the peptide inhibitor comprises an N-terminal Ac group and a C-terminal NH2 group.

3. The method of claim 1, wherein X3 is selected from Glu, (D)Glu, Arg, (D)Arg, Phe, (D)Phe, 2-Nal, Thr, Leu, or (D)Gln.

4. The method of claim 1, wherein X10 is Phe(4-OMe), Phe(4-CONH2), or Phe[4-(2-aminoethoxy)].

5. The method of claim 1, wherein X11 is 2-Nal.

6. The method of claim 1, wherein the peptide inhibitor or pharmaceutically acceptable salt thereof is: Ac-[Abu]-QTWQCY-[2-Nal]-[α-Me-Lys]-ENG-NH2 (SEQ ID NO:704); Ac-[Abu]-QTWQC-[Phe(4-OMe)]-[2-Nal]-[α-Me-Lys]-ENG-NH2 (SEQ ID NO:702); Ac-[Abu]-QTWQC-[Phe[4-(2-aminoethoxy)]]-[2-Nal]-[α-Me-Lys]-[Lys(isovaleric acid)]-NG-NH2 (SEQ ID NO:861); Ac-[Abu]-QTWQC-[Phe[4-(2-aminoethoxy)]]-[2-Nal]-[Aib]-QNG-NH2 (SEQ ID NO:877); or Ac-[Abu]-QTWQC-[Phe[4-(2-aminoethoxy)]]-[2-Nal]-[Aib]-[Lys(Ac)]-NA-NH2 (SEQ ID NO:880); or a pharmaceutically acceptable salt thereof, wherein the peptide inhibitor is cyclized via a thioether bond between Abu and C.

7. The method of claim 1, wherein the peptide inhibitor or pharmaceutically acceptable salt thereof is: Ac-[Abu]-QTWQC-[Phe[4-(2-(acetyl-aminoethoxy)]]-[2-Nal]-[α-Me-Lys(Ac)]-[Lys(Ac)]-NG-NH2 (SEQ ID NO:900); Ac-[Abu]-QTWQC-[Phe[4-(2-aminoethoxy)]]-[2-Nal]-[α-Me-Lys]-ENQ-NH2 (SEQ ID NO:911); Ac-[Abu]-QTWQC-[Phe[4-(2-aminoethoxy)]]-[2-Nal]-[α-Me-Lys]-ENN-NH2 (SEQ ID NO:912); Ac-[Abu]-QTWQC-[Phe[4-(2-aminoethoxy)]]-[2-Nal]-[α-MeVal]-[Lys(Ac)]-NG-NH2 (SEQ ID NO:915); or Ac-[(D)Phe]-[Abu]-QTWQC-[Phe[4-(2-aminoethoxy)]]-[2-Nal]-[α-Me-Lys]-ENN-NH2 (SEQ ID NO:970) or a pharmaceutically acceptable salt thereof, wherein the peptide inhibitor is cyclized via a thioether bond between Abu and C.

8. The method of claim 1, wherein the peptide inhibitor or pharmaceutically acceptable salt thereof is: Ac-[Abu]-QTWQC-[Phe[4-(2-aminoethoxy)]]-[2-Nal]-[α-Me-Leu)-[Cit]-NN-NH2 (SEQ ID NO:954) or a pharmaceutically acceptable salt thereof, wherein the peptide inhibitor is cyclized via a thioether bond between Abu and C.

9. The method of claim 1, wherein the peptide inhibitor or pharmaceutically acceptable salt thereof is: Ac-T-[Abu]-QTWQC-[Phe[4-(2-aminoethoxy)]]-[2-Nal]-[α-Me-Lys]-ENN-NH2 (SEQ ID NO:972) or a pharmaceutically acceptable salt thereof, wherein the peptide inhibitor is cyclized via a thioether bond between Abu and C.

10. The method of claim 1, wherein the peptide inhibitor or pharmaceutically acceptable salt thereof is: Ac-[Abu]-QTWQC-[Phe[4-(2-aminoethoxy)]]-[2-Nal]-[acbc]-ENN-NH2 (SEQ ID NO:976) or a pharmaceutically acceptable salt thereof, wherein the peptide inhibitor is cyclized via a thioether bond between Abu and C.

11. The method of claim 1, wherein the peptide inhibitor or pharmaceutically acceptable salt thereof is: Ac-[Abu]-QTWQC-[Phe[4-(2-aminoethoxy)]]-[2-Nal]-[acpc]-ENN-NH2 (SEQ ID NO:1043) or a pharmaceutically acceptable salt thereof, wherein the peptide inhibitor is cyclized via a thioether bond between Abu and C.

12. The method of claim 1, wherein the peptide inhibitor or pharmaceutically acceptable salt thereof is: Ac-[Abu]-QTWQC-[Phe[4-(2-aminoethoxy)]]-[2-Nal]-[achc]-ENN-NH2 (SEQ ID NO: 977) or a pharmaceutically acceptable salt thereof, wherein the peptide inhibitor is cyclized via a thioether bond between Abu and C.

13. The method of claim 1, wherein the peptide inhibitor or pharmaceutically acceptable salt thereof is: Ac-[Abu]-QTWQC-[Phe[4-(2-aminoethoxy)]]-[2-Nal]-[4-amino-4-carboxy-tetrahydropyran]-ENN-NH2 (SEQ ID NO:980) or a pharmaceutically acceptable salt thereof, wherein the peptide inhibitor is cyclized via a thioether bond between Abu and C.

14. The method of claim 1, wherein the peptide inhibitor or pharmaceutically acceptable salt thereof is: Ac-[Abu]-QTWQC-[Phe[4-(2-aminoethoxy)]]-[2-Nal]-[alpha-methyl-L-Leucine]-QN-[betaAla]-NH2 (SEQ ID NO:984) or a pharmaceutically acceptable salt thereof, wherein the peptide inhibitor is cyclized via a thioether bond between Abu and C.

15. The method of claim 1, wherein the peptide inhibitor or pharmaceutically acceptable salt thereof is: Ac-(D)Phe-[Abu]-QTWQC-[Phe[4-(2-aminoethoxy)]]-[2-Nal]-[4-amino-4-carboxy-tetrahydropyran]-ENN-NH2 (SEQ ID NO:992) or a pharmaceutically acceptable salt thereof, wherein the peptide inhibitor is cyclized via a thioether bond between Abu and C.

16. The method of claim 1, wherein the peptide inhibitor or pharmaceutically acceptable salt thereof is: Ac-[(D)Arg]-[Abu]-QTWQC-[Phe[4-(2-aminoethoxy)]]-[2-Nal]-[4-amino-4-carboxy-tetrahydropyran]-ENN-NH2 (SEQ ID NO:993) or a pharmaceutically acceptable salt thereof, wherein the peptide inhibitor is cyclized via a thioether bond between Abu and C.

17. The method of claim 1, wherein the peptide inhibitor or pharmaceutically acceptable salt thereof is administered to the subject by oral administration.

18. The method of claim 1, wherein the IBD is ulcerative colitis.

19. The method of claim 1, wherein the IBD is Crohn's disease.

20. The method of claim 1, wherein the IBD is pouchitis after an ileoanal anastomosis.
```

---

#### 3.5 US11884748B2 ⚠️단일소스(GP)

| 항목 | 내용 |
|---|---|
| 특허번호 | US11884748B2 (등록, B2) |
| 제목 | Oral peptide inhibitors of interleukin-23 receptor and their use to treat inflammatory bowel diseases |
| 출원번호 / 출원일 | 17/161,370 / 2021-01-28 |
| 우선일 | 2014-07-17 (US Provisional 62/025,899) |
| 등록일 | 2024-01-30 |
| 출원인/양수인 | Protagonist Therapeutics, Inc. |
| 권위 만료일 | **2035-07-15** (GP anticipated expiration; 출원일+20년, PTE 미반영) |
| 교차검증 | GP=21, FPO=0(미수집) → ⚠️단일소스(GP) |

**[ANALYSIS] (한국어)**

**조성물(composition) 청구항** 중심. 청구항 1은 다수 SEQ ID NO(702, 704, 782, 861, 877, 880 등) 서열군을 함유한 약학 조성물이며, X4=Abu와 C 간 티오에터 가교로 환화된다. 원문에 `[Abta]`, `AiN`, `[AibMLys(Ac)]` 등 파싱 잔재가 그대로 남아 있어 원문 보존 원칙에 따라 손대지 않는다. FPO 미수집이라 ⚠️단일소스(GP).

**[VERBATIM] — 출처: Google Patents (`work/05_gp_authoritative/US11884748B2.md`)**

```text
1. A pharmaceutical composition comprising a peptide inhibitor of an interleukin-23 receptor, or a pharmaceutically acceptable salt thereof, and a pharmaceutically acceptable carrier, excipient, or diluent, wherein the peptide inhibitor of an interleukin-23 receptor is selected from the group consisting of: (SEQ ID NO: 702) Ac-[Abta]-QTWQC-[Phe(4-OMe)]-[2-Nal]-[α-Me-Lys]- ENG-NH2;  (SEQ ID NO: 704) Ac-[Abta]-QTWQCY-[2-Nal]-[α-Me-Lys]-ENG-NH2;  (SEQ ID NO: 782) Ac-[Abu]-QTWQC-[Phe[4-(2-aminoethoxy)]-W- [α-Me-Lys]-ENG-NH2; (SEQ ID NO: 861) Ac-[Abta]-QTWQC-[Phe[4-(2-aminoethoxy)]]-[2-Nal]- [α-Me-Lys]-[Lys(isovaleric acid)]-NG-NH2;  (SEQ ID NO: 877) Ac-[Abu]-QTWQC-[Phe[4-(2-aminoethoxy)]]-[2-Nal] AiN-QNG-NH2; (SEQ ID NO: 880) Ac-[Abu]-QTWQC-[Phe[4-(2-aminoethoxy)]]-[2-Nal]- [AibMLys(Ac)]-NA-NH2;  (SEQ ID NO: 900) Ac-[Abu]-QTWQC-[Phe[4-(2-(acetyl-aminoethoxy)]]- [2-Nal]-[α-Me-Lys(Ac)]-[Lys(Ac)]-NG-NH2;  (SEQ ID NO: 911) Ac-[Abta]-QTWQC-[Phe[4-(2-aminoethoxy)]]-[2-Nal]- [α-Me-Lys]-ENQ-NH2;  (SEQ ID NO: 912) Ac-[Abta]-QTWQC-[Phe[4-(2-aminoethoxy)]]-[2-Nal]- [α-Me-Lys]-ENN-NH2;  (SEQ ID NO: 915) Ac-[Abta]-QTWQC-[Phe[4-(2-aminoethoxy)]]-[2-Nal]- [α-MeVal]-[Lys(Ac)]-NG-NH2; (SEQ ID NO: 954) Ac-[Abu]-QTWQC-[Phe[4-(2-aminoethoxy)]]-[2-Nal]- [α-Me-Leu]-[Cit]-NN-NH2;  (SEQ ID NO: 970) Ac-[(D)Phe]-[Abu]-QTWQC-[Phe[4-(2-aminoethoxy)]]- [2-Nal]-[α-Me-Lys]-ENN-NH2;  (SEQ ID NO: 972) Ac-T-[Abu]-QTWQC-[Phe[4-(2-aminoethoxy)]]-[2-Nal]- [α-Me-Lys]-ENN-NH2;  (SEQ ID NO: 976) Ac-[Abu]-QTWQC-[Phe[4-(2-aminoethoxy)]]- [2-Nal]-[acbc]-ENN-NH2; (SEQ ID NO: 980) Ac-[Abu]-QTWQC-[Phe[4-(2-aminoethoxy)]]- [2-Nal]-[4-amino-4-carboxy-tetrahydropyran]- ENN-NH2; (SEQ ID NO: 984) Ac-[Abu]-QTWQC-[Phe[4-(2-aminoethoxy)]]-[2-Nal]- [alphα-methyl-L-Leucine]-QN-[betaAla]-NH2; (SEQ ID NO: 992) Ac-(D)Phe-[Abu]-QTWQC-[Phe[4-(2-aminoethoxy)]]- [2-Nal]-[4-amino-4-carboxy-tetrahydropyran]-  ENN-NH2; (SEQ ID NO: 993) Ac-[(D)Arg]-[Abu]-QTWQC-[Phe[4-(2-aminoethoxy)]]- [2-Nal]-[4-amino-4-carboxy-tetrahydropyran]- ENN-NH2;  (SEQ ID NO: 1043)  Ac-[Abu]-QTWQC-[Phe[4-(2-aminoethoxy)]]-[2-Nal]- [acpc]-ENN-NH2;  or (SEQ ID NO: 1047) Ac-[Abu]-QTWQC-[Phe[4-(2-aminoethoxy)]]-[2-Nal] achc]-ENN-NH2; wherein the peptide inhibitor is cyclized via a thioether bond between Abu and C.

2. The pharmaceutical composition of claim 1, wherein the peptide inhibitor of an interleukin-23 receptor is: Ac-[Abu]-QTWQC-[Phe(4-OMe)]-[2-Nal]-[α-Me-Lys]-ENG-NH2 (SEQ ID NO:702) or a pharmaceutically acceptable salt thereof; wherein the peptide inhibitor is cyclized via a thioether bond between Abu and C.

3. The pharmaceutical composition of claim 1, wherein the peptide inhibitor of an interleukin-23 receptor is: Ac-[Abu]-QTWQCY-[2-Nal]-[a-Me-Lys]-ENG-NH2 (SEQ ID NO:704) or a pharmaceutically acceptable salt thereof; wherein the peptide inhibitor is cyclized via a thioether bond between Abu and C.

4. The pharmaceutical composition of claim 1, wherein the peptide inhibitor of an interleukin-23 receptor is: Ac-[Abu]-QTWQC-[Phe[4-(2-aminoethoxy)]-W-[α-Me-Lys]-ENG-NH2 (SEQ ID NO:782) or a pharmaceutically acceptable salt thereof; wherein the peptide inhibitor is cyclized via a thioether bond between Abu and C.

5. The pharmaceutical composition of claim 1, wherein the peptide inhibitor of an interleukin-23 receptor is: Ac-[Abu]-QTWQC-[Phe[4-(2-aminoethoxy)]]-[2-Nal]-[α-Me-Lys]-[Lys(isovaleric acid)]-NG-NH2 (SEQ ID NO:861) or a pharmaceutically acceptable salt thereof; wherein the peptide inhibitor is cyclized via a thioether bond between Abu and C.

6. The pharmaceutical composition of claim 1, wherein the peptide inhibitor of an interleukin-23 receptor is: Ac-[Abu]-QTWQC-[Phe[4-(2-aminoethoxy)]]-[2-Nal]-[Aib]-QNG-NH2 (SEQ ID NO:877) or a pharmaceutically acceptable salt thereof; wherein the peptide inhibitor is cyclized via a thioether bond between Abu and C.

7. The pharmaceutical composition of claim 1, wherein the peptide inhibitor of an interleukin-23 receptor is: Ac-[Abu]-QTWQC-[Phe[4-(2-aminoethoxy)]]-[2-Nal]-[Aib]-[Lys(Ac)]-NA-NH2 (SEQ ID NO:880) or a pharmaceutically acceptable salt thereof; wherein the peptide inhibitor is cyclized via a thioether bond between Abu and C.

8. The pharmaceutical composition of claim 1, wherein the peptide inhibitor of an interleukin-23 receptor is: Ac-[Abu]-QTWQC-[Phe[4-(2-(acetyl-aminoethoxy)]]-[2-Nal]-[α-Me-Lys(Ac)]-[Lys(Ac)]-NG-NH2 (SEQ ID NO:900) or a pharmaceutically acceptable salt thereof; wherein the peptide inhibitor is cyclized via a thioether bond between Abu and C.

9. The pharmaceutical composition of claim 1, wherein the peptide inhibitor of an interleukin-23 receptor is: Ac-[Abu]-QTWQC-[Phe[4-(2-aminoethoxy)]]-[2-Nal]-[α-Me-Lys]-ENQ-NH2 (SEQ ID NO:911) or a pharmaceutically acceptable salt thereof; wherein the peptide inhibitor is cyclized via a thioether bond between Abu and C.

10. The pharmaceutical composition of claim 1, wherein the peptide inhibitor of an interleukin-23 receptor is: Ac-[Abu]-QTWQC-[Phe[4-(2-aminoethoxy)]]-[2-Nal]-[α-Me-Lys]-ENN-NH2 (SEQ ID NO:912) or a pharmaceutically acceptable salt thereof; wherein the peptide inhibitor is cyclized via a thioether bond between Abu and C.

11. The pharmaceutical composition of claim 1, wherein the peptide inhibitor of an interleukin-23 receptor is: Ac-[Abu]-QTWQC-[Phe[4-(2-aminoethoxy)]]-[2-Nal]-[α-MeVal]-[Lys(Ac)]-NG-NH2 (SEQ ID NO:915) or a pharmaceutically acceptable salt thereof; wherein the peptide inhibitor is cyclized via a thioether bond between Abu and C.

12. The pharmaceutical composition of claim 1, wherein the peptide inhibitor of an interleukin-23 receptor is: Ac-[Abu]-QTWQC-[Phe[4-(2-aminoethoxy)]]-8 2-Nal]-[α-Me-Leu]-[Cit]-NN-NH2 (SEQ ID NO:954) or a pharmaceutically acceptable salt thereof; wherein the peptide inhibitor is cyclized via a thioether bond between Abu and C.

13. The pharmaceutical composition of claim 1, wherein the peptide inhibitor of an interleukin-23 receptor is: Ac-[(D)Phe]-[Abu]-QTWQC-[Phe[4-(2-aminoethoxy)]]-[2-Nal]-[α-Me-Lys]-ENN-NH2 (SEQ ID NO: 970) or a pharmaceutically acceptable salt thereof; wherein the peptide inhibitor is cyclized via a thioether bond between Abu and C.

14. The pharmaceutical composition of claim 1, wherein the peptide inhibitor of an interleukin-23 receptor is: Ac-T-[Abu]-QTWQC-[Phe[4-(2-aminoethoxy)]]-[2-Nal]-[α-Me-Lys]-ENN-NH2 (SEQ ID NO:972) or a pharmaceutically acceptable salt thereof; wherein the peptide inhibitor is cyclized via a thioether bond between Abu and C.

15. The pharmaceutical composition of claim 1, wherein the peptide inhibitor of an interleukin-23 receptor is: Ac-[Abu]-QTWQC-[Phe[4-(2-aminoethoxy)]]-[2-Nal]acbc]-ENN-NH2 (SEQ ID NO:976) or a pharmaceutically acceptable salt thereof; wherein the peptide inhibitor is cyclized via a thioether bond between Abu and C.

16. The pharmaceutical composition of claim 1, wherein the peptide inhibitor of an interleukin-23 receptor is: Ac-[Abu]-QTWQC-[Phe [4-(2-aminoethoxy)]]-[2-Nal]-[4-amino-4-carboxy-tetrahydropyran]-ENN-NH2 (SEQ ID NO:980) or a pharmaceutically acceptable salt thereof; wherein the peptide inhibitor is cyclized via a thioether bond between Abu and C.

17. The pharmaceutical composition of claim 1, wherein the peptide inhibitor of an interleukin-23 receptor is: Ac-[Abu]-QTWQC-[Phe [4-(2-aminoethoxy)]]-[2-Nal]-[alpha-methyl-L-Leucine]-QN-[betaAla]-NH2 (SEQ ID NO:984) or a pharmaceutically acceptable salt thereof; wherein the peptide inhibitor is cyclized via a thioether bond between Abu and C.

18. The pharmaceutical composition of claim 1, wherein the peptide inhibitor of an interleukin-23 receptor is: Ac-(D)Phe-[Abu]-QTWQC-[Phe[4-(2-aminoethoxy)]]-[2-Nal]-[4-amino-4-carboxy-tetrahydropyran]-ENN-NH2 (SEQ ID NO:992) or a pharmaceutically acceptable salt thereof; wherein the peptide inhibitor is cyclized via a thioether bond between Abu and C.

19. The pharmaceutical composition of claim 1, wherein the peptide inhibitor of an interleukin-23 receptor is: Ac-[(D)Arg]-[Abu]-QTWQC-[Phe[4-(2-aminoethoxy)]]-[2-Nal]-[4-amino-4-carboxy-tetrahydropyran]-ENN-NH2 (SEQ ID NO:993) or a pharmaceutically acceptable salt thereof, wherein the peptide inhibitor is cyclized via a thioether bond between Abu and C.

20. The pharmaceutical composition of claim 1, wherein the peptide inhibitor of an interleukin-23 receptor is: Ac-[Abu]-QTWQC-[Phe[4-(2-aminoethoxy)]]-[2-Nal]acpc]- ENN-NH2 (SEQ ID NO:1043) or a pharmaceutically acceptable salt thereof, wherein the peptide inhibitor is cyclized via a thioether bond between Abu and C.

21. The pharmaceutical composition of claim 1, wherein the peptide inhibitor of an interleukin-23 receptor is: Ac-[Abu]-QTWQC-[Phe[4-(2-aminoethoxy)]]-[2-Nal]achc]-ENN-NH2 (SEQ ID NO:1047) or a pharmaceutically acceptable salt thereof, wherein the peptide inhibitor is cyclized via a thioether bond between Abu and C.
```

---

#### 3.6 WO2016011208A1 ⚠️단일소스(GP)

> **💡 핵심 요약** &nbsp;|&nbsp; **유형:** compound·물질(peptide), composition(조성물), use·치료방법
> 
> **무엇을 청구하나:** IL-23R 단환 펩타이드 저해제를 20잔기 Formula (Xa)의 매우 광범위한 1세대 Markush(X4-X9 고리화)로 청구하고, 펩타이드 이량체·의약조성물·IBD/건선 등 치료방법·DSS/TNBS 평가법까지 포괄(패밀리 시초 물질특허, PTG-200 기반)
> 
> **핵심 권리범위:** X1~X20 광범위 Markush, X4-X9 디설파이드/티오에터/락탐/트리아졸/올레핀 등 고리화; Pen-Pen 디설파이드 및 Abu-Cys 티오에터 하위군과 다수 개별 서열; 펩타이드 이량체(linker) 청구; IL-23의 IL-23R 결합 저해; DSS/TNBS 동물모델 평가법 포함
> 
> **독립항:** 1, 36, 44, 47, 52 &nbsp;|&nbsp; **적응증:** IBD/UC/CD/건선/건선성관절염 등 다수 염증질환 &nbsp;|&nbsp; **검증:** ⚠️단일소스(GP) &nbsp;|&nbsp; **추정만료:** PCT(term N/A)


| 항목 | 내용 |
|---|---|
| 특허번호 | WO2016011208A1 (PCT 공개, A1) |
| 제목 | ORAL PEPTIDE INHIBITORS OF INTERLEUKIN-23 RECEPTOR AND THEIR USE TO TREAT INFLAMMATORY BOWEL DISEASES |
| 국제출원 / 공개 | PCT/US2015/040658, 국제출원일 2015-07-15 |
| 우선일 | 2014-07-17 (US Provisional 62/025,899) |
| 출원인/양수인 | Protagonist Therapeutics, Inc. |
| 발명자 | Dinesh V. Patel, David Liu |
| 권위 만료일 | PCT 자체 만료 **N/A**; 추정 국내단계 2034~2035 (우선일/출원일+20년) |
| 교차검증 | GP=52, FPO=0(미수집) → ⚠️단일소스(GP) |

**[ANALYSIS] (한국어)**

Protagonist 경구 IL-23R 프로그램의 **최초 기초 PCT**. 청구항 1은 Formula (Xa)의 가장 넓은 속(X4/X9 = '결합 형성 가능한 임의 아미노산/화학 모이어티')이며, 이후 청구항에서 점진적으로 한정된다. 청구항 52~54는 후보 화합물 스크리닝 방법(항-IL-23p19 항체 양성대조 등)이다. FPO 미수집이라 ⚠️단일소스(GP).

**[VERBATIM] — 출처: Google Patents (`work/05_gp_authoritative/WO2016011208A1.md`)**

```text
1. A peptide inhibitor of an interleukin-23 receptor, or a pharmaceutically acceptable salt or solvate thereof, wherein the peptide inhibitor comprises an amino acid sequence of Formula (Xa): Xl-X2-X3-X4-X5-X6-X7-X8-X9-X10-Xl l-X12-X13-X14-X15-X16-X17-X18-X19-X20 (Xa) wherein XI is any amino acid or absent; X2 is any amino acid or absent; X3 is any amino acid or absent; X4 is any amino acid or chemical moiety capable of forming a bond with X9; X5 is any amino acid; X6 is any amino acid; X7 is any amino acid; X8 is any amino acid; X9 is any amino acid or chemical moiety capable of forming a bond with X4; XI 0 is any amino acid; XI I is any amino acid; XI 2 is any amino acid; XI 3 is any amino acid; XI 4 is any amino acid; XI 5 is any amino acid, XI 6 is any amino acid or absent; XI 7 is any amino acid or absent; XI 8 is any amino acid or absent; XI 9 is any amino acid or absent; and X20 is any amino acid or absent, wherein the peptide inhibitor is cyclized via a bond between X4 and X9, and wherein the peptide inhibitor inhibits the binding of an interleukin-23 (IL-23) to an IL-23 receptor.

2. The peptide inhibitor of claim 1, wherein: XI is absent; X2 is absent; X3 is absent; X4 is Cys, Abu or Pen; X5 is Ala, a-MeOrn, a-MeSer, Cit, Dap, Dab, Dap(Ac), Gly, Lys, Asn, N-MeGln, N-MeArg, Orn, Gin, Arg, Ser or Thr; X6 is Asp or Thr; X7 is Trp or 6-Chloro-Trp; X8 is Glu, Gin or Val; X9 is Cys, Abu or Pen; XI 0 is 2-Nal, a Phe analog, Tyr, or a Tyr analog; XI I is 1-Nal, 2-Nal, Phe(3,4-dimethoxy), 5-HydroxyTrp, Phe(3,4-Cl2), Trp or Tyr(3-tBu); X12 is 3-Pal, Acpc, Acbc, Acvc, Ache, Agp, Aib, a-DiethylGly, a-MeLys, a-MeLys(Ac), a- MeLeu, a- a-MeOrn, a-MeSer, a-MeVal, Cav, Cha, Cit, Cpa, D-Asn, Glu, His, hLeu, hArg, Lys, Leu, Octgly, Orn, 4-amino-4-carboxy-piperidine, Arg, Ser, Thr or THP; XI 3 is Cit, Asp, Dab, Dap, Phe, His, Dap(Peg2-Ac), Dap(pyroglutaric acid), Glu, HArg, Lys, Lys(Ac), Lys(Benzoic acid), Lys(glutaric acid), Lys(IVA), Lys(Peg4-isoGlu-Palm), Lys(pyroglutaric acid), Lys(succinic acid), Asn, Orn,Gln, Arg, Thr or Val; X14 is Asp, Dab(Ac), Dap(Ac), Phe, His, Lys(Ac), Met, Asn(isobutyl), Gin, Arg, Tyr or Asp(l ,4-diaminobutane); and XI 5 is Ala, pAla, Glu, Gly, Asn, Gin, Arg or Ser.

3. The peptide inhibitor of claiml, wherein: XI is absent; X2 is absent; X3 is absent; X4 is Cys, Abu or Pen; X5 is Ala, a-MeOrn, a-MeSer, Cit, Dap, Dab, Dap(Ac), Gly, Lys, Asn, Orn, Gin, Arg, Ser or Thr; X6 is Asp or Thr; X7 is Trp or 6-Chloro-Trp; X8 is Gin or Val; X9 is Cys, Abu or Pen; XI 0 is 2-Nal, a Phe analog, Tyr, or a Tyr analog,; XI 1 is 1-Nal, 2-Nal, Phe(3,4-dimethoxy), 5-HydroxyTrp, Phe(3,4-Cl2), Trp or Tyr(3-tBu); X12 is 3-Pal, Acpc, Acbc, Acvc, Ache, Agp, Aib, a-DiethylGly, a-MeLys, a-MeLys(Ac), a- MeLeu, a-MeOrn, a-MeSer, a-MeVal, Cav, Cha, Cit, Cpa, D-Asn, His, hLeu, hArg, Lys, Leu, Octgly, Orn, 4-amino-4-carboxy-piperidine, or THP; XI 3 is Cit, Asp, Dab, Dap, Phe, His, Dap(Peg2-Ac), Dap(pyroglutaric acid), Glu, hArg, Lys, Lys(Ac), Lys(Benzoic acid), Lys(glutaric acid), Lys(IVA), Lys(Peg4-isoGlu-Palm), Lys(pyroglutaric acid), Lys(succinic acid), Asn, Orn,Gln, Arg, Thr or Val; X14 is Dab(Ac), Dap(Ac), Phe, His, Lys(Ac), Met, Asn, Gin, Arg, or Tyr; and XI 5 is Ala, pAla, Gly, Asn, Gin, or Ser.

4. The peptide inhibitor of claim 1, wherein: XI is absent; X2 is absent; X3 is absent; X4 is Cys, Abu or Pen; X5 is Dap, Dap(Ac), Gly, Lys, Gin, Arg, Ser,Thr or Asn; X6 is Thr; X7 is Trp or 6-Chloro-Trp; X8 is Gin; X9 is Cys, Abu or Pen; XI 0 is 2-Nal, a Phe analog, Tyr, or a Tyr analog; XI 1 is 1-Nal, 2-Nal, Phe(3,4-dimethoxy), Phe(3,4-Cl2), or Trp; X12 is Acpc, Acbc, Acvc, Ache, Aib, a-MeGly(diethyl), a-MeLys, a-MeLys(Ac), a-MeLeu, a- MeOrn, a-MeSer, a-MeVal, Cha, Cit, homoLeu, Lys, Leu, Arg or THP; XI 3 is Cit, Asp, Dap, Dap(Peg2-Ac), Dap(pyroglutaric acid), Glu, HArg, Lys, Lys(Ac), Lys(Benzoic acid), Lys(glutaric acid), Lys(IVA), Lys(Peg4-isoGlu-Palm), Lys(pyroglutaric acid), Lys-succinic acid, Asn, Orn,Gln, Arg, or Val; X14 is Dab(Ac), Dap(Ac), His, Lys(Ac), Asn, Gin, or Tyr; and XI 5 is Ala, pAla, Gly, Asn, Gin, or Ser.

5. The peptide inhibitor of claim 1, wherein: XI is absent; X2 is absent; X3 is absent; X4 is Cys, Abu or Pen; X5 is Dap, Dap(Ac), Gin, Ser, Thr or Asn; X6 is Thr; X7 is Trp; X8 is Gin; X9 is Cys, Abu or Pen; XI 0 is a Phe analog, Tyr, or a Tyr analog; XI I is 2-Nal or Trp; X12 is Acpc, Acbc, Acvc, Ache, Aib, a-DiethylGly, a-MeLys, a-MeLys(Ac), a-MeLeu, a- MeOrn, a-MeSer, a-MeVal, hLeu, Leu, or THP; XI 3 is Cit, Asp, Glu, Lys, Lys(Ac), Asn, or Gin; XI 4 is Dab(Ac), Asn, or His; and XI 5 is Ala, betaAla, Gly, Asn, or Gin.

6. The peptide inhibitor of claim 1, wherein X4 is Cys, Pen, hCys, D-Pen, D-Cys, D-hCys, Met, Glu, Asp, Lys, Orn, Dap, Dab, D-Dap, D- Dab, D-Asp, D-Glu, D-Lys, Sec, 2-chloromethylbenzoic acid, mercapto-propanoic acid, mercapto-butyric acid, 2-chloro-acetic acid, 3-choro-propanoic acid, 4-chloro-butyric acid, 3- chloro-isobutyric acid, Abu, β-azido-Ala-OH, propargylglycine, 2-(3'-butenyl)glycine, 2- allylglycine, 2-(3'-butenyl)glycine, 2-(4'-pentenyl)glycine, 2-(5'-hexenyl)glycine, or Abu; X7 is Trp, Glu, Gly, He, Asn, Pro, Arg, Thr or OctGly, or a corresponding a-methyl amino acid form of any of the foregoing; X9 is Cys, Pen, hCys, D-Pen, D-Cys, D-hCys, Glu, Lys, Orn, Dap, Dab, D-Dap, D-Dab, D-Asp, D-Glu, D-Lys, Asp, Leu, Val, Phe, or Ser, Sec, Abu, β-azido-Ala-OH, propargylglycine, 2-2- allylglycine, 2-(3'-butenyl)glycine, 2-(4'-pentenyl)glycine, Ala, hCys, Abu, Met, MeCys, (D)Tyr or 2-(5'-hexenyl)glycine; XI 0 is Tyr, Phe(4-OMe), 1-Nal, 2-Nal, Aic, a-MePhe, Bip, (D)Cys, Cha, DMT, (D)Tyr, Glu, His, hPhe(3,4-dimethoxy), hTyr, N-Me-Tyr, Trp, Phe(4-CONH2), Phe(4-phenoxy), Thr, Tic, Tyr(3-tBu), Phe(4-tBu), Phe(4-CN), Phe(4-Br), Phe(4-NH2), Phe(4-F), Phe(3,5-F2), Phe(4- CH2C02H), Phe(penta-F), Phe(3,4-Cl2), Phe(4-CF3), Phe(4-OCH3), Bip, Cha, 4-PyridylAlanine, PhTyr, OctGly, Phe(4-N3), Phe(4-Br), Phe[4-(2-aminoethoxy)] or Phe, a Phe analog, a Tyr analog, or a corresponding a-methyl amino acid form of any of the foregoing; XI 1 is 2-Nal, 1-Nal, 2,4-dimethylPhe, Bip, Phe(3,4-Cl2), Phe (3,4-F2), Phe(4-C02H), phPhe(4- F), a-Me-Trp, 4-phenylcyclohexyl, Phe(4-CF3), a-MePhe, phNal, phPhe, phTyr, phTrp, Nva(5- phenyl), Phe, His, hPhe, Tic, Tqa, Trp, Tyr, Phe(4-OMe), Phe(4-Me), Trp(2,5,7-tri-tert-Butyl), Phe(4-Oallyl), Tyr(3-tBu), Phe(4-tBu), Phe(4-guanidino, Phe(4-OBzl), Octgly, Glu(Bzl), 4- Phenylbenzylalanine, Phe[4-(2-aminoethoxy)], 5-Hydroxy-Trp, 6-Chloro-Trp, N-MeTrp, 1,2,3,4-tetrahydro-norharman, Phe(4-CONH2), Phe(3,4-Dimethoxy), Phe(2,3-Cl2), Phe(2,3-F2), Phe(4-F), 4-phenylcyclohexylalanine, Bip, or a corresponding α-methyl amino acid form of any of the foregoing; X12 is His, Phe, Arg, N-Me-His, Val, Cav, Cpa, Leu, Cit, hLeu, 3-Pal, t-butyl-Ala, 4-amino-4- carboxy-tetrahydropyran, Ache Acpc, Acbc, Acvc, Agp, Aib, a-DiethylGly, a-MeLys, a- MeLys(Ac), a-Me-Leu, a-MeOrn, a-MeSer, a-MeVal, Aib„ D-Ala, (D)Asn, (D)Asp, (D)Leu, (D)Phe, (D)Tyr, Aib, a-MeLeu, a-MeOrn, β- Aib, β-Ala, phAla, phArg, phLeu, phVal, β-spiro-pip, Glu, hArg, He, Lys, N-MeLeu, N-MeArg, Ogl, Orn, Pro, Gin, Ser, Thr, Tie, t-butyl-Gly, or a corresponding α-methyl amino acid form of any of the foregoing; XI 3 is Thr, Sarc, Glu, Phe, Arg, Leu, Lys, Arg, Orn, Val, phAla, Lys(Ac), (D)Asn, (D)Leu, (D)Phe, (D)Thr, Ala, a-MeLeu, Aib, β-Ala, β-Glu, phLeu, phVal, β-spiro-pip, Cha, Chg, Asp, Dab, Dap, a-DiethylGly, hLeu, Asn, Ogl, Pro, Gin, Ser, β-spiro-pip, Thr, Tba, Tie or Aib, Cit, hArg, Lys, Asn, Orn, Gin or a corresponding a-methyl amino acid form of any of the foregoing; X14 is Phe, Tyr, Glu, Gly, His, Lys, Leu, Met, Asn, Pro, Gin, Arg, Ser, Thr, TicphPhe, Arg, Lys(Ac), His; Dap(Ac), Dab(Ac), Asp or a corresponding a-methyl amino acid form of any of the foregoing; XI 5 is Gly, Ser, Thr, Gin, Ala, (D)Ala, (D)Asn, (D)Asp, (D)Leu, (D)Phe, (D)Thr, Aea, Asp, Asn, Glu, Phe, Gly, Lys, Leu, Pro, Arg, β-Ala, Sarc, or a corresponding α-methyl amino acid form of any of the foregoing; XI 6 is Asp, Glu, Ala, AEA, AEP, phAla, Gaba, Gly, Ser, Pro, Asn, Thr or absent, or a corresponding α-methyl amino acid form of any of the foregoing; and XI 7 is Leu, Lys, Arg, Glu, Ser, Gly, Gin or absent, or a corresponding α-methyl amino acid form of any of the foregoing.

7. The peptide inhibitor of claim 1 or claim 6, wherein the bond between X4 and X9, is a disulfide bond, a thioether bond, a lactam bond, a triazole ring, a selenoether bond, a diselenide bond, or an olefin bond.

8. The peptide inhibitor of any one of claims 1-7, wherein X4 is Cys and X9 is Cys, and the bond is a disulfide bond.

9. The peptide inhibitor of any one of claims 1-7, wherein X4 is Pen and X9 is Pen, and the bond is a disulfide bond.

10. The peptide inhibitor of claim 8 or claim 9, wherein X7 is Trp; XI 0 is Phe, Tyr, a Phe analog, or a Tyr analog; XI 1 is Trp, 1-Nal or 2-Nal; and X12 is Aib, a-Me-Lys, a-Me-Val a-Me-Leu; Ache, Acvc, Acpc, Acpc or THP,.

11. The peptide inhibitor of claim 10, wherein the peptide inhibitor comprises any of the following the amino acid sequences: Ac-[Pen]-Q-T-W-Q-[Pen]-[Phe(4-OMe)]-[2-Nal]-[a-Me-Lys]-ENG-NH2; Ac-[Pen]-N-T-W-Q-[Pen]-[Phe[4-(2-aminoethoxy)]-[2-Nal]-[Aib]-[Lys(Ac)]- -NH2; Ac-[Pen]-Q-T-W-Q-[Pen]-[Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLeu]-[Lys(Ac)]- -NH2; Ac-[Pen]-QTWQ-[Pen]-[Phe(4-CONH2)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]- -NH2; Ac- [Pen] -QT WQ- [Pen] - [Phe [4-(2-aminoethoxy)] - [2-Nal] - [a-MeLeu] -Q -NH2; Ac-[Pen]-Q-T-W-Q-[Pen]-[Phe(4-CONH2)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]- -NH2; Ac-[Pen]-QTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-NG-NH2; Ac- [Pen] -QT WQ- [Pen] - [Phe [4-(2-aminoethoxy)] - [2-Nal] - [a-MeLys] - [Lys(Ac)] -NN-NH2; Ac- [Pen] -QT WQ- [Pen] - [Phe [4-(2-aminoethoxy)] - [2-Nal] - [a-MeLys] -ENA-NH2; Ac- [Pen] -QT WQ- [Pen] - [Phe [4-(2-aminoethoxy)] - [2-Nal] - [a-MeLeu]- [Lys(Ac)] -NN-NH2; Ac- [Pen] -QT WQ- [Pen] - [Phe [4-(2-aminoethoxy)] - [2-Nal] - [a-MeLeu] -QNN-NH2; Ac- [Pen] -QT WQ- [Pen] - [Phe [4-(2-aminoethoxy)] - [2-Nal] - [Aib]-ENN-NH2; Ac- [Pen] -QT WQ- [Pen] - [Phe [4-(2-aminoethoxy)] - [2-Nal] - Aib- [Lys(Ac)] -NN-NH2; Ac- [Pen] -QT WQ- [Pen] - [Phe [4-(2-aminoethoxy)]- [2-Nal] - [Aib] - [Lys(Ac)] -NQ-NH2; Ac- [Pen] -QT WQ- [Pen] - [Phe [4-(2-acetylaminoethoxy)] - [2-Nal] - [a-MeLeu] - [Lys(Ac)] -NN-NH2; Ac- [Pen] -QT WQ- [Pen] - [Phe [4-(2-acetylaminoethoxy)] - [2-Nal] - [a-MeLeu] -QNN-NH2; Ac-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2-Nal]-[Aib]-[Lys(Ac)]-N-[pAla]-NH2; Ac- [Pen] -NT WQ- [Pen]- [Phe [4-(2-aminoethoxy)] - [2-Nal] - [hLeu] - [Lys(Ac)] -N- [ β Ala] -NH2; Ac- [Pen] -QT WQ- [Pen]- [Phe [4-(2-acetylaminoethoxy)] - [2-Nal] - [ Aib]- [Lys(Ac)] -NN-NH2; Ac- [Pen] -NT WQ- [Pen] - [Phe [4-(2-aminoethoxy)]- [2-Nal] - [Aib] - [Lys(Ac)] -NN-NH2; Ac- [Pen] -QT WQ- [Pen] - [Phe [4-(2-acetylaminoethoxy)] - [2-Nal] - [ Aib]- [Lys(Ac)] -NQ-NH2; or Ac-[Pen]-QTWQ-[Pen]-[Phe(4-OMe)]-[2-Nal]-[Aib]-[Lys(Ac)]-NQ-NH2, wherein the peptide inhibitor comprises a disulfide bond between the two Pen amino acids.

12. The peptide inhibitor of claim 1 or claim 6, wherein X4 is an amino acid, aliphatic acid, alicyclic acid or modified 2- methyl aromatic acid having a carbon side chain capable of forming a thioether bind with X9; X9 is a sulfur-containing amino acid capable of forming a thioether bond with X4, and the bond between X4 and X9 is a thioether bond.

13. The peptide inhibitor of claim 12, wherein X4 is Abu, 2-chloromethylbenzoic acid, mercapto-propanoic acid, mercapto-butyric acid, 2- chloro-acetic acid, 3-chloro-propanoic acid, 4- chloro -butyric acid, 3-chloro-isobutyric acid; and X9 is Abu, Cys, Pen, hCys, D-Pen, D-Cys, or D-hCys.

14. The peptide inhibitor of claim 13, wherein (a) X4 is Abu and X9 is Cys; or (b) X4 is Cys and X9 is Abu. wherein the peptide inhibitor is cyclized via a thioether bond between X4 and X9.

15. The peptide inhibitor of claim 13 or claim 14, wherein X7 is Trp; XI 0 is Phe, Tyr, a Phe analog, or a Tyr analog; XI 1 is Trp, 1-Nal or 2-Nal; and X12 is a-Me-Lys, a-Me-Leu, a-Me-Ser, a-Me-Val, Ache, Acvc, Acpc, Acbc or 4-amino-4- carboxy-tetrahydropyran.

16. The peptide inhibitor of claim 15, wherein the peptide inhibitor comprises any of the following amino acid sequences: Ac-Cyclo-[[Abu]-QTWQC]]-[Phe(4-OMe)]-[2-Nal]-[a-MeLys]-E-N-G; Ac-Cyclo-[[Abu]-QTWQC]]-[Phe(4-OMe)]-[2-Nal]-[a-MeOrn]-ENG-NH2; Ac-Cyclo-[[Abu]-QTWQC]]-[Phe(4-C02H)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-NG-NH2; Ac-Cyclo-[[Abu]-QTWQC]]-[Phe(4-OMe)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-NG-NH2; Ac-Cyclo-[[Abu]-QTWQC]]-[Phe(4-CONH2)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]NG-NH2; Ac-Cyclo-[[Abu]-QTWQC]]-[Phe(4-OMe)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-NA-NH2; Ac-Cyclo-[[Abu]-QTWQC]]-[Phe(4-OMe)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-NAE-NH2; Ac-Cyclo-[[Abu]-QTWQC]]-[Phe[4-(2-aminoethoxy)]]-[2-Nal]-[a-MeLys]-ENG-NH2; Ac-Cyclo-[[Abu]-QTWQC]]-[Phe(4-(2-aminoethoxy))]-W-[a-MeLys]-E-N-G; Ac-Cyclo-[[Abu]-QTWQC]]-[Phe[4-(2-aminoethoxy)]]-[2-Nal]-[a-MeLys]-DNG-NH2; Ac-Cyclo-[[Abu]-QTWQC]]-[Phe[4-(2-aminoethoxy)]]-[2-Nal]-[a-MeLys]-[Lys(succinic acid)]-NG-NH2; Ac-Cyclo-[[Abu]-QTWQC]]-[Phe[4-(2-aminoethoxy)]]-[2-Nal]-[a-MeLys]-[Lys(glutaric acid)]- NG-NH2; Ac-Cyclo-[[Abu]-QTWQC]]-[Phe[4-(2-aminoethoxy)]]-[2-Nal]-[a-MeLys]-[Lys(pyroglutamic acid)]-NG-NH2; Ac-Cyclo-[[Abu]-QTWQC]]-[Phe[4-(2-aminoethoxy)]]-[2-Nal]-[a-MeLys]-[Lys(isovaleric acid)]-NG-NH2; Ac-Cyclo-[[Abu]-QTWQC]]-[Phe[4-(2-aminoethoxy)]]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-NG- [(D)Lys]-NH2; Ac-Cyclo-[[Abu]-QTWQC]]-[Phe[4-(2-aminoethoxy)]]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-NG- [AEA]-NH2; Ac-Cyclo-[[Abu]-QTWQC]]-[Phe[4-(2-aminoethoxy)]]-[2-Nal]-[Aib]-QNG-NH2; Ac-Cyclo-[[Abu]-QTWQC]]-[Phe[4-(2-aminoethoxy)]]-[2-Nal]-[Aib]-[Lys(Ac)]-NA-NH2; Ac-Cyclo-[[Abu]-QTWQC]]-[Phe[4-(2-aminoethoxy)]]-[2-Nal]-[Aib]-K G-NH2; Ac-Cyclo-[[Abu]-QTWQC]]-[Phe[4-(2-aminoethoxy)]]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-NG-NH2; Ac-Cyclo-[[Abu]-QTWQC]]-[Phe[4-(2-(acetyl-aminoethoxy)]]-[2-Nal]-[a-MeLys(Ac)]- [Lys(Ac)]-NG-NH2; Ac-Cyclo-[[Abu]-QTWQC]]-[Phe[4-(2-(acetyl-aminoethoxy)]]-[2-Nal]-[a-MeLys(Ac)]-ENG- NH2; Ac-Cyclo-[[Abu]-QTWQC]]-[Phe[4-(2-aminoethoxy)]]-[2-Nal]-[4-amino-4-carboxy- tetrahydropyr an] -ENN-NH2 ; Ac-Cyclo-[[Abu]-QTWQC]]-[Phe[4-(2-aminoethoxy)]]-[2-Nal]-[a-MeLys]-ENQ-NH2; Ac-Cyclo-[[Abu]-QTWQC]-[Phe[4-(2-aminoethoxy)]]-[2-Nal]-[a-MeLys]-ENN-NH2; Ac-Cyclo-[[Abu]-QTWQC]]-[Phe[4-(2-aminoethoxy)]]-[2-Nal]-[a-MeVal]-[Lys(Ac)]-NG-NH2; Ac-Cyclo-[[Abu]-QTWQC]]-[Phe[4-(2-aminoethoxy)]]-[2-Nal]-[hLeu]-[Lys(Ac)]-N-[pAla]- NH2; Ac-Cyclo-[[Abu]-QTWQC]]-[Phe[4-(2-(acetyl-aminoethoxy)]]-[2-Nal]-[a-MeLys(Ac)]-ENQ- NH2; Ac-Cyclo-[[Abu]-QTWQC]]-[Phe[4-(2-(acetyl-aminoethoxy)]]-[2-Nal]-[a-MeLys(Ac)]-E - NH2; Ac-Cyclo-[[Abu]-QTWQC]]-[Phe[4-(2-aminoethoxy)]]-[2-Nal]-[a-MeLeu]-ENN-NH2; Ac-Cyclo-[[Abu]-QTWQC]]-[Phe[4-(2-aminoethoxy)]]-[2-Nal]-[a-MeLeu)-[Cit]-NN-NH2; Ac-Cyclo-[[Abu]-QTWQC]]-[Phe[4-(2-aminoethoxy)]]-[2-Nal]-[a-MeLeu]-[Lys(Ac)]-NN-NH2; Ac-Cyclo-[[Abu]-QTWQC]]-[ Phe[4-(2-aminoethoxy)]]-[2-Nal]-[Aib]-[Lys(Ac)]-NG-NH2; Ac-E-Cyclo-[[Abu]-QTWQC]-[Phe[4-(2-aminoethoxy)]]-[2-Nal]-[a-MeLys]-E -NH2; Ac-(D)Glu-[Cyclo-[[Abu]-QTWQC]-[Phe[4-(2-aminoethoxy)]]-[2-Nal]-[a-MeLys]-E -NH2; Ac-Arg-Cyclo-[[Abu]-QTWQC]-[Phe[4-(2-aminoethoxy)]]-[2-Nal]-[a-MeLys]-EN -NH2; Ac-[(D)Arg-Cyclo-[[Abu]-QTWQC]-[Phe[4-(2-aminoethoxy)]]-[2-Nal]-[a-MeLys]-ENN-NH2; Ac-F-Cyclo-[[Abu]-QTWQC]]-[Phe[4-(2-aminoethoxy)]]-[2-Nal]-[a-MeLys]-E -NH2; Ac-[(D)Phe]-Cyclo-[[Abu]-QTWQC]-[Phe[4-(2-aminoethoxy)]]-[2-Nal]-[a-MeLys]-E -NH2; Ac-[2-Nal]-Cyclo-[[Abu]-QTWQC]-[Phe[4-(2-aminoethoxy)]]-[2-Nal]-[a-MeLys]-E -NH2; Ac-Leu-Cyclo-[[Abu]-QTWQC]-[Phe[4-(2-aminoethoxy)]]-[2-Nal]-[a-MeLys]-EN -NH2; Ac-[(D)Qln]-Cyclo-[[Abu]-QTWQC]-[Phe[4-(2-aminoethoxy)]]-[2-Nal]-[a-MeLys]-E -NH2; Ac-Cyclo-[[Abu]-QTWQC]-[Phe[4-(2-aminoethoxy)]]-[2-Nal]-[a-MeLeu]-ENG-NH2; Ac-T-Cyclo-[[Abu]-QTWQC]-[Phe[4-(2-aminoethoxy)]]-[2-Nal]-[a-MeLys]-E -NH2; Ac-Cyclo-[[Abu]-QTWQC]]-[Phe[4-(2-aminoethoxy)]]-[2-Nal]-[a-MeLeu]-QN-[pAla]-NH2; Ac-Cyclo-[[Abu]-QTWQC]]-[Phe[4-(2-aminoethoxy)]]-[2-Nal]-[Acbc]-E -NH2; Ac-Cyclo-[[Abu]-QTWQC]]-[Phe[4-(2-aminoethoxy)]]-[2-Nal]-[Achc]- E -NH2; Ac-Cyclo-[[Abu]-QTWQC]]-[Phe[4-(2-aminoethoxy)]]-[2-Nal]-[Acvc]-E -NH2; Ac-Cyclo-[[Abu]-QTWQC]-[Phe[4-(2-aminoethoxy)]]-[2-Nal]-[4-amino-4-carboxy-piperidine]- ENN-NH2; or Ac-Cyclo- [ [ Abu] -QTWQC] - [Phe[4-(2-aminoethoxy)] ]- [2-Nal] - [4-amino-4-carboxy- tetrahydropyr an] -ENN-NH2 , wherein the peptide inhibitor comprises a thioether bond between the Abu and the C.

17. The peptide inhibitor of claim 1 , wherein X4 is Pen, Cys or homo-Cys; X5 is any amino acid; X6 is any amino acid; X7 is Trp, Bip, Gin, His, Glu(Bzl), 4-Phenylbenzylalanine, Tic, Phe[4-(2-aminoethoxy)], Phe(3,4-Cl2), Phe(4-OMe), 5-Hydroxy-Trp, 6-Chloro-Trp, N-MeTrp, a-Me-Trp, 1 ,2,3,4 - tetrahydro-norharman, Phe(4-C02H), Phe(4-CONH2), Phe(3,4-Dimethoxy), Phe(4-CF3), Phe(4-tBu), ββ-diPheAla, Glu, Gly, He, Asn, Pro, Arg, Thr or Octgly, or a corresponding a- methyl amino acid form of any of the foregoing; X8 is any amino acid; X9 is Pen, Cys or hCys; XI 0 is 1-Nal, 2-Nal, Aic, Bip, (D)Cys, Cha, DMT, (D)Tyr, Glu, Phe, His, Trp, Thr, Tic, Tyr, 4- pyridylAla, Octgly, a Phe analog or a Tyr analog (optionally, Phe(3,4-F2), Phe(3,4-Cl2), F(3-Me), Phe[4-(2-aminoethoxy)], Phe[4-(2-(acetyl-aminoethoxy)], Phe(4-Br), Phe(4-CONH2), Phe(4-Cl), Phe(4-CN), Phe(4-guanidino), Phe(4-Me), Phe(4-NH2), Phe(4-N3), Phe(4-OMe), or Phe(4- OBzl)), or a corresponding a-methyl amino acid form of any of the foregoing; XI 1 is 2-Nal, 1-Nal, 2,4-dimethylPhe, Bip, Phe(3,4-Cl2), Phe (3,4-F2), Phe(4-C02H), phPhe(4- F), a-Me-Trp, 4-phenylcyclohexyl, Phe(4-CF3), a-MePhe, phNal, phPhe, phTyr, phTrp, Nva(5- phenyl), Phe, His, hPhe, Tic, Tqa, Trp, Tyr, Phe(4-OMe), Phe(4-Me), Trp(2,5,7-tri-tert-Butyl), Phe(4-Oallyl), Tyr(3-tBu), Phe(4-tBu), Phe(4-guanidino, Phe(4-OBzl), Octgly, Glu(Bzl), 4- Phenylbenzylalanine, Phe[4-(2-aminoethoxy)], 5-Hydroxy-Trp, 6-Chloro-Trp, N-MeTrp, 1,2,3,4-tetrahydro-norharman, Phe(4-CONH2), Phe(3,4-OMe2) Phe(2,3-Cl2), Phe(2,3-F2), Phe(4- F), 4-phenylcyclohexylalanine or Bip, or a corresponding a-methyl amino acid form of any of the foregoing; X12 is a-MeLys, a-MeOrn, a-MeLeu, a-MeVal, 4-amino-4-carboxy-tetrahydropyran, Ache Acpc, Acbc, Acvc, MeLeu, Aib, (D)Ala, (D)Asn, (D)Leu, (D)Asp, (D)Phe, (D)Thr, 3-Pal, Aib, β-Ala, phGlu, PhAla, phLeu, PhVal, β-spiro-pip, Cha, Chg, Asp, Dab, Dap, a-diethylGly, Glu, Phe, hLeu, hArg, hLeu, He, Lys, Leu, Asn, N-MeLeu, N-MeArg, Ogl, Orn, Pro, Gin, Arg, Ser, Thr or Tie, or a corresponding α-methyl amino acid form of any of the foregoing; XI 3 is Lys(Ac), (D)Asn, (D)Leu, (D)Thr, (D)Phe, Ala, Aib, a-MeLeu, β-Ala, phGlu, phAla, PhLeu, phVal, β-spiro-pip, Cha, Chg, Asp, Lys, Arg, Orn, Dab, Dap, a-diethylGly, Glu, Phe, hLeu, Lys, Leu, Asn, Ogl, Pro, Gin, Asp, Arg, Ser, spiro-pip, Thr, Tba, Tic, Val or Tyr, or a corresponding a-methyl amino acid form of any of the foregoing; X14 is Asn, Glu, Phe, Gly, His, Lys, Leu, Met, Asn, Pro, Gin, Arg, Ser, Thr, Tic or Tyr, Lys(Ac), Orn or a corresponding a-methyl amino acid form of any of the foregoing; XI 5 is Gly, (D)Ala, (D)Asn, (D)Asp, Asn, (D)Leu, (D)Phe, (D)Thr, Ala, Asn, Ser, AEA, Asp, Glu, Phe, Gly, Lys, Leu, Pro, Gin, Arg or Ser, β-Ala, Arg or a corresponding α-methyl amino acid form of any of the foregoing; XI 6 is absent, Gly, Ala, Asp, Ser, Pro, Asn or Thr, or a corresponding α-methyl amino acid form of any of the foregoing; XI 7 is absent, Glu, Ser, Gly or Gin, or a corresponding α-methyl amino acid form of any of the foregoing; XI 8 is absent or any amino acid; XI 9 is absent or any amino acid; and X20 is absent or any amino acid.

18. The peptide inhibitor of claim 17, wherein the bond between X4 and X9 is a disulfide bond.

19. The peptide inhibitor of any one of claims 1-18, wherein one or more of XI , X2, and X3 are absent.

20. The peptide inhibitor of any one of claims 1-19, wherein one or more of XI 7, XI 9 and X20 are absent.

21. The peptide inhibitor of any one of claims 17-20, wherein one or both of X4 or X9 is Pen.

22. The peptide inhibitor of claim 21, wherein both X4 and X9 are Pen. The peptide inhibitor of any one of claims 17-22, wherein XI 8 is (D)-Lys.

24. The peptide inhibitor of any one of claims 17-23, comprising one or more, two or more, three or more, or four of the following: X5 is Arg, Asn, Gin, Dap, Orn; X6 is Thr or Ser; X7 is Trp, 2-Nal, 1-Nal, Phe(4-OAllyl), Tyr(3-tBu), Phe(4-tBu), Phe(4-guanidino), Phe(Bzl) or Phe(4-Me), 5-Hydroxy-Trp, 6-Chloro-Trp, N-MeTrp, a-MeTrp or 1,2,3,4 -tetrahydro- norharman; and X8 is Gin, Val, Phe, Glu, Lys.

25. The peptide inhibitor of any one of claims 17-24, comprising one or more, two or more, three or more, four or more, five or more, six or more, or seven of the following: X10 is Tyr, Phe(4-OBzl), Phe(4-OMe), Phe(4-CONH2), Phe(3,4-Cl2), Phe(4-tBu), Phe(4-NH2), Phe(4-Br), Phe(4-CN), Phe(4-C02H), Phe(4-(2aminoethoxy)) or Phe(4-guanidino) ; XI 1 is Trp, 2-Nal, 1-Nal, Phe(4-OAllyl), Tyr(3-tBu), Phe(4-tBu), Phe(4-guanidino), Phe(Bzl) or Phe(4-Me), 5-Hydroxy-Trp, 6-Chloro-Trp, N-MeTrp, a-MeTrp or 1,2,3,4 -tetrahydro- norharman; XI 2 is Arg, a-MeLys a-MeLeu, Aib or a-MeOrn; XI 3 is Lys, Glu or Lys(Ac); XI 4 is Phe or Asn; XI 5 is Asn, Gly, Ser PAla, or Ala; and XI 6 is absent or AEA.

26. The peptide inhibitor of claim 25, wherein X4 and X9 are Pen; X5 is Gin; X6 is Thr; X7 is Trp; X8 is Gin; X10 is Tyr, Phe(4-OMe) or 2-Nal; XI 1 is Trp, 2-Nal or 1-Nal; XI 2 is Arg, aMeLys or a-MeOrn; XI 3 is Lys, Glu or Lys(Ac); XI 4 is Phe or Asn; XI 5 is Gly; and XI 6 is absent.

27. The peptide inhibitor of claim 26, wherein one or more of XI, X2 and X3 are absent; and one or more, two or more, three or more, or four of X17, X18, X19 and X20 are absent.

28. The peptide inhibitor of claim 1 , wherein X4 is Abu, Pen, or Cys; X7 is Trp, Bip, Gin, His, Glu(Bzl), 4-Phenylbenzylalanine, Tic, Phe[4-(2-aminoethoxy)], Phe(3,4-Cl2), Phe(4-OMe), 5-Hydroxy-Trp, 6-Chloro-Trp, N-MeTrp, a-MeTrp, 1,2,3,4 - tetrahydro-norharman, Phe(4-C02H), Phe(4-CONH2), Phe(3,4-Dimethoxy), Phe(4-CF3), ββ- diPheAla, Phe(4-tBu), Glu, Gly, He, Asn, Pro, Arg, Thr or Octgly, or a corresponding a-methyl amino acid form of any of the foregoing; X9 is Abu, Pen, or Cys; XI 0 is 1-Nal, 2-Nal, Aic, Bip, (D)Cys, Cha, DMT, (D)Tyr, Glu, Phe, His, Trp, Thr, Tic, Tyr, 4- pyridylAla, Octgly a Phe analog or a Tyr analog, or a corresponding a-methyl amino acid form of any of the foregoing; XI 1 is 2-Nal, 1-Nal, 2,4-dimethylPhe, Bip, 4-phenylcyclohexyl, Glu(Bzl), 4- Phenylbenzylalanine, Tic, Phe[4-(2-aminoethoxy)], Phe(3,4-Cl2), Phe(3,4-F2), β!ιΡ1ιε(4-Ρ), Phe(4-OMe), 5-Hydroxy-Trp, 6-Chloro-Trp, N-MeTrp, a-MeTrp, 1,2,3,4 -tetrahydro- norharman, Phe(4-C02H), Phe(4-CONH2), Phe(3,4-Dimethoxy), Phe(4-CF3), Phe(2,3-Cl2), Phe(2,3-F2),Phe(4-F), 4-phenylcyclohexylalanine, a-MePhe, phNal, βhPhe, βhTyr, βhTrp, Bip, Nva(5-phenyl), Phe, His, hPhe, Tqa, Trp, Tyr, Phe(4-Me), Trp(2,5,7-tri-tertButyl), Phe(4- OAllyl), Tyr(3-tBu), Phe(4-tBu), Phe(4-guanidino), Phe(4-OBzl), or Octgly, or a corresponding α-methyl amino acid form of any of the foregoing; X12 is a-MeLys, a-MeOrn, a-MeLeu, MeLeu, Aib, Ache, Acvc, Acpc, Acpc, THP, (D)Ala, (D)Asn, (D)Leu, (D)Asp, (D)Phe, (D)Thr, 3-Pal, Aib, β-Ala, phGlu, βΙιΑΚ βhLeu, βhVal, β- spiro-pip, Cha, Chg, Asp, Dab, Dap, a-DiethylGly, Glu, Phe, hLeu, hArg, hLeu, He, Lys, Leu, Asn, N-MeLeu, N-MeArg, Ogl, Orn, Pro, Gin, Arg, Ser, Thr or Tie, or a corresponding a-methyl amino acid form of any of the foregoing; XI 3 is Lys(Ac), (D)Asn, (D)Leu, (D)Thr, (D)Phe, Ala, Aib, a-MeLeu, βΑ1&, phGlu, βηΑΚ βϋευ, phVal, β-spiro-pip, Cha, Chg, Asp, Arg, Orn, Dab, Dap, a-DiethylGly, Glu, Phe, hLeu, Lys, Leu, Asn, Ogl, Pro, Gin, Asp, Arg, Ser, spiro-pip, Thr, Tba, Tic, Val or Tyr, or a corresponding α-methyl amino acid form of any of the foregoing; X14 is Asn, Glu, Phe, Gly, His, Lys, Leu, Met, Asn, Pro, Gin, Arg, Ser, Thr, Tic or Tyr, or a corresponding a-methyl amino acid form of any of the foregoing; XI 5 is Gly, (D)Ala, (D)Asn, (D)Asp, Asn, (D)Leu, (D)Phe, (D)Thr, Ala, AEA, Asp, Glu, Phe, Gly, Lys, Leu, Pro, Gin, Arg or Ser, or a corresponding a-methyl amino acid form of any of the foregoing; XI 6 is absent, Gly, Ala, Asp, Ser, Pro, Asn or Thr, or a corresponding α-methyl amino acid form of any of the foregoing; and XI 7 is absent, Glu, Ser, Gly or Gin, or a corresponding α-methyl amino acid form of any of the foregoing.

29. The peptide inhibitor of claim 28, wherein the peptide inhibitor is cyclized via an intramolecular bond between X4 and X9.

30. The peptide inhibitor of claim 28 or claim 29, wherein one or more of XI , X2, and X3 are absent.

31. The peptide inhibitor of any one of claims 28-30, wherein one or more of XI 7, XI 9 and X20 are absent.

32. The peptide inhibitor of any one of claims 28-31, wherein one of X4 or X9 is Abu, and the other of X4 or X9 is not Abu.

33. The peptide inhibitor of any one of claims 28-32, comprising one or more, two or more, three or more, or four of the following: X5 is Arg, Gin, Dap or Orn; X6 is Thr or Ser; X7 is Trp, 2-Nal, 1-Nal, Phe(4-OAllyl), Tyr(3-tBu), Phe(4-tBu), Phe(4-guanidino), Phe(4-OBzl), Phe(4-Me), 5-Hydroxy-Trp, 6-Chloro-Trp, N-MeTrp, or a-MeTrp, 1 ,2,3,4 -tetrahydro- norharman; and X8 is Gin, Val, Phe, Glu or Lys.

34. The peptide inhibitor of any one of claims 28-33, comprising one or more, two or more, three or more, four or more, five or more, six or more, or seven of the following: X10 is Tyr, Phe(4-OBzl), Phe(4-OMe), Phe(4-CONH2), Phe(3,4-Cl2), Phe(4-tBu), Phe(4-NH2), Phe(4-Br), Phe(4-CN), Phe(4-C02H), Phe(4-(2aminoethoxy)) or Phe(4-guanadino); XI 1 is Trp, 2-Nal, 1-Nal, Phe(4-OAllyl), Tyr(3-tBu), Phe(4-tBu), Phe(4-guanidino), Phe(Bzl) or Phe(4-Me), 5-Hydroxy-Trp, 6-Chloro-Trp, N-MeTrp, a-MeTrp or 1,2,3,4 -tetrahydro- norharman; X12 is Arg, hLeu, (D)Asn, Aib, a-MeLys, a-MeLeu, a-Me-Val, a-MeOrn, Ache, Acvc, Acpc, Acpc, or THP; XI 3 is Lys, Glu or Lys(Ac); XI 4 is Phe or Asn; XI 5 is Gly, Ser, Asn, PAla or Ala; and XI 6 is absent or AEA.

35. The peptide inhibitor of any one of claims 1-34, wherein the peptide inhibitor comprises the structure of Formula I: or a pharmaceutically acceptable salt or solvate thereof, wherein R1 is a bond, hydrogen, a C1-C6 alkyl, a C6-C12 aryl, a C6-C12 aryl, a C1-C6 alkyl, a C1-C20 alkanoyl, and including PEGylated versions alone or as spacers of any of the foregoing; X is the amino acid sequence; and R2 is OH or NH2.

36. A peptide dimer inhibitor of an interleukin-23 receptor, wherein the peptide dimer inhibitor comprises two peptide monomer subunits connected via one or more linker moieties, wherein each peptide monomer subunit has a sequence or structure set forth in any one of claims 1-35.

37. The peptide dimer inhibitor of claim 36, wherein one or both peptide monomer subunit is cyclized via an intramolecular bond between X4 and X9.

38. The peptide dimer inhibitor of claim 37, wherein one or both intramolecular bond is a disulfide bond, a thioether bond, a lactam bond, a selenoether, diselenide, or an olefin bond.

39. The peptide dimer inhibitor of any one of claims 36-38, wherein the linker moiety is a diethylene glycol linker, an iminodiacetic acid (IDA) linker, a β-Ala-iminodiaceticacid (β-Ala- IDA) linker, or a PEG linker.

40. The peptide dimer inhibitor of any one of claims 36-39, wherein the N-terminus of each peptide monomer subunit is connected by the linker moiety or wherein the C-terminus of each peptide monomer subunit is connected by the linker moiety.

41. The peptide dimer inhibitor of claim 36, wherein the peptide dimer inhibitor comprises one of the following amino acid sequences: [Ac-Cyclo-[[Abu]-QTWQC]-[Phe(4-OMe)]-[2-Nal]-[a-MeLys]-ENG-NH2]2 DIG; [Ac-[Pen]-QTWQ-[Pen]-[Phe(4-OMe)]-[2-Nal]-[a-MeVal]-[Lys(Ac)]- -[D)Lys]2 DIG; [Ac-[Pen]-QTWQ-[Pen]-[Phe[4-(2-acetylaminoethoxy)]-[2-Nal]- [a-MeVal]-[Lys(Ac)]-NN- [D)Lys]]2 DIG; [ Ac- [Pen] -QT WQ [Pen] - [Phe [4-(2-acetylaminoethoxy)] ] - [2-Nal] - [a-Me Val] -K N-NH2]2 DIG; [Ac-[Pen]-QTWQ[Pen]-[Phe[4-(2-acetylaminoethoxy)]]-[2-Nal]-K-[Lys(Ac)]- -NH2]2 DIG; [Ac-[Pen]-QTWQ-[Pen]-[Phe(4-OMe)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]- -NH2]2 DIG; [Ac-Cyclo-[[Abu]-QTWQC]-[Phe(4-OMe)]-[2-Nal]-[a-MeLys]-ENG-NH2]2 DIG; or [Ac-[Pen]-QTWQ-[Pen]-[Phe(4-CONH2)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-NN-NH2]2 DIG.

42. A polynucleotide comprising a sequence encoding the peptide inhibitor of any one of claims 1-35 or one or both peptide monomer subunit of the peptide dimer inhibitor of any one of claims 36-41. A vector comprising the polynucelotide of claim 42.

44. A pharmaceutical composition comprising the peptide inhibitor of any one of claims 1-35 or the peptide dimer inhibitor of any one of claims 36-41 , and a pharmaceutically acceptable carrier, excipient, or diluent.

45. The pharmaceutical composition of claim 44, further comprising an enteric coating.

46. The pharmaceutical composition of claim 45, wherein the enteric coating protects and releases the pharmaceutical composition within a subject's lower gastrointestinal system.

47. A method for treating an Inflammatory Bowel Disease (IBD), ulcerative colitis, Crohn's disease, Celiac disease {nontropical Sprue), enteropathy associated with seronegative arthropathies, microscopic colitis, collagenous colitis, eosinophilic gastroenteritis, colitis associated with radio- or chemo -therapy, colitis associated with disorders of innate immunity as in leukocyte adhesion deficiency- 1 , chronic granulomatous disease, glycogen storage disease type lb, Hermansky-Pudlak syndrome, Chediak-Higashi syndrome, and Wiskott-Aldrich Syndrome, pouchitis resulting after proctocolectomy and ileoanal anastomosis, gastrointestinal cancer, pancreatitis, insulin-dependent diabetes mellitus, mastitis, cholecystitis, cholangitis, pericholangitis, chronic bronchitis, chronic sinusitis, asthma, psoriasis, psoriatic arthritis, or graft versus host disease in a subject, comprising providing to the subject an effective amount of the pharmaceutical composition of any one of claims 44-46.

48. The method of claim 47, wherein the pharmaceutical composition is provided to the subject by an oral, parenteral, intravenous, peritoneal, intradermal, subcutaneous, intramuscular, intrathecal, inhalation, vaporization, nebulization, sublingual, buccal, parenteral, rectal, intraocular, inhalation, topically, vaginal, or topical route of administration.

49. The method of claim 47 for treating Inflammatory Bowel Disease (IBD), ulcerative colitis, Crohn's disease, wherein the pharmaceutical composition is provided to the subject orally.

50. The method of claim 47 for treating psoriasis, wherein the pharmaceutical composition is provided to the subject orally, topically, parenterally, intravenously, subcutaneously, peritonealy, or intravenously.

51. The method of any one claims 47-50, wherein the peptide inhibitor or the peptide dimer inhibitor inhibits binding of an interleukin-23 (IL-23) to the interleukin-23 receptor (IL-23R).

52. A method of assessing the ability of a candidate compound to inhibit or reduce an inflammatory disease or disorder, comprising: (a) providing to a rat an amount of dextran sulfate sodium (DSS) or 2,4,6- Trinitrobenzenesulfonic acid (TNBS) sufficient to induce an inflammatory bowel disease (IBD); (b) providing to the rat an amount of a candidate compound; and (c) measuring an amount of IBD symptoms present in the rat after being provided with the DSS and the candidate compound; wherein if the amount of IBD symptoms measured in (c) are significantly lower than the amount measured in a control rat provided with the amount of DSS or TNBS and either an amount of a control compound or no peptide (e.g., vehicle control), the candidate compound inhibits or reduces the inflammatory disease or disorder.

53. The method of claim 52, wherein an anti-IL-23pl 9 antibody is used as a positive control.

54. The method of claim 52, wherein the candidate compound inhibits or reduces the inflammatory disease or disorder in a human.
```

---

### 티어 4 — 주변(Peripheral) lipidated 화학형 및 제제(formulation)

#### 4.1 US12478617B2 ✅교차검증 (40/40 완전일치)

> **💡 핵심 요약** &nbsp;|&nbsp; **유형:** compound·물질(peptide), composition(조성물), use·치료방법
> 
> **무엇을 청구하나:** 구조식 군에서 선택되는 특정 IL-23 수용체 저해제 화합물(claim 1) 자체와 그 의약조성물, IL-23/IL-23R 관련 질환·IBD·UC·CD·PsO·PsA 치료방법을 청구
> 
> **핵심 권리범위:** 청구항 1의 구조식 group에서 선택되는 IL-23R 저해제(개별 구조 도시); 약학적으로 허용되는 염 포함; 의약조성물(담체/부형제/희석제); 적응증별(UC/CD/PsO/PsA) 개별 치료방법
> 
> **독립항:** 1, 24, 25, 26, 27, 28, 29, 30 &nbsp;|&nbsp; **적응증:** IL-23/IL-23R 관련 질환/IBD/UC/CD/건선/건선성관절염 &nbsp;|&nbsp; **검증:** ✅교차검증 &nbsp;|&nbsp; **추정만료:** 2042-07-14


| 항목 | 내용 |
|---|---|
| 특허번호 | US12478617B2 (등록, B2) |
| 제목 | Lipidated peptide inhibitors of interleukin-23 receptor |
| 출원번호 / 출원일 | 18/495,457 / 2023-10-26 |
| 우선일 | 2021-07-14 (US Provisional 63/221,697); PCT/US2022/037205 |
| 등록일 | 2025-11-25 |
| 출원인/양수인 | Janssen Biotech, Inc.; Protagonist Therapeutics, Inc. |
| 패밀리 | US20240173309A1 (동일 출원 공개본), WO2023288019A2 (PCT) |
| 권위 만료일 | **2042-07-14** (GP anticipated expiration; 출원일+20년, PTE 미반영) |
| 교차검증 | GP=40, FPO=40, both=40, agree=40, **substantive_diff=0** → ✅완전일치 |

**[ANALYSIS] (한국어)**

**GP↔FPO 40/40 완전일치** ✅교차검증. 다만 본 특허의 청구항 대부분은 IL-23R 저해제의 **화학구조식**을 청구하는데, GP `/en` 텍스트 파싱에서 구조식 이미지가 렌더링되지 않아 청구항 1~23 및 31~40 본문이 `...selected from the group consisting of: or a pharmaceutically acceptable salt thereof.` / `...having the following structure:` 형태의 **구조 누락 청구항**으로 보존되어 있다(원문 그대로). 구조식 전문은 GP PDF 또는 등록공보 원본 확인이 필요하다. 청구항 24는 조성물, 25~30은 IL-23/IL-23R 질환·IBD·UC·CD·PsO·PsA 치료방법으로 텍스트가 온전하다. lipidated 화학형이므로 icotrokinra(단환, 비지질) 본체와는 주변 관계다.

**[VERBATIM] — 출처: Google Patents (`work/05_gp_authoritative/US12478617B2.md`)**

```text
1. An interleukin-23 receptor inhibitor selected from the group consisting of: or a pharmaceutically acceptable salt thereof.

2. The interleukin-23 receptor inhibitor of claim 1, having the following structure: or a pharmaceutically acceptable salt thereof.

3. The interleukin-23 receptor inhibitor of claim 1, having the following structure: or a pharmaceutically acceptable salt thereof.

4. The interleukin-23 receptor inhibitor of claim 1, having the following structure: or a pharmaceutically acceptable salt thereof.

5. The interleukin-23 receptor inhibitor of claim 1, having the following structure: or a pharmaceutically acceptable salt thereof.

6. The interleukin-23 receptor inhibitor of claim 1, having the following structure: or a pharmaceutically acceptable salt thereof.

7. The interleukin-23 receptor inhibitor of claim 1, having the following structure: or a pharmaceutically acceptable salt thereof.

8. The interleukin-23 receptor inhibitor of claim 1, having the following structure: or a pharmaceutically acceptable salt thereof.

9. The interleukin-23 receptor inhibitor of claim 1, having the following structure: or a pharmaceutically acceptable salt thereof.

10. The interleukin-23 receptor inhibitor of claim 1, having the following structure: or a pharmaceutically acceptable salt thereof.

11. The interleukin-23 receptor inhibitor of claim 1, having the following structure: or a pharmaceutically acceptable salt thereof.

12. The interleukin-23 receptor inhibitor of claim 1, having the following structure: or a pharmaceutically acceptable salt thereof.

13. The interleukin-23 receptor inhibitor of claim 1, having the following structure: or a pharmaceutically acceptable salt thereof.

14. The interleukin-23 receptor inhibitor of claim 1, having the following structure: or a pharmaceutically acceptable salt thereof.

15. The interleukin-23 receptor inhibitor of claim 1, having the following structure: or a pharmaceutically acceptable salt thereof.

16. The interleukin-23 receptor inhibitor of claim 1, having the following structure: or a pharmaceutically acceptable salt thereof.

17. The interleukin-23 receptor inhibitor of claim 1, having the following structure: or a pharmaceutically acceptable salt thereof.

18. The interleukin-23 receptor inhibitor of claim 1, having the following structure: or a pharmaceutically acceptable salt thereof.

19. The interleukin-23 receptor inhibitor of claim 1, having the following structure: or a pharmaceutically acceptable salt thereof.

20. The interleukin-23 receptor inhibitor of claim 1, having the following structure: or a pharmaceutically acceptable salt thereof.

21. The interleukin-23 receptor inhibitor of claim 1, having the following structure: or a pharmaceutically acceptable salt thereof.

22. The interleukin-23 receptor inhibitor of claim 1, having the following structure: or a pharmaceutically acceptable salt thereof.

23. The interleukin-23 receptor inhibitor of claim 1, having the following structure: or a pharmaceutically acceptable salt thereof.

24. A pharmaceutical composition comprising: (i) the interleukin-23 receptor inhibitor of claim 1, or a pharmaceutically acceptable salt thereof, and (ii) a pharmaceutically acceptable carrier, excipient, or diluent.

25. A method for treating a disease or disorder associated with interleukin 23 (IL-23)/interleukin 23 receptor (IL-23R), said method comprising administering an effective amount of the interleukin-23 receptor inhibitor of claim 1, or a pharmaceutically acceptable salt thereof, to a patient in need thereof.

26. A method for treating inflammatory bowel diseases (IBDs), said method comprising administering an effective amount of the interleukin-23 receptor inhibitor of claim 1, or a pharmaceutically acceptable salt thereof, to a patient in need thereof.

27. A method for treating ulcerative colitis (UC), said method comprising administering an effective amount of the interleukin-23 receptor inhibitor of claim 1, or a pharmaceutically acceptable salt thereof, to a patient in need thereof.

28. A method for treating Crohn's disease (CD), said method comprising administering an effective amount of the interleukin-23 receptor inhibitor of claim 1, or a pharmaceutically acceptable salt thereof, to a patient in need thereof.

29. A method for treating psoriasis (PsO), said method comprising administering an effective amount of the interleukin-23 receptor inhibitor of claim 1, or a pharmaceutically acceptable salt thereof, to a patient in need thereof.

30. A method for treating psoriatic arthritis (PsA), said method comprising administering an effective amount of the interleukin-23 receptor inhibitor of claim 1, or a pharmaceutically acceptable salt thereof, to a patient in need thereof.

31. The interleukin-23 receptor inhibitor of claim 1, having the following structure:

32. The interleukin-23 receptor inhibitor of claim 1, having the following structure:

33. The interleukin-23 receptor inhibitor of claim 1, having the following structure:

34. The interleukin-23 receptor inhibitor of claim 1, having the following structure:

35. The interleukin-23 receptor inhibitor of claim 1, having the following structure:

36. The interleukin-23 receptor inhibitor of claim 1, having the following structure:

37. The interleukin-23 receptor inhibitor of claim 1, having the following structure:

38. The interleukin-23 receptor inhibitor of claim 1, having the following structure:

39. The interleukin-23 inhibitor of claim 1, having the following structure:

40. The interleukin-23 receptor inhibitor of claim 6, having the following structure:
```

---

#### 4.2 US20240173309A1 ✅교차검증 (공통 30개 일치)

> **💡 핵심 요약** &nbsp;|&nbsp; **유형:** compound·물질(peptide), composition(조성물), use·치료방법
> 
> **무엇을 청구하나:** 구조식 군에서 선택되는 특정 IL-23 수용체 저해제 화합물(claim 23) 자체와 그 의약조성물, 그리고 IL-23/IL-23R 관련 질환·IBD·UC·CD·PsO·PsA 각각의 치료방법을 청구
> 
> **핵심 권리범위:** 청구항 23의 구조식 group으로부터 선택되는 IL-23R 저해제(개별 구조 도시); 약학적으로 허용되는 염 포함; 의약조성물(담체/부형제/희석제); 적응증별(UC/CD/PsO/PsA) 개별 치료방법 청구
> 
> **독립항:** 23, 46, 47, 48, 49, 50, 51, 52 &nbsp;|&nbsp; **적응증:** IL-23/IL-23R 관련 질환/IBD/UC/CD/건선/건선성관절염 &nbsp;|&nbsp; **검증:** ✅교차검증 &nbsp;|&nbsp; **추정만료:** 2042-07-14


| 항목 | 내용 |
|---|---|
| 특허번호 | US20240173309A1 (pre-grant 공개, A1) |
| 제목 | Lipidated peptide inhibitors of interleukin-23 receptor |
| 출원번호 / 출원일 | 18/495,457 / 2023-10-26 |
| 우선일 | 2021-07-14 (US Provisional 63/221,697) |
| 공개일 | 2024-05-30 |
| 출원인/양수인 | Janssen Biotech, Inc.; Protagonist Therapeutics, Inc. |
| 패밀리 | WO2023288019A2 (PCT), US12478617B2 (동일 출원 등록본) |
| 권위 만료일 | **2042-07-14** (GP anticipated expiration; 출원일+20년, PTE 미반영) |
| 교차검증 | GP=30, FPO=52, both=30, agree=30, **substantive_diff=0** → ✅완전일치(공통분) |

**[ANALYSIS] (한국어)**

US12478617B2와 **동일 출원(18/495,457)**의 공개본. GP 청구항 번호가 **23번부터 시작**하는 것은 공개 시점의 청구항 세트가 23~52였음을 반영한다(원문 그대로 보존). GP↔FPO 공통 30개가 substantive_diff=0으로 일치하여 ✅교차검증(공통분)이며, FPO가 52개를 보유해 일부 청구항은 GP 텍스트에 미포함이다. 본 공개본 역시 구조식 청구항이 텍스트로 깨져 있다(원문 보존).

**[VERBATIM] — 출처: Google Patents (`work/05_gp_authoritative/US20240173309A1.md`)**

```text
23. An interleukin-23 receptor inhibitor selected from the group consisting of: or a pharmaceutically acceptable salt thereof.

24. The interleukin-23 receptor inhibitor of claim 23, having the following structure: or a pharmaceutically acceptable salt thereof.

25. The interleukin-23 receptor inhibitor of claim 23, having the following structure: or a pharmaceutically acceptable salt thereof.

26. The interleukin-23 receptor inhibitor of claim 23, having the following structure: or a pharmaceutically acceptable salt thereof.

27. The interleukin-23 receptor inhibitor of claim 23, having the following structure: or a pharmaceutically acceptable salt thereof.

28. The interleukin-23 receptor inhibitor of claim 23, having the following structure: or a pharmaceutically acceptable salt thereof.

29. The interleukin-23 receptor inhibitor of claim 23, having the following structure: or a pharmaceutically acceptable salt thereof.

30. The interleukin-23 receptor inhibitor of claim 23, having the following structure: or a pharmaceutically acceptable salt thereof.

31. The interleukin-23 receptor inhibitor of claim 23, having the following structure: or a pharmaceutically acceptable salt thereof.

32. The interleukin-23 receptor inhibitor of claim 23, having the following structure: or a pharmaceutically acceptable salt thereof.

33. The interleukin-23 receptor inhibitor of claim 23, having the following structure: or a pharmaceutically acceptable salt thereof.

34. The interleukin-23 receptor inhibitor of claim 23, having the following structure: or a pharmaceutically acceptable salt thereof.

35. The interleukin-23 receptor inhibitor of claim 23, having the following structure: or a pharmaceutically acceptable salt thereof.

36. The interleukin-23 receptor inhibitor of claim 23, having the following structure: or a pharmaceutically acceptable salt thereof.

37. The interleukin-23 receptor inhibitor of claim 23, having the following structure: or a pharmaceutically acceptable salt thereof.

38. The interleukin-23 receptor inhibitor of claim 23, having the following structure: or a pharmaceutically acceptable salt thereof.

39. The interleukin-23 receptor inhibitor of claim 23, having the following structure: or a pharmaceutically acceptable salt thereof.

40. The interleukin-23 receptor inhibitor of claim 23, having the following structure: or a pharmaceutically acceptable salt thereof.

41. The interleukin-23 receptor inhibitor of claim 23, having the following structure: or a pharmaceutically acceptable salt thereof.

42. The interleukin-23 receptor inhibitor of claim 23, having the following structure: or a pharmaceutically acceptable salt thereof.

43. The interleukin-23 receptor inhibitor of claim 23, having the following structure: or a pharmaceutically acceptable salt thereof.

44. The interleukin-23 receptor inhibitor of claim 23, having the following structure: or a pharmaceutically acceptable salt thereof.

45. The interleukin-23 receptor inhibitor of claim 23, having the following structure: or a pharmaceutically acceptable salt thereof.

46. A pharmaceutical composition comprising: (i) the interleukin-23 receptor inhibitor of claim 23, or a pharmaceutically acceptable salt thereof, and (ii) a pharmaceutically acceptable carrier, excipient, or diluent.

47. A method for treating a disease or disorder associated with interleukin 23 (IL-23)/interleukin 23 receptor (IL-23R), said method comprising administering an effective amount of the interleukin-23 receptor inhibitor of claim 23, or a pharmaceutically acceptable salt thereof, to a patient in need thereof.

48. A method for treating inflammatory bowel diseases (IBDs), said method comprising administering an effective amount of the interleukin-23 receptor inhibitor of claim 23, or a pharmaceutically acceptable salt thereof, to a patient in need thereof.

49. A method for treating ulcerative colitis (UC), said method comprising administering an effective amount of the interleukin-23 receptor inhibitor of claim 23, or a pharmaceutically acceptable salt thereof, to a patient in need thereof.

50. A method for treating Crohn's disease (CD), said method comprising administering an effective amount of the interleukin-23 receptor inhibitor of claim 23, or a pharmaceutically acceptable salt thereof, to a patient in need thereof.

51. A method for treating psoriasis (PsO), said method comprising administering an effective amount of the interleukin-23 receptor inhibitor of claim 23, or a pharmaceutically acceptable salt thereof, to a patient in need thereof.

52. A method for treating psoriatic arthritis (PsA), said method comprising administering an effective amount of the interleukin-23 receptor inhibitor of claim 23, or a pharmaceutically acceptable salt thereof, to a patient in need thereof.
```

---

#### 4.3 WO2023288019A2 ☑️부분교차검증 (차이 5개)

> **💡 핵심 요약** &nbsp;|&nbsp; **유형:** compound·물질(peptide), composition(조성물), use·치료방법
> 
> **무엇을 청구하나:** Formula I~X의 광범위 Markush 및 Table 1·실시예로 정의되는 IL-23R 저해 펩타이드(7MeW 등 다양한 비천연 Trp 치환, AEF, THP, 3Pya, 지질/PEG 변형 포함)와 그 의약조성물, 치료용도·치료방법을 청구(차세대 변형 확장)
> 
> **핵심 권리범위:** X4-X9 디설파이드/티오에터(일부 RCM aliphatic) 고리화, 일부 amide 2차 결합; X7에 7MeW 등 다수 비천연 Trp 유도체, X10=AEF/TMAPF, X12=THP; Z=지질 moiety, PEG 사슬 등 지질화/PEG화 변형 포함; Table 1A~1M 및 특정 SEQ(예: SEQ ID NO:2 등) 한정
> 
> **독립항:** 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 19 &nbsp;|&nbsp; **적응증:** IBD/UC/CD/건선/건선성관절염 등 자가면역 염증질환 &nbsp;|&nbsp; **검증:** ☑️부분교차검증(차이5) &nbsp;|&nbsp; **추정만료:** PCT(term N/A)


| 항목 | 내용 |
|---|---|
| 특허번호 | WO2023288019A2 (PCT 공개, A2) |
| 제목 | LIPIDATED PEPTIDE INHIBITORS OF INTERLEUKIN-23 RECEPTOR |
| 국제출원 / 공개 | PCT/US2022/037205, 국제출원일 2022-07-14 |
| 우선일 | 2021-07-14 (US Provisional 63/221,697) |
| 출원인/양수인 | Janssen Biotech, Inc.; Protagonist Therapeutics, Inc. |
| 패밀리 | US20240173309A1, US12478617B2 (출원 18/495,457) |
| 권위 만료일 | PCT 자체 만료 **N/A**; 미국 대응 = 2042-07-14 |
| 교차검증 | GP=22, FPO=22, both=22, agree=17, **substantive_diff=5** → ☑️부분교차검증 |

**[ANALYSIS] (한국어)**

lipidated 화학형 PCT. 청구항 1~10은 Formula I~X의 IL-23R 저해제 속(다수의 비천연 잔기 약어 — 7MeW, AEF, THP, Zlipid 등)이며 X4-X9 이황화/티오에터 가교로 환화된다. 원문에 `XI 0`(=X10), `Ci`(=C1), `40MePh`(=4-OMe-Ph) 등 OCR 잔재가 다수 남아 있어 원문 그대로 보존한다. GP↔FPO 22개 중 17개 일치, 5개 차이로 ☑️부분교차검증이며 권위 소스는 GP.

**[VERBATIM] — 출처: Google Patents (`work/05_gp_authoritative/WO2023288019A2.md`)**

```text
1. An interleukin-23 receptor inhibitor comprising an amino acid sequence of Formula I R1 -X3 -X4-X5 -T -X7 -X8-X9-X 10-Xl 1 -THP-X13-N-X15-X16-R2 (I) wherein: R1 is hydrogen, Ci to C4 alkyl C(O)-, or Ci to C4 alkyl C(O)- substituted with Cl, F, or cyano, or cPEG3aCO; X3 is dR, R, K, dK, or absent; X4 is Pen, Abu, aMeC, or C; X5 is K-Z or dK-Z; X7 is 7MeW, W, 3Pya, 7(2ClPh)W, 7(3(lNMepip)pyraz)W, 7(3(6AzaIndlMe))W, 7(3CF3TAZP)W, 7(3NAcPh)W, 7(3NPyrazPh)W, 7(3NpyrlonePh)W, 7(3UrPh)W, 7(4(CpCNPh))W, 7(4CF3Ph)W, 7(4NAcPh)W, 7(40CF3Ph)W, 7(40MePh)W, 7(4Paz)W, 7(5(2(40MePh)Pyr))W, 7(5(Ina7Pyr))W, 7(6( 1 )7 dMeND AZ)) W, 7(6(2MeNDAZ))W, 7(7(124TAZP))W, 7(7Imzpy)W, 7BrW, 7EtW, 7PhW, 7PyrW, A, DT, or D7MeW; X8 is KAc, dK(Ac), K or dK; X9 is Pen, Abu, aMeC,or C; XI 0 is AEF or dAEF; XI 1 is 2-Nal, Phe(2-Me), Phe(3-Me), Phe(4-Me), Phe(3,4-dimethoxy), 2Quin, 3Quin, 1-Nal, unsubstituted Trp, or Trp substituted with cyano, halo, alkyl, haloalkyl, hydroxy, or alkoxy;X15 is 3Pya, 3MeH, H, F, hF, Y, dY, Y(CHF2), PAF, oAMPhe, F(CF3), dPaf, D3Pya, ACIPA(SR), 60H3Pya, 5PyrimidAla, 5MePyridinAla, 5MeH, 5AmPyridinAla, 4TriazolAla, 4PyridinAla, 4Pya, 3QuinolAla, 30HPhe, 3AmPyrazolAla, 2AmTyr, or IMeH; XI 3 is K(Ac), d(KAc), E, or dE; XI 5 is absent, 3pya, 3MeH, H, F, hF, Y, dY, Y(CHF2), PAF, oAMPhe, F(CF3), dPaf, D3Pya, ACIPA(SR), 60H3Pya, 5PyrimidAla, 5MePyridinAla, 5MeH, 5AmPyridinAla, 4TriazolAla, 4PyridinAla, 4Pya, 3QuinolAla, 30HPhe, 3AmPyrazolAla, 2AmTyr, or IMeH; XI 6 is meG, 4(R)HydroxyPro, 4(S)AminoPro, 4diFPro, 5(R)diMePro, aMeP, N(3AmBenzyl)Gly, N(Cyclohexyl)Gly, N(Isobutyl)Gly, P,or dP; R2 is -OH, -NH2, -NH(C1 to C4 alkyl), -NH(C1-C4 alkyl), or -N(C1 to C4 alkyl)2, each alkyl optionally substituted with Cl, F, or cyano; and Z is group comprising a lipid moiety; and wherein the IL-23R inhibitor is cyclized by a disulfide or thioether first bond between X4 and X9.

2. An interleukin-23 receptor inhibitor comprising an amino acid sequence of Formula II R1-X3-X4-X5-T-X7-X8-X9-X10-X11-X12-X13-X14-X15-X16-X17-R2 (II) wherein: R1 is hydrogen, Cl to C4 alkyl C(O)-, or Cl to C4 alkyl C(O)- substituted with Cl, F, or cyano, 5Ava, AEEP, cPEG3aCO, C12gEPEG2PEG2CO, C14gEPEG2PEG2CO orZ; X3 is dR, dK, dK(d), or absent; X4 is Pen, Abu, aMeC, or C; X5 is L, N, aMeN, dK, dK(d), E, or K; X7 is 7MeW, W, 3Pya, 7(2ClPh)W, 7(3(lNMepip)pyraz)W, 7(3(6AzaIndlMe))W, 7(3CF3TAZP)W, 7(3NAcPh)W, 7(3NPyrazPh)W, 7(3NpyrlonePh)W, 7(3UrPh)W, 7(4(CpCNPh))W, 7(4CF3Ph)W, 7(4NAcPh)W, 7(40CF3Ph)W, 7(40MePh)W, 7(4Paz)W, 7(5(2(40MePh)Pyr))W, 7(5(Ina7Pyr))W, 7(6( 1 )7 dMeND AZ)) W, 7(6(2MeNDAZ))W, 7(7(124TAZP))W, 7(7Imzpy)W, 7BrW, 7EtW, 7PhW, 7PyrW, A, DT, or D7MeW; X8 is K dK, K-Z, or dK-Z; X9 is Pen, C, aMeC, Abu; XI 0 is AEF, F, or F40Me; XI 1 is 2-Nal, Phe(2-Me), Phe(3-Me), Phe(4-Me), Phe(3,4-dimethoxy), 2Quin, 3Quin, 1-Nal, unsubstituted Trp, or Trp substituted with cyano, halo, alkyl, haloalkyl, hydroxy, or alkoxy; XI 2 is THP or aMeL; XI 3 is E, L, KAc, dK, K, dL, dKAc, or dE; XI 4 is N, L, dN, or dL; XI 5 is 3Pya, 3MeH, H, F, hF, Y, dY, Y(CHF2), PAF, oAMPhe, F(CF3), dPaf, D3Pya, ACIPA(SR), 60H3Pya, 5PyrimidAla, 5MePyridinAla, 5MeH, 5AmPyridinAla, 4TriazolAla, 4PyridinAla, 4Pya, 3QuinolAla, 30HPhe, 3AmPyrazolAla, 2AmTyr, IMeH or NH(2-(pyridine-3-yl)ethyl); XI 6 is meG, 4(R)HydroxyPro, 4(S)AminoPro, 4diFPro, 5(R)diMePro, aMeP, N(3AmBenzyl)Gly, N(Cyclohexyl)Gly, N(Isobutyl)Gly, P,or dP, or absent; X17 is absent or (PEG2PEG2PEG2PEG2gEC12), K(PEG2PEG2gEC12); and R2 is -OH -NH2, -NH(C1 to C4 alkyl), -H(C1-C4 alkyl), -N(C1 to C4 alky 1)2, each alkyl optionally substituted with Cl, F, or cyano or K(PEG2PEG2gEC12); and Z is group comprising a lipid moiety; and wherein the IL-23R inhibitor is cyclized by a disulfide or thioether first bond between X4 and X9, and an amide second bond when X5 is E and XI 0 is AEF.

3. An interleukin-23 receptor inhibitor comprising an amino acid sequence of Formula III R1-X3-X4-X5-T-X7-X8-X9-X10-X11-THP-X13-X14-X15-X16- R2 (III) wherein: R1 is hydrogen, Cl to C4 alkyl C(O)-, or Cl to C4 alkyl C(O)- substituted with Cl, F, or cyano, or X3 is dR or absent; X4 is Pen, Abu, aMeC, C; X5 is N or dN; X7 is 7MeW, W, 3Pya, 7(2ClPh)W, 7(3(lNMepip)pyraz)W, 7(3(6AzaIndlMe))W, 7(3CF3TAZP)W, 7(3NAcPh)W, 7(3NPyrazPh)W, 7(3NpyrlonePh)W, 7(3UrPh)W, 7(4(CpCNPh))W, 7(4CF3Ph)W, 7(4NAcPh)W, 7(40CF3Ph)W, 7(40MePh)W, 7(4Paz)W, 7(5(2(40MePh)Pyr))W, 7(5(Ina7Pyr))W, 7(6( 1 )7 dMeND AZ)) W, 7(6(2MeNDAZ))W, 7(7(124TAZP))W, 7(7Imzpy)W, 7BrW, 7EtW, 7PhW, 7PyrW, A, DT, or D7MeW; X8 is KAc; X9 is Pen, Abu, aMeC, C; XIO is F-Z or AEF-Z; XI 1 is 2-Nal, Phe(2-Me), Phe(3-Me), Phe(4-Me), Phe(3,4-dimethoxy), 2Quin, 3Quin, 1-Nal, unsubstituted Trp, or Trp substituted with cyano, halo, alkyl, haloalkyl, hydroxy, or alkoxy; XI 3 is K(Ac) dK(Ac). dE, or E; X14 is L or N; XI 5 is 3Pya, 3MeH, H, F, hF, Y, dY, Y(CHF2), PAF, oAMPhe, F(CF3), dPaf, D3Pya, ACIPA(SR), 60H3Pya, 5PyrimidAla, 5MePyridinAla, 5MeH, 5AmPyridinAla, 4TriazolAla, 4PyridinAla, 4Pya, 3QuinolAla, 30HPhe, 3AmPyrazolAla, 2AmTyr, or IMeH; XI 6 is meG, 4(R)HydroxyPro, 4(S)AminoPro, 4diFPro, 5(R)diMePro, aMeP, N(3AmBenzyl)Gly, N(Cyclohexyl)Gly, N(Isobutyl)Gly, P,or dP; and Z is group comprising a lipid moiety; and R2 is -OH, -NH2, -NH(C1 to C4 alkyl), -NH(C1-C4 alkyl), or -N(C1 to C4 alky 1)2, each alkyl optionally substituted with Cl, F, or cyano; and wherein the IL-23R inhibitor is cyclized by a disulfide or thioether first bond between X4 and X9.

4. An interleukin-23 receptor inhibitor comprising an amino acid sequence of Formula IV R1 -X3 -X4-X5 -T -X7 -KAc-X9-Xl 0-Xl 1-X12-X13-X14-X15-X16-R2 (IV) wherein: R1 is hydrogen, Cl to C4 alkyl C(O)-, or Cl to C4 alkyl C(O)- substituted with Cl, F, or cyano, or; X3 is dR or absent; X4 is Pen, aMeC, Abu, C; X5 is N, A, dN, dA; X7 is 7MeW, W, 3Pya, 7(2ClPh)W, 7(3(lNMepip)pyraz)W, 7(3(6AzaIndlMe))W, 7(3CF3TAZP)W, 7(3NAcPh)W, 7(3NPyrazPh)W, 7(3NpyrlonePh)W, 7(3UrPh)W, 7(4(CpCNPh))W, 7(4CF3Ph)W, 7(4NAcPh)W, 7(40CF3Ph)W, 7(40MePh)W, 7(4Paz)W, 7(5(2(40MePh)Pyr))W, 7(5(Ina7Pyr))W, 7(6( 1 )7 dMeND AZ)) W, 7(6(2MeNDAZ))W, 7(7(124TAZP))W, 7(7Imzpy)W, 7BrW, 7EtW, 7PhW, 7PyrW, A, DT, or D7MeW; X9 is Pen, Abu, aMeC, or C; XI 0 is F40Me, F4CONH2, F, 2Nal, AEF, 4AmF, or 40MeF; XI 1 is 2-Nal, Phe(2-Me), Phe(3-Me), Phe(4-Me), Phe(3,4-dimethoxy), 2Quin, 3Quin, 1-Nal, unsubstituted Trp, or Trp substituted with cyano, halo, alkyl, haloalkyl, hydroxy, or alkoxy; XI 2 is aMeK-Z, Spiral_Pip, or K-Z; XI 3 is KAc, E, A, L, dK, dKAc, dE, or dA; XI 4 is N, L, A, dN, dL, or dA; XI 5 is 3Pya, 3MeH, H, F, hF, Y, dY, Y(CHF2), PAF, oAMPhe, F(CF3), dPaf, D3Pya, ACIPA(SR), 60H3Pya, 5PyrimidAla, 5MePyridinAla, 5MeH, 5AmPyridinAla, 4TriazolAla, 4PyridinAla, 4Pya, 3QuinolAla, 30HPhe, 3AmPyrazolAla, 2AmTyr, or IMeH; XI 6 is meG, 4(R)HydroxyPro, 4(S)AminoPro, 4diFPro, 5(R)diMePro, aMeP, N(3AmBenzyl)Gly, N(Cyclohexyl)Gly, N(Isobutyl)Gly, P,or dP;and R2 is -OH, -NH2, NH(C1 to C4 alkyl), -NH(C1-C4 alkyl), -N(C1 to C4 alkyl)2, each alkyl optionally substituted with Cl, F, or cyano; and Z is group comprising a lipid moiety; and wherein the IL-23R inhibitor is cyclized by a disulfide or thioether first bond between X4 and X9.

5. An interleukin-23 receptor inhibitor comprising an amino acid sequence of Formula V R1 -X3-X4-X5 -T -X7 -X8-X9-X10-Xl 1 -THP-X13-X14-X15-X16-X17-R2 (V) wherein: R1 is hydrogen, Ci to C4 alkyl C(O)-, Ci to C4 alkyl C(O)- substituted with Cl, F, or cyano; X3 is dR, dK, or absent; X4 is Pen, Abu, or C; X5 is N, K, Q, L, dN, dK, dL,or dQ; X7 is 7MeW, W, 3Pya, 7(2ClPh)W, 7(3(lNMepip)pyraz)W, 7(3(6AzaIndlMe))W, 7(3CF3TAZP)W, 7(3NAcPh)W, 7(3NPyrazPh)W, 7(3NpyrlonePh)W, 7(3UrPh)W, 7(4(CpCNPh))W, 7(4CF3Ph)W, 7(4NAcPh)W, 7(40CF3Ph)W, 7(40MePh)W, 7(4Paz)W, 7(5(2(40MePh)Pyr))W, 7(5(Ina7Pyr))W, 7(6( 1 )7 dMeND AZ)) W, 7(6(2MeNDAZ))W, 7(7(124TAZP))W, 7(7Imzpy)W, 7BrW, 7EtW, 7PhW, 7PyrW, A, DT, or D7MeW; X8 is KAc, Q, K, dKAc, or dQ; X9 is Pen, aMeC, Abu, or C; XI 0 is AEF, AEF(G) or F40Me; XI 1 is 2-Nal, Phe(2-Me), Phe(3-Me), Phe(4-Me), Phe(3,4-dimethoxy), 2Quin, 3Quin, 1-Nal, unsubstituted Trp, or Trp substituted with cyano, halo, alkyl, haloalkyl, hydroxy, or alkoxy; XI 3 is K-Z, or dK-Z; XI 4 is N, L, dN, or dL; XI 5 is 3Pya, 3MeH, H, F, bAla, hF, Y, dY, Y(CHF2), PAF, oAMPhe, F(CF3), dPaf, D3Pya, ACIPA(SR), 60H3Pya, 5PyrimidAla, 5MePyridinAla, 5MeH, 5AmPyridinAla, 4TriazolAla, 4PyridinAla, 4Pya, 3QuinolAla, 30HPhe, 3AmPyrazolAla, 2AmTyr, or IMeH; XI 6 is meG, 4(R)HydroxyPro, 4(S)AminoPro, 4diFPro, 5(R)diMePro, aMeP, N(3AmBenzyl)Gly, N(Cyclohexyl)Gly, N(Isobutyl)Gly, P, dP or absent; XI 7 is absent, or K-Z; R2 is -OH, -NH2, -NH(C1 to C4 alkyl), -NH(C1-C4 alkyl), or -N(C1 to C4 alky 1)2, each alkyl optionally substituted with Cl, F, or cyano; and Z is group comprising a lipid moiety; and wherein the IL-23R inhibitor is cyclized by a disulfide or thioether first bond between X4 and X9.

6. An interleukin-23 receptor inhibitor comprising an amino acid sequence of Formula VI R1-X3-X4-X5-T-X7-X8-X9-X10-X11-X12-X13-X14-X15-X16-X17-R2 (VI) wherein R1 is hydrogen, Cl to C4 alkyl C(O)-, or Cl to C4 alkyl C(O)- substituted with Cl, F, or cyano, cPEG3aCO, or 6Ahx; X3 is dR, R, K, dK, dK-Z, K-Z, or absent; X4 is Pen, Abu, aMeC or C; X5 is N, or L; X7 is 7MeW, W, 3Pya, 7(2ClPh)W, 7(3(lNMepip)pyraz)W, 7(3(6AzaIndlMe))W, 7(3CF3TAZP)W, 7(3NAcPh)W, 7(3NPyrazPh)W, 7(3NpyrlonePh)W, 7(3UrPh)W, 7(4(CpCNPh))W, 7(4CF3Ph)W, 7(4NAcPh)W, 7(40CF3Ph)W, 7(40MePh)W, 7(4Paz)W, 7(5(2(40MePh)Pyr))W, 7(5(Ina7Pyr))W, 7(6( 1 )7 dMeND AZ)) W, 7(6(2MeNDAZ))W, 7(7(124TAZP))W, 7(7Imzpy)W, 7BrW, 7EtW, 7PhW, 7PyrW, A, DT, or D7MeW; X8 is KAc, Q, dKAc, or dQ; X9 is Pen, C, aMeC, or Abu; XI 0 is AEF, F40Me, or TMAPF; XI 1 is 2-Nal, Phe(2-Me), Phe(3-Me), Phe(4-Me), Phe(3,4-dimethoxy), 2Quin, 3Quin, 1-Nal, unsubstituted Trp, or Trp substituted with cyano, halo, alkyl, haloalkyl, hydroxy, or alkoxy; XI 2 is THP or Acvc, or Acpx; XI 3 is KAc, dKAc, dE or E; X14 is N or L; XI 5 is 3Pya, 3MeH, H, F, hF, Y, dY, Y(CHF2), PAF, oAMPhe, F(CF3), dPaf, D3Pya, ACIPA(SR), 60H3Pya, 5PyrimidAla, 5MePyridinAla, 5MeH, 5AmPyridinAla, 4TriazolAla, 4PyridinAla, 4Pya, 3QuinolAla, 30HPhe, 3AmPyrazolAla, 2AmTyr, THP, or IMeH; XI 6 is K-Z, nMeK-Z, N-Z, Sarc-Z, dK-Z; XI 7 is absent or K-Z;and R2 is -OH, -NH2, -NH(C1 to C4 alkyl), -NH(C1-C4 alkyl), or -N(C1 to C4 alkyl)2, each alkyl optionally substituted with Cl, F, or cyano; and Z is group comprising a lipid moiety; and wherein the IL-23R inhibitor is cyclized by a disulfide or thioether first bond between X4 and X9, and an amide second bond between R1 and XI 3 when R1 is 6Ahx and XI 3 is E.

7. An interleukin-23 receptor inhibitor comprising an amino acid sequence of Formula VII R 1 -X3 -X4 -X5-T-X7-X8-X9-X10-Xl 1 -XI 2-X13-X14-X15-X16-R2 (VII) wherein: R1 is hydrogen, Cl to C4 alkyl C(O)-, or Cl to C4 alkyl C(O)- substituted with Cl, F, or cyano, GABA, CF3CO, succiniccamitine, or cPEG3aCO, X3 is dK, K, dK-Z, or K-Z; X4 is Pen, aMeC, or C; X5 is N, L, or E; X7 is 7MeW, W, 3Pya, 7(2ClPh)W, 7(3(lNMepip)pyraz)W, 7(3(6AzaIndlMe))W, 7(3CF3TAZP)W, 7(3NAcPh)W, 7(3NPyrazPh)W, 7(3NpyrlonePh)W, 7(3UrPh)W, 7 (4(CpCNPh))W, 7(4CF3Ph)W, 7(4NAcPh)W, 7(40CF3Ph)W, 7(40MePh)W, 7(4Paz)W, 7 (5 (2(40MePh)Py r))W, 7(5(Ina7Pyr))W, 7(6(l)7dMeNDAZ))W, 7 (6(2MeND AZ))W, 7(7(124TAZP))W, 7(7Imzpy)W, 7BrW, 7EtW, 7PhW, 7PyrW, A, DT, or D7MeW; X8 is KAc, K, K(Me)3, dKAc, or dK; X9 is Pen, aMeC, or C; XI 0 is AEF, F, F(4-OMe), or TMAPF; XI 1 is 2-Nal, Phe(2-Me), Phe(3-Me), Phe(4-Me), Phe(3,4-dimethoxy), 2Quin, 3Quin, 1-Nal, unsubstituted Trp, or Trp substituted with cyano, halo, alkyl, haloalkyl, hydroxy, or alkoxy; XI 2 is THP, aMeL, Acvc, or Acpx; X13 is KAc, dKAc, L, E, dE, K(NMeAc), dK(Me)3, or K(Me)3; X14 is N or L; XI 5 is 3Pya, THP, 3MeH, H, F, hF, Y, dY, Y(CHF2), PAF, oAMPhe, F(CF3), dPaf, D3Pya, ACIPA(SR), 60H3Pya, 5PyrimidAla, 5MePyridinAla, 5MeH, 5AmPyridinAla, 4TriazolAla, 4PyridinAla, 4Pya, 3QuinolAla, 30HPhe, 3AmPyrazolAla, 2AmTyr, or IMeH; XI 6 is meG, 4(R)HydroxyPro, 4(S)AminoPro, 4diFPro, 5(R)diMePro, aMeP, N(3AmBenzyl)Gly, N(Cyclohexyl)Gly, N(Isobutyl)Gly, P, dP, Sarc, or absent; R2 is -OH, -NH2, -NH(C1 to C4 alkyl), -NH(C1-C4 alkyl), or -N(C1 to C4 alkyl)2, each alkyl optionally substituted with Cl, F, or cyano; and Z is group comprising a lipid moiety; and wherein the IL-23R inhibitor is cyclized by a disulfide first bond between X4 and X9.

8. An interleukin-23 receptor inhibitor comprising an amino acid sequence of Formula VIII R1 -X3 -X4 -X5-T-X7-X8-X9 - AEF -XI 1 -THP-X13-N-X15-X16-X17-R2 (VIII) wherein: R1 is hydrogen, Cl to C4 alkyl C(O)-, or Cl to C4 alkyl C(O)- substituted with Cl, F, or cyano, C12gEPEG2PEG2CO, ClAcPEG4CO; X3 is dR , R, dK(SP6), K(SP6), K, or dK; X4 is Pen, Abu, aMeC or C; X5 is N or E; X7 is 7MeW, W, 3Pya, 7(2ClPh)W, 7(3(lNMepip)pyraz)W, 7(3(6AzaIndlMe))W, 7(3CF3TAZP)W, 7(3NAcPh)W, 7(3NPyrazPh)W, 7(3NpyrlonePh)W, 7(3UrPh)W, 7 (4(CpCNPh))W, 7(4CF3Ph)W, 7(4NAcPh)W, 7(40CF3Ph)W, 7(40MePh)W, 7(4Paz)W, 7 (5 (2(40MePh)Py r))W, 7(5(Ina7Pyr))W, 7(6(l)7dMeNDAZ))W, 7 (6(2MeND AZ))W, 7(7(124TAZP))W, 7(7Imzpy)W, 7BrW, 7EtW, 7PhW, 7PyrW, A, DT, or D7MeW; X8 is Kac; X9 is Pen, C, aMeC, or Abu; XI 1 is 2-Nal, Phe(2-Me), Phe(3-Me), Phe(4-Me), Phe(3,4-dimethoxy), 2Quin, 3Quin, 1-Nal, unsubstituted Trp, or Trp substituted with cyano, halo, alkyl, haloalkyl, hydroxy, or alkoxy; XI 3 is E, dE, K, or dK; XI 5 is 3Pya, 3MeH, H, F, hF, Y, dY, Y(CHF2), PAF, oAMPhe, F(CF3), dPaf, D3Pya, ACIPA(SR), 60H3Pya, 5PyrimidAla, 5MePyridinAla, 5MeH, 5AmPyridinAla, 4TriazolAla, 4PyridinAla, 4Pya, 3QuinolAla, 30HPhe, 3AmPyrazolAla, 2AmTyr, or IMeH; XI 6 is meG, 4(R)HydroxyPro, 4(S)AminoPro, 4diFPro, 5(R)diMePro, aMeP, N(3AmBenzyl)Gly, N(Cyclohexyl)Gly, N(Isobutyl)Gly, P, dP, or absent; XI 7 is K-Z or dK-Z; or R2 is -OH, -NH2, -NH(C1 to C4 alkyl), -NH(C1-C4 alkyl), or -N(C1 to C4 alkyl)2, each alkyl optionally substituted with Cl, F, or cyano; and Z is group comprising a lipid moiety; and wherein the IL-23R inhibitor is cyclized by a disulfide or thioether first bond between X4 and X9, and an amide second bond when X5 is E and XI 0 is AEF.

9. An interleukin-23 receptor inhibitor comprising an amino acid sequence of Formula IX R1 -X4 -X5-T-X7-X8-X9 - AEF -XI 1 -THP-X13-N-X15-X16-X17-R2 (IX) wherein: R1 is hydrogen, Cl to C4 alkyl C(O)-, or Cl to C4 alkyl C(O)- substituted with Cl, F, or cyano, 5Ava, AEEP or C14gEPEG2PEG2CO; X4 is Pen, Abu, C, aMeC, or absent; X5 is N or absent; X7 is 7MeW, W, 3Pya, 7(2ClPh)W, 7(3(lNMepip)pyraz)W, 7(3(6AzaIndlMe))W, 7(3CF3TAZP)W, 7(3NAcPh)W, 7(3NPyrazPh)W, 7(3NpyrlonePh)W, 7(3UrPh)W, 7 (4(CpCNPh))W, 7(4CF3Ph)W, 7(4NAcPh)W, 7(40CF3Ph)W, 7(40MePh)W, 7(4Paz)W, 7 (5 (2(40MePh)Py r))W, 7(5(Ina7Pyr))W, 7(6(l)7dMeNDAZ))W, 7 (6(2MeND AZ))W, 7(7(124TAZP))W, 7(7Imzpy)W, 7BrW, 7EtW, 7PhW, 7PyrW, A, DT, or D7MeW; X8 is KAc, dK, dQ, or Q; X9 is Pen, S5H, C, or aMeC; XI 1 is 2-Nal, Phe(2-Me), Phe(3-Me), Phe(4-Me), Phe(3,4-dimethoxy), 2Quin, 3Quin, 1-Nal, unsubstituted Trp, or Trp substituted with cyano, halo, alkyl, haloalkyl, hydroxy, or alkoxy; XI 3 is E, KAc, dK(d), S5H, dE, dK(Ac), dK, or R5H; XI 5 is 3Pya, 3MeH, H, F, hF, Y, dY, Y(CHF2), PAF, oAMPhe, F(CF3), dPaf, D3Pya, ACIPA(SR), 60H3Pya, 5PyrimidAla, 5MePyridinAla, 5MeH, 5AmPyridinAla, 4TriazolAla, 4PyridinAla, 4Pya, 3QuinolAla, 30HPhe, 3AmPyrazolAla, 2AmTyr, or IMeH; XI 6 is Sarc, 4(R)HydroxyPro, 4(S)AminoPro, 4diFPro, 5(R)diMePro, aMeP, N(3AmBenzyl)Gly, N(Cyclohexyl)Gly, N(Isobutyl)Gly, P,or dP; XI 7 is K-Z; R2 is -OH, -NH2, -NH(C1 to C4 alkyl), -NH(C1-C4 alkyl), or -N(C1 to C4 alky 1)2, each alkyl optionally substituted with Cl, F, or cyano; and Z is group comprising a lipid moiety; and wherein the IL-23R inhibitor is cyclized by a disulfide or thioether first bond between X4 and X9 or an aliphatic bond (generated from a Ring Closing Metathesis “RCM” reaction) between X9 and XI 3 when both residues are S5H.

10. An interleukin-23 receptor inhibitor comprising an amino acid sequence of Formula X Rl- X3 -X4-X5 -T -X7 -X8-X9-X 10-X11-X12-X13-X14-X15-X16-X17-R2 (X) wherein: Rl is hydrogen, Cl to C4 alkyl C(O)-, or Cl to C4 alkyl C(O)- substituted with Cl, F, or cyano, 7Ahp, 6Ahx, 5Ava, 6Ava, AEEP, GABA, succinylcamitine. cPEG3aCO, ClAcPEG4CO, lPEG2_lPEG2_IsoGlu_C18, lPEG2_lPEG2_IsoGlu_Cl 8_Diacid, PentCO, PEG12_OMe, HOC 18gEPEG2PEG2, PEG2PEG2gEC160H, PEG4_Decyl, PEG4_Lauryl, PEG4_Capryl, PEG4_Hexyl, PEG2_Palm, PEG2_Myristyl, PEG2_Lauryl, Hexyl, Decyl, PEG2_Decyl, PEG2_Capryl, Oct, PEG4_Palm, Palm, Lauryl, 1 PEG2 1 PEG2_IsoGlu_C 16_Diacid, HOC16gEPEG2PEG2om, or Z; X3 is dR, dK, dK-Z, or absent; X4 is Pen, aMeC, Abu, or C; X5 is N, L, Q, K, E, aMeN, dN, dL, dQ, dK, dE, K-Z, or dK-Z; X7 is 7MeW, W, 3Pya, 7(2ClPh)W, 7(3(lNMepip)pyraz)W, 7(3(6AzaIndlMe))W, 7(3CF3TAZP)W, 7(3NAcPh)W, 7(3NPyrazPh)W, 7(3NpyrlonePh)W, 7(3UrPh)W, 7 (4(CpCNPh))W, 7(4CF3Ph)W, 7(4NAcPh)W, 7(40CF3Ph)W, 7(40MePh)W, 7(4Paz)W, 7 (5 (2(40MePh)Py r))W, 7(5(Ina7Pyr))W, 7(6(l)7dMeNDAZ))W, 7 (6(2MeND AZ))W, 7(7(124TAZP))W, 7(7Imzpy)W, 7BrW, 7EtW, 7PhW, 7PyrW, A, DT, or D7MeW; X8 is KAc, dK(Ac), dQ, or Q; X9 is Pen, C, aMeC, or Abu; XI 0 is AEF, F40Me, F(4-CONH2), TMAPF, AEF(G), or F; XI 1 is 2-Nal, Phe(2-Me), Phe(3-Me), Phe(4-Me), Phe(3,4-dimethoxy), 2Quin, 3Quin, 1-Nal, unsubstituted Trp, or Trp substituted with cyano, halo, alkyl, haloalkyl, hydroxy, or alkoxy; XI 2 is THP, aMeL, Acvc, Acpx, aMeK, or aMeK-Z; XI 3 is K(Ac), dK(Ac), E, dE, L, dL, dK-Z, or K-Z; XI 4 is N, K, or K-Z; XI 5 is 3Pya, 3MeH, H, F, hF, Y, dY, Y(CHF2), PAF, oAMPhe, F(CF3), dPaf, D3Pya, ACIPA(SR), 60H3Pya, 5PyrimidAla, 5MePyridinAla, 5MeH, 5AmPyridinAla, 4TriazolAla, 4PyridinAla, 4Pya, 3QuinolAla, 30HPhe, 3AmPyrazolAla, 2AmTyr, THP, NH(2-(pyridin-3-yl)ethyl), bAla, THP, aMeF, or IMeH; XI 6 is Sarc, K-Z, NMeK-Z, or absent; XI 7 is K-Z, dK-Z, or absent; R2 is -OH, -NH2, -NH(C1 to C4 alkyl), -NH(C1-C4 alkyl), or -N(C1 to C4 alkyl)2, each alkyl optionally substituted with Cl, F, cyano or Z; Z is group comprising a lipid moiety; and wherein the IL-23R inhibitor is cyclized by a disulfide or thioether first bond between X4 and X9, and an amide second bond (i) between X5 and XI 0 when X5 is E and X10 is AEF, or (ii) between X13 and R1 when X13 is E and R1 is 7Ahp, 6Ahx, 5Ava, 6Ava, AEEP, or GABA.

11. A interleukin-23 receptor inhibitor selected from Table 1 A, Table IB, Table 1C, Table ID, Table IE, Table IF, Table 1G, Table 1H, Table II, Table 1J, Table IK, Table 1L, or Table 1M respectively.

12. Example 2 (compound 2 SEQ ID NO:2); Example (SEQ ID NO:4); Example 11 (SEQ ID NO:ll); Example 17 (SEQ ID NO:17); Example 18 (SEQ ID NO:18); Example 19 (SEQ ID NO: 19); Example 20 SEQ ID NO:20); Example 21 SEQ ID NO:21); Example 23 (SEQ ID NO:23); and Example 24 (SEQ ID NO:24).

13. A pharmaceutical composition comprising: (i) an interleukin-23 receptor inhibitor or pharmaceutically acceptable salt, solvate, or form thereof, according to any of claims 1 to 10, and (ii) a pharmaceutically acceptable carrier, excipient, or diluent.

14. A pharmaceutical composition which comprises: (i) an interleukin-23 receptor inhibitor or pharmaceutically acceptable salt, solvate, or form thereof, according to claim 11, and (ii) a pharmaceutically acceptable carrier, excipient, or diluent.

15. A pharmaceutical composition which comprises: (i) an interleukin-23 receptor inhibitor or pharmaceutically acceptable salt, solvate, or form thereof according to claim 12: and (ii) a pharmaceutically acceptable carrier, excipient, or diluent.

16. The use of an interleukin-23 receptor inhibitor or compound according to any of claims 1 to 12, or a pharmaceutical composition according to any of claims 13 to 15, for the preparation of a medicament for the treatment of an inflammatory disorder or autoimmune inflammatory disorder.

17. The use of claim 16, for the preparation of a medicament for the treatment of autoimmune inflammation and related diseases and disorders including, but not limited to: multiple sclerosis, asthma, rheumatoid arthritis, inflammation of the gut, inflammatory bowel diseases (IBDs), juvenile IBD, adolescent IBD, Crohn’s disease, ulcerative colitis, Celiac disease (nontropical Sprue), microscopic colitis, collagenous colitis, eosinophilic gastroenteritis/esophagitis, colitis associated with radio- or chemo therapy, colitis associated with disorders of innate immunity as in leukocyte adhesion deficiency- 1, sarcoidosis, Systemic Lupus Erythematosus, ankylosing spondylitis (axial spondyloarthritis), psoriatic arthritis, psoriasis (e.g., plaque psoriasis, guttate psoriasis, inverse psoriasis, pustular psoriasis, Palmo-Plantar Pustulosis, psoriasis vulgaris, or erythrodermic psoriasis), atopic dermatitis, acne ectopica, enteropathy associated with seronegative arthropathies, chronic granulomatous disease, glycogen storage disease type lb, Hermansky-Pudlak syndrome, Chediak-Higashi syndrome, Wiskott-Aldrich Syndrome, pouchitis, pouchitis resulting after proctocolectomy and ileoanal anastomosis, gastrointestinal cancer, pancreatitis, insulin-dependent diabetes mellitus, mastitis, cholecystitis, cholangitis, primary biliary cirrhosis, viral-associated enteropathy, pericholangitis, chronic bronchitis, chronic sinusitis, asthma, uveitis, or graft versus host disease.

18. The use of claim 16 for the preparation of a medicament for the treatment of a disease or disorder selected from Inflammatory Bowel Disease (IBD), Ulcerative colitis (UC), Crohn’s Disease (CD), psoriasis (PsO) or psoriatic arthritis (PsA).

19. A method for treating a disease or disorder associated with Interleukin 23 (IL- 23)/Interleukin 23 Receptor (IL-23R), which comprises administering: (i) an effective amount of a peptide inhibitor of an interleukin-23 receptor, or a pharmaceutically acceptable salt, solvate, or form thereof according to any of claims 1 to 12, or (ii) a pharmaceutical composition according to any of claims 13 to 15, respectively to a patient in need thereof.

20. The method of claim 19, wherein the disease or disorder is associated with autoimmune inflammation.

21. The method of claim 20, wherein the disease or disorder is multiple sclerosis, asthma, rheumatoid arthritis, inflammation of the gut, inflammatory bowel diseases (IBDs), juvenile IBD, adolescent IBD, Crohn’s disease, ulcerative colitis, Celiac disease (nontropical Sprue), microscopic colitis, collagenous colitis, eosinophilic gastroenteritis/esophagitis, colitis associated with radio- or chemo-therapy, colitis associated with disorders of innate immunity as in leukocyte adhesion deficiency- 1, sarcoidosis, Systemic Lupus Erythematosus, ankylosing spondylitis (axial spondyloarthritis), psoriatic arthritis, psoriasis (e.g., plaque psoriasis, guttate psoriasis, inverse psoriasis, pustular psoriasis, Palmo-Plantar Pustulosis, psoriasis vulgaris, or erythrodermic psoriasis), atopic dermatitis, acne ectopica, enteropathy associated with seronegative arthropathies, chronic granulomatous disease, glycogen storage disease type lb, Hermansky-Pudlak syndrome, Chediak-Higashi syndrome, Wiskott-Aldrich Syndrome, pouchitis, pouchitis resulting after proctocolectomy and ileoanal anastomosis, gastrointestinal cancer, pancreatitis, insulin-dependent diabetes mellitus, mastitis, cholecystitis, cholangitis, primary biliary cirrhosis, viral-associated enteropathy, pericholangitis, chronic bronchitis, chronic sinusitis, asthma, uveitis, or graft versus host disease.

22. The method of claim 20, wherein the disease or disorder is associated with Ulcerative colitis (UC), Crohn’s Disease (CD), psoriasis (PsO), or psoriatic arthritis (PsA).
```

---

#### 4.4 WO2024155552A1 ☑️부분교차검증 (차이 19개)

> **💡 핵심 요약** &nbsp;|&nbsp; **유형:** formulation(제형), compound·물질(peptide), use·치료방법
> 
> **무엇을 청구하나:** 지질화(lipidated) IL-23R 펩타이드와 흡수촉진제를 함유하는 경구 제형(claim 1) 및 그 펩타이드 구조(Formula A/B, 단일·이중고리, 3Pya 고정, PEG/지질 치환)와 흡수촉진제 비율·생체이용률, 치료용도·치료방법을 청구
> 
> **핵심 권리범위:** 지질화 펩타이드 + 흡수촉진제(SNAC/LC/sodium caprate/octanoate 등) 경구 제형; 흡수촉진제:펩타이드 중량비 약 1~200, 약 10:1 등; Formula A/B: X4-X9 등 고리화, 3Pya 고정, Zlipid/Zpeg 치환, 2차 고리 옵션; 경구 생체이용률 약 2~500배 개선 — ※claim 1 verbatim은 GP 추출본에서 누락(claim 2부터 수록)
> 
> **독립항:** 1, 69, 73, 76 &nbsp;|&nbsp; **적응증:** IBD/UC/CD/건선/건선성관절염 등 자가면역 염증질환 &nbsp;|&nbsp; **검증:** ☑️부분교차검증(차이19) &nbsp;|&nbsp; **추정만료:** PCT(term N/A)


| 항목 | 내용 |
|---|---|
| 특허번호 | WO2024155552A1 (PCT 공개, A1) |
| 제목 | FORMULATIONS OF LIPIDATED PEPTIDE INHIBITORS OF INTERLEUKIN-23 RECEPTOR |
| 국제출원 / 공개 | PCT/US2024/011549, 국제출원일 2024-01-15 |
| 우선일 | 2023-01-16 (US Provisional 63/480,068) |
| 출원인/양수인 | Janssen Pharmaceutica NV (Protagonist 미표기) |
| 발명자 | David A. Lane (et al.) |
| 권위 만료일 | PCT 자체 만료 **N/A**; 추정 국내단계 2043~2044 (우선일/출원일+20년) |
| 교차검증 | GP=78, FPO=79, both=78, agree=59, **substantive_diff=19** → ☑️부분교차검증 |

**[ANALYSIS] (한국어)**

lipidated 펩타이드의 **경구 제제(oral formulation)** PCT. 주의: GP 청구항 본문이 **2번부터 시작**한다(청구항 1이 GP `/en` 텍스트에 누락 — 원문 보존, 1번은 GP PDF/원본 확인 필요). 청구항 2 이하는 Formula (A) 지질화 펩타이드와 그 경구 제제를 청구하며, 후반부(77~79)는 광범위 자가면역/염증 질환 치료방법이다. GP↔FPO 공통 78개 중 59개 일치, 19개 차이로 ☑️부분교차검증이며 권위 소스는 GP. (FPO 79 vs GP 78의 1건 차이도 존재.)

**[VERBATIM] — 출처: Google Patents (`work/05_gp_authoritative/WO2024155552A1.md`)**

```text
2. The oral pharmaceutical formulation of claim 1, wherein the lipidated peptide comprises the amino acid sequence of Formula (A): R1a-X3-X4-X5-X6-X7-X8-X9-X10-X11-X12-X13-X14-3Pya-X16-X17-R2a (A), or a pharmaceutically acceptable salt thereof, wherein: R1a is an N-terminal capping group (e.g., MeCO), Zpeg, or Zlipid; X3 is any amino acid or absent; X4 is 4AminoPro, Abu, aG, aMeC, C, Dap, Pen, Pen(oXyl), Pen(mXyl), Pen(pXyl), or Pra; X5 is any amino acid; X6 is any amino acid; X7 is 7MeW, W, or absent; X8 is any amino acid; X9 is aMeC, aG, C, D, E, hE, Pen, Dap, or Dap(N3) X10 is AEF, TMAPF, AEF(d), TMAPF-Zlipid, APEG3F, or AEF-Zlipid; X11 is any amino acid; X12 is any amino acid; X13 is any amino acid; X14 is any amino acid; X16 is any amino acid; X17 is any amino acid or absent; R2a is a C-terminal capping group (e.g., CONH2), CONH-Zpeg, or CO-Zlipid; Zpeg, independently for each occurrence, is a polyethylene glycol chain; Zlipid, independently for each occurrence, is a lipophilic substituent; wherein the peptide comprises a linkage between the residues at X4 and X9; and wherein the polypeptide comprises at least one lipophilic substituent at a position selected from R1, X3, X5, X6, X8, X10, X12, X13, X14, X16, X17, or R2.

3. The oral pharmaceutical formulation of claim 2, wherein: R1a is MeCO, Zpeg, Zlipid, succiniccarn, 5cpaCO, or AEEP-Zlipid; X3 is R, K-Zlipid, Dab-Zlipid, NMeK-Zlipid, or absent; X4 is 4AminoPro, Abu, aG, aMeC, C, Dap, Pen, Pen(oXyl), Pen(mXyl), Pen(pXyl), or Pra; X5 is N, N(NMe2), K(d), K-Zlipid, Dab-Zlipid, or NMeK-Zlipid; X6 is T, K-Zlipid, NMeK-Zlipid, or Dab-Zlipid; X7 is 7MeW, W, or absent; X8 is K(Ac), K(d), K(NMeAc), Q, K-Zlipid, K-Zpeg, NMeK-Zlipid, Dab-Zlipid, Dab(NMecarn), or Dab-Zpeg; X9 is aMeC, aG, C, D, E, hE, Pen, Dap, or Dap(N3); X10 is AEF, TMAPF, AEF(d), TMAPF-Zlipid, APEG3F, or AEF-Zlipid; X11 is a substituted or unsubstituted 2Nal or a substituted or unsubstituted 3Quin, X12 is THP, K-Zlipid, Dab-Zlipid, or NMeK-Zlipid; X13 is E, K(Ac), K(d), K-Zpeg, K(NMeAc), Dab(NMecarn), E(OAll), K-Zlipid, Dab- Zlipid, NMeK-Zlipid, or absent; X14 is N, K-Zlipid, NMeK-Zlipid, or Dab-Zlipid X16 is Sar, NMeK(d), K-Zlipid, Dab-Zlipid, or NMeK-Zlipid; X17 is K-Zlipid, Dab-Zlipid, NMeK-Zlipid, or absent; and R2 is CONH2, CONMe2, CONH-Zpeg, or CO-Zlipid.

4. The oral pharmaceutical composition of claim 1, wherein the lipidated peptide comprises the amino acid sequence of Formula (B): R1a-X3-X4-X5-X6-X7-X8-X9-X10-X11-X12-X13-X14-3Pya-X16-X17-R2a (B), or a pharmaceutically acceptable salt thereof, wherein: R1a is an N-terminal capping group (e.g., MeCO), Zpeg, or Zlipid; X3 is any amino acid or absent; X4 is any amino acid; X5 is any amino acid; X6 is any amino acid; X7 is 7MeW or W; X8 is any amino acid; X9 is any amino acid; X10 is AEF, TMAPF, AEF(d), TMAPF-Zpeg, TMAPF-Zlipid, APEG3F, AEF-Zpeg, or AEF-Zlipid; X11 is any amino acid; X12 is any amino acid; X13 is any amino acid; X14 is any amino acid; X16 is any amino acid; X17 is any amino acid or absent; R2a is a C-terminal capping group (e.g., CONH2), CONH-Zpeg, or CO-Zlipid; Zpeg, independently for each occurrence, is a polyethylene glycol chain; Zlipid, independently for each occurrence, is a lipophilic substituent; wherein the polypeptide comprises at least one lipophilic substituent or polyethylene glycol chain at a position selected from R1a, X3, X4 X5, X6, X8, X9 X10, X11, X12, X13, X14, X16, X17, or R2a; and wherein the peptide is cyclized to form a first ring, wherein the first ring comprises 4- 14 amino acids.

5. The oral pharmaceutical composition of claim 4, wherein the first ring comprises 4-9 or 11 amino acids.

6. The oral pharmaceutical composition of claim 4, wherein the first ring is formed between X4 and X9, X4 and X13, X5 and X10, X3 and X13, or X6 and X9.

7. The oral pharmaceutical composition of claim 4, wherein the first ring is formed between X4 and X9, X4 and X13, or X6 and X9.

8. The oral pharmaceutical composition of claim 7, wherein the first ring is formed between X4 and X9 via a linker having one or more groups selected from the group consisting of a disulfide, thioether, amide, olefin, ether, alkylene, and triazole.

9. The peptide of claim 7, wherein the first ring is formed between X4 and X13 via a linker having one or more groups selected from the group consisting of a disulfide, thioether, amide, olefin, ether, alkylene, and triazole.

10. The peptide of claim 7, wherein the first ring is formed between X6 and X9 via a linker having one or more groups selected from the group consisting of a disulfide, thioether, amide, olefin, ether, alkylene, and triazole.

11. The peptide of any one of claims 4-10, wherein the peptide is further cyclized to form a second ring comprising 4-14 amino acids.

12. The peptide of claim 11, wherein the second ring comprises 4, 6, 10, or 11 amino acids.

13. The peptide of claim 8, wherein the peptide is further cyclized to form a second ring, wherein: the second ring is formed between X3 and X13 via a linker having one or more groups selected from the group consisting of a disulfide, thioether, amide, olefin, ether, alkylene, and triazole; the second ring is formed between X5 and X10 via a linker having one or more groups selected from the group consisting of a disulfide, thioether, amide, olefin, ether, alkylene, and triazole; the second ring is formed between X10 and X13 via a linker having one or more groups selected from the group consisting of a disulfide, thioether, amide, olefin, ether, alkylene, and triazole; or the second ring is formed between X13 and the N-terminus of the peptide via a linker having one or more groups selected from the group consisting of a disulfide, thioether, amide, olefin, ether, alkylene, and triazole.

14. The peptide of claim 9, wherein the peptide is further cyclized to form a second ring, wherein: the second ring is formed between X5 and X10 via a linker having one or more groups selected from the group consisting of a disulfide, thioether, amide, olefin, ether, alkylene, and triazole; or the second ring is formed between X6 and X9 via a linker having one or more groups selected from the group consisting of a disulfide, thioether, amide, olefin, ether, alkylene, and triazole.

15. The peptide of claim 10, wherein the peptide is further cyclized to form a second ring, wherein: the second ring is formed between X3 and X13 via a linker having one or more groups selected from the group consisting of a disulfide, thioether, amide, olefin, ether, alkylene, and triazole; the second ring is formed between X4 and X13 via a linker having one or more groups selected from the group consisting of a disulfide, thioether, amide, olefin, ether, alkylene, and triazole; the second ring is formed between X5 and X10 via a linker having one or more groups selected from the group consisting of a disulfide, thioether, amide, olefin, ether, alkylene, and triazole; the second ring is formed between X10 and X13 via a linker having one or more groups selected from the group consisting of a disulfide, thioether, amide, olefin, ether, alkylene, and triazole; or the second ring is formed between X13 and the N-terminus of the peptide via a linker having one or more groups selected from the group consisting of a disulfide, thioether, amide, olefin, ether, alkylene, and triazole.

16. The oral pharmaceutical composition of claim 4, or a pharmaceutically acceptable salt thereof, wherein: R1a is an N-terminal capping group (e.g., MeCO), Zpeg, or Zlipid; X3 is r, k(d), k-Zlipid, dab-Zlipid, NMek-Zlipid, or absent; X4 is 4AminoPro, Abu, aG, aMeC, C, Dap, Pen, Pen(oXyl), Pen(mXyl), Pen(pXyl), or Pra; X5 is E, N, N(NMe2), K(d), K-Zlipid, Dab-Zlipid, or NMeK-Zlipid; X6 is T, K-Zlipid, NMeK-Zlipid, or Dab-Zlipid; X7 is 7MeW or W; X8 is K(Ac), K(d), K(NMeAc), Q, K-Zlipid, K-Zpeg, NMeK-Zlipid, Dab-Zlipid, Dab(NMecarn), or Dab-Zpeg; X9 is aMeC, aG, C, D, E, hE, Pen, Dap, or Dap(N3); X10 is AEF, TMAPF, AEF(d), TMAPF-Zpeg, TMAPF-Zlipid, APEG3F, AEF-Zpeg, or AEF-Zlipid; X11 is 2Nal or 6OH2Nal; X12 is THP, K-Zlipid, Dab-Zlipid, or NMeK-Zlipid; X13 is E, K(Ac), K(d), K-Zpeg, K(NMeAc), Dab(NMecarn), E(OAll), K-Zlipid, Dab- Zlipid, NMeK-Zlipid; X14 is N, K-Zlipid, NMeK-Zlipid, or Dab-Zlipid; X16 is Sar, NMeK(d), K-Zlipid, Dab-Zlipid, NMeK-Zlipid, or absent; X17 is K-Zlipid, Dab-Zlipid, NMeK-Zlipid, or absent; R2a is a C-terminal capping group (e.g., CONH2), CONH-Zpeg, or CO-Zlipid; Zpeg, independently for each occurrence, is a polyethylene glycol chain; Zlipid, independently for each occurrence, is a lipophilic substituent; wherein the peptide comprises a linkage between the residues at X4 and X9; and wherein the polypeptide comprises at least one lipophilic substituent at a position selected from R1a, X3, X5, X6, X8, X10, X12, X13, X14, X16, X17, or R2a, or a polyethylene glycol chain at a position selected from R1a, X8, X10, X13, or R2a.

17. The oral pharmaceutical composition of claim 4 or claim 16, wherein: R1a is an MeCO, Zpeg, Zlipid, or 5cpaCO; X3 is r, k(d), k-Zlipid, dab-Zlipid, NMek-Zlipid, or absent; X4 is Pen; X5 is E, N, N(NMe2), K-Zlipid, Dab-Zlipid, or NMeK-Zlipid; X6 is T; X7 is 7MeW; X8 is K(Ac), K(d), K(NMeAc), K-Zlipid, K-Zpeg, NMeK-Zlipid, Dab-Zlipid, or Dab-Zpeg; X9 is Pen; X10 is AEF, TMAPF, APEG3F, AEF-Zpeg, or AEF-Zlipid; X11 is 2Nal or 6OH2Nal; X12 is THP; X13 is E, K(Ac), K-Zpeg, K(NMeAc), K-Zlipid, Dab-Zlipid, or NMeK-Zlipid; X14 is N; X16 is Sar or NMeK-Zlipid; X17 is K-Zlipid, Dab-Zlipid, NMeK-Zlipid, or absent; R2a is CONH2, CONMe2, CONH-Zpeg, or CO-Zlipid; wherein the peptide comprises a disulfide linkage between the residues at X4 and X9; and wherein the polypeptide comprises at least one lipophilic substituent at a position selected from R1a, X3, X5, X8, X10, X13, X16, X17, or R2a, or a polyethylene glycol chain at a position selected from R1a, X8, X10, X13, or R2a.

18. The oral pharmaceutical formulation of claim 1, wherein the lipidated peptide is a compound having a formula of

19. The oral pharmaceutical formulation of claim 18, wherein the lipidated peptide is a compound having a formula of

20. The oral pharmaceutical formulation of claim 18, wherein the compound is a compound having a formula of

21. The oral pharmaceutical formulation of claim 18, wherein the compound is a compound having a formula of

22. The oral pharmaceutical formulation of claims 18-21, wherein each lipid moiety or lipophilic substituent is independently selected from a Z1 to Z5 group: Z1 is

23. The oral pharmaceutical formulation of claims 18-21, wherein each lipid moiety or lipophilic substituent is ,

24. The oral pharmaceutical formulation of any one of claims 18-23, wherein R2 is methyl.

25. The oral pharmaceutical formulation of any one of claims 18-24, wherein R3 is H.

26. The oral pharmaceutical formulation of any one of claims 18-25, wherein R4 is H.

27. The oral pharmaceutical formulation of any one of claims 18-26, wherein R5 is H.

28. The oral pharmaceutical formulation of any one of claims 18-27, wherein R8 is H.

29. The oral pharmaceutical formulation of any one of claims 18-28, wherein R4 is H.

30. The oral pharmaceutical formulation of any one of claims 18-29, wherein R9 is H.

31. The oral pharmaceutical formulation of any one of claims 18-30, wherein R10 is -C(=O)CH3.

32. The oral pharmaceutical formulation of any one of claims 18-23, wherein the compound, or a pharmaceutically acceptable salt thereof, has a formula of

33. The oral pharmaceutical formulation of claim 32, wherein R7 is -(CH2)qC(=O)NH)NH2.

34. The oral pharmaceutical formulation of claim 33, wherein q is 3.

35. The oral pharmaceutical formulation of claim 34, wherein the compound has a formula of

36. The oral pharmaceutical formulation of claim 35, wherein the compound, or a pharmaceutically acceptable salt thereof, has a formula of

37. The oral pharmaceutical formulation of claim 32, wherein R6 is -C(=O)CH3.

38. The oral pharmaceutical formulation of claim 37, wherein R7 is -(CH2)pNHR12.

39. The oral pharmaceutical formulation of claim 38, wherein p is 4.

40. The oral pharmaceutical formulation of claim 39, wherein the compound, or a pharmaceutically acceptable salt thereof, has a formula of

41. The oral pharmaceutical formulation of claim 40, wherein the compound, or a pharmaceutically acceptable salt thereof, has a formula of

42. The oral pharmaceutical formulation of any one of claims 18-23, wherein the compound, or a pharmaceutically acceptable salt thereof, has a formula of

43. The oral pharmaceutical formulation of claim 42, wherein R1 is

44. The oral pharmaceutical formulation of claim 43, wherein m is 4.

45. The oral pharmaceutical formulation of claim 44, wherein the compound, or a pharmaceutically acceptable salt thereof, has a formula of

46. The oral pharmaceutical formulation of claim 19, wherein the compound, or a pharmaceutically acceptable salt thereof, has a formula of

47. The oral pharmaceutical formulation of claim 1, wherein the lipidated peptide is selected from the group consisting of SEQ ID NOS: 1-40.

48. The oral pharmaceutical formulation of any one of claims 1-47, wherein the weight ratio (w/w) of the absorption enhancer to the lipidated peptide or a pharmaceutically acceptable salt or solvate form thereof is in a range from about 1 to about 200.

49. The oral pharmaceutical formulation of any one of claims 1-47, wherein the weight ratio (w/w) of the absorption enhancer to the lipidated peptide or a pharmaceutically acceptable salt or solvate form thereof is in a range from about 1 to about 100.

50. The oral pharmaceutical formulation of any one of claims 1-47, wherein the weight ratio (w/w) of the absorption enhancer to the lipidated peptide or a pharmaceutically acceptable salt or solvate form thereof is in a range from about 1 to about 20.

51. The oral pharmaceutical formulation of any one of claims 1-47, wherein the weight ratio (w/w) of the absorption enhancer to the lipidated peptide or a pharmaceutically acceptable salt or solvate form thereof is in an range from about 1 to about 10.

52. The oral pharmaceutical formulation of any one of claims 1-47, wherein the ratio of the absorption enhancer to the lipidated peptide is no less than 3:1 (w/w).

53. The oral pharmaceutical formulation of any one of claims 1-47, wherein the ratio of the absorption enhancer to the lipidated peptide is between 3:1 (w/w) and 30:1 (w/w).

54. The oral pharmaceutical formulation of claim 4 of any one of claims 1-47, wherein the ratio of the absorption enhancer to the lipidated peptide is between 5:1 (w/w) and 50:1 (w/w).

55. The oral pharmaceutical formulation of any one of claims 1-47, wherein the ratio of the absorption enhancer to the lipidated peptide is about 10:1 (w/w).

56. The oral pharmaceutical formulation of any one of claims 1-55, wherein the absorption enhancer is present in an amount greater than 250 mg.

57. The oral pharmaceutical formulation of any one of claims 1-56, wherein the absorption enhancer is present in an amount less than 700 mg.

58. The oral pharmaceutical formulation of any one of claims 1-57, wherein the absorption enhancer comprises one or more of sodium caprate, sodium caprylate, sodium palmitate, sodium stearate, sodium citrate, sodium salicylate, sodium salcaprozate (SNAC), a polyethylene glycol (PEG)-modified medium chain fatty acid triglyceride of capric and caprylic acid, sucrose laurate, sodium octanoate, labrasol, and lauroyl-L-carnitine (LC).

59. The oral pharmaceutical formulation of any one of claims 1-58, wherein the absorption enhancer comprises sodium salcaprozate (SNAC).

60. The oral pharmaceutical formulation of any one of claims 1-58, wherein the absorption enhancer comprises lauroyl-L-carnitine (LC).

61. The oral pharmaceutical formulation of any one of claims 1-58, wherein the absorption enhancer comprises sodium octanoate.

62. The oral pharmaceutical formulation of any one of claims 1-58, wherein the absorption enhancer comprises sodium labrasol.

63. The oral pharmaceutical formulation of any one of claims 1-58, wherein the absorption enhancer comprises sodium caprate.

64. The oral pharmaceutical formulation of any one of claims 63, wherein the sodium caprate has a purity of at least 98%.

65. The oral pharmaceutical formulation of any one of claims 1-64, wherein the oral pharmaceutical formulation further comprises one or more pharmaceutically acceptable excipients.

66. The oral pharmaceutical formulation of any one of claims 1-65, wherein the oral pharmaceutical formulation improves oral bioavailability of the compound.

67. The oral pharmaceutical formulation of any one of claims 1-65, wherein the oral pharmaceutical formulation improves oral bioavailability of the compound by about 2 to about 500 fold.

68. The oral pharmaceutical formulation of any one of claims 1-65, wherein the oral pharmaceutical formulation improves oral bioavailability of the compound by about 2 to about 250 fold.

69. A method of increasing the bioavailability of a lipidated peptide as described in any one of claims 1-47 in a subject comprising orally administering the compound, or a pharmaceutically acceptable salt or solvate form thereof, and an absorption enhancer.

70. The method of claim 69, wherein the absorption enhancer comprises one or more of sodium caprate, sodium caprylate, sodium palmitate, sodium stearate, sodium citrate, sodium salicylate, sodium salcaprozate (SNAC), a polyethylene glycol (PEG)- modified medium chain fatty acid triglyceride of capric and caprylic acid, sucrose laurate, sodium octanoate, labrasol, and lauroyl-L-carnitine (LC).

71. The method of claims 69 or 70, wherein the compound or a pharmaceutically acceptable salt or solvate form thereof, and the absorption enhancer are co- administered.

72. The method of any one of claims 69-71, wherein the compound or a pharmaceutically acceptable salt or solvate form thereof, and the enhancer are co-administered in a pharmaceutically acceptable formulation.

73. Use of an oral pharmaceutical formulation according to any of claims 1-68 for the preparation of a medicament for the treatment of an inflammatory disorder or autoimmune inflammatory disorder.

74. The use of claim 73 for the preparation of a medicament for the treatment of autoimmune inflammation and related diseases and disorders including, but not limited to: multiple sclerosis, asthma, rheumatoid arthritis, inflammation of the gut, inflammatory bowel diseases (IBDs), juvenile IBD, adolescent IBD, Crohn’ s disease, ulcerative colitis, Celiac disease (nontropical Sprue), microscopic colitis, collagenous colitis, eosinophilic gastroenteritis/esophagitis, colitis associated with radio- or chemo-therapy, colitis associated with disorders of innate immunity as in leukocyte adhesion deficiency-1, sarcoidosis, Systemic Lupus Erythematosus, ankylosing spondylitis (axial spondyloarthritis), psoriatic arthritis, psoriasis (e.g., plaque psoriasis, guttate psoriasis, inverse psoriasis, pustular psoriasis, Palmo-Plantar Pustulosis, psoriasis vulgaris, or erythrodermic psoriasis), atopic dermatitis, acne ectopica, enteropathy associated with seronegative arthropathies, chronic granulomatous disease, glycogen storage disease type 1b, Hermansky-Pudlak syndrome, Chediak-Higashi syndrome, Wiskott-Aldrich Syndrome, pouchitis, pouchitis resulting after proctocolectomy and ileoanal anastomosis, gastrointestinal cancer, pancreatitis, insulin-dependent diabetes mellitus, mastitis, cholecystitis, cholangitis, primary biliary cirrhosis, viral-associated enteropathy, pericholangitis, chronic bronchitis, chronic sinusitis, asthma, uveitis, or graft versus host disease.

75. The use of claim 73 for the preparation of a medicament for the treatment of a disease or disorder selected from Inflammatory Bowel Disease (IBD), Ulcerative colitis (UC), Crohn’ s Disease (CD), psoriasis (PsO), and psoriatic arthritis (PsA).

76. A method for treating a disease or disorder associated with Interleukin 23 (IL- 23)/Interleukin 23 Receptor (IL-23R), which comprises administering an effective amount of a pharmaceutical formulation according to any of claims 1-68 to a patient in need thereof.

77. The method of claim 76, wherein the disease or disorder is associated with autoimmune inflammation.

78. The method of claim 77, wherein the disease or disorder is multiple sclerosis, asthma, rheumatoid arthritis, inflammation of the gut, inflammatory bowel diseases (IBDs), juvenile IBD, adolescent IBD, Crohn’ s disease, ulcerative colitis, Celiac disease (nontropical Sprue), microscopic colitis, collagenous colitis, eosinophilic gastroenteritis/esophagitis, colitis associated with radio- or chemo-therapy, colitis associated with disorders of innate immunity as in leukocyte adhesion deficiency-1, sarcoidosis, Systemic Lupus Erythematosus, ankylosing spondylitis (axial spondyloarthritis), psoriatic arthritis, psoriasis (e.g., plaque psoriasis, guttate psoriasis, inverse psoriasis, pustular psoriasis, Palmo-Plantar Pustulosis, psoriasis vulgaris, or erythrodermic psoriasis), atopic dermatitis, acne ectopica, enteropathy associated with seronegative arthropathies, chronic granulomatous disease, glycogen storage disease type 1b, Hermansky-Pudlak syndrome, Chediak-Higashi syndrome, Wiskott-Aldrich Syndrome, pouchitis, pouchitis resulting after proctocolectomy and ileoanal anastomosis, gastrointestinal cancer, pancreatitis, insulin-dependent diabetes mellitus, mastitis, cholecystitis, cholangitis, primary biliary cirrhosis, viral-associated enteropathy, pericholangitis, chronic bronchitis, chronic sinusitis, asthma, uveitis, or graft versus host disease.

79. The method of claim 78, wherein the disease or disorder is associated with Ulcerative colitis (UC), Crohn’s Disease (CD), psoriasis (PsO), or psoriatic arthritis (PsA).
```

---

### 티어 5 — 조성물 일본 대응 (청구항 미확보)

#### 5.1 JP2023145581A ⚠️미확보 (Google Patents /en 청구항 0건)

> **💡 핵심 요약** &nbsp;|&nbsp; **유형:** formulation(제형), composition(조성물), use·치료방법
> 
> **무엇을 청구하나:** CA3202226과 동일 내용의 일본 출원으로, SEQ ID NO:1(icotrokinra)을 0.1~15%(w/w)로 함유하는 경구 제형(카프린산나트륨 흡수촉진제·SMCC·장용코팅)과 그 치료·IL-23R 억제 방법을 청구(원문은 일본어; GP 블록에 청구항 번호 없어 분절 불확실)
> 
> **핵심 권리범위:** 配列番号1(SEQ ID NO:1) 0.1~15%(w/w), 아세테이트/비정질 형태; 카프린산나트륨 흡수촉진제 약 20~50%(w/w); 내상/외상 + ケイ化微結晶セルロース(SMCC) + 장용코팅; 경구 10/25/50mg 용량, IL-23R·IL-17A/F·IL-22 억제 — ※청구항 번호 분절 불확실(J-PlatPat 확인 필요)
> 
> **독립항:** —(JP: 번호불확실) &nbsp;|&nbsp; **적응증:** IBD/크론병/궤양성대장염/건선/건선성관절염 &nbsp;|&nbsp; **검증:** ⚠️부분(번호불확실) &nbsp;|&nbsp; **추정만료:** 2043-07-24


| 항목 | 내용 |
|---|---|
| 특허번호 | JP2023145581A (일본 공개, A) |
| 제목 | Compositions of peptide inhibitors of interleukin-23 receptors |
| 출원일 / 공개일 | 2023-07-24 / 2023-10-11 |
| 우선일 | 2020-11-20 |
| 출원인/양수인 | Janssen Pharmaceutica NV; Protagonist Therapeutics Inc |
| 패밀리 | US11939361B2, CA3202226A1 (동일 조성물 패밀리) |
| 권위 만료일 | 추정 ~2041 (우선일/출원일+20년; 일본 산정 별도) |
| 교차검증 | GP `/en`=0(영어 페이지 미수록); GP `/ja`=일본어 청구항 본문 **verbatim 확보(165개 블록)**; FPO=실패 → **⚠️부분(텍스트 확보·번호 불확실)** |

**[ANALYSIS] (한국어)**

icotrokinra 조성물 패밀리(US11939361B2/CA3202226A1과 동일 제목·동일 우선일 2020-11-20)의 **일본 대응 출원**임은 서지정보로 확정된다. 청구항 원문은 Google Patents 영어(`/en`) 페이지엔 없었으나, **일본어(`/ja`) 페이지에서 청구항 본문을 verbatim으로 확보**했다(165개 `claim-text` 블록, `work/05_gp_authoritative/JP2023145581A.md`에 원문 보존 — 번역·교정 없음). 청구항 1은 `「組成物であって、前記組成物の約０．１％～約１５％（ｗ／ｗ）の量の配列番号１のペプチド又はその医薬的に許容される塩若しくは溶媒和物形態と、…」`로 시작해 **US11939361B2 청구항 1과 동일한 SEQ ID NO:1 조성물(0.1~15% w/w)** 임이 원문으로 확인된다. **단, Google Patents `/ja`의 `claim-text` 블록에 `【請求項N】` 번호 마커가 없어 청구항 번호 분절은 불확실**하므로, 정확한 청구항 번호·종속관계는 **J-PlatPat(일본 특허청)** 원문 확인이 필요하다(부록 B). 번역·추측으로 채우지 않고 원문만 보존한다.

---

## 부록 A — 오귀속(misattributed) 특허 (icotrokinra 무관) ❌

> 아래 9건은 디스커버리 단계에서 후보로 수집되었으나, 권위 소스 확인 결과 icotrokinra/Protagonist+Janssen 프로그램과 **무관**함이 확정되었다. 누락 방지를 위해 드롭하지 않고 부록으로 보존한다.

| # | 번호 | 실제 주제 / 출원인 | 근거 | GP 청구항 |
|---|---|---|---|---|
| A1 | WO2023212427A1 | IC-TROSA 점-대-다점 광통신 네트워크 / **Dell Products LP** | 제목·IPC(H04B10) 광통신, IL-23 무관 | 20 (광통신) |
| A2 | WO2023212432A1 | 보호커버 부착 다중날 칼 어셈블리 / **Larry Kalkstein** | 제목·IPC(B26B) 주방기구 | 다수 (칼) |
| A3 | WO2024026471A1 | CD98HC 항원결합 도메인(혈뇌장벽 항체) / **Alector LLC** | 항체 특허, IL-23 무관 | 0 (GP 본문 미수록) |
| A4 | WO2024026472A1 | 트랜스페린수용체 항원결합 도메인 / **Alector LLC** (실제 kind=A2) | 항체 특허; 요청 A1 vs 실제 A2 불일치 | (Alector 항체) |
| A5 | WO2023099669A1 | IL-23R 펩타이드 저해제 / **Zealand Pharma A/S** (경쟁사) | 진짜 IL-23R 펩타이드이나 출원인이 J&J/Protagonist 아님 | 87 (경쟁사 IL-23R) |
| A6 | US9605027B2 | IL-23R 결합 폴리펩타이드 / **Medical Diagnostic Laboratories, LLC** | 다른 당사자의 IL-23R 폴리펩타이드 | 13 |
| A7 | USRE49026E1 | 동상(US9169292의 재발행) / **Medical Diagnostic Laboratories, LLC** | 재발행 특허, Protagonist 아님 | 36 |
| A8 | US11180535B2 | 박테리아 종양침투 키메라 펩타이드(YebF 융합) | Google Patents 404 + FPO는 박테리아 펩타이드 → **오귀속 확정** | n/a (GP 404) |

### A.1 WO2023212427A1 (Dell 광통신) — 오귀속 근거 [VERBATIM 발췌]

**[ANALYSIS]** 청구항 전체가 광 트랜시버·점-대-다점 광네트워크 기술이며 펩타이드/IL-23과 전혀 무관하다.

**[VERBATIM] — 출처: Google Patents (`work/05_gp_authoritative/WO2023212427A1.md`)**

```text
2. The system of claim 1, further comprising: a hub signal processing subsystem that is included in the hub coherent optical transceiver device, coupled to the quadrature optical modulator subsystem, and configured to transmit first electrical signals to the quadrature optical modulator subsystem that are used by the quadrature optical modulator subsystem to generate the first optical signals and the second optical signals.

3. The system of claim 2, wherein the hub IC-TROSA device includes: an optical hybrid mixer subsystem; a second optical directional coupler device that is included in the optical hybrid mixer subsystem; a first receive connection provided by the second optical direction coupler device, wherein the second optical directional coupler device is configured to receive third optical signals at the first receive connection via the point-to-multipoint optical network; and a second receive connection provided by the second optical direction coupler device, wherein the second optical directional coupler device is configured to receive fourth optical signals at the second receive connection via the point-to-multipoint optical network, and wherein the optical hybrid mixer subsystem is configured to perform mixing operations on the third optical signals and fourth optical signals and provide mixing results for conversion to second electrical signals and third electrical signals that are then transmitted to the hub signal processing subsystem.

4. The system of claim 3, wherein hub signal processing subsystem is configured to: perform first signal processing operations on the second electrical signals and the third electrical signals to identify first data included in the second electrical signals and the third electrical signals; and perform second signal processing operations that are different than the first signal processing operations on the second electrical signals and the third electrical signals to identify second data included in the second electrical signals and the third electrical signals.

5. The system of claim 2, wherein the hub IC-TROSA device includes: an optical hybrid mixer subsystem; a MultiMode Interference (MMI) device that is included in the optical hybrid mixer subsystem; a first receive connection provided by the MMI device, wherein the MMI device is configured to receive third optical signals at the first receive connection via the point- to-multipoint optical network; and a second receive connection provided by the MMI device, wherein the MMI device is configured to receive fourth optical signals at the second receive connection via the point-to-multipoint optical network, wherein the optical hybrid mixer subsystem is configured to perform mixing operations on the third optical signals and fourth optical signals and provide mixing results for conversion to second electrical signals and third electrical signals that are then transmitted to the hub signal processing subsystem.

6. The system of claim 5, wherein hub signal processing subsystem is configured to: perform first signal processing operations on the second electrical signals and the third electrical signals to identify first data included in the second electrical signals and the third electrical signals; and perform second signal processing operations that are different than the first signal processing operations on the second electrical signals and the third electrical signals to identify second data included in the second electrical signals and the third electrical signals.

7. A hub coherent optical transceiver device, comprising: a quadrature optical modulator subsystem; a first optical directional coupler device that is included in the quadrature optical modulator subsystem; a first transmit connection provided by the first optical direction coupler device, wherein the first optical directional coupler device is configured to receive first optical signals from the quadrature optical modulator subsystem and transmit the first optical signals via the first transmit connection to a first subset of the plurality of subscriber devices via the point-to-multipoint optical network; and a second transmit connection provided by the first optical direction coupler device, wherein the first optical directional coupler device is configured to receive second optical signals from the quadrature optical modulator subsystem and transmit the second optical signals via the second transmit connection to a second subset of the plurality of subscriber devices via the point-to-multipoint optical network.

8. The hub coherent optical transceiver device of claim 7, further comprising: a hub signal processing subsystem that is coupled to the quadrature optical modulator subsystem and that is configured to transmit first electrical signals to the quadrature optical modulator subsystem that are used by the quadrature optical modulator subsystem to generate the first optical signals and the second optical signals.

9. The hub coherent optical transceiver device of claim 8, further comprising: an optical hybrid mixer subsystem; a second optical directional coupler device that is included in the optical hybrid mixer subsystem; a first receive connection provided by the second optical direction coupler device, wherein the second optical directional coupler device is configured to receive third optical signals at the first receive connection via the point-to-multipoint optical network; and a second receive connection provided by the second optical direction coupler device, wherein the second optical directional coupler device is configured to receive fourth optical signals at the second receive connection via the point-to-multipoint optical network, and wherein the optical hybrid mixer subsystem is configured to perform mixing operations on the third optical signals and fourth optical signals and provide mixing results for conversion to second electrical signals and third electrical signals that are then transmitted to the hub signal processing subsystem.

10. The hub coherent optical transceiver device of claim 9, wherein hub signal processing subsystem is configured to: perform first signal processing operations on the second electrical signals and the third electrical signals to identify first data included in the second electrical signals and the third electrical signals; and perform second signal processing operations that are different than the first signal processing operations on the second electrical signals and the third electrical signals to identify second data included in the second electrical signals and the third electrical signals.

11. The hub coherent optical transceiver device of claim 8, further comprising: an optical hybrid mixer subsystem; a MultiMode Interference (MMI) device that is included in the optical hybrid mixer subsystem; a first receive connection provided by the MMI device, wherein the MMI device is configured to receive third optical signals at the first receive connection via the point- to-multipoint optical network; and a second receive connection provided by the MMI device, wherein the MMI device is configured to receive fourth optical signals at the second receive connection via the point-to-multipoint optical network, wherein the optical hybrid mixer subsystem is configured to perform mixing operations on the third optical signals and fourth optical signals and provide mixing results for conversion to second electrical signals and third electrical signals that are then transmitted to the hub signal processing subsystem.

12. The hub coherent optical transceiver device of claim 7, wherein hub signal processing subsystem is configured to: perform first signal processing operations on the second electrical signals and the third electrical signals to identify first data included in the second electrical signals and the third electrical signals; and perform second signal processing operations that are different than the first signal processing operations on the second electrical signals and the third electrical signals to identify second data included in the second electrical signals and the third electrical signals.

13. The IC-TROSA device of claim 7, wherein the first optical signals received from the quadrature optical modulator subsystem include a first quadrature and a second quadrature in a first optical phase relationship, and wherein the second optical signals received from the quadrature optical modulator subsystem include the first quadrature and the second quadrature in a second optical phase relationship that is different than the first optical phase relationship.

14. A method for transmitting data via a point-to-multipoint optical network, comprising: receiving, by a first optical directional coupler device included in a quadrature optical modulator subsystem in a hub Integrated Coherent Transmit-Receive Optical Sub- Assembly (IC-TROSA) device, first optical signals from the quadrature optical modulator subsystem; transmitting, by the first optical directional coupler device, the first optical signals via a first transmit connection provided by the first optical directional coupler device and to a first subset of a plurality of subscriber devices via a point-to-multipoint optical network; receiving, by the first optical directional coupler device, second optical signals from the quadrature optical modulator subsystem; and transmitting, by the first optical directional coupler device, the second optical signals via a second transmit connection provided by the first optical directional coupler device and to a second subset of the plurality of subscriber devices via the point-to- multipoint optical network.

15. The method of claim 14, further comprising: transmitting, by a hub signal processing subsystem that is coupled to the quadrature optical modulator subsystem, first electrical signals to the quadrature optical modulator subsystem that are used by the quadrature optical modulator subsystem to generate the first optical signals and the second optical signals.

16. The method of claim 15, further comprising: receiving, by a first receive connection on a second optical directional coupler device included in an optical hybrid mixer subsystem in the hub IC-TROSA device, third optical signals via the point-to-multipoint optical network; and receiving, by a second receive connection on the second optical directional coupler device included in the optical hybrid mixer subsystem in the hub IC-TROSA device, fourth optical signals via the point-to-multipoint optical network; and mixing, by the optical hybrid mixer subsystem, the third optical signals and fourth optical signals to provide mixing results for conversion to second electrical signals and third electrical signals that are then transmitted to the hub signal processing subsystem.

17. The method of claim 16, further comprising: performing, by the hub signal processing subsystem, first signal processing operations on the second electrical signals and the third electrical signals to identify first data included in the second electrical signals and the third electrical signals; and performing, by the hub signal processing subsystem, second signal processing operations that are different than the first signal processing operations on the second electrical signals and the third electrical signals to identify second data included in the second electrical signals and the third electrical signals.

18. The method of claim 15, further comprising: receiving, by a first receive connection on a MultiMode Interference (MMI) device included in an optical hybrid mixer subsystem in the hub IC-TROSA device, third optical signals via the point-to-multipoint optical network; and receiving, by a second receive connection on the MMI device included in the optical hybrid mixer subsystem in the hub IC-TROSA device, fourth optical signals via the point-to-multipoint optical network; and mixing, by the optical hybrid mixer subsystem the third optical signals and fourth optical signals to provide mixing results for conversion to second electrical signals and third electrical signals that are then transmitted to the hub signal processing subsystem.

19. The method of claim 18, further comprising: performing, by the hub signal processing subsystem, first signal processing operations on the second electrical signals and the third electrical signals to identify first data included in the second electrical signals and the third electrical signals; and performing, by the hub signal processing subsystem, second signal processing operations that are different than the first signal processing operations on the second electrical signals and the third electrical signals to identify second data included in the second electrical signals and the third electrical signals.

20. The method of claim 14, wherein the first optical signals received from the quadrature optical modulator subsystem include a first quadrature and a second quadrature in a first optical phase relationship, and wherein the second optical signals received from the quadrature optical modulator subsystem include the first quadrature and the second quadrature in a second optical phase relationship that is different than the first optical phase relationship.
```


### A.2 WO2023212432A1 (다중날 칼) — 오귀속 근거 [VERBATIM 발췌]

**[ANALYSIS]** 청구항 1이 '복수의 날과 보호커버를 갖는 칼 어셈블리'로 주방기구 특허임이 명백하다.

**[VERBATIM] — 출처: Google Patents (`work/05_gp_authoritative/WO2023212432A1.md`)**

```text
1. A knife assembly comprising: a multi -bladed knife comprising: a handle, and a plurality of blades attached to the handle, each blade of the plurality of blades extending longitudinally from the handle and substantially parallel to each other, each blade comprising a bottom cutting edge and a top non-cutting edge connected therebetween by opposing blade side surfaces; and a protective cover comprising a cover top and a pair of opposing cover side walls, the cover top configured to fit over a substantial portion of each of the top non-cutting edges of the plurality of blades, the cover side walls extending downward and substantially parallel to each other from opposing end portions of the cover top, the cover side walls spaced a predetermined distance apart to frictionally fit against outer most side surfaces of opposing outer most blades of the plurality of blades.

2. The knife assembly of claim 1, wherein the protective cover includes a finger ring pivotally attached to the cover top, the finger ring sized to receive a finger of a user’s hand therethrough.

3. The knife assembly of claim 2, wherein: the protective cover is operable to protect and cushion a user’s hand when pressing on the non-cutting edges of the plurality of blades during a chopping operation; and the finger ring is operable to anchor the user’s finger to the cover such that the user’s hand does not inadvertently slide off of the plurality of blades during the chopping operation.

4. The knife assembly of claim 1, wherein the protective cover is removably fit over the plurality of blades.

5. The knife assembly of claim 1, wherein the protective cover comprises at least one spacer tab extending downward and substantially parallel to the cover side walls from the cover top, the at least one spacer tab having a thickness that is sized to frictionally fit into at least one separation space formed between side surfaces of a pair of adjacent blades of the knife.

6. The knife assembly of claim 5, wherein the at least one spacer tab comprises a plurality of spacer tabs, each spacer tab sized to frictionally fit into each separation space formed between side surfaces of each pair of adjacent blades of the knife.

7. The knife assembly of claim 5, wherein the at least one spacer tab comprises a single spacer tab sized to frictionally fit between a single pair of blades of the knife.

8. The knife assembly of claim 5, wherein the at least one spacer tab comprises a first and a second spacer tab, the first spacer tab sized to frictionally fit between a first separation space formed between side surfaces of a first blade adjacent to a second blade of the knife, and the second spacer tab sized to frictionally fit between a second space formed between side surfaces of the second blade adjacent to a third blade of the knife.

9. The knife assembly of claim 1, wherein the plurality of blades comprises at least a pair of blades.

10. The knife assembly of claim 1, wherein the plurality of blades comprises at least three blades.

11. The knife assembly of claim 1, wherein each blade of the plurality of blades are removably attached to the handle of the knife.

12. The knife assembly of claim 1, comprising a blade connector mechanism positioned between the handle and the plurality of blades, the blade connector mechanism operable to attach and detach each blade of the plurality of blades to the handle of the knife.

13. A protective cover for a multi bladed knife, the knife including a handle, and a plurality of blades attached to the handle, each blade of the plurality of blades extending longitudinally from the handle and substantially parallel to each other, each blade comprising a bottom cutting edge and a top non-cutting edge connected therebetween by opposing blade side surfaces, the protective cover comprising: a cover top configured to fit over a substantial portion of each of the top non-cutting edges of the plurality of blades; and a pair of opposing cover side walls, the cover side walls extending downward and substantially parallel to each other from opposing end portions of the cover top, the cover side walls spaced a predetermined distance apart to frictionally fit against outer most side surfaces of opposing outer most blades of the plurality of blades of the knife.

14. The protective cover of claim 13, comprising a finger ring pivotally attached to the cover top, the finger ring sized to receive a finger of a user therethrough.

15. The protective cover of claim 14, wherein: the protective cover is operable to protect and cushion a user’s hand when pressing on the non-cutting edges of the plurality of blades during a chopping operation; and the finger ring is operable to anchor the user’s finger to the cover such that the user’s hand does not inadvertently slide off of the plurality of blades during the chopping operation.

16. The protective cover of claim 13, wherein the protective cover is removably fit over the plurality of blades.

17. The protective cover of claim 13, wherein the protective cover comprises at least one spacer tab extending downward and substantially parallel to the cover side walls from the cover top, the at least one spacer tab having a thickness that is sized to frictionally fit into at least one separation space formed between side surfaces of a pair of adjacent blades of the knife.

18. The protective cover of claim 17, wherein the at least one spacer tab comprises a plurality of spacer tabs, each spacer tab sized to frictionally fit into each separation space formed between side surfaces of each pair of adjacent blades of the knife.

19. The protective cover of claim 17, wherein the at least one spacer tab comprises a single spacer tab sized to frictionally fit between a single pair of blades of the knife.

20. The protective cover of claim 17, wherein the at least one spacer tab comprises a first and a second spacer tab, the first spacer tab sized to frictionally fit between a first separation space formed between side surfaces of a first blade adjacent to a second blade of the knife, and the second spacer tab sized to frictionally fit between a second space formed between side surfaces of the second blade adjacent to a third blade of the knife.
```


### A.3 WO2023099669A1 (Zealand Pharma, 경쟁사 IL-23R 펩타이드) — 오귀속 근거 [VERBATIM 발췌]

**[ANALYSIS]** 진짜 IL-23R 펩타이드 저해제이나 출원인이 **Zealand Pharma A/S**(경쟁사)로, Janssen/Protagonist icotrokinra 패밀리가 아니다. 화학형(lactam/dithioether/triazole 가교, Formula I X1~X14)도 별개 분자다. 발췌만 싣는다.

**[VERBATIM] — 출처: Google Patents (`work/05_gp_authoritative/WO2023099669A1.md`)**

```text
1. A compound of the formula: R1-Z-R2 wherein R1 is H, C1-4 acyl, benzoyl, C1-4 alkyl, or is absent; R2 is NHR3, OH, or is absent, wherein R3 is hydrogen or C1-3 alkyl optionally substituted with NH2; and Z is an amino acid sequence of formula I: X1-X2-X3-X4-X5-X6-X7-X8-X9-X10-X11-X12-X13-X14 (I) wherein X1 is absent or is selected from the group consisting of Asp, Gly, Leu, Glu, Ser, Cys, and Lys; X3 is selected from the group consisting of Ser, beta-homo-Ser, Thr, Leu, Cys, Gin, Vai, lie, N-Me-Ser, and Q(pyrrolidin); X5 is selected from the group consisting of Trp, Tyr, Ala, 1-Me-Trp, 7-Me-Trp, 7-Ph-Trp, 7- (Naphth-2-yl)-Trp, 2-Nal, Bip, 4-F-Trp, 7-F-Trp, and N-Me-Trp; X6 is selected from the group consisting of Gin, Glu, Tyr, Cys, Vai, His, N-Me-GIn, and Q(pyrrolidin); X8 is selected from the group consisting of Trp, Tyr, Asn, Ala, His, 2-Nal, Dab, 2,4- diaminobutanoyl([2-(trimethyl-2-aminoethoxy)ethoxy]propyl), F(4-NH2-(2-(trimethyl-2- aminoethoxy)ethoxy)propyl), Phe, Vai, 4-Me-Phe, 2-Me-Phe, Bip, 2-Me-F(4-F), {d}F(4-F), 4-CI-Phe, alpha-Me-Trp, 3,3-Diphenyl-Ala, and Phg, wherein the hydroxyl group of Tyr is optionally substituted with C1-3 alkyl optionally substituted with NH2; X9 is selected from the group consisting of 2-Nal, Trp, 1-Me-Trp, 6-CI-Trp, 3-(3- Quinolinyl)-Ala, Phe, 4-F-Phe, Glu, Cys, Ala, 6-F-Trp, His, 3-F-Phe, 3, 4-Me-Phe, Bip, and {d}6-F-Trp; X10 is selected from the group consisting of Leu, D-Leu, 2-Me-Leu, 2-Me-Lys, Trp, Asn, Cys, 4-aminotetrahydro-2H-pyran-4-acetyl, and 2-Me-Val; X12 is selected from the group consisting of Arg, D-Arg, 2-Me-Arg, N-Me-Arg, Ser, Phe, 4- NH2-Phe, Tyr, Thr, Met, Gly, Glu, Asn, Dab, 3-(3-Pyridyl)-Ala, 3-(4-Pyridyl)-Ala, {d}2,4- diaminobutanoyl([2-(trimethyl-2-aminoethoxy)ethoxy]propyl), D-GIn, D-Glu, D-His, 3- aminopropanoyl, and GABA, or is absent; X13 is absent or is selected from the group consisting of Asn, Gly, 3-(3-Pyridyl)-Ala, 3-(4- Pyridyl)-Ala, 3-(3-Quinolinyl)-Ala, {d}[3-(3-Pyridyl)-Ala], 3-amino-3-(3'-pyridyl)propionyl, 3- F-Phe, 3,5-F-Phe, 4-aminomethyl-2-pyridineacetyl, 2,3-diaminopropanoyl(3-pyridylacetyl), 2,3-diaminopropanoyl(3-pyridylpropionyl), 2,3-diaminopropanoyl(3-fluorobenzoyl), 2,3- diaminopropanoyl(3-fluorophenylacetyl), and 2-Me-3-(3-Pyridyl)-Ala; X14 is absent or is Gly; X2 and X11 are amino acid residues who together form a lactam bridge, a dithioether bridge, or a bridge containing a triazole ring; and X4 and X7 are amino acid residues who together form a lactam bridge, a dithioether bridge, or a bridge containing a triazole ring; or a pharmaceutically acceptable salt or solvate thereof; wherein the compound is not: I3 (isomer 3) H-DC(1a)SC(2a)WQC(2a)WWLC(1a)R-[NH2]; wherein (1a) is a [2,11] 1 ,3-dithio-propan-2-one bridge and (2a) is a [4,7] 1 ,3-dithio- propan-2-one bridge.

2. The compound according to claim 1 of the formula: R1-Z-R2 wherein R1 is H, C1-4 acyl, benzoyl, C1-4 alkyl, or is absent; R2 is NHR3, OH, or is absent, wherein R3 is hydrogen or C1-3 alkyl; and Z is an amino acid sequence of formula I: X1-X2-X3-X4-X5-X6-X7-X8-X9-X10-X11-X12-X13-X14 (I) wherein X1 is absent or is selected from the group consisting of Asp, Glu, Ser, Cys, and Lys; X3 is selected from the group consisting of Ser, beta-homo-Ser, Thr, Leu, Cys, and Gin; X5 is selected from the group consisting of Trp, Tyr, Ala, 1-Me-Trp, 7-Me-Trp, 7-Ph-Trp, 7- (Naphth-2-yl)-Trp, 2-Nal, and Bip; X6 is selected from the group consisting of Gin, Glu, Tyr and Cys; X8 is selected from the group consisting of Trp, Tyr, Asn, Ala, His, and 2-Nal, wherein the hydroxyl group of Tyr is optionally substituted with C1-3 alkyl optionally substituted with NH2; X9 is selected from the group consisting of 2-Nal, Trp, 1-Me-Trp, 6-CI-Trp, 3-(3- Quinolinyl)-Ala, Phe, 4-F-Phe, Glu, Cys, and Ala; X10 is selected from the group consisting of Leu, D-Leu, 2-Me-Leu, 2-Me-Lys, Trp, Asn, Cys, and 4-aminotetrahydro-2H-pyran-4-acetyl; X12 is selected from the group consisting of Arg, D-Arg, 2-Me-Arg, N-Me-Arg, Ser, Phe, 4- NH2-Phe, Tyr, Thr, Met, Gly, Glu, Asn, Dab, 3-(3-Pyridyl)-Ala, and 3-(4-Pyridyl)-Ala, or is absent; X13 is absent or is selected from the group consisting of Asn, Gly, 3-(3-Pyridyl)-Ala, and 3-(4-Pyridyl)-Ala; X14 is absent or is Gly; X2 and X11 are amino acid residues who together form a lactam bridge, a dithioether bridge, or a bridge containing a triazole ring; and X4 and X7 are amino acid residues who together form a lactam bridge, a dithioether bridge, or a bridge containing a triazole ring; or a pharmaceutically acceptable salt or solvate thereof; wherein the compound is not: 13 (isomer 3) H-DC(1a)SC(2a)WQC(2a)WWLC(1a)R-[NH2]; wherein (1a) is a [2,11] 1,3-dithio-propan-2-one bridge and (2a) is a [4,7] 1 ,3-dithio- propan-2-one bridge.

3. The compound according to claim 1 or 2, wherein X1 is absent or Asp.

4. The compound according to any one of the preceding claims, wherein X1 is absent.

5. The compound according to any one of the preceding claims, wherein X3 is Ser or lie.

6. The compound according to any one of the preceding claims, wherein X5 is Trp or 7-Me-Trp.

7. The compound according to any one of the preceding claims, wherein X6 is Gin or Glu.

8. The compound according to any one of the preceding claims, wherein X8 is Trp, Tyr, or 4-Me-Phe; wherein the hydroxyl group of Tyr is optionally substituted with - CH2CH2NH2.

9. The compound according to any one of the preceding claims, wherein X9 is 2-Nal, Trp, or 3, 4-Me-Phe.

10. The compound according to any one of the preceding claims, wherein X9 is 2-Nal.

11. The compound according to any one of the preceding claims, wherein X10 is Leu, 2-Me-Leu, or 2-Me-Val.

12. The compound according to any one of the preceding claims, wherein X10 is Leu, or 2-Me Leu.

13. The compound according to any one of the preceding claims, wherein X12 is Arg, D-Arg, and Dab.

14. The compound according to any one of the preceding claims, wherein X13 is absent, 3-(3-Pyridyl)-Ala, or 2-Me-3-(3-Pyridyl)-Ala.

15. The compound according to any one of the preceding claims, wherein X14 is absent.

16. The compound according to any one of the preceding claims, wherein R1 is H, C1-2 acyl, or absent.

17. The compound according to any one of the preceding claims, wherein R1 is absent.

18. The compound according to any one of claims 1 to 16, wherein R1 is -C(=O)CH3.

19. The compound according to any one of the preceding claims, wherein R2 is NH2.

20. The compound according to any one of the preceding claims, wherein the length of the bridge between X2 and X11 and/or X4 and X7 is 5 to 10 atoms long.

21. The compound according to any one of the preceding claims, wherein X1 is absent, R1 is absent, and X2 and X11 are amino acid residues that together form a lactam bridge or a bridge containing a triazole ring via the /V-terminus of X2.

22. The compound according to any one of the preceding claims, wherein X1 and X12 to X14 are absent, R1 and R2 are absent, and X2 and X11 are amino acid residues that together form a head-to-tail cyclised lactam bridge via the /V-terminus of X2 and the C- terminus of X11.

23. The compound according to any one of the preceding claims, wherein the dithioether bridge between X2 and X11 and/or X4 and X7 is of the formula -S-L-Y-L-S-, wherein: each S is a sulfur atom and is part of the amino acid residue at X2 and X11 and/or X4 and X7; each L is independently C1-4 alkylene; and Y is either absent, C(=O), or arylene.

24. The compound according to claim 23, wherein each L is independently C1-2 alkylene.

25. The compound according to claims 23 or 24, wherein each L is methylene.

26. The compound according to any one of claims 23 to 25, wherein Y is C(=O).

27. The compound according to any one of claims 23 to 25, wherein Y is arylene selected from phenylene.

28. The compound according to claim 27, wherein Y is phenylene selected from 1 ,2- phenylene, 1 ,3-phenylene, and 1 ,4-phenylene.

29. The compound according to claim 27 or 28, wherein Y is 1 ,2-phenylene.

30. The compound according to any one of the preceding claims, wherein the bridge containing a triazole ring between X2 and X11 and/or X4 and X7 contains a 1 ,2,3-triazole ring.

31. The compound according to any one of the preceding claims, wherein the bridge containing a triazole ring between X2 and X11 and/or X4 and X7 is attached to positions 1 and 4 of the triazole ring.

32. The compound according to any one of the preceding claims, wherein X2 and X11 are amino acid residues who together form a lactam bridge.

33. The compound according to claim 32, wherein the location of the amide bond in the lactam bridge is closer to X11 than X2.

34. The compound according to claim 32 or 33, wherein one of the residues at position X2 and X11 is selected from Lys, Arg, Orn, bAla, 3-(4-aminophenyl)propanoyl, (3- aminomethyl)benzoyl, (4-aminomethyl)benzoyl, 4-(2-aminoethyl)benzoyl, 2-aminomethyl- phenylacetyl, 3-aminomethyl-phenylacetyl, 4-aminomethyl-phenylacetyl, 4-aminomethyl-2- pyridineacetyl, 4-aminomethyl-3-pyridineacetyl, 4-aminomethyl-2-fluoro-phenylacetyl, 4- aminomethyl-3-fluoro-phenylacetyl, 4-aminomethyl-2-methyl-phenylacetyl, 4-aminomethyl- 3-methyl-phenylacetyl, 4-aminomethyl-2-methoxy-phenylacetyl, 4-aminomethyl-3- methoxy-phenylacetyl, Dab, 6-aminohexanoyl, 6-amino-4-oxahexanoyl, trans-4- aminomethyl-cyclohexyl-1 -carbonyl, (4-(2-aminoethyl)-piperazine-1-yl)-acetyl, 2,4- diaminobutanoyl([2-(trimethyl-2-aminoethoxy)ethoxy]propyl), and 4-methylaminomethyl- phenylacetyl, and the other is selected from Glu and Asp.

35. The compound according to claim 34, wherein X2 is selected from Lys, Orn, bAla, 3-(4-aminophenyl)propanoyl, (3-aminomethyl)benzoyl, (4-aminomethyl)benzoyl, 4-(2- aminoethyl)benzoyl, 2-aminomethyl-phenylacetyl, 3-aminomethyl-phenylacetyl, 4- aminomethyl-phenylacetyl, 4-aminomethyl-2-pyridineacetyl, 4-aminomethyl-3- pyridineacetyl, 4-aminomethyl-2-fluoro-phenylacetyl, 4-aminomethyl-3-fluoro-phenylacetyl, 4-aminomethyl-2-methyl-phenylacetyl, 4-aminomethyl-3-methyl-phenylacetyl, 4- aminomethyl-2-methoxy-phenylacetyl, 4-aminomethyl-3-methoxy-phenylacetyl, 6- aminohexanoyl, 6-amino-4-oxahexanoyl, trans-4-aminomethyl-cyclohexyl-1-carbonyl, (4- (2-aminoethyl)-piperazine-1-yl)-acetyl, 2,4-diaminobutanoyl([2-(trimethyl-2- aminoethoxy)ethoxy]propyl), and 4-methylaminomethyl-phenylacetyl, and X11 is selected from Glu and Asp.

36. The compound according to claim 35, wherein: X2 is Lys and X11 is Glu; X2 is Orn and X11 is Glu; X2 is bAla and X11 is Glu; X2 is 3-(4-aminophenyl)propanoyl and X11 is Glu; X2 is (3-aminomethyl)benzoyl and X11 is Glu; X2 is (4-aminomethyl)benzoyl and X11 is Glu; X2 is 4-(2-aminoethyl)benzoyl and X11 is Glu; X2 is 2-aminomethyl-phenylacetyl and X11 is Glu; X2 is 3-aminomethyl-phenylacetyl and X11 is Glu; X2 is 4-aminomethyl-phenylacetyl and X11 is Glu; X2 is 6-aminohexanoyl and X11 is Glu; X2 is 6-amino-4-oxahexanoyl and X11 is Glu; X2 is trans-4-aminomethyl-cyclohexyl-1-carbonyl and X11 is Glu; X2 is (4-(2-aminoethyl)-piperazine-1-yl)-acetyl and X11 is Glu; X2 is (4-(2-aminoethyl)-piperazine-1-yl)-acetyl and X11 is Asp; X2 is 4-aminomethyl-2-pyridineacetyl and X11 is Glu; X2 is 4-aminomethyl-3-pyridineacetyl and X11 is Glu; X2 is 4-aminomethyl-2-fluoro-phenylacetyl and X11 is Glu; X2 is 4-aminomethyl-3-fluoro-phenylacetyl and X11 is Glu; X2 is 4-aminomethyl-2-methyl-phenylacetyl and X11 is Glu; X2 is 4-aminomethyl-3-methyl-phenylacetyl and X11 is Glu; X2 is 4-aminomethyl-2-methoxy-phenylacetyl and X11 is Glu; X2 is 4-aminomethyl-3-methoxy-phenylacetyl and X11 is Glu; X2 is Dab and X11 is Glu; X2 is 2,4-diaminobutanoyl([2-(trimethyl-2-aminoethoxy)ethoxy]propyl) and X11 is Glu; or X2 is 2,4-diaminobutanoyl([2-(trimethyl-2-aminoethoxy)ethoxy]propyl) and X11 is Glu.

37. The compound according to claim 35 or 36, wherein: X2 is Lys and X11 is Glu; X2 is (3-aminomethyl)benzoyl and X11 is Glu; or X2 is 4-aminomethyl-phenylacetyl and X11 is Glu.

38. The compound according to claim 34, wherein X2 is selected from Glu and Asp, and X11 is selected from Lys, Arg, and Dab.

39. The compound according to claim 38, wherein: X2 is Glu and X11 is Lys; X2 is Glu and X11 is Dab; or X2 is Asp and X11 is Arg.

40. The compound according to any one claims 1 to 31 , wherein X2 and X11 are amino acid residues who together form a dithioether bridge.

41. The compound according to claim 40, wherein X2 and X11 are each independently selected from Cys and N-Me-Cys.

42. The compound according to claim 40 or 41 , wherein X2 is Cys and X11 is Cys.

43. The compound according to any one claims 1 to 31 , wherein X2 and X11 are amino acid residues who together form a bridge containing a triazole ring.

44. The compound according to claim 43, wherein one of the residues at position X2 and X11 is selected from Lys(N3), azidoacetic acid, (N3)-Ala, Dab(azidoacetic acid), and Dab((N3)-Ala), and the other is selected from Pra, Glu(propargylamine), Dab(3-butynoic acid), and but-3-ynoic acid.

45. The compound according to claim 44, wherein X2 is selected from Lys(Ns), azidoacetic acid, and (Ns)-Ala; and X11 is selected from Pra, Glu(propargylamine), and Dab(3-butynoic acid).

46. The compound according to claim 45, wherein: X2 is Lys(Ns) and X11 is Pra; X2 is azidoacetic acid and X11 is Glu(propargylamine); X2 is azidoacetic acid and X11 is Dab(3-butynoic acid); X2 is (Ns)-Ala and X11 is Glu(propargylamine); or X2 is (Ns)-Ala and X11 is Dab(3-butynoic acid).

47. The compound according to claim 45 or 46, wherein: X2 is Lys(Ns) and X11 is Pra.

48. The compound according to claim 44, wherein X2 is selected from Pra, and but-3- ynoic acid; and X11 is selected from Dab(azidoacetic acid), and Dab((N3)-Ala).

49. The compound according to claim 48, wherein: X2 is Pra and X11 is Dab(azidoacetic acid); X2 is Pra and X11 is Dab((N3)-Ala); or X2 is but-3-ynoic acid and X11 is Dab(azidoacetic acid); or X2 is but-3-ynoic acid and X11 is Dab((N3)-Ala).

50. The compound according to any one of the preceding claims, wherein X4 and X7 are amino acid residues who together form a dithioether bridge.

51. The compound according to claim 50, wherein X4 and X7 are each independently selected from Cys and N-Me-Cys.

52. The compound according to claim 50 or 51 , wherein X4 is Cys and X7 is Cys; or X4 is N-Me-Cys and X7 is Cys.

53. The compound according to any one of claims 1 to 49, wherein X4 and X7 are amino acid residues who together form a lactam bridge.

54. The compound according to claim 53, wherein one of the residues at position X4 and X7 is Lys, Dpr, Dab, or Orn, and the other is Glu.

55. The compound according to claim 54, wherein X4 is selected from Lys, Dpr, Dab, and Orn, and X7 is Glu.

56. The compound according to claim 55, wherein: X4 is Dpr and X7 is Glu; X4 is Dab and X7 is Glu; or X4 is Orn and X7 is Glu.

57. The compound according to claim 54, wherein X4 is Glu, and X7 is selected from Lys, Dpr, Dab, and Orn.

58. The compound according to claim 57, wherein: X4 is Glu and X7 is Lys; X4 is Glu and X7 is Dpr; X4 is Glu and X7 is Orn; or X4 is Glu and X7 is Dab.

59. The compound according to any one claims 1 to 49, wherein X4 and X7 are amino acid residues who together form a bridge containing a triazole ring.

60. The compound according to claim 59, wherein one of the residues at position X4 and X7 is selected from Lys(Na) and Aha, and the other is Pra.

61. The compound according to claim 60, wherein: X4 is Lys(Na) and X7 is Pra; or X4 is Aha and X7 is Pra.

62. The compound according to any one of claims 1 to 7, 9, 10, and 13 to 61 , wherein X8 is Trp; X10 is D-Leu; and X12 is selected from the group consisting of Arg, D-Arg, 2- Me-Arg, N-Me-Arg, Ser, Phe, 4-NH2-Phe, Tyr, Thr, Met, Gly, Glu, Asn, Dab, 3-(3-Pyridyl)- Ala, and 3-(4-Pyridyl)-Ala, or is absent.

63. The compound according to any one of claims 1 to 10, and 13 to 61 , wherein X8 is Tyr wherein the hydroxyl group of Tyr is optionally substituted with C1-3 alkyl optionally substituted with NH2; X10 is D-Leu; and X12 is selected from the group consisting of Arg, D-Arg, 2-Me-Arg, N-Me-Arg, Ser, Phe, 4-NH2-Phe, Tyr, Thr, Met, Gly, Glu, Asn, Dab, 3-(3- Pyridyl)-Ala, and 3-(4-Pyridyl)-Ala, or is absent.

64. The compound according to any one of claims 1 to 7, 9, 10, and 13 to 61 , wherein X8 is Asn; X10 is D-Leu; and X12 is selected from the group consisting of Arg, D-Arg, 2- Me-Arg, N-Me-Arg, Ser, Phe, 4-NH2-Phe, Tyr, Thr, Met, Gly, Glu, Asn, Dab, 3-(3-Pyridyl)- Ala, and 3-(4-Pyridyl)-Ala, or is absent.

65. The compound according to any one of claims 1 to 7, 9, 10, and 13 to 61 , wherein X8 is Ala; X10 is D-Leu; and X12 is selected from the group consisting of Arg, D-Arg, 2- Me-Arg, N-Me-Arg, Ser, Phe, 4-NH2-Phe, Tyr, Thr, Met, Gly, Glu, Asn, Dab, 3-(3-Pyridyl)- Ala, and 3-(4-Pyridyl)-Ala, or is absent.

66. The compound according to any one of claims 1 to 7, 9, 10, and 13 to 61 , wherein X8 is His; X10 is D-Leu; and X12 is selected from the group consisting of Arg, D-Arg, 2- Me-Arg, N-Me-Arg, Ser, Phe, 4-NH2-Phe, Tyr, Thr, Met, Gly, Glu, Asn, Dab, 3-(3-Pyridyl)- Ala, and 3-(4-Pyridyl)-Ala, or is absent.

67. The compound according to any one of claims 1 to 7, 9, 10, and 13 to 61 , wherein X8 is 2-Nal; X10 is D-Leu; and X12 is selected from the group consisting of Arg, D-Arg, 2- Me-Arg, N-Me-Arg, Ser, Phe, 4-NH2-Phe, Tyr, Thr, Met, Gly, Glu, Asn, Dab, 3-(3-Pyridyl)- Ala, and 3-(4-Pyridyl)-Ala, or is absent.

68. The compound according to any one of claims 1 to 11 , and 13 to 61 , wherein X8 is Tyr wherein the hydroxyl group of Tyr is optionally substituted with -CH2CH2NH2; X10 is 2- Me-Leu; and X12 is Arg or is absent.

69. The compound according to any one of claims 1 to 7, 9 to 11 , and 13 to 61 , wherein X8 is Trp; X10 is 2-Me-Leu; and X12 is selected from the group consisting of Arg, D-Arg, 2-Me-Arg, N-Me-Arg, Ser, Phe, 4-NH2-Phe, Tyr, Thr, Met, Gly, Glu, Asn, Dab, 3-(3- Pyridyl)-Ala, and 3-(4-Pyridyl)-Ala, or is absent.

70. The compound according to any one of claims 1 to 11 , and 13 to 61 , wherein X8 is Tyr wherein the hydroxyl group of Tyr is optionally substituted with C1-3 alkyl optionally substituted with NH2; X10 is 2-Me-Leu; and X12 is selected from the group consisting of Arg, D-Arg, 2-Me-Arg, N-Me-Arg, Ser, Phe, 4-NH2-Phe, Tyr, Thr, Met, Gly, Glu, Asn, Dab, 3-(3-Pyridyl)-Ala, and 3-(4-Pyridyl)-Ala, or is absent.

71. The compound according to any one of claims 1 to 7, 9 to 11 , and 13 to 61 , wherein X8 is Asn; X10 is 2-Me-Leu; and X12 is selected from the group consisting of Arg, D-Arg, 2-Me-Arg, N-Me-Arg, Ser, Phe, 4-NH2-Phe, Tyr, Thr, Met, Gly, Glu, Asn, Dab, 3-(3- Pyridyl)-Ala, and 3-(4-Pyridyl)-Ala, or is absent.

72. The compound according to any one of claims 1 to 7, 9 to 11 , and 13 to 61 , wherein X8 is Ala; X10 is 2-Me-Leu; and X12 is selected from the group consisting of Arg, D-Arg, 2-Me-Arg, N-Me-Arg, Ser, Phe, 4-NH2-Phe, Tyr, Thr, Met, Gly, Glu, Asn, Dab, 3-(3- Pyridyl)-Ala, and 3-(4-Pyridyl)-Ala, or is absent.

73. The compound according to any one of claims 1 to 7, 9 to 11 , and 13 to 61 , wherein X8 is His; X10 is 2-Me-Leu; and X12 is selected from the group consisting of Arg, D-Arg, 2-Me-Arg, N-Me-Arg, Ser, Phe, 4-NH2-Phe, Tyr, Thr, Met, Gly, Glu, Asn, Dab, 3-(3- Pyridyl)-Ala, and 3-(4-Pyridyl)-Ala, or is absent.

74. The compound according to any one of claims 1 to 7, 9 to 11 , and 13 to 61 , wherein X8 is 2-Nal; X10 is 2-Me-Leu; and X12 is selected from the group consisting of Arg, D-Arg, 2-Me-Arg, N-Me-Arg, Ser, Phe, 4-NH2-Phe, Tyr, Thr, Met, Gly, Glu, Asn, Dab, 3-(3-Pyridyl)-Ala, and 3-(4-Pyridyl)-Ala, or is absent.

75. The compound according to any one of claims 1 to 10, and 13 to 61 , wherein X8 is Tyr wherein the hydroxyl group of Tyr is optionally substituted with -CH2CH2NH2; X10 is D- Leu; and X12 is Arg or is absent.

76. The compound according to any one of claims 1 to 11 , and 13 to 61 , wherein X8 is Tyr wherein the hydroxyl group of Tyr is optionally substituted with -CH2CH2NH2; X10 is 2- Me-Leu; and X12 is Arg or is absent.

77. The compound according to claim 1 wherein Z is an amino acid sequence selected from the group consisting of: SEQ ID NO: 1 DC(1 a)SC(2a)WQC(2a)WW[2-Me-Leu]C(1 a)R SEQ ID NO: 2 LC(1a)SC(2a)WQC(2a)WWLC(1 a)R SEQ ID NO: 3 DC(1 a)SC(2a)WEC(2a)WWLC(1 a)R SEQ ID NO: 4 DE(1 c)SC(2a)WQC(2a)WWLK(1 c)R SEQ ID NO: 5 DC(1 a)SE(2c)WQK(2c)WWLC(1 a)R SEQ ID NO: 6 D(1 c)*SC(2a) WQC(2a)WWLR(1 c) SEQ ID NO: 7 DK(1 c)SC(2a)WQC(2a)WWLE(1 c)R SEQ ID NO: 8 D[Orn](1 c)SC(2a)WQC(2a)WWLE(1 c)R SEQ ID NO: 9 DE(1 c)SC(2a)WQC(2a)WWL[Dab](1 c)R SEQ ID NO: 10 E(1 c)SC(2a)WQC(2a)WWLK(1 c)R SEQ ID NO: 1 1 DE(1 c)SC(2a)WQC(2a)WWLK(1 c) SEQ ID NO: 12 E(1 c)SC(2a)WQC(2a)WWLK(1 c) SEQ ID NO: 13 DE(1 c)SC(2a)AQC(2a)VWVLK(1 c)R SEQ ID NO: 14 DE(1 c)SC(2a)WQC(2a)AWLK(1 c)R SEQ ID NO: 15 DE(1 c)SC(2a)WQC(2a)WALK(1 c)R SEQ ID NO: 16 DE(1 c)SC(2a)[7-Me-Trp]QC(2a)WWLK(1 c)R SEQ ID NO: 17 DE(1 c)SC(2a)WQC(2a)W[2-Nal]LK(1 c)R SEQ ID NO: 18 K(1 c)SC(2a)WQC(2a)W[2-Nal]LE(1 c)R SEQ ID NO: 19 DK(1 c)SC(2a)WQC(2a)W[2-Nal]LE(1 c)R SEQ ID NO: 20 DK(1 c)SC(2d)WQC(2d)W[2-Nal]LE(1 c)R SEQ ID NO: 21 DK(1 c)SC(2e)WQC(2e)W[2-Nal]LE(1 c)R SEQ ID NO: 22 DK(1 c)SC(2f)WQC(2f)W[2-Nal]LE(1 c)R SEQ ID NO: 23 DK(1 c)S[K(N3)](2g)WQ[Pra](2g)W[2-Nal]LE(1 c)R SEQ ID NO: 24 DK(1 c)S[Aha](2g)WQ[Pra](2g)W[2-Nal]LE(1 c)R SEQ ID NO: 25 K(1 c)SC(2a)[2-Nal]QC(2a)W[2-Nal]LE(1 c)R SEQ ID NO: 26 K(1 c)SC(2a)[Bip]QC(2a)W[2-Nal]LE(1 c)R SEQ ID NO: 27 K(1 c)SC(2a)[1 -Me-Trp]QC(2a)W[2-Nal]LE(1 c)R SEQ ID NO: 28 DK(1 c)SC(2a)WQC(2a)[2-Nal][2-Nal]LE(1 c)R SEQ ID NO: 29 K(1 c)SC(2a)WQC(2a)[Y(2-aminoethoxy)][2-Nal]LE(1 c)R SEQ ID NO: 30 K(1 c)SC(2a)WQC(2a)H[2-Nal]LE(1 c)R SEQ ID NO: 31 K(1 c)SC(2a)WQC(2a)W[F(4-F)]LE(1 c)R SEQ ID NO: 32 K(1 c)SC(2a) WQC(2a) W[1 -Me-Trp]LE(1 c)R SEQ ID NO: 33 C(1 a)TC(2a)WEC(2a)WW[2-Me-Leu]C(1 a)S SEQ ID NO: 34 GK(1 c)TC(2a)WEC(2c)WW[2-Me-Leu]E(1 c)S SEQ ID NO: 35 GC(1 a)TC(2a)WEC(2a)W[2-Nal][2-Me-Leu]C(1 a)R SEQ ID NO: 36 [bAla](1 c)*SC(2a)WQC(2a)W[2-Nal]LE(1 c)R SEQ ID NO: 37 [(3-Aminomethyl)benzoyl](1 c)*SC(2a)WQC(2a)W[2-Nal]LE(1 c)R [(3-Aminomethyl)benzoyl](1 c)*SC(2a)WQC(2a)[Y(2-aminoethoxy)][2- SEQ ID NO: 38 Nal][2-Me-Leu]E(1 c)R-[NH2] [(3-Aminomethyl)benzoyl](1 c)*SC(2a)WQC(2a)[Y(2-aminoethoxy)][2- SEQ ID NO: 39 Nal]LE(1 c)R SEQ ID NO: 40 [(3-Aminomethyl)benzoyl](1 c)*SC(2a)WQC(2a)W[2-Nal][2-Me-Leu]E(1 c)R [(3-Aminomethyl)benzoyl](1 c)*SC(2a)WQC(2a)[Y(2-aminoethoxy)][2- SEQ ID NO: 41 Nal][2-Me-Leu]E(1 c)[{d}R] [(3-Aminomethyl)benzoyl](1 c)*SC(2a)WQC(2a)[Y(2-aminoethoxy)][2- SEQ ID NO: 42 Nal][2-Me-Leu]E(1 c)[2-Me-Arg] SEQ ID NO: 43 [(3-Aminomethyl)benzoyl](1 c)*SC(2a)WQC(2a)[Y(2-aminoethoxy)][2- Nal][2-Me-Leu]E(1 c)[N-Me-Arg] QFn in kin AA [(3-Aminomethyl)benzoyl](1 c)*SC(2a)WQC(2a)[Y(2-aminoethoxy)][2- btu ID O. 44 Na|][2-Me-Leu]E(1 c)S urn in MO AH [(3-Aminomethyl)benzoyl](1 c)*SC(2a)WQC(2a)[Y(2-aminoethoxy)][2- bl=U ID NO. 4b Na|][2-Me-Leu]E(1 c)[F(4-NH2)] QFn in kin A [(3-Aminomethyl)benzoyl](1 c)*SC(2a)WQC(2a)[Y(2-aminoethoxy)][2- otO ID NO. 40 Na|][{d}L]E(1 c)Y SEQ ID NO: 47 [Ac]-K(1 c)SC(2a)WQC(2a)[Y(2-aminoethoxy)][2-Nal][2-Me-Leu]E(1c)R SEQ ID NO: 48 [Ac]-K(1 c)SC(2a)WQC(2a)[Y(2-aminoethoxy)][2-Nal][{d}L]E(1 c)R SEQ ID NO: 49 [(4-Aminomethyl)benzoyl](1 c)*SC(2a)WQC(2a)[Y(2-aminoethoxy)][2- Nal][2-Me-Leu]E(1 c)R SEQ ID NO: 50 [4-(2-Aminoethyl)benzoyl](1 c)*SC(2a)WQC(2a)[Y(2-aminoethoxy)][2- Nal][2-Me-Leu]E(1 c)R SEQ ID NO: 51 [3-(4-Aminophenyl)propanoyl](1 c)*SC(2a)WQC(2a)[Y(2-aminoethoxy)][2- Nal][2-Me-Leu]E(1 c)R SEQ ID NO: 52 [4-Aminomethyl-phenylacetyl](1 c)*SC(2a)WQC(2a)[Y(2-aminoethoxy)][2- Nal][2-Me-Leu]E(1 c)R SEQ ID NO: 53 DC(1 a)SC(2b)WQC(2b)WWLC(1 a)R SEQ ID NO: 54 K(1 c)SC(2b)WQC(2b)[Y(2-aminoethoxy)][2-Nal]LE(1 c)R SEQ ID NO: 55 DE(1 c)QC(2a)WQC(2a)YW[2-Me-Leu]K(1 c)R SEQ ID NO: 56 DE(1 c)QC(2a)WQC(2a)[2-Nal]W[2-Me-Leu]K(1 c)R SEQ ID NO: 57 DE(1 c)TC(2a)WQC(2a)W[2-Nal][2-Me-Leu]K(1 c) SEQ ID NO: 58 DE(1 c)SC(2a)WQC(2a)W[2-Nal][2-Me-Leu]K(1 c)ENG SEQ ID NO: 59 DE(1 c)SC(2a)WQC(2a)W[2-Nal][2-Me-Leu]K(1 c)NG SEQ ID NO: 60 DE(1 c)SC(2a)WQC(2a)W[2-Nal][2-Me-Leu]K(1 c)G SEQ ID NO: 61 DE(1 c)SC(2a)WQC(2a)W[2-Nal][2-Me-Lys]K(1 c)ENG SEQ ID NO: 62 DC(1 a)QC(2a)WQC(2a)[2-Nal]W[2-Me-Leu]C(1 a)R SEQ ID NO: 63 DC(1 a)QC(2a)WQC(2a)YW[2-Me-Leu]C(1 a)R SEQ ID NO: 64 DC(1 a)QC(2a)WQC(2a)WW[2-Me-Leu]C(1 a)ENG SEQ ID NO: 65 [(3-Aminomethyl)benzoyl](1 c)*S[Dpr](2c)VVQE(2c)[Y(2-aminoethoxy)][2- Nal][2-Me-Leu]E(1 c)R SEQ ID NO: 66 [(3-Aminomethyl)benzoyl](1 c)*SE(2c)VVQ[Dpr](2c)[Y(2-aminoethoxy)][2- Nal][2-Me-Leu]E(1 c)R SEQ ID NO: 67 [(3-Aminomethyl)benzoyl](1c)*SE(2c)WQ[Dab](2c)[Y(2-aminoethoxy)][2- Nal][2-Me-Leu]E(1c)R SEQ ID NO: 68 [(3-Aminomethyl)benzoyl](1c)*S[Orn](2c)WQE(2c)[Y(2-aminoethoxy)][2- Nal][2-Me-Leu]E(1c)R SEQ ID NO: 69 [(3-Aminomethyl)benzoyl](1c)*SE(2c)WQ[Orn](2c)[Y(2-aminoethoxy)][2- Nal][2-Me-Leu]E(1c)R SEQ ID NO: 70 [(3-Aminomethyl)benzoyl](1c)*SC(2a)[7-Me-Trp]QC(2a)[Y(2- aminoethoxy)][2-Nal][2-Me-Leu]E(1c)R SEQ ID NO: 71 [(3-Aminomethyl)benzoyl](1c)*SC(2a)[7-Ph-Trp]QC(2a)[Y(2- aminoethoxy)][2-Nal][2-Me-Leu]E(1c)R SEQ ID NO: 72 [(3-Aminomethyl)benzoyl](1c)*SC(2a)[7-(Naphth-2-yl)-Trp]QC(2a)[Y(2- aminoethoxy)][2-Nal][2-Me-Leu]E(1c)R SEQ ID NO: 73 [(3-Aminomethyl)benzoyl](1c)*SC(2a)WQC(2a)[Y(2-aminoethoxy)][3-(3- Quinolinyl)-Ala][2-Me-Leu]E(1c)R SEQ ID NO: 74 [(3-Aminomethyl)benzoyl](1c)*SC(2a)WQC(2a)[Y(2-aminoethoxy)][6-Cl- Trp][2-Me-Leu]E(1c)R SEQ ID NO: 75 [(3-Aminomethyl)benzoyl](1c)*SC(2a)WQC(2a)[Y(2-aminoethoxy)][2- Nal][4-aminotetrahydro-2H-pyran-4-acetyl]E(1c)R SEQ ID NO: 76 [(3-Aminomethyl)benzoyl](1c)*SC(2a)WQC(2a)[Y(2-aminoethoxy)][2- Nal][2-Me-Leu]E(1c)[3-(3-Pyridyl)-Ala] SEQ ID NO: 77 [(3-Aminomethyl)benzoyl](1c)*SC(2a)WQC(2a)[Y(2-aminoethoxy)][2- Nal][2-Me-Leu]E(1c)[3-(4-Pyridyl)-Ala] SEQ ID NO: 78 [(3-Aminomethyl)benzoyl](1c)*SC(2a)WQC(2a)[Y(2-aminoethoxy)][2- Nal][2-Me-Leu]E(1c)R[3-(3-Pyridyl)-Ala] SEQ ID NO: 79 [(3-Aminomethyl)benzoyl](1c)*SC(2a)WQC(2a)[Y(2-aminoethoxy)][2- Nal][2-Me-Leu]E(1c)R[3-(4-Pyridyl)-Ala] SEQ ID NO: 80 [4-Aminomethyl-phenylacetyl](1c)*SC(2a)WQC(2a)[Y(2-aminoethoxy)][2- Nal][2-Me-Leu]E(1c)[{d}R] SEQ ID NO: 81 [4-Aminomethyl-phenylacetyl](1c)*SC(2a)WQC(2a)[Y(2-aminoethoxy)][2- Nal][2-Me-Leu]E(1c)S SEQ ID NO: 82 [4-Aminomethyl-phenylacetyl](1c)*SC(2a)WQC(2a)[Y(2-aminoethoxy)][2- Nal][2-Me-Leu]E(1c)[Dab] SEQ ID NO: 83 [4-Aminomethyl-phenylacetyl](1c)*TC(2a)WQC(2a)[Y(2-aminoethoxy)][2- Nal][2-Me-Leu]E(1c)[{d}R] SEQ ID NO: 84 K(1c)SC(2a)WQC(2a)[Y(2-aminoethoxy)][2-Nal][2-Me-Leu]E(1c)[{d}R] SEQ ID NO: 85 K(1c)TC(2a)WQC(2a)[Y(2-aminoethoxy)][2-Nal][2-Me-Leu]E(1c)[{d}R] SEQ ID NO: 86 K(1c)SC(2a)WQC(2a)[Y(2-aminoethoxy)][2-Nal][2-Me-Leu]E(1c)S SEQ ID NO: 87 [6-Aminohexanoyl](1c)*SC(2a)WQC(2a)[Y(2-aminoethoxy)][2-Nal][2-Me- Leu]E(1c)[{d}R] SEQ ID NO: 88 [6-Amino-4-oxahexanoyl](1c)*SC(2a)WQC(2a)[Y(2-aminoethoxy)][2- Nal][2-Me-Leu]E(1c)[{d}R] SEQ ID NO: 89 [trans-4-Aminomethyl-cyclohexyl-1-carbonyl](1c)*[beta-homo- Ser]C(2a)WQC(2a)[Y(2-aminoethoxy)][2-Nal][2-Me-Leu]E(1c)[{d}R] SEQ ID NO: 90 [(4-(2-Aminoethyl)-piperazine-1-yl)-acetyl](1c)*SC(2a)WQC(2a)[Y(2- aminoethoxy)][2-Nal][2-Me-Leu]E(1c)[{d}R] SEQ ID NO: 91 [(4-(2-Aminoethyl)-piperazine-1-yl)-acetyl](1c)*SC(2a)WQC(2a)[Y(2- aminoethoxy)][2-Nal][2-Me-Leu]D(1c)[{d}R] SEQ ID NO: 92 [3-Aminomethyl-phenylacetyl](1c)*SC(2a)WQC(2a)[Y(2-aminoethoxy)][2- Nal][2-Me-Leu]E(1c)[{d}R] SEQ ID NO: 93 [2-Aminomethyl-phenylacetyl](1c)*SC(2a)WQC(2a)[Y(2-aminoethoxy)][2- Nal][2-Me-Leu]E(1c)[{d}R] SEQ ID NO: 94 [K(N3)](1g)SC(2a)WQC(2a)[Y(2-aminoethoxy)][2-Nal][2-Me- Leu][Pra](1g)[{d}R] SEQ ID NO: 95 [Azidoacetic acid](1g)*SC(2a)WQC(2a)[Y(2-aminoethoxy)][2-Nal][2-Me- Leu][Glu(propargylamine)](1g)[{d}R] SEQ ID NO: 96 [Azidoacetic acid](1g)*SC(2a)WQC(2a)[Y(2-aminoethoxy)][2-Nal][2-Me- Leu][Dab(3-butynoic acid)](1g)[{d}R] SEQ ID NO: 97 [but-3-ynoic acid](1g)*SC(2a)WQC(2a)[Y(2-aminoethoxy)][2-Nal][2-Me- Leu][Dab(azidoacetic acid)](1g)[{d}R] SEQ ID NO: 98 [(N3)-Ala](1g)*SC(2a)WQC(2a)[Y(2-aminoethoxy)][2-Nal][2-Me- Leu][Glu(propargylamine)](1g)[{d}R] SEQ ID NO: 99 [(N3)-Ala](1g)*SC(2a)WQC(2a)[Y(2-aminoethoxy)][2-Nal][2-Me- Leu][Dab(3-butynoic acid)](1g)[{d}R] SEQ ID NO: 100 [but-3-ynoic acid](1g)*SC(2a)WQC(2a)[Y(2-aminoethoxy)][2-Nal][2-Me- Leu][Dab((N3)-Ala))](1g)[{d}R] SEQ ID NO: 101 [4-Aminomethyl-2-pyridineacetyl](1c)*SC(2a)WQC(2a)[Y(2- aminoethoxy)][2-Nal][2-Me-Leu]E(1c)[{d}R] SEQ ID NO: 102 [4-Aminomethyl-3-pyridineacetyl](1c)*SC(2a)WQC(2a)[Y(2- aminoethoxy)][2-Nal][2-Me-Leu]E(1c)[{d}R] SEQ ID NO: 103 [4-Aminomethyl-2-fluoro-phenylacetyl](1c)*SC(2a)WQC(2a)[Y(2- aminoethoxy)][2-Nal][2-Me-Leu]E(1c)[{d}R] SEQ ID NO: 104 [4-Aminomethyl-3-methyl-phenylacetyl](1c)*SC(2a)WQC(2a)[Y(2- aminoethoxy)][2-Nal][2-Me-Leu]E(1c)[{d}R] SEQ ID NO: 105 [4-Aminomethyl-3-methoxy-phenylacetyl](1c)*SC(2a)WQC(2a)[Y(2- aminoethoxy)][2-Nal][2-Me-Leu]E(1c)[{d}R] 241 SEQ ID NO: 106 [but-3-ynoic acid](1h)*SC(2a)WQC(2a)[Y(2-aminoethoxy)][2-Nal][2-Me- Leu][Dab(azidoacetic acid)](1h)[{d}R] SEQ ID NO: 107 [but-3-ynoic acid](1h)*SC(2a)WQC(2a)[Y(2-aminoethoxy)][2-Nal][2-Me- Leu][Dab((N3)-Ala)](1h)[{d}R] SEQ ID NO: 108 [4-Aminomethyl-phenylacetyl](1c)*SC(2a)WQC(2a)[Y(2-aminoethoxy)][2- Nal][2-Me-Leu]E(1c)[{d}R] [4-Aminomethyl-phenylacetyl](1c)*SC(2a)WQC(2a)[Y(2-aminoethoxy)][2- SEQ ID NO: 109 Nal][2-Me-Leu]E(1c)[{d}2,4-Diaminobutanoyl([2-(trimethyl-2- aminoethoxy)ethoxy]propyl)] SEQ ID NO: 110 [4-Aminomethyl-phenylacetyl](1c)*SC(2a)WQC(2a)[Dab][2-Nal][2-Me- Leu]E(1c)[{d}R] [4-Aminomethyl-phenylacetyl](1c)*SC(2a)WQC(2a)[2,4- SEQ ID NO: 111 Diaminobutanoyl([2-(trimethyl-2-aminoethoxy)ethoxy]propyl)][2-Nal][2-Me- Leu]E(1c)[{d}R] SEQ ID NO: 112 [Dab](1c)*SC(2a)WQC(2a)[Y(2-aminoethoxy)][2-Nal][2-Me- Leu]E(1c)[{d}R] [2,4-Diaminobutanoyl([2-(trimethyl-2- SEQ ID NO: 113 aminoethoxy)ethoxy]propyl)](1c)*SC(2a)WQC(2a)[Y(2-aminoethoxy)][2- Nal][2-Me-Leu]E(1c)[{d}R] SEQ ID NO: 114 [4-Aminomethyl-phenylacetyl](1c)*SC(2a)WQC(2a)[F(4-NH2-(2-(trimethyl- 2-aminoethoxy)ethoxy)propyl)][2-Nal][2-Me-Leu]E(1c)[{d}R] SEQ ID NO: 115 [4-Aminomethyl-phenylacetyl](1c)*SC(2a)WQC(2a)[Y(2-aminoethoxy)][2- Nal][2-Me-Leu]E(1c)[{d}Q] SEQ ID NO: 116 [4-Aminomethyl-phenylacetyl](1c)*SC(2a)WQC(2a)[Y(2-aminoethoxy)][2- Nal][2-Me-Leu]E(1c)[{d}E] SEQ ID NO: 117 [4-Aminomethyl-phenylacetyl](1c)*SC(2a)WQC(2a)[Y(2-aminoethoxy)][2- Nal][2-Me-Leu]E(1c)[{d}H] SEQ ID NO: 118 [4-Aminomethyl-phenylacetyl](1c)*SC(2a)WQC(2a)[Y(2-aminoethoxy)][2- Nal][2-Me-Leu]E(1c)[3-Aminopropanoyl] SEQ ID NO: 119 [4-Aminomethyl-phenylacetyl](1c)*SC(2a)WQC(2a)[Y(2-aminoethoxy)][2- Nal][2-Me-Leu]E(1c)[3-Aminopropanoyl] SEQ ID NO: 120 [4-Aminomethyl-phenylacetyl](1c)*SC(2a)WQC(2a)[Y(2-aminoethoxy)][2- Nal][2-Me-Leu]E(1c)[Dab][3-(3-Pyridyl)-Ala] SEQ ID NO: 121 [4-Aminomethyl-phenylacetyl](1c)*SC(2a)WQC(2a)[Y(2-aminoethoxy)][6- F-Trp][2-Me-Leu]E(1c)[Dab][3-(3-Pyridyl)-Ala] SEQ ID NO: 122 [4-Aminomethyl-phenylacetyl](1c)*SE(2c)WQ[Dab](2c)[Y(2- aminoethoxy)][2-Nal][2-Me-Leu]E(1c)[Dab][3-(3-Pyridyl)-Ala] SEQ ID NO: 123 [4-Aminomethyl-phenylacetyl](1c)*S[Dab](2c)WQE(2c)[Y(2- aminoethoxy)][2-Nal][2-Me-Leu]E(1c)[Dab][3-(3-Pyridyl)-Ala] SEQ ID NO: 124 [4-Aminomethyl-phenylacetyl](1c)*SE(2c)WQ[Orn](2c)[Y(2- aminoethoxy)][2-Nal][2-Me-Leu]E(1c)[Dab][3-(3-Pyridyl)-Ala] SEQ ID NO: 125 [4-Aminomethyl-phenylacetyl](1c)*SE(2c)WQ[Dab](2c)[Y(2- aminoethoxy)][2-Nal][2-Me-Leu]E(1c)[Dab] SEQ ID NO: 126 [4-Aminomethyl-phenylacetyl](1c)*VE(2c)WQ[Dab](2c)[Y(2- aminoethoxy][2-Nal][2-Me-Leu]E(1c)[Dab] SEQ ID NO: 127 [4-Aminomethyl-phenylacetyl](1c)*IE(2c)WQ[Dab](2c)[Y(2- aminoethoxy)][2-Nal][2-Me-Leu]E(1c)[Dab] SEQ ID NO: 128 [4-Aminomethyl-phenylacetyl](1c)*SE(2c)WV[Dab](2c)[Y(2- aminoethoxy)][2-Nal][2-Me-Leu]E(1c)[Dab] SEQ ID NO: 129 [4-Aminomethyl-phenylacetyl](1c)*SE(2c)WH[Dab](2c)[Y(2- aminoethoxy)][2-Nal][2-Me-Leu]E(1c)[Dab] SEQ ID NO: 130 [4-Aminomethyl-phenylacetyl](1c)*SE(2c)WQ[Dab](2c)F[2-Nal][2-Me- Leu]E(1c)[Dab] SEQ ID NO: 131 [4-Aminomethyl-phenylacetyl](1c)*SE(2c)WQ[Dab](2c)V[2-Nal][2-Me- Leu]E(1c)[Dab] SEQ ID NO: 132 [4-Aminomethyl-phenylacetyl](1c)*SE(2c)WQ[Dab](2c)[F(4-Me)][2-Nal][2- Me-Leu]E(1c)[Dab] SEQ ID NO: 133 [4-Aminomethyl-phenylacetyl](1c)*SE(2c)WQ[Dab](2c)[Y(2- aminoethoxy)]H[2-Me-Leu]E(1c)[Dab] SEQ ID NO: 134 [4-Aminomethyl-phenylacetyl](1c)*SE(2c)WQ[Dab](2c)[Y(2- aminoethoxy)][F(3-F)][2-Me-Leu]E(1c)[Dab] SEQ ID NO: 135 [4-Aminomethyl-phenylacetyl](1c)*SE(2c)WQ[Dab](2c)[Y(2- aminoethoxy)][F(3,4-Me)][2-Me-Leu]E(1c)[Dab] SEQ ID NO: 136 [4-Aminomethyl-phenylacetyl](1c)*SE(2c)WQ[Dab](2c)[Y(2- aminoethoxy)][2-Nal][2-Me-Val]E(1c)[Dab] ID NO: 137 [4-Aminomethyl-phenylacetyl](1c)*SE(2c)WQ[Dab](2c)[Y(2- aminoethoxy)][2-Nal][2-Me-Leu]E(1c) SEQ ID NO: 138 [4-Aminomethyl-phenylacetyl](1c)*SE(2c)[4-F-Trp]Q[Dab](2c)[Y(2- aminoethoxy)][2-Nal][2-Me-Leu]E(1c)[Dab] SEQ ID NO: 139 [4-Aminomethyl-phenylacetyl](1c)*SE(2c)[7-F-Trp]Q[Dab](2c)[Y(2- aminoethoxy)][2-Nal][2-Me-Leu]E(1c)[Dab] SEQ ID NO: 140 [4-Methylaminomethyl-phenylacetyl](1c)*SC(2a)WQC(2a)[Y(2- aminoethoxy)][2-Nal][2-Me-Leu]E(1c)[Dab] SEQ ID NO: 141 [4-Aminomethyl-phenylacetyl](1c)*[N-Me-Ser]C(2a)WQC(2a)[Y(2- aminoethoxy)][2-Nal][2-Me-Leu]E(1c)[Dab] SEQ ID NO: 142 [4-Aminomethyl-phenylacetyl](1c)*S[N-Me-Cys](2a)WQC(2a)[Y(2- aminoethoxy)][2-Nal][2-Me-Leu]E(1c)[Dab] SEQ ID NO: 143 [4-Aminomethyl-phenylacetyl](1c)*SC(2a)[N-Me-Trp]QC(2a)[Y(2- aminoethoxy)][2-Nal][2-Me-Leu]E(1c)[Dab] SEQ ID NO: 144 [4-Aminomethyl-phenylacetyl](1c)*SC(2a)W[N-Me-Gln]C(2a)[Y(2- aminoethoxy)][2-Nal][2-Me-Leu]E(1c)[Dab] SEQ ID NO: 145 [4-Aminomethyl-phenylacetyl](1c)*[Q(pyrrolidin)]E(2c)WQ[Dab](2c)[Y(2- aminoethoxy)][2-Nal][2-Me-Leu]E(1c)[Dab] SEQ ID NO: 146 [4-Aminomethyl-phenylacetyl](1c)*SE(2c)W[Q(pyrrolidin)][Dab](2c)[Y(2- aminoethoxy)][2-Nal][2-Me-Leu]E(1c)[Dab] SEQ ID NO: 147 [4-Aminomethyl-phenylacetyl](1c)*SC(2a)WQC(2a)[Y(2-aminoethoxy)][2- Nal][2-Me-Leu]E(1c)R[3-(3-Pyridyl)-Ala] SEQ ID NO: 148 [(3-Aminomethyl)benzoyl](1c)*SC(2a)WQC(2a)[Y(2-aminoethoxy)][2- Nal][2-Me-Leu]E(1c)[Dab][3-(3-Pyridyl)-Ala] SEQ ID NO: 149 [(3-Aminomethyl)benzoyl](1c)*SC(2a)WQC(2a)][Y(2-aminoethoxy)][2- Nal][2-Me-Leu]E(1c)R[3-(3-Quinolinyl)-Ala] SEQ ID NO: 150 [(3-Aminomethyl)benzoyl](1c)*SC(2a)WQC(2a)][Y(2-aminoethoxy)][2- Nal][2-Me-Leu]E(1c)R[{d}[3-(3-Pyridyl)-Ala]] SEQ ID NO: 151 [(3-Aminomethyl)benzoyl](1c)*SC(2a)WQC(2a)][Y(2-aminoethoxy)][2- Nal][2-Me-Leu]E(1c)R[3-Amino-3-(3'-pyridyl)propionyl] SEQ ID NO: 152 [(3-Aminomethyl)benzoyl](1c)*SC(2a)WQC(2a)][Y(2-aminoethoxy)][2- Nal][2-Me-Leu]E(1c)R[F(3-F)] SEQ ID NO: 153 [(3-Aminomethyl)benzoyl](1c)*SC(2a)WQC(2a)][Y(2-aminoethoxy)][2- Nal][2-Me-Leu]E(1c)R[F(3,5-F)] SEQ ID NO: 154 [(3-Aminomethyl)benzoyl](1c)*SC(2a)WQC(2a)][Y(2-aminoethoxy)][2- Nal][2-Me-Leu]E(1c)R[4-Aminomethyl-2-pyridineacetyl] SEQ ID NO: 155 K(1c)TC(2a)WQC(2a)[Y(2-aminoethoxy)][2-Nal][2-Me-Leu]E(1c)[Dab][3- (3-Pyridyl)-Ala] SEQ ID NO: 156 [(3-Aminomethyl)benzoyl](1c)*IE(2c)WQ[Dab](2c)[Y(2-aminoethoxy)][2- Nal][2-Me-Val]E(1c)[Dab][3-(3-Pyridyl)-Ala] SEQ ID NO: 157 [4-Aminomethyl-phenylacetyl](1c)*IE(2c)WQ[Dab](2c)[Y(2- aminoethoxy)][2-Nal][2-Me-Val]E(1c)[Dab][3-(3-Pyridyl)-Ala] SEQ ID NO: 158 [4-Aminomethyl-phenylacetyl](1c)*IE(2c)WQ[Dab](2c)[Y(2- aminoethoxy)][F(3,4-Me)][2-Me-Val]E(1c)G[3-(3-Pyridyl)-Ala] SEQ ID NO: 159 [4-Aminomethyl-phenylacetyl](1c)*IE(2c)WQ[Dab](2c)[F(4-Me)][F(3,4- Me)][2-Me-Val]E(1c)G[3-(3-Pyridyl)-Ala] ID NO: 160 [4-Aminomethyl-phenylacetyl](1c)*IE(2c)WQ[Dab](2c)[F(4-Me)][F(3,4- Me)][2-Me-Val]E(1c)[GABA][3-(3-Pyridyl)-Ala] SEQ ID NO: 161 [4-Aminomethyl-phenylacetyl](1c)*IE(2c)WQ[Dab](2c)[F(4-Me)][F(3,4- Me)][2-Me-Val]E(1c)G[2,3-Diaminopropanoyl(3-pyridylacetyl)] SEQ ID NO: 162 [4-Aminomethyl-phenylacetyl](1c)*IE(2c)WQ[Dab](2c)[F(4-Me)][F(3,4- Me)][2-Me-Val]E(1c)G[2,3-Diaminopropanoyl(3-pyridylpropionyl)] SEQ ID NO: 163 [4-Aminomethyl-phenylacetyl](1c)*IE(2c)WQ[Dab](2c)[F(4-Me)][F(3,4- Me)][2-Me-Val]E(1c)G[2,3-Diaminopropanoyl(3-fluorobenzoyl)] SEQ ID NO: 164 [4-Aminomethyl-phenylacetyl](1c)*IE(2c)WQ[Dab](2c)[F(4-Me)][F(3,4- Me)][2-Me-Val]E(1c)G[2,3-Diaminopropanoyl(3-fluorophenylacetyl)] SEQ ID NO: 165 [4-Aminomethyl-phenylacetyl](1c)*IE(2c)WQ[Dab](2c)[Y(2- aminoethoxy)][F(3,4-Me)][2-Me-Val]E(1c)[Dab][2-Me-3-(3-Pyridyl)-Ala] SEQ ID NO: 166 [4-Aminomethyl-phenylacetyl](1c)*IE(2c)WQ[Dab](2c)[Y(Me)][F(3,4- Me)][2-Me-Val]E(1c)[Dab][2-Me-3-(3-Pyridyl)-Ala] SEQ ID NO: 167 [4-Aminomethyl-phenylacetyl](1c)*IE(2c)WQ[Dab](2c)[2-Me-Phe][F(3,4- Me)][2-Me-Val]E(1c)[Dab][2-Me-3-(3-Pyridyl)-Ala] SEQ ID NO: 168 [4-Aminomethyl-phenylacetyl](1c)*IE(2c)WQ[Dab](2c)[Bip][F(3,4-Me)][2- Me-Val]E(1c)[Dab][2-Me-3-(3-Pyridyl)-Ala] SEQ ID NO: 169 [4-Aminomethyl-phenylacetyl](1c)*IE(2c)WQ[Dab](2c)[2-Me-F(4-F)][F(3,4- Me)][2-Me-Val]E(1c)[Dab][2-Me-3-(3-Pyridyl)-Ala] SEQ ID NO: 170 [4-Aminomethyl-phenylacetyl](1c)*IE(2c)WQ[Dab](2c)[{d}F(4-F)][F(3,4- Me)][2-Me-Val]E(1c)[Dab][2-Me-3-(3-Pyridyl)-Ala] SEQ ID NO: 171 [4-Aminomethyl-phenylacetyl](1c)*IE(2c)WQ[Dab](2c)[F(4-Cl)][F(3,4- Me)][2-Me-Val]E(1c)[Dab][2-Me-3-(3-Pyridyl)-Ala] SEQ ID NO: 172 [4-Aminomethyl-phenylacetyl](1c)*IE(2c)WQ[Dab](2c)[alpha-Me- Trp][F(3,4-Me)][2-Me-Val]E(1c)[Dab][2-Me-3-(3-Pyridyl)-Ala] SEQ ID NO: 173 [4-Aminomethyl-phenylacetyl](1c)*IE(2c)WQ[Dab](2c)[3,3-Diphenyl- Ala][F(3,4-Me)][2-Me-Val]E(1c)[Dab][2-Me-3-(3-Pyridyl)-Ala] SEQ ID NO: 174 [4-Aminomethyl-phenylacetyl](1c)*IE(2c)WQ[Dab](2c)[Phg][F(3,4-Me)][2- Me-Val]E(1c)[Dab][2-Me-3-(3-Pyridyl)-Ala] SEQ ID NO: 175 [4-Aminomethyl-phenylacetyl](1c)*IE(2c)WQ[Dab](2c)[F(4-Me)][1-Me- Trp][2-Me-Val]E(1c)[Dab][2-Me-3-(3-Pyridyl)-Ala] SEQ ID NO: 176 [4-Aminomethyl-phenylacetyl](1c)*IE(2c)WQ[Dab](2c)[F(4-Me)][Bip][2-Me- Val]E(1c)[Dab][2-Me-3-(3-Pyridyl)-Ala] SEQ ID NO: 177 [4-Aminomethyl-phenylacetyl](1c)*IE(2c)WQ[Dab](2c)[F(4-Me)][{d}6-F- Trp][2-Me-Val]E(1c)[Dab][2-Me-3-(3-Pyridyl)-Ala] or a pharmaceutically acceptable salt or solvate thereof; wherein: * = bridge uses the peptide backbone amine or carboxylic acid at the N- or C-terminus, not the side chain amine or carboxylic acid (1a) = [2,11] 1,3-dithio-propan-2-one bridge; (1c) = [2,11] lactam bridge; (1g) = [2,11] 1,4- disubstituted 1,2,3-triazole bridge; (1h) = [2,11] 1,5-disubstituted 1,2,3-triazole bridge; (2a) = [4,7] 1,3-dithio-propan-2-one bridge; (2c) = [4,7] lactam bridge; (2d) = [4,7] 1,2- phenylenedimethanethiol bridge; (2e) = [4,7] 1,3-phenylenedimethanethiol bridge; (2f) = [4,7] 1,4-phenylenedimethanethiol bridge; (2g) = [4,7] 1 ,4-disubstituted 1,2,3-triazole bridge.

78. A compound according to claim 1 which is selected from: * = bridge uses the peptide backbone amine or carboxylic acid at the /V- or C-terminus, not the side chain amine or carboxylic acid (1a) = [2,11] 1,3-dithio-propan-2-one bridge; (1c) = [2,11] lactam bridge; (1g) = [2,11] 1,4- disubstituted 1,2,3-triazole bridge; (1h) = [2,11] 1,5-disubstituted 1,2,3-triazole bridge; (2a) = [4,7] 1,3-dithio-propan-2-one bridge; (2c) = [4,7] lactam bridge; (2d) = [4,7] 1,2- phenylenedimethanethiol bridge; (2e) = [4,7] 1,3-phenylenedimethanethiol bridge; (2f) = [4,7] 1,4-phenylenedimethanethiol bridge; (2g) = [4,7] 1 ,4-disubstituted 1,2,3-triazole bridge.

79. A pharmaceutical composition comprising a compound according to any one of the preceding claims in combination with a pharmaceutically acceptable carrier, excipient or vehicle.

80. A method for the synthesis of a compound according to any one of claims 1 to 78, comprising synthesising the analogue by solid-phase or liquid-phase peptide synthesis methodology, optionally isolating and/or purifying the final product, and optionally further comprising the step of forming an amide bond, forming two thioether bonds with a linker, or forming a triazole between the amino acid residues at positions X2 and X11, and optionally further comprising the step of forming an amide bond, forming two thioether bonds with a linker, or forming a triazole between the amino acid residues at positions X4 and X7.

81. A compound according to any one of claims 1 to 78, or a pharmaceutical composition according to claim 79, for use in a method of medical treatment.

82. A compound according to any one of claims 1 to 78, or a pharmaceutical composition according to claim 79, for use in a method of prevention or treatment of Inflammatory Bowel Disease (IBD), ulcerative colitis, Crohn's disease, Celiac disease (nontropical Sprue), enteropathy associated with seronegative arthropathies, microscopic colitis, collagenous colitis, eosinophilic gastroenteritis, colitis associated with radio- or chemo-therapy, colitis associated with disorders of innate immunity as in leukocyte adhesion deficiency-l, chronic granulomatous disease, glycogen storage disease type 1b, Hermansky-Pudlak syndrome, Chediak-Higashi syndrome, and Wiskott-Aldrich Syndrome, pouchitis resulting after proctocolectomy and ileoanal anastomosis, gastrointestinal cancer, pancreatitis, insulin-dependent diabetes mellitus, mastitis, cholecystitis, cholangitis, pericholangitis, chronic bronchitis, chronic sinusitis, asthma, psoriasis, psoriatic arthritis, ankylosing spondylitis, or graft versus host disease in a subject, and combinations thereof.

83. The compound or pharmaceutical composition for use according to claim 82, wherein the compound or pharmaceutical composition is for use in a method of prevention or treatment of inflammatory bowel (IBD), Crohn’s Disease, ulcerative colitis, and psoriasis.

84. Use of a compound according to any one of claims 1 to 78, or a pharmaceutical composition according to claim 79, in the manufacture of a medicament for the prevention or treatment of Inflammatory Bowel Disease (IBD), ulcerative colitis, Crohn's disease, Celiac disease (nontropical Sprue), enteropathy associated with seronegative arthropathies, microscopic colitis, collagenous colitis, eosinophilic gastroenteritis, colitis associated with radio- or chemo-therapy, colitis associated with disorders of innate immunity as in leukocyte adhesion deficiency-l, chronic granulomatous disease, glycogen storage disease type 1b, Hermansky-Pudlak syndrome, Chediak-Higashi syndrome, and Wiskott-Aldrich Syndrome, pouchitis resulting after proctocolectomy and ileoanal anastomosis, gastrointestinal cancer, pancreatitis, insulin-dependent diabetes mellitus, mastitis, cholecystitis, cholangitis, pericholangitis, chronic bronchitis, chronic sinusitis, asthma, psoriasis, psoriatic arthritis, ankylosing spondylitis, or graft versus host disease in a subject, and combinations thereof.

85. The use of the compound or pharmaceutical composition according to claim 84, wherein the use of the compound or pharmaceutical compositions is in the manufacture of a medicament for the prevention or treatment of inflammatory bowel (IBD), Crohn’s Disease, ulcerative colitis, and psoriasis.

86. A method of prevention or treatment of Inflammatory Bowel Disease (IBD), ulcerative colitis, CrolT's disease, Celiac disease (nontropical Sprue), enteropathy associated with seronegative arthropathies, microscopic colitis, collagenous colitis, eosinophilic gastroenteritis, colitis associated with radio- or chemo-therapy, colitis associated with disorders of innate immunity as in leukocyte adhesion deficiency-l, chronic granulomatous disease, glycogen storage disease type 1b, Hermansky-Pudlak syndrome, Chediak-Higashi syndrome, and Wiskott-Aldrich Syndrome, pouchitis resulting after proctocolectomy and ileoanal anastomosis, gastrointestinal cancer, pancreatitis, insulin-dependent diabetes mellitus, mastitis, cholecystitis, cholangitis, pericholangitis, chronic bronchitis, chronic sinusitis, asthma, psoriasis, psoriatic arthritis, ankylosing spondylitis, or graft versus host disease in a subject, and combinations thereof; which comprises administering to a subject an effective amount of a compound according to any one of claims 1 to 78, or a pharmaceutical composition according to claim 79.

87. The method of prevention or treatment according to claim 86, wherein the method of prevention or treatment is for inflammatory bowel (IBD), Crohn’s Disease, ulcerative colitis, and psoriasis.
```


### A.4 US9605027B2 (Medical Diagnostic Laboratories) — 오귀속 근거 [VERBATIM]

**[ANALYSIS]** 출원인이 **Medical Diagnostic Laboratories, LLC**이며, SEQ ID NO:177~179의 환형 폴리펩타이드를 청구한다 — Protagonist의 Pen-Pen 단환 펩타이드와 무관한 별개 당사자/분자다.

**[VERBATIM] — 출처: Google Patents (`work/05_gp_authoritative/US9605027B2.md`)**

```text
1. An isolated cyclic polypeptide consisting of an amino acid sequence selected from the group consisting of SEQ ID NO: 177, SEQ ID NO: 178 and SEQ ID NO: 179, wherein said isolated cyclic polypeptide inhibits binding of IL-23 to IL-23 receptor and inhibits IL-23-mediated cell signaling.

2. The isolated cyclic polypeptide of claim 1, wherein said isolated cyclic polypeptide consisting of SEQ ID NO: 177.

3. The isolated cyclic polypeptide of claim 1, wherein said isolated cyclic polypeptide consisting of SEQ ID NO: 178.

4. The isolated cyclic polypeptide of claim 1, wherein said isolated cyclic polypeptide consisting of SEQ ID NO: 179.

5. A method of inhibiting production of IL-17F in a Th17 cell in a human, comprising the steps of: a) providing a human Th17 cell in need of inhibiting production of IL-17F; and b) exposing said Th17 cell to said isolated cyclic polypeptide of claim 1.

6. The method of claim 5, wherein said IL-17F is IL-17F protein.

7. The method of claim 5, wherein said production of IL-17F is assayed by an ELISA.

8. A method of inhibiting production of IL-17F in a splenocyte in a human, comprising the steps of: a) providing a human splenocyte in need of inhibiting production of IL-17F from said splenocyte; and b) exposing said splenocyte to said isolated cyclic polypeptide of claim 1.

9. The method of claim 8, wherein said IL-17F is IL-17F mRNA.

10. The method of claim 8, wherein said production of IL-17F is assayed by RT-PCR.

11. A method of inhibiting production of IL-22 from a mononuclear cell in a human, comprising the steps of: a) providing a human mononuclear cell in need of inhibiting production of IL-22 from said mononuclear cell; and b) exposing said mononuclear cell to said isolated cyclic polypeptide of claim 1.

12. The method of claim 11, wherein said IL-22 is IL-22 protein.

13. The method of claim 11, wherein said production of IL-22 is assayed by an ELISA.
```


### A.5 USRE49026E1 (Medical Diagnostic Laboratories, US9169292 재발행) — 오귀속 근거 [VERBATIM]

**[ANALYSIS]** A.4와 동일 출원인의 재발행 특허(US9169292 재발행)이며 청구항 1이 동일하게 SEQ ID NO:177~179 환형 폴리펩타이드다. icotrokinra 무관.

**[VERBATIM] — 출처: Google Patents (`work/05_gp_authoritative/USRE49026E1.md`)**

```text
1. An isolated cyclic polypeptide consisting of an amino acid sequence selected from the group consisting of SEQ ID NO: 177, SEQ ID NO: 178 and SEQ ID NO: 179, wherein said isolated cyclic polypeptide inhibits binding of IL-23 to IL-23 receptor and inhibits IL-23-mediated cell signaling.

2. The isolated cyclic polypeptide of claim 1, wherein said isolated cyclic polypeptide consisting of SEQ ID NO: 177.

3. The isolated cyclic polypeptide of claim 1, wherein said isolated cyclic polypeptide consisting of SEQ ID NO: 178.

4. The isolated cyclic polypeptide of claim 1, wherein said isolated cyclic polypeptide consisting of SEQ ID NO: 179.

5. A method of inhibiting production of IL-17F in a Th17 cell in a human, comprising the steps of: a) providing a human Th17 cell in need of inhibiting production of IL-17F; and b) exposing said Th17 cell to said isolated cyclic polypeptide of claim 1.

6. The method of claim 5, wherein said IL-17F is IL-17F protein.

7. The method of claim 5, wherein said production of IL-17F is assayed by an ELISA.

8. A method of inhibiting production of IL-17F in a splenocyte in a human, comprising the steps of: a) providing a human splenocyte in need of inhibiting production of IL-17F from said splenocyte; and b) exposing said splenocyte to said isolated cyclic polypeptide of claim 1.

9. The method of claim 8, wherein said IL-17F is IL-17F mRNA.

10. The method of claim 8, wherein said production of IL-17F is assayed by RT-PCR.

11. A method of inhibiting production of IL-22 from a mononuclear cell in a human, comprising the steps of: a) providing a human mononuclear cell in need of inhibiting production of IL-22 from said mononuclear cell; and b) exposing said mononuclear cell to said isolated cyclic polypeptide of claim 1.

12. The method of claim 11, wherein said IL-22 is IL-22 protein.

13. The method of claim 11, wherein said production of IL-22 is assayed by an ELISA.

14. The method of claim 11, wherein said isolated cyclic polypeptide is SEQ ID NO: 177.

15. The method of claim 11, wherein said isolated cyclic polypeptide is SEQ ID NO: 178.

16. The method of claim 11, wherein said isolated cyclic polypeptide is SEQ ID NO: 179.

17. A method of identifying a polypeptides that inhibits binding of IL-23 to IL-23 receptor on a cell, comprising screening a phage display library of phage displaying candidate polypeptides for ability to bind a protein comprising a fragment of Δ9 IL-23 receptor, wherein the fragment consists of an amino acid sequence selected from amino acids 1-250 of Δ9 IL-23 receptor and amino acids 24-250 of Δ9 IL-23 receptor sequence, selecting a candidate polypeptide that was determined to have an ability to bind the protein by said screening; and determining the ability of the candidate polypeptide from said selecting to inhibit binding of IL-23 to IL-23 receptor.

18. The method according to claim 17, wherein said candidate polypeptides comprise 12 to 18 amino acids.

19. The method according to claim 17, wherein said protein further comprises a Flag protein.

20. The method according to claim 19, wherein said Flag protein has the sequence of SEO ID NO: 175.

21. The method according to claim 19, wherein said method further comprises capturing the polypeptide that interacts with the protein with an anti-Flag affinity gel.

22. The method according to claim 17, wherein said protein further comprises an Fc chimera.

23. The method according to claim 22, wherein the Fc chimera comprises an Fc region of human IgG1.

24. The method according to claim 22, wherein said method further comprises capturing the polypeptide that interacts with the protein with protein A Sepharose.

25. The method according to claim 17, further comprising conducting a binding assay to detect binding between candidate polypeptides from said selecting to verify said candidate polypeptide binds the IL-23 receptor.

26. The method according to claim 25, wherein said binding assay is by immunoprecipitation.

27. The method according to claim 25, wherein said binding assay is an ELISA assay.

28. The method according to claim 17, wherein said determining the ability of the candidate polypeptide from said selecting to inhibit the binding of IL-23 to IL-23 receptor is by competitive ELISA.

29. The method according to claim 17, further comprising sequencing candidate polypeptide determined to inhibit the binding of IL-23 to IL-23 receptor.

30. The method according to claim 17, wherein the binding of IL-23 is via the p19 subunit of IL-23 cytokine.

31. The method of claim 5, wherein said isolated cyclic polypeptide is SEQ ID NO: 177.

32. The method of claim 5, wherein said isolated cyclic polypeptide is SEQ ID NO: 178.

33. The method of claim 5, wherein said isolated cyclic polypeptide is SEQ ID NO: 179.

34. The method of claim 8, wherein said isolated cyclic polypeptide is SEQ ID NO: 177.

35. The method of claim 8, wherein said isolated cyclic polypeptide is SEQ ID NO: 178.

36. The method of claim 8, wherein said isolated cyclic polypeptide is SEQ ID NO: 179.
```


### A.6 US11180535B2 (박테리아 종양침투 키메라 펩타이드) — 오귀속 확정 [VERBATIM: FPO 추출본]

**[ANALYSIS]** 본 번호는 **Google Patents에서 404**가 반환되어 권위 소스 청구항을 얻지 못했고, FPO 추출본은 '살아있는 유전자조작 박테리아가 YebF-종양침투 펩타이드 키메라를 발현'하는 **박테리아 종양침투 특허**(SEQ ID NO:33/34)다. 이는 icotrokinra(SEQ ID NO:1, 단환 IL-23R 펩타이드)와 전혀 무관하므로 **오귀속 확정**으로 부록 A에 둔다. 아래는 권위 GP가 아닌 FPO 추출본(`work/02_extracted/US11180535B2.md`)이며, 무관 특허임을 입증하는 용도로만 인용한다.

**[VERBATIM] — 출처: FreePatentsOnline (`work/02_extracted/US11180535B2.md`); GP 미확보(404)**

```text
1. A genetic construct configured to cause a live genetically engineered host bacterium containing the genetic construct to express and at least one of surface display, secrete, and release, a chimeric peptide comprising a YebF sequence fused to a tumor-penetrating peptide sequence adapted to enhance the penetration of the live genetically engineered host bacterium into a tumor, wherein the YebF sequence fused to the tumor-penetrating peptide sequence comprises the amino acid sequence of SEQ ID NO: 33 or SEQ ID NO: 34.

2. The genetic construct according to claim 1, wherein the genetic construct is contained within the live genetically engineered host bacterium.

3. The genetic construct according to claim 2, wherein the live genetically engineered host bacterium is contained in a pharmaceutically acceptable dosage form.

4. The genetic construct according to claim 3, wherein the pharmaceutically acceptable dosage form containing the live genetically engineered host bacterium is adapted to cause colonization of a region of a human or an animal after administration of the pharmaceutically acceptable dosage form and expression of the chimeric peptide within the colonized region.

5. The genetic construct according to claim 3, wherein the pharmaceutically acceptable dosage form is adapted for administration to a human or animal.

6. The genetic construct according to claim 4, wherein the pharmaceutically acceptable dosage form comprises between about 105 to 1012 of the live genetically engineered host bacterium.

7. The genetic construct according to claim 4, wherein the pharmaceutically acceptable dosage form is adapted for oral administration.

8. The genetic construct according to claim 4, wherein the YebF sequence is fused to sunflower trypsin inhibitor.

9. The genetic construct according to claim 1, wherein the chimeric peptide comprises the amino acid sequence of SEQ ID NO: 33.

10. The genetic construct according to claim 1, wherein the chimeric peptide comprises the amino acid sequence of SEQ ID NO: 34.

11. The genetic construct according to claim 1, wherein the chimeric peptide comprises further comprises a secretion signal.

12. A live genetically engineered host bacterium comprising the genetic construct of claim 1, wherein the live genetically engineered host bacterium expresses and at least one of surface displays, secretes, and releases the chimeric peptide.

13. The live genetically engineered host bacterium according to claim 12, wherein the live genetically engineered host bacterium is contained in a pharmaceutically acceptable dosage form.

14. The live genetically engineered host bacterium according to claim 13, wherein the pharmaceutically acceptable dosage form is adapted for administration to a human or an animal to cause colonization of a region of the human or the animal and expression of the chimeric peptide within the colonized region.

15. The live genetically engineered host bacterium according to claim 14, wherein the YebF sequence is fused to sunflower trypsin inhibitor.

16. The live genetically engineered host bacterium according to claim 12, wherein the chimeric peptide comprises the amino acid sequence of SEQ ID NO: 33.

17. The live genetically engineered host bacterium according to claim 12, wherein the chimeric peptide comprises the amino acid sequence of SEQ ID NO: 34.

18. The live genetically engineered host bacterium according to claim 12, wherein the genetically engineered host bacterium surface displays the chimeric peptide.

19. The live genetically engineered host bacterium according to claim 12, wherein the genetically engineered host bacterium secretes the chimeric peptide.

20. The live genetically engineered host bacterium according to claim 12, wherein the genetically engineered host bacterium releases the chimeric peptide.
```

> A4 WO2024026471A1 / WO2024026472A1(Alector 항체)는 Google Patents 본문에 청구항이 미수록(claims=0)되어 [VERBATIM] 발췌가 불가하다. 서지정보(부록 A 표)만으로 오귀속 판정하며, 화학/생물학적으로 IL-23 펩타이드와 무관한 혈뇌장벽 통과 항체 특허다.

---

## 부록 B — 잔여 한계 및 주의사항

1. **JP2023145581A 청구항 미확보:** 일본어 청구항이 Google Patents `/en` 페이지에 실리지 않아(claims=0) 청구항 원문을 확보하지 못했다. **J-PlatPat(일본 특허청)** 원문 또는 일본어 GP 페이지에서 재수집 필요. 원문 보존 원칙상 청구항을 추측·번역해 채우지 않았다.
2. **PCT 출원의 만료일:** WO2021146441A1, WO2016011208A1, WO2023288019A2, WO2024155552A1은 PCT 국제출원으로, PCT 자체에는 특허 존속기간 만료 개념이 **해당없음(N/A)**이다. 만료는 각 지정국 국내단계 진입 후 해당국 법제로 산정된다(대응 미국 출원 만료일은 부록 C 참조).
3. **PTE/Hatch-Waxman 미반영:** 부록 C의 권위 만료일은 모두 Google Patents anticipated expiration(출원일/우선일+20년 base term)이며 **특허존속기간연장(PTE), PTA(존속기간조정)는 반영되지 않았다**. icotrokinra가 2026-03 FDA 승인 약물이므로, 특히 조성물 특허 **US11939361B2**에 Hatch-Waxman PTE(최대 +5년)가 적용되면 **실질 만료가 ~2045년까지 연장**될 수 있다.
4. **구조식 누락 청구항:** US12478617B2, US20240173309A1, US11041000B2 등 다수 청구항은 화학구조식 이미지를 청구하는데 GP `/en` 텍스트에 구조식이 렌더링되지 않아 본문이 빈 형태로 보존되어 있다. 구조 전문은 GP PDF/등록공보 원본 확인이 필요하다. 원문 보존 원칙상 추측 보충하지 않았다.
5. **청구항 번호 비연속/누락:** US20240173309A1(23번부터 시작), WO2024155552A1(2번부터 시작), US20210261622A1(`(canceled)` 표기 포함)은 GP 원문 자체가 그러하므로 그대로 보존했다.
6. **OCR/파싱 잔재 보존:** `Gin`/`Gln`, `lie`/`Ile`, `XI 0`/`X10`, `[Abta]`, `Ci`/`C1` 등은 권리범위를 바꿀 수 있으므로 교정하지 않고 원문 그대로 두었다(THE ONE RULE).
7. **CA3202226A1 우선일:** 캐나다 소스에서 우선일이 직접 확인되지 않아 '확인불가'로 둔다(미국 자매는 2020-11-20).

---

## 부록 C — 권위 만료일 표 (Google Patents anticipated expiration, 출원일/우선일+20년, PTE 미반영)

| 특허 | 권위 만료일 | base | 비고 |
|---|---|---|---|
| **US11939361B2** (조성물, SEQ ID NO:1) | **2041-11-19** | 출원일 2021-11-19 | **FDA 승인약 → Hatch-Waxman PTE 최대 +5년 시 ~2045 가능** |
| CA3202226A1 (조성물 CA) | ~2041-11-19 | 출원일 2021-11-19 | 캐나다 산정 별도 |
| JP2023145581A (조성물 JP) | ~2041 | 우선일 2020-11-20 | 일본 산정 별도; 청구항 미확보 |
| US20210261622A1 (속, 공개) | **2041-01-14** | 출원일 2021-01-14 | 17/149,509 계열 |
| US11845808B2 (속, 등록) | **2041-01-14** | 출원일 2021-01-14 | 17/149,509 등록본 |
| US12018057B2 (속/종) | **2041-01-14** | 출원일 2021-01-14 | 자매 17/149,544 |
| WO2021146441A1 (속 PCT) | N/A (PCT) | — | 미국 대응 2041-01-14 |
| US12552836B2 (속) | **2039-07-12** | 우선일 2018-07-12 | 계속출원 |
| US11041000B2 (속) | **2040-07-09** | PCT 2020-07-09 | |
| US10787490B2 (PTG-200/lipidated 종) | **2035-07-15** | 우선일 2015-07-15 | |
| US9624268B2 (PTG-200 기초) | **2035-07-15** | 우선일 2014-07-17 표시; GP base 2035-07-15 | |
| US10023614B2 (PTG-200) | **2035-07-15** | 동상 | |
| US10941183B2 (PTG-200) | **2035-07-15** | 동상 | |
| US11884748B2 (PTG-200) | **2035-07-15** | 동상 | |
| WO2016011208A1 (PTG-200 PCT) | N/A (PCT) | — | 추정 국내 ~2035 |
| US12478617B2 (lipidated) | **2042-07-14** | 우선일 2021-07-14 | |
| US20240173309A1 (lipidated 공개) | **2042-07-14** | 우선일 2021-07-14 | |
| WO2023288019A2 (lipidated PCT) | N/A (PCT) | — | 미국 대응 2042-07-14 |
| WO2024155552A1 (lipidated 제제 PCT) | N/A (PCT) | — | 추정 국내 ~2043 |

---

## 종합(Synthesis)

- **권리 핵심:** icotrokinra(=SEQ ID NO:1)의 시장 독점은 **조성물 특허 US11939361B2**(✅GP↔FPO 16/16 완전일치, 권위 만료 2041-11-19, **PTE 시 ~2045 가능**)가 가장 직접적이고 검증 강도가 높다. 동일 조성물의 캐나다(CA3202226A1, 153항) 대응까지 이번에 GP로 확보되어 조성물 권리의 영토 범위가 명확해졌다. 일본(JP2023145581A)만 청구항 미확보로 남는다.

- **다층 방어:** 조성물(US11939361B2/CA/JP) 위에 **속/종 Markush 특허**(WO2021146441A1 186항, US20210261622A1, US11845808B2, US12018057B2, US12552836B2, US11041000B2; 만료 2039~2041)가 단환 Pen-Pen 펩타이드 골격을 폭넓게 덮고, 그 아래에 **PTG-200 초기 세대**(2035 만료)와 **lipidated 화학형/제제**(2042~2043)가 전후 세대를 보강하는 다층(layered) 포트폴리오 구조다.

- **교차검증 신뢰도:** ✅완전일치 4건(US11939361B2, US12018057B2, US12552836B2, US12478617B2; + 공통분 일치 US20240173309A1)은 두 독립 소스가 청구항을 char-level로 동일하게 재현해 신뢰도가 가장 높다. ☑️부분교차검증 건들의 차이는 대부분 FPO의 Markush 치환기 목록 파싱 잡음에서 기인하며, **권위 원문은 Google Patents**다. ⚠️단일소스(GP) 건들은 FPO 미수집이나 GP 자체가 권위 소스이므로 청구항 자체의 신뢰도는 유지된다.

- **공백 해소 성과(이번 회차):** WO2021146441A1 168~186번(19항)과 CA3202226A1 전체(153항)를 신규 확보. **잔여 공백은 JP2023145581A 청구항 1건**(J-PlatPat 필요)으로 축소되었다.

- **오귀속 정리:** 9건(Dell 광통신, 칼, Alector 항체 2건, Zealand 경쟁사 펩타이드, MDL 폴리펩타이드 2건, 박테리아 키메라 펩타이드)은 권위 소스로 무관함을 확인해 부록 A로 격리했다. 특히 US11180535B2는 GP 404 + FPO 박테리아 펩타이드로 **오귀속 확정**했다.

> 본 보고서의 모든 [VERBATIM] 블록은 `work/05_gp_authoritative/<id>.md`(권위: Google Patents)에서 char-for-char 복사했으며(US11180535B2만 GP 404로 인해 FPO 추출본 인용), 한국어 [ANALYSIS]는 그 위에 덧붙였을 뿐 원문을 대체·변형하지 않았다. 생성일 2026-06-16.