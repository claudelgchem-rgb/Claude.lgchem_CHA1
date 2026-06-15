# icotrokinra (ICOTYDE / JNJ-2113 / PN-235) 특허 청구항 통합 분석 보고서

> **[VERBATIM] 표기 규칙:** 본 보고서에서 코드블록(```)으로 둘러싼 청구항 원문은 `work/02_extracted/<id>.md`에서 **한 글자도 수정·번역·정리하지 않고** 그대로 복사한 것이다. OCR 오류·오탈자(예: `Gin`=Gln, `lie`=Ile, `[Abta]`, `XI 0` 등)도 원문 보존 원칙에 따라 **그대로** 두었다. 그 위에 덧붙인 한국어 서술은 [ANALYSIS] 블록으로 분리하였으며, 청구항 원문과 절대 혼합하지 않는다.

---

## 1. 표지 / 머리말

| 항목 | 내용 |
|---|---|
| 보고서 제목 | icotrokinra (경구 IL-23R 길항 거대고리 펩타이드) 특허 패밀리 청구항 통합 분석 |
| 분석 대상 약물 | **ICOTYDE / icotrokinra / JNJ-2113 / PN-235** — 경구용 인터루킨-23 수용체(IL-23R) 길항 단환(monocyclic) 펩타이드 |
| 개발 주체 | Protagonist Therapeutics, Inc. + Janssen (Janssen Biotech / Janssen Pharmaceutica NV, J&J 계열) |
| 핵심 물질 정의 | icotrokinra = **SEQ ID NO: 1** (조성물 특허 US11939361B2 기준) |
| 후보 총건수 | **27건** |
| 생성일 | **2026-06-15** |

### 후보 27건 분류 요약

| 구분 | 건수 | 비고 |
|---|---|---|
| 진짜 icotrokinra / Protagonist+Janssen 패밀리 | **18건** | 본문 제3장 (티어별 정리) |
| 오귀속(misattributed) — icotrokinra 무관 | **8건** | 부록 A. 매니페스트에는 misattributed 7건 + US11180535B2(검증으로 확정된 오귀속 1건) = 실질 8건 |
| (이중 분류) US11180535B2 | — | 본래 core로 분류되었으나 검증 결과 무관 박테리아 펩타이드 특허로 확정 → 부록 A |
| **합계** | **27건** | (진짜 18 + 오귀속 8 + US11180535B2 1건 = 27. 단 US11180535B2는 매니페스트 genuine 목록에 들어있었으나 검증으로 오귀속 확정) |

> 분류상 주의: 매니페스트 `genuine_icotrokinra_family` 목록은 19개를 담고 있으나 그 중 **US11180535B2**가 검증 단계에서 무관 특허(박테리아 종양침투 키메라 펩타이드)로 확정되어 부록 A로 이동했다. 따라서 본문(진짜 패밀리)은 **18건**, 부록 A(오귀속)는 **8건**이다.

### 검증 현황 (verification verdict)

| Verdict | 건수 | 해당 특허 |
|---|---|---|
| ✅ 검증완료 (verified) | **1건** | **US11939361B2** (PASS 16/16, MISMATCH 0) |
| ⚠ 미검증-재작업필요 (needs_rework) | **7건** | US10787490B2, US11041000B2, US11845808B2, US12018057B2, US12552836B2, US20210261622A1, WO2021146441A1 |
| ⚠ 검증불가 (unverifiable) | JP2023145581A, CA3202226A1, (그리고 US11180535B2는 unverifiable+오귀속) | 추출 실패 또는 무관 |
| ⚠ 부분추출 (partial extraction) | 다수 | WO2023288019A2, US20240173309A1, US12478617B2, WO2024155552A1, US11884748B2, WO2016011208A1 등 — 화학구조 이미지·OCR 한계 |
| 미검증(pending, 검증 미실시) | 다수 | 03_verified에 검증 산출물 없는 진짜 패밀리(예: US9624268B2, US10023614B2, US10941183B2, US11884748B2, WO2016011208A1, US12478617B2, US20240173309A1, WO2023288019A2, WO2024155552A1) |
| ❌ icotrokinra무관(오귀속) | 8건 | 부록 A |

> 정확한 needs_rework 판정 건수: 03_verified 폴더 기준으로 **US10787490B2, US11041000B2, US11845808B2, US12018057B2, US12552836B2, US20210261622A1, WO2021146441A1 = 7건**이 needs_rework이다. 검증을 통과(verified)한 것은 **US11939361B2 단 1건**뿐이다.

### 소스 제약 고지 (중요)

- 본 실행(run) 동안 **WIPO Patentscope · Espacenet · Google Patents가 모두 차단(HTTP 403/503)** 되었다.
- 유일하게 접근 가능했던 1차 소스는 **FreePatentsOnline(FPO)** 단일 소스이며, 따라서 **`cross_source = false`** (교차 출처 검증 불가)이다.
- 모든 검증 산출물(03_verified)의 verdict는 "FPO HTML 단일 소스 대비 추출본 일치 여부"를 의미하며, 다수의 MISMATCH는 **FPO의 OCR/공백/화학구조 이미지 렌더링 노이즈**에서 기인한다(아래 각 특허 [ANALYSIS] 참조).
- **모든 특허의 만료일(estimated_expiry)은 확인불가**이다. 20년 존속기간·USPTO 존속기간조정(PTA)·존속기간연장(PTE)을 1차 소스로 확인할 수 없었다.

---

## 2. 핵심 요약 (Executive Summary)

icotrokinra(개발코드 JNJ-2113 / PN-235, 상표명 ICOTYDE)는 Protagonist Therapeutics가 발굴하고 Janssen(J&J)이 공동 개발 중인 **경구용 IL-23 수용체 길항 단환 펩타이드**이다. 본 분석에서 icotrokinra 물질 자체는 조성물 특허 **US11939361B2**에서 **SEQ ID NO: 1** 펩타이드로 명시적으로 정의된다.

이 패밀리에서 **가장 중요하고 유일하게 검증을 통과(✅검증완료)한 특허가 US11939361B2**이다. 16개 청구항 전부가 FPO 소스 대비 PASS(16/16, MISMATCH 0)로 일치했고, icotrokinra(SEQ ID NO:1) 펩타이드 및 그 약학적으로 허용되는 염/용매화물(특히 아세테이트 비결정형)을 **0.1~15%(w/w)** 농도로 함유하는 경구 제약 조성물과 그 치료 용도를 직접 보호한다. 이것이 icotrokinra 완제 의약품 자체에 가장 근접한 조성물 권리다.

패밀리는 다음 4개 티어로 구성된다.

1. **CORE genus(거대고리 단환 펩타이드 속(屬) 청구)** — WO2021146441A1, US20210261622A1, US11845808B2, US12018057B2, US12552836B2, US11041000B2, US10787490B2. Pen-Pen 이황화 결합으로 환화된 단환 펩타이드(Formula I/Z′/II 등) 속(genus)과 다수의 구체 서열(SEQ ID NO)을 청구. icotrokinra 분자 골격(Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-...-Sarc 등)이 이 속에 포함된다.
2. **CORE composition(조성물/염·용매화물)** — **US11939361B2**(✅), CA3202226A1, JP2023145581A. SEQ ID NO:1 조성물 패밀리.
3. **Lipidated(지질화 화학형, 주변부)** — US12478617B2, US20240173309A1, WO2023288019A2, WO2024155552A1. icotrokinra 거대고리와 같은 프로그램이나 별도 지질화 화학형/제형.
4. **PTG-200 earlier(초기 세대, icotrokinra 이전)** — WO2016011208A1, US9624268B2, US10023614B2, US10941183B2, US11884748B2. 2014~2015년 우선일의 광의(廣義) 경구 IL-23R 펩타이드 골격(PTG-200 계열).

핵심 보호 구조: **물질·조성물(US11939361B2 + 속 청구 US11845808B2/US12552836B2 등) + 초기 광의 골격(PTG-200)** 의 다층 구조로 icotrokinra를 보호한다. 경쟁사로는 동일 표적(IL-23R 펩타이드)을 다른 분자로 추구하는 **Zealand Pharma(WO2023099669A1)**가 식별되었다(부록 A).

---

## 3. 진짜 icotrokinra / Protagonist+Janssen 패밀리

### 3-A. CORE composition 티어 — icotrokinra 물질·조성물

#### 3-A-1. ✅검증완료 US11939361B2 — "Compositions of peptide inhibitors of Interleukin-23 receptor" (최우선 특허)

**(a) 서지 메타데이터** (`01_metadata/US11939361B2.json` 인용)

| 항목 | 값 |
|---|---|
| publication_number | US11939361B2 |
| application_number | 17/531,538 |
| kind_code | B2 |
| title | Compositions of peptide inhibitors of Interleukin-23 receptor |
| applicants / assignees | Janssen Pharmaceutica NV; Protagonist Therapeutics, Inc. |
| priority_date | 2020-11-20 (US provisional 63/116,568; 추가 63/275,222 = 2021-11-03) |
| filing_date | 2021-11-19 |
| publication / grant_date | 2024-03-26 (Granted) |
| legal_status | Granted (issued 2024-03-26) |
| patent_family | CA3202226A1, JP2023145581A |
| **estimated_expiry** | **확인불가** (20년 존속기간 + PTA/PTE 1차 소스 미확인) |

**(b) [VERBATIM] 청구항 원문 — 전체 16개 전부** (출처: `work/02_extracted/US11939361B2.md`)

```
1. A pharmaceutical composition comprising: a peptide of SEQ ID NO: 1 or a pharmaceutically acceptable salt or solvate form thereof in an amount of from about 0.1% to about 15% (w/w) of the pharmaceutical composition; and one or more pharmaceutically acceptable excipients.

2. The pharmaceutical composition of claim 1, wherein the peptide of SEQ ID NO: 1 or a pharmaceutically acceptable salt or solvate form thereof, has the chemical structure: [IMAGE] and wherein the peptide of SEQ ID NO: 1 or a pharmaceutically acceptable salt or solvate form thereof is a pharmaceutically acceptable salt form.

3. The pharmaceutical composition of claim 1, wherein the peptide of SEQ ID NO: 1 or a pharmaceutically acceptable salt or solvate form thereof is an acetate form.

4. The pharmaceutical composition of claim 3, wherein the acetate form is in an amorphous form.

5. The pharmaceutical composition of claim 1, wherein the amount of the peptide of SEQ ID NO: 1 or a pharmaceutically acceptable salt or solvate form thereof is from about 1 mg to about 1000 mg.

6. The pharmaceutical composition of claim 1, wherein the amount of the peptide of SEQ ID NO: 1 or a pharmaceutically acceptable salt or solvate form thereof is from about 10 mg to about 300 mg.

7. The pharmaceutical composition of claim 1, wherein the amount of the peptide of SEQ ID NO: 1 or a pharmaceutically acceptable salt or solvate form thereof is from about 25 mg to about 150 mg.

8. The pharmaceutical composition of claim 1, wherein the pharmaceutical composition further comprises an absorption enhancer.

9. The pharmaceutical composition of claim 8 comprising: a peptide of SEQ ID NO: 1 or a pharmaceutically acceptable salt or solvate form thereof in an amount of from about 0.1% to about 15% (w/w) of the pharmaceutical composition; an absorption enhancer in an amount from about 10% to about 60% (w/w); and one or more pharmaceutically acceptable excipients.

10. A method of treating an inflammatory disease in a subject comprising administering to the subject a therapeutically effective amount of a pharmaceutical composition of claim 1.

11. A pharmaceutical composition comprising: a peptide of SEQ ID NO: 1 or a pharmaceutically acceptable salt or solvate form thereof in an amount of from about 0.1% to about 20% (w/w) of the pharmaceutical composition; and one or more pharmaceutically acceptable excipients.

12. The pharmaceutical composition of claim 11, wherein the peptide of SEQ ID NO: 1 or a pharmaceutically acceptable salt or solvate form thereof, has the chemical structure: [IMAGE] and wherein the peptide of SEQ ID NO: 1 or a pharmaceutically acceptable salt or solvate form thereof is a pharmaceutically acceptable salt form.

13. The pharmaceutical composition of claim 12, wherein the amount of the peptide of SEQ ID NO: 1 or a pharmaceutically acceptable salt or solvate form thereof is from about 1 mg to about 1000 mg.

14. The pharmaceutical composition of claim 13, wherein the amount of the peptide of SEQ ID NO: 1 or a pharmaceutically acceptable salt or solvate form thereof is from about 10 mg to about 500 mg.

15. The pharmaceutical composition of claim 14, wherein the amount of the peptide of SEQ ID NO: 1 or a pharmaceutically acceptable salt or solvate form thereof is from about 10 mg to about 300 mg.

16. A method of treating an inflammatory disease in a subject comprising administering to the subject a therapeutically effective amount of a pharmaceutical composition of claim 11.
```

**(c) [ANALYSIS]** (한국어)

- **독립항/종속 트리:** 독립항은 **3개** — 청구항 1(조성물, 0.1~15% w/w), 청구항 11(조성물, 0.1~20% w/w), 그리고 방법항 10·16(각각 청구항 1·11 인용). 청구항 1 계열: 2,3,4(아세테이트→비결정형 단계 한정),5,6,7(용량),8→9(흡수촉진제),10. 청구항 11 계열: 12,13,14,15,16.
- **청구항 카테고리:** composition(조성물) + method of treating(치료방법) 혼합. 청구항 1·11·…은 product(제약 조성물), 청구항 10·16은 use/method.
- **핵심 한정요소:** (i) 활성성분이 **SEQ ID NO:1**(=icotrokinra) 또는 그 약학적 허용 염/용매화물, (ii) **함량 0.1~15%(w/w)** 또는 0.1~20%(w/w), (iii) 청구항 3·4의 **아세테이트 염·비결정형(amorphous)**, (iv) 청구항 8·9의 **흡수촉진제(absorption enhancer) 10~60%(w/w)** — 경구 펩타이드 흡수 향상 기술. 청구항 2·12의 화학구조는 FPO에서 `[IMAGE]`로 렌더(원문 보존).
- **권리범위 요지:** icotrokinra **완제 의약품(조성물)** 자체에 가장 근접한 보호. 용량 단위(예: 25~150 mg, 10~300 mg)와 흡수촉진제 처방은 ICOTYDE 정제 처방을 직접 겨냥.
- **검증 결과 요약:** **verdict = verified, PASS 16/16, MISMATCH 0, 누락 없음.** 본 패밀리에서 유일하게 FPO 단일 소스와 완전 일치한 특허다. 다만 `cross_source=false`이므로 교차 출처 확정은 아니다.

---

#### 3-A-2. ⚠검증불가 CA3202226A1 — "Compositions of peptide inhibitors of interleukin-23 receptor"

**(a) 서지 메타데이터** (`01_metadata/CA3202226A1.json`)

| 항목 | 값 |
|---|---|
| publication_number | CA3202226A1 (kind A1) |
| application_number | CA3202226 |
| applicants / assignees | Janssen Pharmaceutica NV; Protagonist Therapeutics, Inc. |
| filing_date | 2021-11-19 |
| publication_date | 2022-05-27 |
| priority_date / legal_status / **estimated_expiry** | 모두 **확인불가** |
| patent_family | US11939361B2(동일 명칭, app 17/531,538), JP2023145581A |

**(b) [VERBATIM] 청구항 원문** (출처: `work/02_extracted/CA3202226A1.md`)

```
EXTRACTION FAILED — claims not retrievable as of 2026-06-15.

Title: Compositions of peptide inhibitors of interleukin-23 receptor (published 2022).

Sources attempted and result:
- FreePatentsOnline: NO page for this Canadian application (HTTP 404 for CA3202226A1.html and CA3202226.html).
- Google Patents (patents.google.com/patent/CA3202226A1/en and /ko): HTTP 503.
- WIPO Patentscope / Espacenet: HTTP 403.

No claims fabricated. See review-queue flag.
```

**(c) [ANALYSIS]** US11939361B2 조성물 패밀리의 캐나다 국내단계 멤버. 청구항 본문은 어떤 도달 가능한 소스에서도 확보 실패(FPO 404, 기타 차단). verdict=unverifiable. **가족 멤버로부터 청구항을 추정·전사하지 않았다(원칙 준수).** CIPO 캐나다 특허DB 또는 Espacenet PDF에서 재수집 필요.

---

#### 3-A-3. ⚠검증불가 JP2023145581A — "COMPOSITIONS OF PEPTIDE INHIBITORS OF INTERLEUKIN-23 RECEPTOR"

**(a) 서지 메타데이터** (`01_metadata/JP2023145581A.json`)

| 항목 | 값 |
|---|---|
| publication_number | JP2023145581A (kind A = 미심사 공개) |
| application_number | JP2023119735A (JP2023-119735) |
| applicants / assignees | Janssen Pharmaceutica NV; Protagonist Therapeutics, Inc. |
| filing_date | 2023-07-24 |
| publication_date | 2023-10-11 |
| priority_date / legal_status / **estimated_expiry** | 모두 **확인불가** |
| patent_family | US11939361B2, CA3202226A1, JP7397239B2(관련 등록건 가능성) |

**(b) [VERBATIM] 청구항 원문** (출처: `work/02_extracted/JP2023145581A.md`)

```
EXTRACTION FAILED — claims not retrievable as of 2026-06-15.

Claims (特許請求の範囲 / 請求項) are in Japanese and must be transcribed verbatim WITHOUT translation once a source is obtained.

Sources attempted and result:
- FreePatentsOnline (JP2023145581A.html and JP2023145581.html): metadata/abstract only, NO claims section.
- Google Patents (patents.google.com/patent/JP2023145581A/ja): HTTP 503.
- WIPO Patentscope: HTTP 403.
- J-PlatPat (j-platpat.inpit.go.jp): requires interactive session (not fetchable).

No claims fabricated. See review-queue flag.
```

**(c) [ANALYSIS]** 조성물 패밀리의 일본 국내단계 공개건(kind A). 청구항(請求項)은 일본어이며 확보 시 **번역 없이 일본어 원문 그대로** 전사해야 한다. FPO는 서지/요약만 제공, 청구항 미게재. verdict=unverifiable. J-PlatPat/JPO에서 재수집 필요.

---

### 3-B. CORE genus 티어 — 단환 펩타이드 속(屬) 청구

#### 3-B-1. ⚠미검증-재작업필요 WO2021146441A1 — "PEPTIDE INHIBITORS OF INTERLEUKIN-23 RECEPTOR AND THEIR USE TO TREAT INFLAMMATORY DISEASES" (프로그램 PCT)

**(a) 서지 메타데이터** (`01_metadata/WO2021146441A1.json`)

| 항목 | 값 |
|---|---|
| publication_number | WO2021146441A1 (WO/2021/146441) |
| application_number | PCT/US2021/013463 |
| applicants / assignees | Janssen Biotech, Inc.; Protagonist Therapeutics, Inc. |
| filing_date | 2021-01-14 |
| publication_date | 2021-07-22 |
| priority_date / legal_status / **estimated_expiry** | 모두 **확인불가** (US sibling US20210261622A1는 US provisional 62/961,624 = 2020-01-15 인용, 단 WO 페이지 자체 미확인) |
| patent_family | US20210261622A1 (동일 출원 국내단계) |
| 청구항 수 | 167 (단 FPO는 186까지 렌더 — 아래 검증 충돌 참조) |

**(b) [VERBATIM] 독립항 원문**

청구항 1은 매우 긴 Markush 속(屬) 청구항이다. 아래는 출처 `work/02_extracted/WO2021146441A1.md`의 **청구항 1 전문 verbatim**이다 (OCR 아티팩트 `Gin`/`lie` 등 원문 보존).

```
1. A monocyclic peptide inhibitor of an interleukin-23 receptor, or a pharmaceutically acceptable salt thereof, wherein the peptide inhibitor comprises an amino acid sequence of Formula (I): X3-X4-X5-X6-X7-X8-X9-X10-X11-X12-X13-X14-X15-X16 (I) wherein X3 is absent or any amino acid; X4 is Abu, Cys, (D)Cys, alpha-MeCys, (D)Pen, Pen, or Pen(sulfoxide); X5 is Cit, Glu, Gly, substituted Gly, Leu, lie, beta-Ala, Ala, Lys, Asn, Pro, Ser, alpha-MeGln, alpha-MeLys, alpha-MeLeu, alpha-MeAsn, Lys(Ac), alpha-MeLys(Ac), Dab(Ac), Dap(Ac), homo-Lys(Ac), Gin, or Asp; X6 is Thr, Aib, Asp, Dab, Gly, Pro, Ser, alpha-MeGln, alpha-MeLys, alpha-MeLeu, alpha-MeAsn, alpha-MeThr, alpha-MeSer, or Val; X7 is unsubstituted Trp, or Trp substituted with cyano, halo, alkyl, haloalkyl, hydroxy, alkoxy, substituted or unsubstituted aryl, or substituted or unsubstituted heteroaryl; X8 is Gin, alpha-MeLys, alpha-MeLeu, alpha-MeLys(Ac), beta-homoGln, Cit, Glu, Phe, substituted Phe, Tyr, Asn, Thr, Val, Aib, alpha-MeGln, alpha-MeAsn, Lys(Ac), Dab(Ac), Dap(Ac), homo-Lys(Ac), 1-Nal, 2-Nal, Lys(b-Ala), Lys(Gly), Lys(Benzyl, Ac), Lys(butyl, Ac), Lys(isobutyl,Ac), Lys(propyl,Ac), or Trp; X9 is Abu, Cys, (D)Cys, alpha-MeCys, (D)Pen, Pen, or Pen(sulfoxide); X10 is Tyr, or substituted Tyr, unsubstituted Phe, or Phe substituted with halo, alkyl, haloalkyl, hydroxy, alkoxy, cyano, cycloalkyl, carboxy, carboxamido, 2-aminoethoxy, or 2-acetylaminoethoxy; and X11 is 2-Nal, Phe(2-Me), Phe(3-Me), Phe(4-Me), Phe(3,4-dimethoxy), 2Quin, 3Quin, 1-Nal, unsubstituted Trp, or Trp substituted with cyano, halo, alkyl, haloalkyl, hydroxy, or alkoxy; X12 is 4-amino-4-carboxy-tetrahydropyran (THP), Acvc, alpha-MeLys, alpha-MeLeu, alpha-MeArg, alpha-MePhe, alpha-MeLeu, alpha-MeLys, alpha-MeAsn, alpha-MeTyr, Ala, cyclohexylAla, Lys, or Aib; X13 is any amino acid; X14 is any amino acid; and i) X15 is any amino acid other than His, (D)His, substituted or unsubstituted His, 2Pal, 3Pal, or 4Pal; X16 is Sarc, aMeLeu, (D)NMeTyr, His, (D)Thr, bAla, Pro, or (D)Pro; and the peptide inhibitor is other than Ac-[Abu]-QTWQC-[Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-[Lys(Ac)]-NNPG-NH2; Ac-[Pen]-N-T-W-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[aMeLeu]-[Lys(Ac)]-NN-[Sarc]-NH2; Ac-[(D)Arg]-[Abu]-Q-T-[W(7-Me)]-[Lys(Ac)]-[Cys]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N-[(D)Lys]-[Sarc]-NH2; or Ac-[Pen]-N-T-[W(7-Me)]-[Cit]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N-[Aib]-[bA]-NH2; or ii) X15 is His, (D)His, substituted or unsubstituted His, 2Pal, 3Pal, 4Pal, 4TriazolAla, or 5Pyal; and X16 is absent, (D)aMeTyr, (D)NMeTyr or any amino acid other than THP, substituted or unsubstituted Phe, substituted or unsubstituted (D)Phe, substituted or unsubstituted His, substituted or unsubstituted (D)His, substituted or unsubstituted Trp, substituted or unsubstituted 2-Nal, or N-substituted Asp; and the compound is other than Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[a-MeLys]-[Lys(Ac)]-N-H-NH2; wherein 2Pal is 2-pyridyl substituted alanine, and 3Pal is 3-pyridyl substituted alanine, and 4Pal is 4-pyridyl substituted alanine 5Pyal is 5-pyrimidine substituted alanine: and wherein X4 and X9 form a disulfide bond or a thioether bond; and wherein the peptide inhibitor inhibits the binding of an interleukin-23 (IL-23) to an IL-23 receptor.
```

> 종속항 2~167(서열·Markush 종속항 다수, 1000자 초과)은 verbatim 그대로 보존되어 있다 — **(전문: `work/02_extracted/WO2021146441A1.md`)**. 단, 추출본은 청구항 1~161만 신뢰 가능하게 포착했으며, 162~167은 FPO가 순서 뒤섞임·부분 렌더했고 168~186은 누락(아래 검증·부록 B 참조).

**(c) [ANALYSIS]**

- **카테고리/구조:** 청구항 1 = 단환(monocyclic) 펩타이드 IL-23R 저해제 속(genus). Formula (I) 13-잔기 골격, X4/X9가 disulfide 또는 thioether로 환화. 다수의 "other than ~" 단서(disclaimer)로 선행 화학형을 제외. 종속항은 Formula (Ia/Ib …) 한정, 잔기 한정, 구체 서열, 조성물·방법으로 이어진다.
- **핵심 한정요소:** Pen-Pen 또는 Abu-Cys 환화, X7=치환 Trp(W(7-Me) 등), X10=Phe[4-(2-aminoethoxy)], X11=2-Nal, X12=THP — icotrokinra 골격 모티프와 일치하는 속.
- **권리범위 요지:** icotrokinra 및 다수 유사체를 포괄하는 **프로그램 PCT 광역 속 청구**. icotrokinra(SEQ ID NO:1)는 본 속에 포섭된다.
- **검증 결과 요약:** verdict=**needs_rework**. PASS 50 / MISMATCH 117 / 누락 19(청구항 168~186). MISMATCH의 절대다수는 (i) **FPO 공백/줄바꿈 노이즈**, (ii) 청구항 71~167 구간의 "substantive text difference"인데, 검증자는 이를 **FPO가 162~167을 다른 렌더링(Table E1A/E1B 기반)에서 가져온 소스-버전 충돌**로 판단(추출본의 서열-리스트 버전과 불일치). 즉 다수 MISMATCH는 진짜 청구항 오류라기보다 **FPO 단일소스 노이즈 + 버전 불일치**가 원인. 168~186 누락 및 162~167 재수집이 권고됨.

---

#### 3-B-2. ⚠미검증-재작업필요 US20210261622A1 — "Peptide Inhibitors of Interleukin-23 Receptor and Their Use to Treat Inflammatory Diseases" (WO2021146441A1의 미국 공개건)

**(a) 서지 메타데이터** (`01_metadata/US20210261622A1.json`)

| 항목 | 값 |
|---|---|
| publication_number | US20210261622A1 (US 2021/0261622 A1) |
| application_number | 17/149,509 |
| kind_code | A1 (공개출원) |
| applicants / assignees | Janssen Biotech, Inc.; Protagonist Therapeutics, Inc. |
| priority_date | 2020-01-15 (US provisional 62/961,624) |
| filing_date | 2021-01-14 |
| publication_date | 2021-08-26 |
| grant_date / **estimated_expiry** | 없음 / **확인불가** |
| patent_family | WO2021146441A1 (PCT/US2021/013463); 동일 출원 17/149,509은 후에 US11845808B2로 등록 |

**(b) [VERBATIM] 독립항 원문** (출처: `work/02_extracted/US20210261622A1.md`)

청구항 1은 WO 대응건과 동일 계열의 장문 Markush 속 청구항이다. 본문 첫 부분 verbatim(소스에서 청구항 1은 한 줄로 렌더):

```
1. A monocyclic peptide inhibitor of an interleukin-23 receptor; or a pharmaceutically acceptable salt thereof; wherein the monocyclic peptide inhibitor of the interleukin-23 receptor comprises an amino acid sequence of Formula (I):X3-X4-X5-X6-X7-X8-X9-X10-X11-X12-X13-X14-X15-X16  (I) wherein; X3 is absent or any amino acid; X4 is Abu, Cys, (D)Cys, alpha-MeCys, (D)Pen, Pen, or Pen(sulfoxide); X5 is Cit, Glu, Gly, substituted Gly, Leu, lie, beta-Ala, Ala, Lys, Asn, Pro, Ser, alpha-MeGln, alpha-MeLys, alpha-MeLeu, alpha-MeAsn, Lys(Ac), alpha-MeLys(Ac), Dab(Ac), Dap(Ac), homo-Lys(Ac), Gin, or Asp; ... [이하 Formula (I) 전체 잔기 정의 — 전문: work/02_extracted/US20210261622A1.md]
```

> 청구항 1의 잔기 정의 전체 및 종속항(105~182, 다수 "(canceled)" 포함)은 1000자 초과 Markush/서열 청구항으로, verbatim 그대로 보존되어 있다 — **(전문: `work/02_extracted/US20210261622A1.md`)**. 추가 독립항 verbatim:

```
162. A monocyclic peptide inhibitor of an interleukin-23 receptor of an interleukin-23 receptor, wherein the monocyclic peptide inhibitor is one of the specific sequences listed (SEQ ID NOs: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 261, 262, 266, 267, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 299, 308, 309, 310, 311, 332, 333, 334, 335, 339, 347, 373), or a pharmaceutically acceptable salt thereof.

174. A polynucleotide comprising a sequence encoding the monocyclic peptide inhibitor of an interleukin-23 receptor of claim 1 or a pharmaceutically acceptable salt thereof.

175. A vector comprising the polynucleotide of claim 174.

176. A pharmaceutical composition comprising the monocyclic peptide inhibitor of an interleukin-23 receptor or pharmaceutically acceptable salt thereof of claim 1, and a pharmaceutically acceptable carrier, excipient, or diluent.

179. A method for treating an Inflammatory Bowel Disease (IBD), ulcerative colitis, Crohn's disease, Celiac disease (nontropical Sprue), enteropathy associated with seronegative arthropathies, microscopic colitis, collagenous colitis, eosinophilic gastroenteritis, colitis associated with radio- or chemo-therapy, colitis associated with disorders of innate immunity as in leukocyte adhesion deficiency-1, chronic granulomatous disease, glycogen storage disease type 1b, Hermansky-Pudlak Syndrome, Chediak-Higashi Syndrome, and Wiskott-Aldrich Syndrome, pouchitis resulting after proctocolectomy and ileoanal anastomosis, gastrointestinal cancer, pancreatitis, insulin-dependent diabetes mellitus, mastitis, cholecystitis, cholangitis, pericholangitis, chronic bronchitis, chronic sinusitis, asthma, psoriasis, psoriatic arthritis, or graft versus host disease in a subject, comprising administering an effective amount of the monocyclic peptide inhibitor according to claim 1 or pharmaceutically acceptable salt thereof to a subject or patient in need thereof.

181. A method for treating Inflammatory Bowel Disease (IBD), ulcerative colitis, Crohn's Disease (CD), psoriasis or psoriatic arthritis, which comprises administering an effective amount of: the monocyclic peptide inhibitor of an interleukin-23 receptor of claim 1 or pharmaceutically acceptable salt thereof; to a subject or patient in need thereof.
```

**(c) [ANALYSIS]**

- **독립항:** 1(단환 펩타이드 속), 162(구체 SEQ ID NO 군 — **SEQ ID NO:1 = icotrokinra 포함**), 174(폴리뉴클레오타이드), 175(벡터), 176(조성물), 179·181(치료방법). 종속항 다수가 청구항 105/15/160 등을 인용하며, 115·134·143 등은 "(canceled)".
- **카테고리:** product(펩타이드/폴리뉴클레오타이드/벡터/조성물) + method of treating.
- **권리범위 요지:** WO2021146441A1의 미국 공개건. **청구항 162가 SEQ ID NO:1(icotrokinra)을 명시 열거**하여 icotrokinra 분자를 직접 포섭. 동일 출원(17/149,509)이 후에 US11845808B2로 등록됨.
- **검증 결과 요약:** verdict=**needs_rework**. PASS 14 / MISMATCH 36 / FABRICATED 0 / **MISSING 12**(2,106,112,117,121,124,128,131,136,147,177,183). MISMATCH 원인은 주로 (i) 추출본이 "(canceled)" 줄을 청구항 본문에 흡수(세그먼테이션 오류), (ii) FPO 공백 노이즈, (iii) 화학구조 이미지→[NOTE] 치환, (iv) 일부 substantive 차이. 대부분 **FPO 단일소스 포맷 노이즈**로 판단되며 재추출 권고.

---

#### 3-B-3. ⚠미검증-재작업필요 US11845808B2 — "Peptide inhibitors of interleukin-23 receptor..." (17/149,509 등록건)

**(a) 서지 메타데이터** (`01_metadata/US11845808B2.json`)

| 항목 | 값 |
|---|---|
| publication_number | US11845808B2 |
| application_number | 17/149,509 |
| applicants / assignees | Janssen Biotech, Inc.; Protagonist Therapeutics, Inc. |
| priority_date | 2020-01-15 (US provisional 62/961,624) |
| filing_date | 2021-01-14 |
| grant_date | 2023-12-19 (Granted) |
| **estimated_expiry** | **확인불가** |
| patent_family | US20210261622A1(동일 출원 공개건), WO2021146441A1 |

**(b) [VERBATIM] 독립항 원문** (출처: `work/02_extracted/US11845808B2.md`)

```
1. A monocyclic peptide, comprising the amino acid sequence of Formula (I): X3-Pen-N-T-X7-Lys(Ac)-Pen-X10-2Nal-X12-E-N—X15-Sarc (I) wherein: X3 is absent or any amino acid; X7 is Trp, 7-methyl tryptophan (W(7-Me)), or 7 phenyl tryptophan (W(7-Ph)); X10 is Phe(4-(2-aminoethoxy)); X12 is 4-amino-4-carboxy-tetrahydropyran (THP); and X15 is 3-pyridyl substituted alanine (3Pal); or a pharmaceutically acceptable salt thereof; wherein the monocyclic peptide is cyclized via a Pen-Pen disulfide bond.

5. A monocyclic peptide comprising the amino acid sequence selected from the group consisting of: Ac-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-[Phe(4-(2-aminoethoxy))]-[2-Nal]-[THP]-E-N-[3Pal]-[Sarc]-NH2 (SEQ ID NO:104); Ac-[Pen]-N-T-W-[Lys(Ac)]-[Pen]-[Phe(4-(2-aminoethoxy))]-[2-Nal]-[THP]-E-N-[3Pal]-[Sarc]-NH2 (SEQ ID NO:158); and Ac-[(D)Arg]-[Pen]-N-T-[W(7-Me)]-[Lys(Ac)]-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[3Pal]-[Sarc]-NH2 (SEQ ID NO:247); or a pharmaceutically acceptable salt thereof; wherein the monocyclic peptide is cyclized via a Pen-Pen disulfide bond.

12. A method for treating a disease or disorder associated with Interleukin 23 (IL-23) or Interleukin 23 Receptor (IL-23R) in a patient in need thereof, comprising administering to the patient an effective amount of the monocyclic peptide or pharmaceutically acceptable salt thereof of claim 5, wherein the disease or disorder is inflammatory bowel disease (IBD), ulcerative colitis (UC), Crohn's disease (CD), psoriasis (PsO), or psoriatic arthritis (PsA).

19. A method for treating a disease or disorder associated with Interleukin 23 (IL-23) or Interleukin 23 Receptor (IL-23R) in a patient in need thereof, comprising administering to the patient an effective amount of the monocyclic peptide or pharmaceutically acceptable salt thereof of claim 6, wherein the disease or disorder is inflammatory bowel disease (IBD), ulcerative colitis (UC), Crohn's disease (CD), psoriasis (PsO), or psoriatic arthritis (PsA).

27. A method for treating a disease or disorder associated with Interleukin 23 (IL-23) or Interleukin 23 Receptor (IL-23R) in a patient in need thereof, comprising administering to the patient an effective amount of the monocyclic peptide or pharmaceutically acceptable salt thereof of claim 7, wherein the disease or disorder is inflammatory bowel disease (IBD), ulcerative colitis (UC), Crohn's disease (CD), psoriasis (PsO), or psoriatic arthritis (PsA).

28. A method for treating a disease or disorder associated with Interleukin 23 (IL-23) or Interleukin 23 Receptor (IL-23R) in a patient in need thereof, comprising administering to the patient an effective amount of the monocyclic peptide or pharmaceutically acceptable salt thereof of claim 8, wherein the disease or disorder is inflammatory bowel disease (IBD), ulcerative colitis (UC), Crohn's disease (CD), psoriasis (PsO), or psoriatic arthritis (PsA).
```

> 종속항 2,3,4,6,7,8,9,10,11,13~18,20~26,29,30(일부는 화학구조 이미지 [NOTE] 포함)은 verbatim 보존 — **(전문: `work/02_extracted/US11845808B2.md`)**.

**(c) [ANALYSIS]**

- **독립항:** 1(Formula I 단환 펩타이드, 좁은 골격), 5(SEQ ID NO:104/158/247 군 — Pen-Pen 이황화 환화), 12·19·27·28(치료방법, 각 청구항 5/6/7/8 인용). 청구항 6·7·9·10은 화학구조 도면 청구항(FPO에서 [NOTE]로 표시, 원문 보존).
- **카테고리:** composition(펩타이드 물질) + method of treating.
- **핵심 한정요소:** Formula I = **X3-Pen-N-T-X7-Lys(Ac)-Pen-X10-2Nal-X12-E-N-X15-Sarc**, X7=W/W(7-Me)/W(7-Ph), X10=Phe(4-(2-aminoethoxy)), X12=THP, X15=3Pal. icotrokinra 골격에 매우 근접한 **좁은 속(narrow genus)** 물질 청구.
- **권리범위 요지:** WO2021146441A1 계열의 등록 물질항. icotrokinra 분자 골격(W(7-Me), Lys(Ac), Phe(4-(2-aminoethoxy)), 2Nal, THP, 3Pal, Sarc)을 직접 포섭하는 핵심 물질 보호.
- **검증 결과 요약:** verdict=**needs_rework**, PASS 22 / MISMATCH 8. MISMATCH는 전부 (i) 공백 노이즈 또는 (ii) 화학구조 이미지→[NOTE] 치환에서 기인 — 즉 **FPO 소스노이즈**. 실질 텍스트 청구항(1,3,4,12~18,20~30)은 PASS.

---

#### 3-B-4. ⚠미검증-재작업필요 US12018057B2 — "Peptide inhibitors of interleukin-23 receptor..."

**(a) 서지 메타데이터** (`01_metadata/US12018057B2.json`)

| 항목 | 값 |
|---|---|
| publication_number | US12018057B2 |
| application_number | 17/149,544 |
| applicants / assignees | Janssen Biotech, Inc.; Protagonist Therapeutics, Inc. |
| priority_date | 2020-01-15 (US provisional 62/961,618) |
| filing_date | 2021-01-14 |
| grant_date | 2024-06-25 (Granted) |
| **estimated_expiry** | **확인불가** |
| patent_family | US20210261622A1/US11845808B2 형제 출원, WO2021146441A1 |

**(b) [VERBATIM] 독립항 원문** (출처: `work/02_extracted/US12018057B2.md`)

청구항 1은 다수 SEQ ID NO(3~137)를 선택군으로 열거하는 장문 청구항이다. 첫 부분 + 다른 독립항 verbatim:

```
1. A peptide that is:

(SEQ ID NO: 3)
[Propionic_acid]-[(D)Arg]-[Pen]-Q-T-W-Q-[Pen]-Phe[4-(2-aminoethoxy)]-[2-Nal]-[THP]-E-N-[alpha-MePhe]-NH2;
... [SEQ ID NO 4~137 다수 서열 — 전문: work/02_extracted/US12018057B2.md] ...
wherein the peptide is cyclized via a Pen-Pen disulfide bond; or a pharmaceutically acceptable salt thereof.

3. A pharmaceutical composition comprising the peptide or a pharmaceutically acceptable salt thereof of claim 1 and a pharmaceutically acceptable carrier, excipient, or diluent.

5. A method for treating an Inflammatory Bowel Disease (IBD), ulcerative colitis, Crohn's disease, Celiac disease (nontropical Sprue), enteropathy associated with seronegative arthropathies, microscopic colitis, collagenous colitis, eosinophilic gastroenteritis, colitis associated with radio- or chemo-therapy, colitis associated with disorders of innate immunity as in leukocyte adhesion deficiency-1, chronic granulomatous disease, glycogen storage disease type 1b, Hermansky-Pudlak syndrome, Chediak-Higashi syndrome, and Wiskott-Aldrich Syndrome, pouchitis resulting after proctocolectomy and ileoanal anastomosis, gastrointestinal cancer, pancreatitis, insulin-dependent diabetes mellitus, mastitis, cholecystitis, cholangitis, pericholangitis, chronic bronchitis, chronic sinusitis, asthma, psoriasis, psoriatic arthritis, or graft versus host disease in a subject in need thereof, comprising administering an effective amount of the peptide or a pharmaceutically acceptable salt thereof of claim 1 to the subject.
```

> 청구항 1의 전체 서열군(SEQ ID NO 3~137) 및 종속항 2,4,6~10은 verbatim 보존 — **(전문: `work/02_extracted/US12018057B2.md`)**.

**(c) [ANALYSIS]**

- **독립항:** 1(구체 서열군 펩타이드, Pen-Pen 환화), 3(조성물), 5(치료방법). 종속항 2(SEQ ID NO:105), 4, 6~10(질환 한정).
- **카테고리:** composition + method.
- **권리범위 요지:** 형제 출원(US11845808B2)과 같은 2020-01-15 우선일 계열로, 다른 SEQ ID NO 군(Q-T-W-Q 코어, propionic acid/Ac 변형 등)을 좁게 청구. 좁은 물질 청구로 icotrokinra 인접 유사체 보호.
- **검증 결과 요약:** verdict=**needs_rework**, PASS 7 / MISMATCH 3(전부 공백 노이즈). 실질 충돌 없음 — **FPO 소스노이즈**.

---

#### 3-B-5. ⚠미검증-재작업필요 US12552836B2 — "Peptide inhibitors of interleukin-23 receptor..."

**(a) 서지 메타데이터** (`01_metadata/US12552836B2.json`)

| 항목 | 값 |
|---|---|
| publication_number | US12552836B2 |
| application_number | 17/549,579 |
| applicants / assignees | Protagonist Therapeutics, Inc. (FPO 페이지상 Janssen 미기재) |
| priority_date | 2018-07-12 (US prov. 62/697,218; 추가 62/872,477=2019-07-10) |
| filing_date | 2021-12-13 |
| grant_date | 2026-02-17 (Granted) |
| **estimated_expiry** | **확인불가** |
| patent_family | 모출원 US App 16/510,118 (2019-07-12)의 계속출원 |

**(b) [VERBATIM] 독립항 원문** (출처: `work/02_extracted/US12552836B2.md`)

```
1. A peptide inhibitor or pharmaceutically acceptable salt or solvate thereof, wherein the peptide inhibitor comprises the amino acid sequence of Formula (II): X4-X5-X6-X7-X8-X9-X10-X11  (II) wherein X4 is Pen; X5 is Asn, or Gln; X6 is Thr; X7 is Trp substituted with alkyl; X8 is Gln, alpha-Me-Lys, alpha-MeLys(Ac), or Lys(Ac); X9 is Pen; X10 is Phe substituted with 2-aminoethoxy, or 2-acetylaminoethoxy; and X11 is 2-Nal, or 1-Nal; wherein the peptide inhibitor is cyclized via a bond between X4 and X9, and wherein the peptide inhibitor inhibits the binding of an interleukin-23 (IL-23) to an IL-23 receptor.

20. A pharmaceutical composition comprising the peptide inhibitor or pharmaceutically acceptable salt or solvate thereof of claim 1, and a pharmaceutically acceptble carrier, excipient, or diluent.
```

> 종속항 2~19(잔기 한정·서열군·구조 Formula Z 등) 및 21(장용 코팅)은 verbatim 보존 — **(전문: `work/02_extracted/US12552836B2.md`)**. (청구항 16/17의 `α-MeLeu`, `—NN—` 등 OCR/표기는 원문 보존.)

**(c) [ANALYSIS]**

- **독립항:** 1(Formula II 8-잔기 코어 속), 20(조성물). 종속항: 2~19(잔기 한정·SEQ ID NO 군 11번 등·Formula Z·conjugate 한정), 21(enteric coating, 경구 장용 제형).
- **카테고리:** composition + 제형 한정.
- **핵심 한정요소:** X4/X9=Pen 환화, X7=alkyl 치환 Trp, X10=Phe(2-aminoethoxy/2-acetylaminoethoxy), X11=Nal — 가장 이른 우선일(2018-07-12)의 코어 속.
- **권리범위 요지:** 2018년 우선일을 갖는 비교적 이른 코어 속(屬) 청구로, icotrokinra 골격(W(7-Me), Lys(Ac), Phe(4-(2-aminoethoxy)), 2-Nal)을 포섭. 청구항 9·10의 conjugate(지질·PEG) 한정은 지질화 화학형으로의 가교.
- **검증 결과 요약:** verdict=**needs_rework**, PASS 14 / MISMATCH 7(전부 공백 노이즈) — **FPO 소스노이즈**.

---

#### 3-B-6. ⚠미검증-재작업필요 US11041000B2 — "Peptide inhibitors of interleukin-23 receptor..."

**(a) 서지 메타데이터** (`01_metadata/US11041000B2.json`)

| 항목 | 값 |
|---|---|
| publication_number | US11041000B2 |
| application_number | 17/001,428 |
| applicants / assignees | Protagonist Therapeutics, Inc. |
| priority_date | 2019-07-10 (US provisional 62/872,477; PCT/US2020/041409) |
| filing_date | 2020-08-24 |
| grant_date | 2021-06-22 (Granted) |
| **estimated_expiry** | **확인불가** |
| patent_family | WO2021146441A1(프로그램 PCT), PCT/US2020/041409 |

**(b) [VERBATIM] 독립항 원문** (출처: `work/02_extracted/US11041000B2.md`)

청구항 1은 장문 Markush(Formula Z′) 속 청구항이다. 전문 verbatim:

```
1. A peptide inhibitor according to Formula (Z′): R1-X4-X5-X6-X7-X8-X9-X10-X11-X12-X13-X14-X15-R2 (Z′) or a pharmaceutically acceptable salt thereof, wherein X4 is Pen; X5 is Asn; X6 is Thr; X7 is Trp substituted with alkyl; X8 is Gln, alpha-MeLys, alpha-MeLeu, alpha-MeLys(Ac), beta-homoGln, Cit, Glu, Phe, Asn, Thr, Val, Aib, alpha-MeGln, alpha-MeAsn, Lys(Ac), Dab(Ac), Dap(Ac), homo-Lys(Ac), 1-Nal, 2-Nal, or Trp; X9 is Pen; X10 is unsubstituted Phe, or Phe substituted with halo, alkyl, haloalkyl, hydroxy, alkoxy, carboxy, carboxamido, 2-aminoethoxy, or 2-acetylaminoethoxy; X11 is 2-Nal, Phe(2-Me), Phe(3-Me), Phe(4-Me), Phe(3,4-dimethoxy), 1-Nal, unsubstituted Trp, or Trp substituted with cyano, halo, alkyl, haloalkyl, hydroxy, or alkoxy; X12 is 4-amino-4-carboxy-tetrahydropyran (THP), alpha-MeLys, alpha-MeLeu, alpha-MeArg, alpha-MePhe, alpha-MeLeu, alpha-MeLys, alpha-MeAsn, alpha-MeTyr, Ala, cyclohexylAla, Lys, or Aib; X13 is Aib, Glu, Cit, Gln, Lys(Ac), alpha-MeArg, alpha-MeGlu, alpha-MeLeu, alpha-MeLys, alpha-Me-Asn, alpha-MeLys(Ac), Dab(Ac), Dap(Ac), homo-Lys(Ac), Lys, pegylated Lys, b-homoGlu, or Lys(Y2-Ac), wherein Y2 is an amino acid; X14 is Asn, 2-Nap, Aib, Arg, Cit, Asp, Phe, Gly, Lys, Leu, Ala, (D)Ala, beta-Ala, His, Thr, n-Leu, Gln, Ser, (D)Ser, Tic, Trp, alpha-MeGln, alpha-MeAsn, alpha-MeLys(Ac), Dab(Ac), Dap(Ac), homo-Lys(Ac), or Lys(Ac); X15 is Leu, (D)Leu, beta-Ala, Cit, or (D)Lys; R1 is hydrogen, a C1-C6 alkyl, a C6-C12 aryl, a C6-C12aryl-C1-C6alkyl, or a C1-C20 alkanoyl; and R2 is OH or NH2; wherein the peptide inhibitor or pharmaceutically acceptable salt or solvate thereof comprises a disulfide bond between two Pen residues; and wherein the peptide inhibitor or pharmaceutically acceptable salt thereof inhibits the binding of an interleukin-23 (IL-23) to an IL-23 receptor.

24. A pharmaceutical composition comprising the peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1, and a pharmaceutically acceptable carrier, excipient, or diluent.
```

> 종속항 2~23(잔기 한정·SEQ ID NO 군·화학구조 도면 [NOTE] 청구항 16~23), 25~26은 verbatim 보존 — **(전문: `work/02_extracted/US11041000B2.md`)**. 청구항 15/25의 `[W(7-Et]`, `N--T` 등 OCR/표기는 원문 보존.

**(c) [ANALYSIS]**

- **독립항:** 1(Formula Z′ 13-잔기 속), 24(조성물). 종속항 16~23·26은 펩타이드를 비텍스트 화학구조 도면으로 청구(FPO에서 [NOTE] 처리, 원문 보존).
- **카테고리:** composition + 화학구조 도면 청구.
- **권리범위 요지:** 2019-07-10 우선일의 코어 속. icotrokinra 골격(W(7-Me), Lys(Ac), Phe(4-(2-aminoethoxy)), 2-Nal, THP/α-MeLys) 포섭.
- **검증 결과 요약:** verdict=**needs_rework**, PASS 12 / MISMATCH 14. MISMATCH 원인: (i) 청구항 16~23·26 화학구조 이미지→[NOTE] 치환(8건), (ii) 공백 노이즈(나머지). **FPO 소스노이즈·이미지 미포착**이 주원인이며, 텍스트 청구항(2~13,24)은 대부분 PASS. 청구항 27+ 존재 여부 확인 권고(부록 B).

---

#### 3-B-7. ⚠미검증-재작업필요 US10787490B2 — "Peptide inhibitors of interleukin-23 receptor..." (초기 우선일 광역 서열군)

**(a) 서지 메타데이터** (`01_metadata/US10787490B2.json`)

| 항목 | 값 |
|---|---|
| publication_number | US10787490B2 |
| application_number | 15/745,371 |
| applicants / assignees | Protagonist Therapeutics, Inc. |
| priority_date | 2015-07-15 (PCT/US2015/040658; US 14/800,627의 CIP; 추가 62/264,820, 62/281,123) |
| filing_date | 2016-07-15 |
| grant_date | 2020-09-29 (Granted) |
| **estimated_expiry** | **확인불가** |
| patent_family | US 14/800,627, PCT/US2015/040658, PCT/US2016/042680 |

**(b) [VERBATIM] 독립항 원문** (출처: `work/02_extracted/US10787490B2.md`)

청구항 1은 SEQ ID NO 1115~1206을 열거하는 매우 긴 선택군 청구항이다. 첫 부분 + 끝부분 wherein 절 verbatim:

```
1. A peptide inhibitor of an interleukin-23 receptor, or a pharmaceutically acceptable salt thereof, wherein the peptide inhibitor is:

(SEQ ID NO: 1115)
[Palm]-[isoGlu]-[PEG4]-[Pen]-NTWQ-[Pen]-[Phe[4-(2-aminoethoxy)]-[2-Nal]-[Aib]-[Lys(Ac)]-NN-NH2;
... [SEQ ID NO 1116~1206 다수 서열 — 전문: work/02_extracted/US10787490B2.md] ...
wherein the peptide inhibitor is cyclized via a disulfide bond between Pen and Pen; and wherein 2-Nal is L-2-napthylalanine, α-MeLys is alpha-methyl-L-Lysine, α-MeLeu is alpha-methyl-L-Leucine, and Aib is 2-aminoisobutyric acid.

10. A method for treating an Inflammatory Bowel Disease (IBD) in a subject, comprising administering to the subject an effective amount of the peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1.
```

> 종속항 2~9(SEQ ID NO 선택군), 11~18(방법·서열 한정)은 verbatim 보존 — **(전문: `work/02_extracted/US10787490B2.md`)**.

**(c) [ANALYSIS]**

- **독립항:** 1(SEQ ID NO 1115~1206 광역 서열군 펩타이드, Pen-Pen 환화), 10(IBD 치료방법). 종속항 2~9(구체 서열), 11(UC/CD), 12~18(서열 한정 방법).
- **카테고리:** composition(서열군) + method of treating.
- **핵심 한정요소:** 다수가 **지질화/PEG화(Palm, isoGlu, PEG4, Octanyl, Lauryl, Biotin 등)** 변형을 포함 — 초기 골격이면서 지질화 화학형의 선구. NTWQ 코어.
- **권리범위 요지:** 2015-07-15 이른 우선일의 광역 서열군. icotrokinra 자체보다 넓고 이른 스캐폴드 속이며, 지질화 화학형(이후 US12478617B2 계열)으로 연결.
- **검증 결과 요약:** verdict=**needs_rework**, PASS 2 / MISMATCH 16. 대부분 공백 노이즈, 일부 substantive(서열·문장부호 차이)와 OCR 노이즈. **FPO 단일소스의 긴 서열 렌더링 노이즈**가 주원인. 재추출 권고.


---

### 3-C. Lipidated 티어 — 지질화 화학형 / 제형 (주변부, 동일 프로그램)

#### 3-C-1. ⚠부분추출 US12478617B2 — "Lipidated peptide inhibitors of interleukin-23 receptor"

**(a) 서지 메타데이터** (`01_metadata/US12478617B2.json`)

| 항목 | 값 |
|---|---|
| publication_number | US12478617B2 |
| application_number | 18/495,457 |
| applicants / assignees | Janssen Biotech, Inc.; Protagonist Therapeutics, Inc. |
| priority_date | 2021-07-14 (US prov. 63/221,697; PCT/US2022/037205) |
| filing_date | 2023-10-26 |
| grant_date | 2025-11-25 (Granted) |
| **estimated_expiry** | **확인불가** |
| patent_family | US20240173309A1(동일 출원 공개건), WO2023288019A2 |

**(b) [VERBATIM] 독립항 원문** (출처: `work/02_extracted/US12478617B2.md`)

청구항 1 및 대부분의 종속항은 비텍스트 화학구조 도면(Markush)으로 청구되어 FPO가 구조를 텍스트로 포착하지 못했다(아래 도면 한정부는 원문 보존상 누락 — 부록 B).

```
1. An interleukin-23 receptor inhibitor selected from the group consisting of: or a pharmaceutically acceptable salt thereof.

24. A pharmaceutical composition comprising: (i) the interleukin-23 receptor inhibitor of claim 1, or a pharmaceutically acceptable salt thereof, and (ii) a pharmaceutically acceptable carrier, excipient, or diluent.

25. A method for treating a disease or disorder associated with interleukin 23 (IL-23)/interleukin 23 receptor (IL-23R), said method comprising administering an effective amount of the interleukin-23 receptor inhibitor of claim 1, or a pharmaceutically acceptable salt thereof, to a patient in need thereof.

26. A method for treating inflammatory bowel diseases (IBDs), said method comprising administering an effective amount of the interleukin-23 receptor inhibitor of claim 1, or a pharmaceutically acceptable salt thereof, to a patient in need thereof.

27. A method for treating ulcerative colitis (UC), said method comprising administering an effective amount of the interleukin-23 receptor inhibitor of claim 1, or a pharmaceutically acceptable salt thereof, to a patient in need thereof.

28. A method for treating Crohn's disease (CD), said method comprising administering an effective amount of the interleukin-23 receptor inhibitor of claim 1, or a pharmaceutically acceptable salt thereof, to a patient in need thereof.

29. A method for treating psoriasis (PsO), said method comprising administering an effective amount of the interleukin-23 receptor inhibitor of claim 1, or a pharmaceutically acceptable salt thereof, to a patient in need thereof.

30. A method for treating psoriatic arthritis (PsA), said method comprising administering an effective amount of the interleukin-23 receptor inhibitor of claim 1, or a pharmaceutically acceptable salt thereof, to a patient in need thereof.
```

> 종속항 2~23, 31~40("having the following structure:" + 화학구조 도면)은 도면 한정부가 비텍스트이므로 FPO에서 구조 미포착 — 텍스트부만 verbatim 보존 — **(전문: `work/02_extracted/US12478617B2.md`)**. (청구항 39는 "interleukin-23 inhibitor"로 "receptor" 누락, 청구항 40은 청구항 6 인용 — 원문 보존.)

**(c) [ANALYSIS]**

- **독립항:** 1(구체 지질화 화합물 선택군, 도면), 24(조성물), 25~30(질환별 치료방법: IL-23/IL-23R, IBD, UC, CD, PsO, PsA).
- **카테고리:** composition(화학구조 Markush) + method of treating.
- **권리범위 요지:** **지질화(lipidated) 화학형** — icotrokinra 거대고리와 별개 화학형이지만 동일 프로그램. 핵심 구조 한정은 모두 도면이므로 권리범위 정밀 분석은 PDF 도면 필요.
- **검증 결과 요약:** 03_verified에 검증 산출물 없음(pending). 추출 status=partial(화학구조 도면 미포착). 텍스트부는 신뢰 가능.

---

#### 3-C-2. ⚠부분추출 US20240173309A1 — "Lipidated peptide inhibitors of interleukin-23 receptor" (US12478617B2 공개건)

**(a) 서지 메타데이터** (`01_metadata/US20240173309A1.json`)

| 항목 | 값 |
|---|---|
| publication_number | US20240173309A1 (US 2024/0173309 A1) |
| application_number | 18/495,457 |
| kind_code | A1 (공개출원, 심사계속) |
| applicants / assignees | Janssen Biotech, Inc.; Protagonist Therapeutics, Inc. |
| priority_date | 2021-07-14 |
| filing_date | 2023-10-26 |
| publication_date | 2024-05-30 |
| **estimated_expiry** | **확인불가** |
| patent_family | WO2023288019A2, US12478617B2(동일 출원 등록건) |

**(b) [VERBATIM] 독립항 원문** (출처: `work/02_extracted/US20240173309A1.md`)

청구항 1~22는 모두 "(canceled)"이다. 실질 독립항부 verbatim:

```
23. An interleukin-23 receptor inhibitor selected from the group consisting of: or a pharmaceutically acceptable salt thereof.

46. A pharmaceutical composition comprising: (i) the interleukin-23 receptor inhibitor of claim 23, or a pharmaceutically acceptable salt thereof, and (ii) a pharmaceutically acceptable carrier, excipient, or diluent.

47. A method for treating a disease or disorder associated with interleukin 23 (IL-23)/interleukin 23 receptor (IL-23R), said method comprising administering an effective amount of the interleukin-23 receptor inhibitor of claim 23, or a pharmaceutically acceptable salt thereof, to a patient in need thereof.

48. A method for treating inflammatory bowel diseases (IBDs), said method comprising administering an effective amount of the interleukin-23 receptor inhibitor of claim 23, or a pharmaceutically acceptable salt thereof, to a patient in need thereof.

49. A method for treating ulcerative colitis (UC), said method comprising administering an effective amount of the interleukin-23 receptor inhibitor of claim 23, or a pharmaceutically acceptable salt thereof, to a patient in need thereof.

50. A method for treating Crohn's disease (CD), said method comprising administering an effective amount of the interleukin-23 receptor inhibitor of claim 23, or a pharmaceutically acceptable salt thereof, to a patient in need thereof.

51. A method for treating psoriasis (PsO), said method comprising administering an effective amount of the interleukin-23 receptor inhibitor of claim 23, or a pharmaceutically acceptable salt thereof, to a patient in need thereof.

52. A method for treating psoriatic arthritis (PsA), said method comprising administering an effective amount of the interleukin-23 receptor inhibitor of claim 23, or a pharmaceutically acceptable salt thereof, to a patient in need thereof.
```

> 청구항 1~22("(canceled)") 및 종속항 24~45(화학구조 도면)는 verbatim 보존, 도면 한정부 미포착 — **(전문: `work/02_extracted/US20240173309A1.md`)**.

**(c) [ANALYSIS]**

- **독립항:** 23(지질화 화합물 선택군), 46(조성물), 47~52(질환별 치료방법). 1~22 취소.
- **카테고리:** composition + method. US12478617B2의 사전공개 형제건(취소된 22항만큼 번호가 밀려있음, claim 23 = US12478617B2 claim 1에 대응).
- **검증 결과 요약:** 검증 미실시(pending), 추출 partial. 화학구조 도면 PDF 검증 필요(부록 B).

---

#### 3-C-3. ⚠부분추출 WO2023288019A2 — "LIPIDATED PEPTIDE INHIBITORS OF INTERLEUKIN-23 RECEPTOR"

**(a) 서지 메타데이터** (`01_metadata/WO2023288019A2.json`)

| 항목 | 값 |
|---|---|
| publication_number | WO2023288019A2 (WO/2023/288019) |
| application_number | PCT/US2022/037205 |
| kind_code | A2 |
| applicants / assignees | Janssen Biotech, Inc.; Protagonist Therapeutics, Inc. |
| priority_date | 2021-07-14 (US provisional 63/221,697) |
| filing_date | 2022-07-14 |
| publication_date | 2023-01-19 |
| legal_status / **estimated_expiry** | 확인불가 / **확인불가** |
| patent_family | US20240173309A1, US12478617B2 |

**(b) [VERBATIM] 독립항 원문** (출처: `work/02_extracted/WO2023288019A2.md` — **심한 OCR 아티팩트, 원문 보존**)

```
1. An interleukin-23 receptor inhibitor comprising an amino acid sequence of Formula I R1 -X3 -X4-X5 -T -X7 -X8-X9-X 10-Xl 1 -THP-X13-N-X15-X16-R2 (I) wherein: R1 is hydrogen, Ci to C4 alkyl C(O)-, or Ci to C4 alkyl C(O)- substituted with Cl, F, or cyano, or cPEG3aCO; X3 is dR, R, K, dK, or absent; X4 is Pen, Abu, aMeC, or C; X5 is K-Z or dK-Z; X7 is 7MeW, W, 3Pya, 7(2ClPh)W, ... [Formula I 잔기 정의 전문: work/02_extracted/WO2023288019A2.md]

11. A interleukin-23 receptor inhibitor selected from Table 1 A, Table IB, Table 1C, Table ID, Table IE, Table IF, Table 1G, Table 1H, Table II, Table 1J, Table IK, Table 1L, or Table 1M respectively.

13. A pharmaceutical composition comprising: (i) an interleukin-23 receptor inhibitor or pharmaceutically acceptable salt, solvate, or form thereof, according to any of claims 1 to 10, and (ii) a pharmaceutically acceptable carrier, excipient, or diluent.

16. The use of an interleukin-23 receptor inhibitor or compound according to any of claims 1 to 12, or a pharmaceutical composition according to any of claims 13 to 15, for the preparation of a medicament for the treatment of an inflammatory disorder or autoimmune inflammatory disorder.

19. A method for treating a disease or disorder associated with Interleukin 23 (IL-23)/Interleukin 23 Receptor (IL-23R), which comprises administering: (i) an effective amount of a peptide inhibitor of an interleukin-23 receptor, or a pharmaceutically acceptable salt, solvate, or form thereof according to any of claims 1 to 12, or (ii) a pharmaceutical composition according to any of claims 13 to ...
```

> 독립항 2~10(Formula II~X 각 변형), 종속항 12,14,15,17,18,20~22는 verbatim 보존(심한 OCR 아티팩트 포함) — **(전문: `work/02_extracted/WO2023288019A2.md`)**.

**(c) [ANALYSIS]**

- **독립항:** 1~10(Formula I~X 지질화 펩타이드 속), 11(Table 1A~1M 선택), 13·14·15(조성물), 16~18(use/medicament), 19(치료방법).
- **카테고리:** composition + use(스위스형) + method of treating.
- **권리범위 요지:** US12478617B2/US20240173309A1의 PCT. 지질화 IL-23R 펩타이드 속(屬). icotrokinra 거대고리와 같은 프로그램의 지질화 화학형.
- **검증 결과 요약:** 검증 미실시(pending), 추출 partial — **OCR 오류율 높음**(Formula I~X 잔기 정의). 화학분석 전 WIPO PDF 대조 강력 권고(부록 B).

---

#### 3-C-4. ⚠부분추출 WO2024155552A1 — "FORMULATIONS OF LIPIDATED PEPTIDE INHIBITORS OF INTERLEUKIN-23 RECEPTOR"

**(a) 서지 메타데이터** (`01_metadata/WO2024155552A1.json`)

| 항목 | 값 |
|---|---|
| publication_number | WO2024155552A1 (WO/2024/155552) |
| application_number | PCT/US2024/011549 |
| applicants / assignees | Janssen Pharmaceutica NV (Protagonist 미기재) |
| priority_date | 2023-01-16 (US provisional 63/480,068) |
| filing_date | 2024-01-15 |
| publication_date | 2024-07-25 |
| inventors | David A. Lane (et al.) |
| legal_status / **estimated_expiry** | 확인불가 / **확인불가** |

**(b) [VERBATIM] 독립항 원문** (출처: `work/02_extracted/WO2024155552A1.md`)

```
1. An oral pharmaceutical formulation comprising: an absorption enhancer; and a lipidated peptide comprising 9 to 20 amino acids; wherein the lipidated peptide is cyclized to form a ring, wherein the ring comprises 4 to 14 amino acids; and wherein the ratio of the absorption enhancer to the lipidated peptide is no greater than 50:1 (w/w).

69. A method of increasing the bioavailability of a lipidated peptide as described in any one of claims 1-47 in a ... [전문: work/02_extracted/WO2024155552A1.md]

73. Use of an oral pharmaceutical formulation according to any of claims 1-68 for the preparation of a medicament for the treatment of an inflammatory disorder or autoimmune inflammatory disorder.

76. A method for treating a disease or disorder associated with Interleukin 23 (IL-23)/Interleukin 23 Receptor (IL-23R), which comprises administering an effective amount of a pharmaceutical formulation according to any of claims 1-68 to a patient in need thereof.
```

> 종속항 2~68(흡수촉진제·제형 파라미터·화학구조 도면 청구항 18~23,32,35,43 포함), 69~79는 verbatim 보존, 도면 한정부 미포착 — **(전문: `work/02_extracted/WO2024155552A1.md`)**.

**(c) [ANALYSIS]**

- **독립항:** 1(경구 제형: 흡수촉진제 + 지질화 펩타이드, 흡수촉진제:펩타이드 ≤ 50:1 w/w), 69(생체이용률 증대 방법), 73(use/medicament), 76(치료방법).
- **카테고리:** formulation(제형) + method + use.
- **권리범위 요지:** **지질화 펩타이드 경구 제형** 특허. 흡수촉진제 비율 한정이 핵심. Janssen Pharmaceutica NV 단독 출원(제형 단계). 지질화 화학형 제품화 보호.
- **검증 결과 요약:** 검증 미실시(pending), 추출 partial(청구항 18~23,32,35,43 화학구조 도면 미포착). 텍스트부 신뢰 가능.

---

### 3-D. PTG-200 earlier 티어 — 초기 세대 (icotrokinra 이전, 광의 골격)

#### 3-D-1. WO2016011208A1 — "ORAL PEPTIDE INHIBITORS OF INTERLEUKIN-23 RECEPTOR..." (최초 기초 PCT)

**(a) 서지 메타데이터** (`01_metadata/WO2016011208A1.json`)

| 항목 | 값 |
|---|---|
| publication_number | WO2016011208A1 (WO/2016/011208) |
| application_number | PCT/US2015/040658 |
| applicants / assignees | Protagonist Therapeutics, Inc. |
| inventors | Dinesh V. Patel, David Liu |
| priority_date | 2014-07-17 (US prov. 62/025,899; 추가 62/119,685, 62/119,688=2015-02-23) |
| filing_date | 2015-07-15 |
| publication_date | 2016-01-21 |
| legal_status / **estimated_expiry** | 확인불가 / **확인불가** |
| patent_family | US9624268B2(국내단계/모출원 14/800,627), US10023614B2, US10941183B2, US11884748B2 |

**(b) [VERBATIM] 독립항 원문** (출처: `work/02_extracted/WO2016011208A1.md` — **심한 OCR 아티팩트, 원문 보존**)

```
1. A peptide inhibitor of an interleukin-23 receptor, or a pharmaceutically acceptable salt or solvate thereof, wherein the peptide inhibitor comprises an amino acid sequence of Formula (Xa): Xl-X2-X3-X4-X5-X6-X7-X8-X9-X10-Xl l-X12-X13-X14-X15-X16-X17-X18-X19-X20 (Xa) wherein XI is any amino acid or absent; X2 is any amino acid or absent; X3 is any amino acid or absent; X4 is any amino acid or chemical moiety capable of forming a bond with X9; X5 is any amino acid; X6 is any amino acid; X7 is any amino acid; X8 is any amino acid; X9 is any amino acid or chemical moiety capable of forming a ... [Formula (Xa) 잔기 정의 전문: work/02_extracted/WO2016011208A1.md]

36. A peptide dimer inhibitor of an interleukin-23 receptor, wherein the peptide dimer inhibitor comprises two peptide monomer subunits connected via one or more linker moieties, wherein each peptide monomer subunit has a sequence or structure set forth in any one of claims 1-35.

44. A pharmaceutical composition comprising the peptide inhibitor of any one of claims 1-35 or the peptide dimer inhibitor of any one of claims 36-41 , and a pharmaceutically acceptable carrier, excipient, or diluent.

47. A method for treating an Inflammatory Bowel Disease (IBD), ulcerative colitis, Crohn's disease, Celiac disease {nontropical Sprue), enteropathy associated with seronegative arthropathies, microscopic colitis, collagenous colitis, eosinophilic gastroenteritis, colitis associated with radio- or chemo -therapy, colitis associated with disorders of innate immunity as in leukocyte adhesion deficiency- 1 , chronic granulomatous disease, glycogen storage disease type lb, Hermansky-Pudlak syndro ... [전문: work/02_extracted/WO2016011208A1.md]

52. A method of assessing the ability of a candidate compound to inhibit or reduce an inflammatory disease or disorder, comprising: (a) providing to a rat an amount of dextran sulfate sodium (DSS) or 2,4,6- Trinitrobenzenesulfonic acid (TNBS) sufficient to induce an inflammatory bowel disease (IBD); (b) providing to the rat an amount of a candidate compound; and (c) measuring an amount of IBD symptoms present in the rat after being provided with the DSS and the candidate compound; wherein if ... [전문: work/02_extracted/WO2016011208A1.md]
```

> 청구항 1의 전체 Formula (Xa) 정의, 종속항 2~35(청구항 35는 Formula I 화학구조 도면, 미포착), 36~43(이량체), 44~46(조성물), 47~54(방법, 54까지)는 verbatim 보존(심한 OCR 아티팩트 포함) — **(전문: `work/02_extracted/WO2016011208A1.md`)**.

**(c) [ANALYSIS]**

- **독립항:** 1(Formula Xa 20-잔기 광역 속), 36(이량체 저해제), 44(조성물), 47(치료방법), 52(후보화합물 평가 방법 — DSS/TNBS 래트 모델).
- **카테고리:** composition + dimer + method of treating + assay method.
- **권리범위 요지:** Protagonist 경구 IL-23R 프로그램의 **최초 기초 PCT**(2014-07-17 우선일). PTG-200 계열의 광의(廣義) 골격으로 icotrokinra보다 이르고 넓음. icotrokinra의 직접 선행 계보.
- **검증 결과 요약:** 검증 미실시(pending), 추출 partial — **스캔 PDF OCR로 광범위 아티팩트**(`XI 0`=X10, `Ache`=Achc, `He`=Ile, 베타-호모 잔기 mojibake, C-말단 절단). WIPO PDF 재수집 필요(부록 B). 청구항 골격·의존구조·방법항(47~54)은 신뢰 가능.

---

#### 3-D-2. US9624268B2 — "Oral peptide inhibitors of interleukin-23 receptor..." (WO2016 미국 모출원 등록건)

**(a) 서지 메타데이터** (`01_metadata/US9624268B2.json`)

| 항목 | 값 |
|---|---|
| publication_number | US9624268B2 |
| application_number | 14/800,627 |
| applicants / assignees | Protagonist Therapeutics, Inc. |
| priority_date | 2014-07-17 |
| filing_date | 2015-07-15 |
| grant_date | 2017-04-18 (Granted) |
| **estimated_expiry** | **확인불가** |
| patent_family | WO2016011208A1, US10023614B2, US10941183B2, US11884748B2 |

**(b) [VERBATIM] 독립항 원문** (출처: `work/02_extracted/US9624268B2.md`)

청구항 1·11·19는 매우 긴 Formula (Ir)/(Xa) Markush 속 청구항이다. 각 도입부 + 조성물항 verbatim:

```
1. A peptide inhibitor of an interleukin-23 receptor, or a pharmaceutically acceptable salt or solvate thereof, wherein the peptide inhibitor comprises the amino acid sequence of Formula Ir:X1-X2-X3-X4-X5-X6-X7-X8-X9-X10-X11-X12-X13-X14-X15-X16-X17-X18-X19-X20 (Ir) wherein X1 is any amino acid or absent; X2 is any amino acid or absent; X3 is any amino acid or absent; X4 is Cys, Pen, hCys, D-Pen, D-Cys, D-hCys, Met, Glu, Asp, Lys, Orn, Dap, Dab, ... [Formula Ir 잔기 정의 전문: work/02_extracted/US9624268B2.md] ... wherein the peptide inhibitor is cyclized via a bond between X4 and X9, and wherein the peptide inhibitor inhibits the binding of an interleukin-23 (IL-23) to an IL-23 receptor.

11. A peptide inhibitor of an interleukin-23 receptor, or a pharmaceutically acceptable salt or solvate thereof, wherein the peptide inhibitor comprises the amino acid sequence of Formula Xa:X1-X2-X3-X4-X5-X6-X7-X8-X9-X10-X11-X12-X13-X14-X15-X16-X17-X18-X19-X20  (Xa) wherein X1 is any amino acid or absent; ... [Formula Xa 잔기 정의 전문: work/02_extracted/US9624268B2.md] ... wherein the peptide inhibitor comprises a disulfide bond between X4 and X9.

19. A peptide inhibitor of an interleukin-23 receptor, or a pharmaceutically acceptable salt or solvate thereof, wherein the peptide inhibitor comprises the amino acid sequence of Formula Xa: ... [전문: work/02_extracted/US9624268B2.md] ... wherein the peptide inhibitor is cyclized via an intramolecular bond between X4 and X9.

24. A pharmaceutical composition comprising the peptide inhibitor of any one of claims 1, 2-5, 6-11, 12-16, 19 or 10-20, and a pharmaceutically acceptable carrier, excipient, or diluent.
```

> 종속항 2~10, 12~18, 20~23(잔기 한정·SEQ ID NO 군·이황화/티오에테르 변형)은 verbatim 보존 — **(전문: `work/02_extracted/US9624268B2.md`)**.

**(c) [ANALYSIS]**

- **독립항:** 1(Formula Ir 속), 11(Formula Xa 속, disulfide), 19(Formula Xa 속, intramolecular bond), 24(조성물).
- **카테고리:** composition(광역 속) — 방법항은 본 등록건에 미포함(자매건 US10941183B2가 방법 담당).
- **권리범위 요지:** WO2016011208A1의 미국 모출원(14/800,627) 등록건. 2014 우선일 광역 골격. icotrokinra의 직접 선행 계보.
- **검증 결과 요약:** 검증 미실시(pending). 추출 status=done(완전 추출).

---

#### 3-D-3. US10023614B2 — "Oral peptide inhibitors of interleukin-23 receptor..." (계속출원)

**(a) 서지 메타데이터** (`01_metadata/US10023614B2.json`)

| 항목 | 값 |
|---|---|
| publication_number | US10023614B2 |
| application_number | 15/831,100 |
| applicants / assignees | Protagonist Therapeutics, Inc. (inventors: Bhandari, Bourne, Smythe) |
| priority_date | 2014-07-17 |
| filing_date | 2017-12-04 |
| grant_date | 2018-07-17 (Granted) |
| **estimated_expiry** | **확인불가** |
| patent_family | US9624268B2(14/800,627→15/442,229 체인), WO2016011208A1, US10941183B2, US11884748B2 |

**(b) [VERBATIM] 독립항 원문** (출처: `work/02_extracted/US10023614B2.md`)

```
1. A peptide inhibitor of an interleukin-23 receptor, or a pharmaceutically acceptable salt thereof, comprising an amino acid sequence consisting of Formula (Xa): X1-X2-X3-X4-X5-X6-X7-X8-X9-X10-X11-X12-X13-X14-X15-X16-X17-X18-X19-X20 (Xa), wherein X1 is absent; X2 is absent; X3 is Glu, (D)Glu, Arg, (D)Arg, Phe, (D)Phe, 2-Nal, Thr, Leu, (D)Gln, or absent; X4 is Pen; X5 is Dap, Dap(Ac), Gly, Lys, Gln, Arg, Ser, Thr, or Asn; X6 is Thr; X7 is Trp; X8 is Gln; X9 is Pen; X10 is 2-Nal, a Phe analog, Tyr, or a Tyr analog; X11 is 1-Nal, 2-Nal, Phe(3,4-dimethoxy), or Phe(3,4-Cl2); ... [Formula (Xa) 잔기 정의 전문: work/02_extracted/US10023614B2.md] ... wherein the peptide inhibitor is cyclized via a disulfide bond between X4 and X9 of the amino acid sequence, and wherein 2-Nal is L-2-Naphthylalanine, Pen is L-Penicillamine, ... and betaAla is Beta-alanine.

21. A pharmaceutical composition comprising the peptide inhibitor or pharmaceutically acceptable salt thereof of claim 1.
```

> 종속항 2~20(N말단 Ac/C말단 NH2 한정, 구체 SEQ ID NO, DIG 링커 이량체 등)은 verbatim 보존 — **(전문: `work/02_extracted/US10023614B2.md`)**.

**(c) [ANALYSIS]**

- **독립항:** 1(Formula Xa 속, X4/X9=Pen 이황화), 21(조성물).
- **카테고리:** composition. icotrokinra 이전 PTG-200 계열의 좀 더 한정된 속(X4=Pen, X6=Thr, X7=Trp, X8=Gln 고정). 이량체(DIG 링커) 청구 포함.
- **검증 결과 요약:** 검증 미실시(pending). 추출 done.

---

#### 3-D-4. US10941183B2 — "Oral peptide inhibitors of interleukin-23 receptor..." (방법 청구)

**(a) 서지 메타데이터** (`01_metadata/US10941183B2.json`)

| 항목 | 값 |
|---|---|
| publication_number | US10941183B2 |
| application_number | 16/217,864 |
| applicants / assignees | Protagonist Therapeutics, Inc. (inventors: Bhandari, Bourne) |
| priority_date | 2014-07-17 |
| filing_date | 2018-12-12 |
| grant_date | 2021-03-09 (Granted) |
| **estimated_expiry** | **확인불가** |
| patent_family | US9624268B2, US10023614B2, WO2016011208A1, US11884748B2 |

**(b) [VERBATIM] 독립항 원문** (출처: `work/02_extracted/US10941183B2.md`)

```
1. A method of treating an inflammatory bowel disease (IBD) in a subject, comprising administering to the subject an effective amount of a peptide inhibitor of an interleukin-23 receptor, or a pharmaceutically acceptable salt thereof, wherein the peptide inhibitor comprises an amino acid sequence consisting of Formula (Xa):X1-X2-X3-X4-X5-X6-X7-X8-X9-X10-X11-X12-X13-X14-X15-X16-X17-X18-X19-X20 (Xa), wherein X1 is any amino acid or absent; ... X4 is Abu; X5 is Gln; X6 is Thr; X7 is Trp; X8 is Gln; X9 is Cys; X10 is Phe, Tyr, a Phe analog, or a Tyr analog; ... [Formula (Xa) 잔기 정의 전문: work/02_extracted/US10941183B2.md] ... wherein the peptide inhibitor is cyclized via a thioether bond between X4 and X9, and wherein 1-Nal is L-1-napthylalanine, ... and Aib is 2-aminoisobutyric acid.
```

> 종속항 2~20(N말단 Ac/C말단 NH2, 구체 SEQ ID NO, 경구투여, UC/CD/pouchitis 한정)은 verbatim 보존 — **(전문: `work/02_extracted/US10941183B2.md`)**. 본 등록건은 청구항 1이 유일 독립항(나머지 모두 종속).

**(c) [ANALYSIS]**

- **독립항:** 1(IBD 치료방법, Formula Xa 속 — X4=Abu, X9=Cys, 티오에테르 환화). 나머지(2~20)는 모두 청구항 1 인용 종속항.
- **카테고리:** method of treating(IBD/UC/CD/pouchitis). 경구투여 한정(청구항 17).
- **권리범위 요지:** PTG-200 골격의 **방법(치료용도)** 청구. 동일 우선일(2014)의 자매 등록건(물질=US9624268B2/US10023614B2, 조성물=US11884748B2)과 역할 분담.
- **검증 결과 요약:** 검증 미실시(pending). 추출 done.

---

#### 3-D-5. ⚠부분추출 US11884748B2 — "Oral peptide inhibitors of interleukin-23 receptor..." (조성물, OCR 손상)

**(a) 서지 메타데이터** (`01_metadata/US11884748B2.json`)

| 항목 | 값 |
|---|---|
| publication_number | US11884748B2 |
| application_number | 17/161,370 |
| applicants / assignees | Protagonist Therapeutics, Inc. (inventors: Bhandari) |
| priority_date | 2014-07-17 |
| filing_date | 2021-01-28 |
| grant_date | 2024-01-30 (Granted) |
| **estimated_expiry** | **확인불가** |
| patent_family | US9624268B2, US10023614B2, US10941183B2, WO2016011208A1 |

**(b) [VERBATIM] 독립항 원문** (출처: `work/02_extracted/US11884748B2.md` — **OCR 손상 토큰 포함, 원문 보존**)

```
1. A pharmaceutical composition comprising a peptide inhibitor of an interleukin-23 receptor, or a pharmaceutically acceptable salt thereof, and a pharmaceutically acceptable carrier, excipient, or diluent, wherein the peptide inhibitor of an interleukin-23 receptor is selected from the group consisting of:

(SEQ ID NO: 702) Ac-[Abta]-QTWQC-[Phe(4-OMe)]-[2-Nal]-[α-Me-Lys]-ENG-NH2;

(SEQ ID NO: 704) Ac-[Abta]-QTWQCY-[2-Nal]-[α-Me-Lys]-ENG-NH2;

(SEQ ID NO: 782) Ac-[Abu]-QTWQC-[Phe[4-(2-aminoethoxy)]-W-[α-Me-Lys]-ENG-NH2;
... [SEQ ID NO 861~1047 — 전문: work/02_extracted/US11884748B2.md] ...
wherein the peptide inhibitor is cyclized via a thioether bond between Abu and C.
```

> 종속항 2~21(각 구체 SEQ ID NO 한정 조성물)은 verbatim 보존(OCR 손상 토큰 `[Abta]`, `-AiN-`, `[AibMLys(Ac)]`, `-8 2-Nal]`, `acbc]` 등 그대로) — **(전문: `work/02_extracted/US11884748B2.md`)**.

**(c) [ANALYSIS]**

- **독립항:** 1(선택군 펩타이드 조성물, 티오에테르 Abu-C 환화). 2~21 종속(각 단일 SEQ ID NO).
- **카테고리:** composition(조성물).
- **권리범위 요지:** PTG-200 골격의 조성물 청구(2014 우선일). 자매건 US10941183B2의 SEQ ID NO와 동일군.
- **검증 결과 요약:** 검증 미실시(pending), 추출 partial — **FPO OCR 손상 심각**. 선행 잔기 `[Abta]`는 `[Abu]`의 OCR 오류로 강하게 추정(모든 청구항이 "between Abu and C" 환화 명시, 자매건 US10941183B2는 동일 SEQ ID NO 702/704를 `[Abu]`로 기재). USPTO PPUBS 재수집 전 서열 문자열을 권위 있는 것으로 취급 금지(부록 B).


---

## 부록 A — ❌ 오귀속(misattributed) / icotrokinra 무관 번호

> 아래 8건은 discovery 단계에서 icotrokinra 패밀리로 잘못 귀속(또는 본래 core로 분류되었다가 검증으로 무관 확정)된 것들이다. **본문(진짜 패밀리)에서 제외**하고 여기 별도 표기한다. 절대 드롭하지 않는다.

| 번호 | 실제 정체 (출원인) | 한 줄 설명 + 제외 사유 |
|---|---|---|
| **WO2023212427A1** | IC-TROSA Point-to-Multipoint Optical Network System (**Dell Products LP**) | 광네트워크(광통신 하드웨어) 특허. IL-23/펩타이드와 무관. discovery가 icotrokinra 경구 펩타이드 PCT로 오표기. → 제외. |
| **WO2023212432A1** | Multi-Blade Knife Assembly with Protective Cover (**Larry Kalkstein**) | 다중날 칼(주방기구) 특허(IPC B26B). icotrokinra와 전혀 무관. → 제외. |
| **WO2024026471A1** | CD98HC Antigen-Binding Domains and Uses Therefor (**Alector LLC**) | CD98HC 항체(혈뇌장벽 수송) 특허. 펩타이드 거대고리 아님. → 제외. |
| **WO2024026472A2** | Transferrin Receptor Antigen-Binding Domains and Uses Therefor (**Alector LLC**) | 트랜스페린 수용체 항체 특허. 요청 번호는 A1이나 실제 공개 kind는 **A2**. icotrokinra 무관. → 제외. |
| **WO2023099669A1** | Peptide Inhibitors of Interleukin-23 Receptor (**Zealand Pharma A/S**) | **진짜 IL-23R 펩타이드 저해제이나 출원인이 Zealand Pharma(경쟁사)**. Janssen/Protagonist 아님, icotrokinra 분자 아님. → 패밀리에서 제외(경쟁사 랜드스케이프 참조용). |
| **US9605027B2** | Polypeptides that bound to IL-23 receptor... (**Medical Diagnostic Laboratories, LLC**) | IL-23R 결합 폴리펩타이드이나 출원인이 MDL(다른 주체). Protagonist 프로그램 아님. → 제외. |
| **USRE49026E1** | Polypeptides that bound to IL-23 receptor... (**Medical Diagnostic Laboratories, LLC**) | 위 US9169292의 재발행(reissue, RE). 동일하게 MDL 소유, icotrokinra 무관. → 제외. (재발행 가감 표기 미확인.) |
| **US11180535B2** | Saccharide binding, tumor penetration... chimeric peptides from therapeutic bacteria | **검증으로 확정된 오귀속.** FPO 기준 본 번호는 박테리아 종양침투 키메라 펩타이드(YebF 융합) 특허(app 15/835,137, 등록 2021-11-23)다. discovery는 icotrokinra 조성물 특허로 추정했으나, 추출된 20개 청구항이 이 **무관 특허**와 verbatim 일치(PASS 19, MISMATCH 1=공백). → icotrokinra 패밀리에서 제거. |

### 부록 A 보충 — 무관 특허 청구항 상태 (원문 보존 원칙)

- **WO2023212427A1 / WO2023212432A1 / WO2024026471A1 / WO2024026472A1**: 추출 FAILED. FPO가 반환한 off-subject 콘텐츠(광네트워크/칼/항체)는 **verbatim 무결성을 보증할 수 없어 전사하지 않음**. 어떤 청구항도 본 보고서에 전사하지 않았다.
- **US9605027B2 (MDL)**: 13개 청구항이 추출됨(IL-23R 결합 환형 폴리펩타이드, SEQ ID NO 177~179; IL-17F/IL-22 생성 억제 방법). icotrokinra 무관이므로 본문 미수록. (원문은 `work/02_extracted/US9605027B2.md`.)
- **USRE49026E1 (MDL)**: 36개 청구항 추출(reissue), 단 재발행 가감 표기(브래킷/이탤릭) 미보존 — 정확 권리범위 미확인. (원문은 `work/02_extracted/USRE49026E1.md`.)
- **US11180535B2 (박테리아 펩타이드)**: 검증 확정용으로 추출된 20개 청구항 원문은 `work/02_extracted/US11180535B2.md`에 보존(예: "1. A genetic construct configured to cause a live genetically engineered host bacterium ... a YebF sequence fused to a tumor-penetrating peptide sequence ..."). 이는 **icotrokinra가 아님**을 입증하는 근거 자료이며 본문 패밀리에서 제외한다.

---

## 부록 B — 데이터 한계 / 리뷰 큐 (Human-in-the-loop)

### B-1. 공통 소스 차단 (전 특허 영향)
- **WIPO Patentscope · Espacenet · Google Patents 전부 HTTP 403/503 차단**. 1차 소스는 FPO 단일.
- 따라서 모든 검증의 `cross_source = false`. 진정한 교차출처 확정 불가.
- **모든 특허의 만료일(estimated_expiry) = 확인불가.** 20년 존속기간·PTA·PTE 미확인.

### B-2. 특허별 리뷰 큐 항목 요약 (`work/_review_queue/`)

| 특허 | 플래그 | 핵심 이슈 |
|---|---|---|
| **WO2021146441A1** | partial / needs_rework | **청구항 168~186 누락**(FPO는 186까지 렌더, 추출은 167까지). 청구항 162~167은 FPO가 **다른 렌더링(Table E1A/E1B 기반)** 으로 순서 뒤섞임·부분 렌더 → **버전 불일치**. 158~161 preamble 모호. WIPO PDF 재수집 필요. |
| **US20210261622A1** | needs_rework | 12개 청구항 MISSING(2,106,112,117,121,124,128,131,136,147,177,183). "(canceled)" 줄 본문 흡수, 화학구조 이미지→[NOTE]. |
| **US11041000B2** | partial / needs_rework | 청구항 16~23,26 화학구조 **도면**(미포착). FPO 페이지가 claim 26 직후 절단 → **청구항 27+ 존재 여부 미확인**. |
| **US11884748B2** | partial | **FPO OCR 손상 심각**: `[Abta]`(=[Abu] 추정), `-AiN-`(=[Aib]), `[AibMLys(Ac)]`, `-8 2-Nal]`, `acbc]`/`acpc]`/`achc]` 브래킷 깨짐. 서열 문자열 권위 취급 금지. |
| **WO2016011208A1** | partial | 스캔 PDF OCR 광범위 아티팩트(`XI 0`=X10, `Ache`=Achc, `He`=Ile, 베타-호모 mojibake, C-말단 절단). 청구항 35 Formula I 화학구조 도면 미포착. |
| **US12478617B2 / US20240173309A1** | partial | 화학구조 **도면 청구항** 다수(구조=권리범위 핵심)인데 비텍스트 이미지로 미포착. 텍스트부만 신뢰. claim 39 "receptor" 누락, claim 40은 claim 6 인용(원문). |
| **WO2023288019A2** | partial | Formula I~X 잔기 정의에 **OCR 오류율 높음**. claim 12 모호(독립/종속 불명). 화학분석 전 WIPO PDF 대조 필수. |
| **WO2024155552A1** | partial | claim 18~23,32,35,43 화학구조 도면 미포착. claim 54 다중종속 이상, 사소 OCR. |
| **CA3202226A1** | failed / unverifiable | 도달 가능 소스에서 청구항 확보 실패(FPO 404). **가족 멤버로부터 추정 금지.** CIPO에서 재수집 필요. |
| **JP2023145581A** | failed / unverifiable | FPO 서지/요약만, 청구항 미게재. 청구항은 일본어이며 **번역 없이** J-PlatPat에서 재수집·전사 필요. |
| **WO2023099669A1 (Zealand)** | partial | claim 77(177개 SEQ ID NO)·claim 78(화학구조) 미전사. 경쟁사 특허로 본문 제외. |
| **WO2023212427/212432/2024026471/2024026472** | failed | 번호 오귀속 + 소스 차단. 정확 번호 재확인 필요(부록 A). |
| **US11180535B2** | unverifiable(오귀속) | 번호↔주제 충돌이 검증으로 해소(박테리아 펩타이드 특허). icotrokinra 패밀리에서 제거(부록 A). |

### B-3. 권고 조치 (요약)
1. WIPO Patentscope / Espacenet / USPTO PPUBS(이미지·전문)에서 재수집 후 `scripts/claim_diff.py` 재대조.
2. 화학구조 도면 청구항(US12478617B2, US20240173309A1, US11041000B2 16~23, WO2024155552A1, WO2023288019A2)은 PDF 도면을 사람이 확인.
3. WO2021146441A1 청구항 156~167 + 168~186 완전 재수집(버전 일치 확인).
4. CA/JP 청구항 1차 소스 확보(JP는 일본어 verbatim).
5. icotrokinra 경구제형 PCT의 정확한 WO 번호 재발굴(오귀속된 WO2023212427/212432 대체).

---

## 6. 특허 간 종합 (Synthesis)

### 6-1. IL-23R 경구 펩타이드 패밀리 권리범위 비교

| 세대/티어 | 대표 특허 | 우선일 | 청구 유형 | 권리범위 폭 |
|---|---|---|---|---|
| PTG-200 earlier | WO2016011208A1, US9624268B2, US10023614B2, US10941183B2, US11884748B2 | 2014-07-17 | 광역 속(Formula Xa/Ir, 20잔기) + 이량체 + 방법 | **가장 넓음** (any amino acid 다수) |
| CORE genus (2018~2020) | US12552836B2(2018-07-12), US11041000B2(2019-07-10), WO2021146441A1·US20210261622A1·US11845808B2·US12018057B2(2020-01-15) | 2018~2020 | 단환 속(Formula I/Z′/II) + 구체 SEQ ID NO + 조성물 + 방법 | 중간(골격 한정 좁아짐) |
| CORE composition | **US11939361B2**(✅), CA3202226A1, JP2023145581A | 2020-11-20 | SEQ ID NO:1 조성물·염/용매화물 + 용량 + 흡수촉진제 | **가장 좁고 직접적**(icotrokinra 완제품) |
| Lipidated (주변부) | US12478617B2·US20240173309A1·WO2023288019A2(2021-07-14), WO2024155552A1(2023-01-16) | 2021~2023 | 지질화 화학형 화합물 + 제형 + 방법 | 별도 화학형(다른 분자 계열) |

### 6-2. icotrokinra 핵심 보호 구조
- **물질·조성물 보호의 정점은 US11939361B2(✅검증완료)** — icotrokinra(SEQ ID NO:1)를 명시 정의하고, 그 염/용매화물(아세테이트 비결정형), 함량(0.1~15%/20% w/w, 25~150 mg 등), 흡수촉진제(10~60% w/w)를 청구. ICOTYDE 완제 의약품에 가장 근접.
- **속(genus) 보호**: US11845808B2(좁은 Formula I, W(7-Me)·Lys(Ac)·Phe(4-(2-aminoethoxy))·2Nal·THP·3Pal·Sarc 골격)와 US20210261622A1 claim 162(SEQ ID NO:1 명시 열거)가 icotrokinra 분자를 직접 포섭. US12552836B2·US11041000B2·US12018057B2가 코어 속을 보강.
- **초기 광의 골격(PTG-200)**: 2014 우선일의 WO2016011208A1 / US9624268B2 등이 가장 넓은 스캐폴드를 선점 — icotrokinra의 계보적 뿌리.

### 6-3. 세대 흐름 (PTG-200 → icotrokinra)
2014-2015년 Protagonist 단독의 **PTG-200(경구 IL-23R 펩타이드) 광역 골격**(WO2016011208A1 계열)에서 출발 → 2018-2020년 **Janssen 공동출원**으로 단환 거대고리 속을 좁히며 최적화(W(7-Me), Sarc 말단, 3Pal 도입) → 2020-11 우선일의 **조성물 특허 US11939361B2에서 icotrokinra(SEQ ID NO:1)를 확정**. 이후 2021~2023년 **지질화 화학형/제형**(US12478617B2, WO2024155552A1 등)으로 화학공간을 확장. 출원인 변천(Protagonist 단독 → Janssen Biotech 공동 → Janssen Pharmaceutica NV 조성물/제형)이 개발·제휴 단계 진전을 반영한다.

### 6-4. 경쟁(Zealand) 메모
- **WO2023099669A1 (Zealand Pharma A/S)**: 동일 표적(IL-23R 펩타이드 저해제)을 추구하나 **다른 분자·다른 환화 화학(lactam/dithioether/triazole 브리지, 14잔기 Formula I)** 으로, Janssen/Protagonist의 Pen-Pen 이황화 거대고리와 구조적으로 구별된다. icotrokinra 패밀리가 아니며 경쟁사 랜드스케이프로만 참조.

### 6-5. FTO(Freedom-to-Operate) 관점의 제한
- **모든 특허의 만료일(존속기간·PTA·PTE)이 확인불가**이므로, 본 보고서로 FTO/권리 잔존기간을 판단하는 것은 **불가능**하다. 또한 다수 특허가 `needs_rework`(FPO 단일소스 노이즈) 또는 `partial`(화학구조 도면 미포착) 상태이고 `cross_source=false`이므로, **권리범위 정밀 판단 전 1차 소스(USPTO/WIPO/Espacenet PDF) 재수집·재검증이 선행되어야 한다.** 현재 확정적으로 검증된 것은 US11939361B2 단 1건뿐이다.

---

*보고서 생성일: 2026-06-15 · 출처: FreePatentsOnline 단일 소스(cross_source=false) · 청구항 원문은 verbatim 보존(번역·교정 없음).*

---

## 부록 C — 특허 만료일 추정 (계산값, 2026-06-15 추가)

> ⚠ **방법론·한계 고지(반드시 읽을 것):** 아래 만료일은 권위 출처(USPTO/EPO 법적상태)에서 확인한 값이 **아니라**, 수집된 우선일/출원일에 **미국 특허 존속기간 규정(35 U.S.C. §154, 비가출원·PCT 출원일+20년)**을 적용해 **계산한 추정치**다. 다음을 **반영하지 않았다**: (i) **PTA**(특허존속기간조정, 심사지연으로 일수 가산 — 본 패밀리는 심사가 길어 수백 일 가산 가능), (ii) **PTE/Hatch-Waxman 연장**(icotrokinra가 2026-03 FDA 승인되었으므로 핵심 물질·조성물 특허, 특히 US11939361B2는 **최대 5년 연장** 대상 가능), (iii) 가출원 vs 비가출원 구분 미검증(가출원 우선일을 쓴 경우 실제 기산일이 더 늦을 수 있음). 따라서 아래 값은 **명목 기본존속기간의 근사치**이며 법적 자문이 아니다.

| patent_id | 분류 | 기산일 | 기준 | 추정 만료(기본 20년) |
|---|---|---|---|---|
| CA3202226A1 | 진짜패밀리 | 2021-11-19 | 출원일 | 2041-11-19  (출원일+20년; PTA/PTE 미반영) |
| JP2023145581A | 진짜패밀리 | 2023-07-24 | 출원일 | 2043-07-24  (출원일+20년; PTA/PTE 미반영) |
| US10023614B2 | 진짜패밀리 | 2014-07-17 | 우선일 | 2034-07-17  (우선일+20년; PTA/PTE 미반영) |
| US10787490B2 | 진짜패밀리 | 2015-07-15 | 우선일 | 2035-07-15  (우선일+20년; PTA/PTE 미반영) |
| US10941183B2 | 진짜패밀리 | 2014-07-17 | 우선일 | 2034-07-17  (우선일+20년; PTA/PTE 미반영) |
| US11041000B2 | 진짜패밀리 | 2019-07-10 | 우선일 | 2039-07-10  (우선일+20년; PTA/PTE 미반영) |
| US11180535B2 | 오귀속/무관 | - | - | 확인불가 |
| US11845808B2 | 진짜패밀리 | 2020-01-15 | 우선일 | 2040-01-15  (우선일+20년; PTA/PTE 미반영) |
| US11884748B2 | 진짜패밀리 | 2014-07-17 | 우선일 | 2034-07-17  (우선일+20년; PTA/PTE 미반영) |
| US11939361B2 | 진짜패밀리 | 2020-11-20 | 우선일 | 2040-11-20  (우선일+20년; PTA/PTE 미반영) |
| US12018057B2 | 진짜패밀리 | 2020-01-15 | 우선일 | 2040-01-15  (우선일+20년; PTA/PTE 미반영) |
| US12478617B2 | 진짜패밀리 | 2021-07-14 | 우선일 | 2041-07-14  (우선일+20년; PTA/PTE 미반영) |
| US12552836B2 | 진짜패밀리 | 2018-07-12 | 우선일 | 2038-07-12  (우선일+20년; PTA/PTE 미반영) |
| US20210261622A1 | 진짜패밀리 | 2020-01-15 | 우선일 | 2040-01-15  (우선일+20년; PTA/PTE 미반영) |
| US20240173309A1 | 진짜패밀리 | 2021-07-14 | 우선일 | 2041-07-14  (우선일+20년; PTA/PTE 미반영) |
| US9605027B2 | 오귀속/무관 | 2011-06-14 | 우선일 | 2031-06-14  (우선일+20년; PTA/PTE 미반영) |
| US9624268B2 | 진짜패밀리 | 2014-07-17 | 우선일 | 2034-07-17  (우선일+20년; PTA/PTE 미반영) |
| USRE49026E1 | 오귀속/무관 | 2011-06-14 | 우선일 | 2031-06-14  (우선일+20년; PTA/PTE 미반영) |
| WO2016011208A1 | 진짜패밀리 | 2014-07-17 | 우선일 | 2034-07-17  (우선일+20년; PTA/PTE 미반영) |
| WO2021146441A1 | 진짜패밀리 | 2021-01-14 | 출원일 | 2041-01-14  (출원일+20년; PTA/PTE 미반영) |
| WO2023099669A1 | 오귀속/무관 | 2022-12-01 | 출원일 | 2042-12-01  (출원일+20년; PTA/PTE 미반영) |
| WO2023212427A1 | 오귀속/무관 | 2023-01-19 | 출원일 | 2043-01-19  (출원일+20년; PTA/PTE 미반영) |
| WO2023212432A1 | 오귀속/무관 | 2022-04-26 | 우선일 | 2042-04-26  (우선일+20년; PTA/PTE 미반영) |
| WO2023288019A2 | 진짜패밀리 | 2021-07-14 | 우선일 | 2041-07-14  (우선일+20년; PTA/PTE 미반영) |
| WO2024026471A1 | 오귀속/무관 | 2022-07-29 | 우선일 | 2042-07-29  (우선일+20년; PTA/PTE 미반영) |
| WO2024026472A1 | 오귀속/무관 | 2022-07-29 | 우선일 | 2042-07-29  (우선일+20년; PTA/PTE 미반영) |
| WO2024155552A1 | 진짜패밀리 | 2023-01-16 | 우선일 | 2043-01-16  (우선일+20년; PTA/PTE 미반영) |

**핵심:** icotrokinra 물질·조성물 특허 **US11939361B2** 기본존속기간 추정 **2040-11-20** — 여기에 PTA(가산)와 신약 PTE(최대 +5년) 가능성을 고려하면 실제 만료는 **2040년대 중반(~2045)** 까지 연장될 수 있다. 정확한 만료일은 차단되지 않은 권위 출처(USPTO Patent Center/PEDS, FDA Orange Book)에서 PTA·PTE를 확인해야 확정된다.
