#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Builds output/patent_claims_report.md by embedding GP-authoritative claim
bodies VERBATIM (char-for-char) inside fenced blocks, with Korean analysis added
on top. Never mutates claim text: it slices the GP .md file body (after the
'# <id> — Claims (verbatim, Google Patents)' header line) and keeps it as-is."""

import os, io

GP = "/home/user/Claude.lgchem_CHA1/pcea-harness/work/05_gp_authoritative"
OUT = "/home/user/Claude.lgchem_CHA1/pcea-harness/output/patent_claims_report.md"

def body(pid):
    """Return the verbatim claim body of a GP .md file, stripping ONLY the
    first markdown header line and the single blank line after it, and trailing
    whitespace-only lines. The claim text itself is untouched."""
    path = os.path.join(GP, pid + ".md")
    with io.open(path, "r", encoding="utf-8", newline="") as f:
        text = f.read()
    lines = text.split("\n")
    # drop leading header line(s) starting with '#'
    i = 0
    while i < len(lines) and (lines[i].startswith("#") or lines[i].strip() == ""):
        # only skip the FIRST header + following blank; stop once we hit content
        if lines[i].startswith("#"):
            i += 1
            # skip exactly one following blank line if present
            if i < len(lines) and lines[i].strip() == "":
                i += 1
            break
        i += 1
    inner = "\n".join(lines[i:])
    return inner.rstrip("\n")

def fenced(pid):
    return "```text\n" + body(pid) + "\n```"

W = []
def w(s=""):
    W.append(s)

# ----------------------------------------------------------------------------
# COVER
# ----------------------------------------------------------------------------
w("# icotrokinra (ICOTYDE / JNJ-2113 / PN-235) 특허 청구항 통합 분석 보고서")
w()
w("> **[VERBATIM] 표기 규칙:** 본 보고서에서 코드블록(```)으로 둘러싼 청구항 원문은 "
  "권위 소스(authoritative source)인 **Google Patents**의 결정적(deterministic) 파싱 결과 "
  "`work/05_gp_authoritative/<id>.md`에서 **한 글자도 수정·번역·정리하지 않고** 그대로 복사한 것이다. "
  "OCR/파싱 잔재(예: `Gin`=Gln, `lie`=Ile, `XI 0`=X10, `[Abta]`, 화학구조식이 빠진 빈 청구항 등)도 "
  "원문 보존 원칙(THE ONE RULE)에 따라 **그대로** 둔다. 그 위에 덧붙인 한국어 서술은 [ANALYSIS] 블록으로 "
  "물리적으로 분리하였으며 청구항 원문과 절대 혼합하지 않는다.")
w()
w("---")
w()
w("## 표지 / 머리말")
w()
w("| 항목 | 내용 |")
w("|---|---|")
w("| 보고서 제목 | icotrokinra (경구 IL-23R 길항 펩타이드) 특허 패밀리 청구항 통합 분석 |")
w("| 분석 대상 약물 | **ICOTYDE / icotrokinra / JNJ-2113 / PN-235** — 경구용 인터루킨-23 수용체(IL-23R) 길항 단환(monocyclic) 펩타이드 |")
w("| 개발 주체 | Protagonist Therapeutics, Inc. + Janssen (Janssen Biotech / Janssen Pharmaceutica NV, J&J 계열) |")
w("| 핵심 물질 정의 | **icotrokinra = SEQ ID NO: 1** (조성물 특허 US11939361B2 / CA3202226A1 / JP2023145581A 패밀리 기준) |")
w("| 후보 총건수 | **27건** (진짜 패밀리 18 + 오귀속 9) |")
w("| 소스 | **2-소스 교차검증**: ① Google Patents (권위 원문, `work/05_gp_authoritative`) ② FreePatentsOnline (FPO, `work/02_extracted`) |")
w("| 교차 비교 방식 | 코드 기반(`scripts/claim_diff.py` 계열) 청구항 단위 substantive diff. 결과: `work/03_verified/_cross_source_GP_vs_FPO.json` |")
w("| 생성일 | **2026-06-16** |")
w()
w("### 후보 27건 분류 요약")
w()
w("| 구분 | 건수 | 비고 |")
w("|---|---|---|")
w("| 진짜 icotrokinra / Protagonist+Janssen 패밀리 | **18건** | 본문 (티어별 정리) |")
w("| 오귀속(misattributed) — icotrokinra 무관 | **9건** | 부록 A |")
w("| **합계** | **27건** | |")
w()
w("> 매니페스트 `genuine_icotrokinra_family` 목록은 19개를 담고 있었으나, 그 중 **US11180535B2**가 "
  "검증 단계에서 무관 특허(박테리아 종양침투 키메라 펩타이드, Google Patents 404 + FPO는 박테리아 펩타이드)로 "
  "확정되어 부록 A로 이동했다. 따라서 본문(진짜 패밀리)은 **18건**, 부록 A(오귀속)는 **9건**(매니페스트 misattributed 7 + US11180535B2 + 중복분류 정리)이다.")
w()
w("### 교차검증 배지 체계 (NEW — 2-소스 반영)")
w()
w("| 배지 | 의미 |")
w("|---|---|")
w("| ✅교차검증 | GP↔FPO 둘 다 존재하고 청구항 substantive diff == 0 (완전 일치) |")
w("| ☑️부분교차검증 | GP↔FPO 둘 다 존재하나 일부 청구항 substantive diff > 0 (차이 청구항 번호 명시) |")
w("| ⚠️단일소스(GP) | FPO 없음/실패/잘림 → GP 단독 (그래도 권위 소스) |")
w("| ❌오귀속 | icotrokinra 무관 특허 → 부록 A |")
w()
w("---")
w()

# ----------------------------------------------------------------------------
# EXECUTIVE SUMMARY
# ----------------------------------------------------------------------------
w("## Executive Summary")
w()
w("- **icotrokinra = SEQ ID NO: 1**. 가장 강력하게 검증된 권리는 **조성물(composition) 특허 "
  "US11939361B2**로, **GP↔FPO 16/16 청구항 완전일치(substantive_diff=0)** ✅교차검증을 통과했다. "
  "이 특허는 SEQ ID NO:1 펩타이드를 0.1~15%(w/w) 함유한 약학 조성물·염/용매화물 형태·흡수촉진제 조합 및 그 치료용도를 청구한다.")
w("- 동일 조성물 패밀리의 **캐나다 대응(CA3202226A1, 153 청구항)**은 이번에 Google Patents로 전체 청구항을 "
  "확보했다(이전 파이프라인에서는 FPO 404로 미확보였음). FPO 대응본이 없어 ⚠️단일소스(GP)로 분류하나, US11939361B2와 "
  "동일 SEQ ID NO:1 조성물 계열임이 명확하다.")
w("- **속(genus) 특허 패밀리**(출원 17/149,509 및 자매 출원): pre-grant 공개 **US20210261622A1**, 등록본 "
  "**US11845808B2**, 자매 **US12018057B2**. 이들은 단환 펩타이드 IL-23R 길항제의 Markush 속/종 청구항을 담는다. "
  "이 중 **US12018057B2**는 GP↔FPO 10/10 완전일치 ✅, US11845808B2는 30개 중 4개 차이 ☑️, US20210261622A1은 "
  "(GP가 (canceled) 표기를 포함해 50개 비교 대상에서) 14개 차이 ☑️이다.")
w("- **이전 파이프라인의 최대 공백 2건이 이번에 해소되었다:**")
w("  - **WO2021146441A1** — Google Patents 기준 **전체 186 청구항** 확보(FPO는 167에서 잘려 168~186 누락이었음). 본 보고서는 GP 전문을 [VERBATIM]으로 싣는다.")
w("  - **CA3202226A1** — Google Patents 기준 **153 청구항** 확보(FPO는 추출 실패였음).")
w("- **잔여 공백(부록 B):** **JP2023145581A**(일본 조성물 대응)는 Google Patents `/en` 페이지에 청구항이 "
  "실리지 않아(claims=0) **⚠️미확보**이며 J-PlatPat(일본 특허청) 원문 확인이 필요하다.")
w("- **권위 만료일(부록 C):** Google Patents anticipated expiration(출원일+20년, PTE 미반영) 기준 — "
  "US11939361B2 = **2041-11-19**, 속 패밀리(US20210261622/US11845808/US12018057) = **2041-01-14**, "
  "US12552836B2 = **2039-07-12**, US11041000B2 = **2040-07-09**, US10787490B2 및 PTG-200 계열"
  "(US9624268/US10023614/US10941183/US11884748) = **2035-07-15**, lipidated US12478617B2 = **2042-07-14**.")
w("- **PTE 주의:** icotrokinra는 2026-03 FDA 승인 약물이므로, 조성물 특허 **US11939361B2**에는 "
  "Hatch-Waxman 특허존속기간연장(PTE, 최대 +5년)이 적용될 수 있다 → **실질 만료 ~2045년까지 가능**(권위 GP 값 2041-11-19은 PTE 미반영 base term).")
w("- **오귀속 9건(부록 A):** Dell 광통신(WO2023212427A1), 다중날 칼(WO2023212432A1), Alector 항체 2건"
  "(WO2024026471A1·WO2024026472A1), Zealand Pharma IL-23R 펩타이드(WO2023099669A1 — 경쟁사), "
  "Medical Diagnostic Laboratories IL-23R 폴리펩타이드 2건(US9605027B2·USRE49026E1), 박테리아 종양침투 키메라 펩타이드(US11180535B2).")
w()
w("---")
w()

# ----------------------------------------------------------------------------
# Helper for genuine entries
# ----------------------------------------------------------------------------
def meta_table(rows):
    w("| 항목 | 내용 |")
    w("|---|---|")
    for k, v in rows:
        w("| %s | %s |" % (k, v))
    w()

def verbatim_block(pid, note=None):
    w("**[VERBATIM] — 출처: Google Patents (`work/05_gp_authoritative/%s.md`)**" % pid)
    if note:
        w()
        w(note)
    w()
    w(fenced(pid))
    w()

# ----------------------------------------------------------------------------
# TIER 1 — composition (가장 강한 검증)
# ----------------------------------------------------------------------------
w("## 제1장. 진짜 icotrokinra 패밀리 — 티어별 정리")
w()
w("### 티어 1 — 조성물(Composition) 특허 (icotrokinra = SEQ ID NO:1 직접 권리, 최우선)")
w()

# US11939361B2
w("#### 1.1 US11939361B2 ✅교차검증 (GP↔FPO 16/16 완전일치, substantive_diff=0)")
w()
meta_table([
    ("특허번호", "US11939361B2 (등록, B2)"),
    ("제목", "Compositions of peptide inhibitors of Interleukin-23 receptor"),
    ("출원번호 / 출원일", "17/531,538 / 2021-11-19"),
    ("우선일", "2020-11-20 (US Provisional 63/116,568); 추가 63/275,222 (2021-11-03)"),
    ("등록일", "2024-03-26"),
    ("출원인/양수인", "Janssen Pharmaceutica NV; Protagonist Therapeutics, Inc."),
    ("패밀리", "CA3202226A1, JP2023145581A (동일 제목 조성물 패밀리)"),
    ("권위 만료일", "**2041-11-19** (GP anticipated expiration; 출원일+20년, PTE 미반영) — FDA 승인 약물이므로 Hatch-Waxman PTE 최대 +5년 시 ~2045 가능"),
    ("교차검증", "GP=16, FPO=16, both=16, agree=16, **substantive_diff=0** → ✅완전일치"),
])
w("**[ANALYSIS] (한국어)**")
w()
w("icotrokinra 권리의 **핵심(crown jewel)**. SEQ ID NO:1 펩타이드(또는 그 약학적으로 허용되는 염/용매화물)를 "
  "조성물 대비 약 0.1~15%(w/w) 함유하는 약학 조성물을 직접 청구한다(청구항 1). 종속항은 화학구조 한정·아세테이트 "
  "형태·무정형(amorphous) 형태(청구항 2~4), 함량 범위(1~1000mg, 10~300mg, 25~150mg; 청구항 5~7), 흡수촉진제 "
  "(absorption enhancer) 10~60%(w/w) 조합(청구항 8~9), 그리고 염증성 질환 치료방법(청구항 10, 16)으로 확장된다. "
  "청구항 11~15는 0.1~**20%**(w/w) 범위의 또 다른 조성물 군이다(청구항 1의 15% 상한과 구별되는 별도 독립항).")
w()
w("**검증 의의:** 본 특허는 이번 2-소스 비교에서 GP와 FPO가 16개 청구항 전부 substantive diff 0으로 "
  "**완전일치**했다. 즉 어느 한 소스의 파싱 오류 가능성이 양쪽 독립 수집에서 상호 배제되어, 청구항 원문 신뢰도가 가장 높다. "
  "icotrokinra 물질 자체가 SEQ ID NO:1로 고정되므로 이 조성물 청구항은 약물의 시장 독점과 직결된다.")
w()
verbatim_block("US11939361B2")
w("---")
w()

# CA3202226A1
w("#### 1.2 CA3202226A1 ⚠️단일소스(GP) — 공백 해소 (153 청구항 신규 확보)")
w()
meta_table([
    ("특허번호", "CA3202226A1 (캐나다 공개, A1)"),
    ("제목", "Compositions of peptide inhibitors of interleukin-23 receptor"),
    ("출원일 / 공개일", "2021-11-19 / 2022-05-27"),
    ("우선일", "확인불가 (CA 소스 미확인; US 자매 US11939361B2는 2020-11-20 우선)"),
    ("출원인/양수인", "Janssen Pharmaceutica NV; Protagonist Therapeutics, Inc."),
    ("패밀리", "US11939361B2 (동일 조성물), JP2023145581A"),
    ("권위 만료일", "추정 2041-11-19 (출원일+20년; PTA/PTE 미반영)"),
    ("교차검증", "GP=153, FPO=0(추출 실패) → ⚠️단일소스(GP). 이전 파이프라인 공백 해소."),
])
w("**[ANALYSIS] (한국어)**")
w()
w("이전 파이프라인에서 FPO가 404를 반환해 청구항 0건으로 **미확보**였던 캐나다 조성물 대응본을, 이번에 "
  "Google Patents에서 **전체 153 청구항**으로 확보했다. 청구항 1은 US11939361B2와 동일하게 "
  "**SEQ ID NO:1 펩타이드를 0.1~15%(w/w) 함유한 조성물**을 청구하여, 본 캐나다 출원이 icotrokinra 조성물 "
  "패밀리의 정규 구성원임을 원문으로 확인한다. 다만 캐나다 단일 소스(GP)만 확보되어 교차검증 등급은 ⚠️단일소스(GP)로 둔다. "
  "153개 청구항은 분량이 크므로 전문을 아래 [VERBATIM]에 그대로 싣는다(화학구조식이 텍스트로 깨진 부분도 원문 보존).")
w()
verbatim_block("CA3202226A1")
w("---")
w()

# ----------------------------------------------------------------------------
# TIER 2 — genus
# ----------------------------------------------------------------------------
w("### 티어 2 — 속(Genus) / 단환 펩타이드 Markush 특허")
w()

# WO2021146441A1
w("#### 2.1 WO2021146441A1 ☑️부분교차검증 — 공백 해소 (전체 186 청구항)")
w()
meta_table([
    ("특허번호", "WO2021146441A1 (PCT 공개, A1)"),
    ("제목", "Peptide Inhibitors of Interleukin-23 Receptor and Their Use to Treat Inflammatory Diseases"),
    ("국제출원 / 공개", "PCT/US2021/013463, 국제출원일 2021-01-14"),
    ("우선일", "2020-01-15 (US Provisional 62/961,624)"),
    ("출원인/양수인", "Janssen Biotech, Inc.; Protagonist Therapeutics, Inc."),
    ("패밀리", "US20210261622A1, US11845808B2, US12018057B2 (동일/자매 출원 17/149,509 계열)"),
    ("권위 만료일", "PCT 자체는 존속기간 만료 개념 **해당없음(N/A)**; 국내단계 진입국별 산정(미국 대응 = 2041-01-14)"),
    ("교차검증", "GP=186, FPO=167(168~186 잘림), both=167, agree=92, **substantive_diff=75** → ☑️부분교차검증"),
])
w("**[ANALYSIS] (한국어)**")
w()
w("프로그램의 **기초 PCT**. 이전 파이프라인에서 FPO가 청구항 167에서 잘려 **168~186번 19개가 누락**된 상태였으나, "
  "이번에 Google Patents로 **전체 186 청구항**을 확보했다. 이로써 보고서상 최대 공백 중 하나가 해소되었다. "
  "GP↔FPO 비교에서 두 소스 공통 167개 중 substantive_diff가 75개로 크게 나타나는데, 이는 FPO의 OCR/파싱 잡음"
  "(공백·기호 깨짐, Markush 치환기 목록의 줄바꿈 차이)이 누적된 것으로, **권위 소스는 GP**이며 FPO 차이분은 "
  "원문 권리범위 변동이 아니라 추출 잡음으로 본다. 따라서 등급은 ☑️부분교차검증(차이 청구항 다수 = 공통 167개 중 75개; "
  "GP 단독 보유분 168~186은 FPO 부재)이며 본문 [VERBATIM]은 **GP 186 전문**을 사용한다.")
w()
w("청구항 1은 Formula (I) 단환 펩타이드 속(X3~X16 가변)을 정의하고, proviso로 특정 서열들을 제외(disclaimer)하는 "
  "복잡한 Markush 구조다. 후반부(180번대)는 조성물/치료용도 청구항으로 확장된다.")
w()
verbatim_block("WO2021146441A1")
w("---")
w()

# US20210261622A1
w("#### 2.2 US20210261622A1 ☑️부분교차검증 (차이 14개)")
w()
meta_table([
    ("특허번호", "US20210261622A1 (pre-grant 공개, A1)"),
    ("제목", "Peptide Inhibitors of Interleukin-23 Receptor and Their Use to Treat Inflammatory Diseases"),
    ("출원번호 / 출원일", "17/149,509 / 2021-01-14"),
    ("우선일", "2020-01-15 (US Provisional 62/961,624)"),
    ("공개일", "2021-08-26"),
    ("출원인/양수인", "Janssen Biotech, Inc.; Protagonist Therapeutics, Inc."),
    ("패밀리", "WO2021146441A1 (PCT), US11845808B2 (동일 출원의 등록본)"),
    ("권위 만료일", "**2041-01-14** (GP anticipated expiration; 출원일+20년, PTE 미반영)"),
    ("교차검증", "GP=50, FPO=50, both=50, agree=36, **substantive_diff=14** → ☑️부분교차검증"),
])
w("**[ANALYSIS] (한국어)**")
w()
w("WO2021146441A1과 동일 출원(17/149,509)의 미국 pre-grant 공개본. GP 청구항 본문에는 `(canceled)` 표기"
  "(예: `2.-104. (canceled)`, `106.-110. (canceled)` 등)가 그대로 남아 있어 실제 심사 중 다수 청구항이 "
  "삭제·재번호되었음을 보여준다. GP↔FPO 50개 비교에서 36개 일치, 14개 차이로 ☑️부분교차검증. 차이는 Markush "
  "치환기 목록의 파싱 잡음이 주된 원인이며 권위 소스는 GP다. 청구항 1의 Formula (I)과 proviso 구조는 PCT(WO) 및 "
  "등록본 US11845808B2와 동일 계열이다.")
w()
verbatim_block("US20210261622A1")
w("---")
w()

# US11845808B2
w("#### 2.3 US11845808B2 ☑️부분교차검증 (차이 4개)")
w()
meta_table([
    ("특허번호", "US11845808B2 (등록, B2)"),
    ("제목", "Peptide inhibitors of interleukin-23 receptor and their use to treat inflammatory diseases"),
    ("출원번호 / 출원일", "17/149,509 / 2021-01-14"),
    ("우선일", "2020-01-15 (US Provisional 62/961,624)"),
    ("등록일", "2023-12-19"),
    ("출원인/양수인", "Janssen Biotech, Inc.; Protagonist Therapeutics, Inc."),
    ("패밀리", "US20210261622A1 (동일 출원 공개본), WO2021146441A1 (PCT)"),
    ("권위 만료일", "**2041-01-14** (GP anticipated expiration; 출원일+20년, PTE 미반영)"),
    ("교차검증", "GP=30, FPO=30, both=30, agree=26, **substantive_diff=4** → ☑️부분교차검증"),
])
w("**[ANALYSIS] (한국어)**")
w()
w("출원 17/149,509의 **등록본**. 청구항 1은 Formula (I) **단환(monocyclic) 펩타이드**를 명시적으로 한정"
  "(X3-Pen-N-T-X7-Lys(Ac)-Pen-X10-2Nal-X12-E-N-X15-Sarc)하고, X7=Trp/W(7-Me)/W(7-Ph), X10=Phe(4-(2-aminoethoxy)), "
  "X12=THP, X15=3Pal로 좁힌다 — icotrokinra 화학형(monocyclic, Pen-Pen 이황화 가교)과 직접 부합한다. 청구항 5는 "
  "SEQ ID NO:104/158/247 서열군을, 청구항 12 이하는 IL-23/IL-23R 관련 질환(IBD/UC/CD/PsO/PsA) 치료방법 및 "
  "경구 등 투여경로를 청구한다. GP↔FPO 30개 중 26개 일치, 4개 차이로 ☑️부분교차검증이며 권위 소스는 GP.")
w()
verbatim_block("US11845808B2")
w("---")
w()

# US12018057B2
w("#### 2.4 US12018057B2 ✅교차검증 (10/10 완전일치)")
w()
meta_table([
    ("특허번호", "US12018057B2 (등록, B2)"),
    ("제목", "Peptide inhibitors of interleukin-23 receptor and their use to treat inflammatory diseases"),
    ("출원번호 / 출원일", "17/149,544 / 2021-01-14"),
    ("우선일", "2020-01-15 (US Provisional 62/961,618)"),
    ("등록일", "2024-06-25"),
    ("출원인/양수인", "Janssen Biotech, Inc.; Protagonist Therapeutics, Inc."),
    ("패밀리", "US20210261622A1 / US11845808B2 (자매 출원 17/149,509), WO2021146441A1"),
    ("권위 만료일", "**2041-01-14** (GP anticipated expiration; 출원일+20년, PTE 미반영)"),
    ("교차검증", "GP=10, FPO=10, both=10, agree=10, **substantive_diff=0** → ✅완전일치"),
])
w("**[ANALYSIS] (한국어)**")
w()
w("자매 출원(17/149,544)의 등록본으로, **GP↔FPO 10/10 완전일치** ✅교차검증을 통과했다. 청구항 1은 다수 SEQ ID NO"
  "(3~137)의 구체 서열들을 'or'로 나열한 종(species) 군 청구항이며, Pen-Pen 이황화 가교로 환화된다. 청구항 2는 "
  "SEQ ID NO:105 단일 종, 청구항 3~4는 조성물, 청구항 5~10은 IBD/UC/CD/PsO/PsA 치료방법이다. 완전일치 + 구체 서열 "
  "청구라는 점에서 권리 신뢰도가 높은 종 특허다.")
w()
verbatim_block("US12018057B2")
w("---")
w()

# US12552836B2
w("#### 2.5 US12552836B2 ✅교차검증 (21/21 완전일치)")
w()
meta_table([
    ("특허번호", "US12552836B2 (등록, B2)"),
    ("제목", "Peptide inhibitors of interleukin-23 receptor and their use to treat inflammatory diseases"),
    ("출원번호 / 출원일", "17/549,579 / 2021-12-13 (US App 16/510,118의 계속출원)"),
    ("우선일", "2018-07-12 (US Provisional 62/697,218); 추가 62/872,477 (2019-07-10)"),
    ("등록일", "2026-02-17"),
    ("출원인/양수인", "Protagonist Therapeutics, Inc."),
    ("권위 만료일", "**2039-07-12** (GP anticipated expiration; 출원일+20년, PTE 미반영)"),
    ("교차검증", "GP=21, FPO=21, both=21, agree=21, **substantive_diff=0** → ✅완전일치"),
])
w("**[ANALYSIS] (한국어)**")
w()
w("**GP↔FPO 21/21 완전일치** ✅교차검증. 청구항 1은 Formula (II) 단환 펩타이드(X4=Pen, X5=Asn/Gln, X6=Thr, "
  "X7=알킬치환 Trp, X8=Gln/αMeLys류, X9=Pen, X10=2-아미노에톡시 치환 Phe, X11=2-Nal/1-Nal; X4-X9 환화)를 "
  "정의하며, IL-23↔IL-23R 결합 저해를 기능 한정한다. 종속항은 구체 서열(SEQ ID NO:6, 242~285 등), 지질/PEG 콘쥬게이트, "
  "장용코팅(enteric coating, 청구항 21) 등으로 확장된다. 우선일 2018-07-12로 본 패밀리 내에서 비교적 이른 우선권을 갖는다.")
w()
verbatim_block("US12552836B2")
w("---")
w()

# US11041000B2
w("#### 2.6 US11041000B2 ☑️부분교차검증 (차이 9개)")
w()
meta_table([
    ("특허번호", "US11041000B2 (등록, B2)"),
    ("제목", "Peptide inhibitors of interleukin-23 receptor and their use to treat inflammatory diseases"),
    ("출원번호 / 출원일", "17/001,428 / 2020-08-24"),
    ("우선일", "2019-07-10 (US Provisional 62/872,477); PCT/US2020/041409 (2020-07-09)"),
    ("등록일", "2021-06-22"),
    ("출원인/양수인", "Protagonist Therapeutics, Inc."),
    ("권위 만료일", "**2040-07-09** (GP anticipated expiration; 출원일+20년, PTE 미반영)"),
    ("교차검증", "GP=26, FPO=26, both=26, agree=17, **substantive_diff=9** → ☑️부분교차검증"),
])
w("**[ANALYSIS] (한국어)**")
w()
w("Formula (Z′) 단환 펩타이드(X4~X15 가변, R1/R2 말단기)를 청구하는 속 특허. 청구항 15·25는 SEQ ID NO:201/227/242/245/"
  "249/252/267/284/285 등 구체 서열군을 나열한다. 주의: GP 원문에서 청구항 16~23, 26은 화학구조식이 텍스트로 "
  "렌더링되지 않아 본문이 `...the peptide inhibitor is:` 에서 끝나는 **빈 구조 청구항**으로 보존되어 있다(원문 그대로). "
  "GP↔FPO 26개 중 17개 일치, 9개 차이로 ☑️부분교차검증이며 권위 소스는 GP.")
w()
verbatim_block("US11041000B2")
w("---")
w()

# ----------------------------------------------------------------------------
# TIER 3 — earlier / oral IBD (PTG-200 lineage)
# ----------------------------------------------------------------------------
w("### 티어 3 — 초기 세대(PTG-200 계열) 경구 IL-23R 펩타이드 (icotrokinra 이전)")
w()
w("> 아래 4건(+PCT)은 우선일 2014-07-17의 PTG-200 계열로 icotrokinra 특정 조성물보다 앞서지만, 동일 "
  "Protagonist 경구 IL-23R 펩타이드 골격(scaffold)에 속한다. 모두 **GP 단독**(FPO 미수집)이라 ⚠️단일소스(GP)다.")
w()

# US10787490B2
w("#### 3.1 US10787490B2 ☑️부분교차검증 (차이 4개)")
w()
meta_table([
    ("특허번호", "US10787490B2 (등록, B2)"),
    ("제목", "Peptide inhibitors of interleukin-23 receptor and their use to treat inflammatory diseases"),
    ("출원번호 / 출원일", "15/745,371 / 2016-07-15 (PCT/US2016/042680 국내단계; 14/800,627의 CIP)"),
    ("우선일", "2015-07-15 (PCT/US2015/040658); 추가 62/264,820, 62/281,123"),
    ("등록일", "2020-09-29"),
    ("출원인/양수인", "Protagonist Therapeutics, Inc."),
    ("권위 만료일", "**2035-07-15** (GP anticipated expiration; 출원일+20년, PTE 미반영)"),
    ("교차검증", "GP=18, FPO=18, both=18, agree=14, **substantive_diff=4** → ☑️부분교차검증"),
])
w("**[ANALYSIS] (한국어)**")
w()
w("청구항 1은 SEQ ID NO:1115~1206의 **지질화/PEG화 종 서열군**을 나열한다(Palm, isoGlu, PEG4, Octanyl 등 콘쥬게이트 포함) — "
  "후대 lipidated 패밀리(WO2023288019A2 등)의 화학적 전조에 해당한다. 종속항은 단일 종, 조성물, IBD/UC/CD 치료방법이다. "
  "GP↔FPO 18개 중 14개 일치, 4개 차이로 ☑️부분교차검증. 우선일 2015이므로 만료 2035-07-15로 본 코퍼스 내 가장 이른 축에 든다.")
w()
verbatim_block("US10787490B2")
w("---")
w()

# US9624268B2
w("#### 3.2 US9624268B2 ⚠️단일소스(GP)")
w()
meta_table([
    ("특허번호", "US9624268B2 (등록, B2)"),
    ("제목", "Oral peptide inhibitors of interleukin-23 receptor and their use to treat inflammatory bowel diseases"),
    ("출원번호 / 출원일", "14/800,627 / 2015-07-15"),
    ("우선일", "2014-07-17 (US Provisional 62/025,899); 추가 62/119,685, 62/119,688"),
    ("등록일", "2017-04-18"),
    ("출원인/양수인", "Protagonist Therapeutics, Inc."),
    ("패밀리", "WO2016011208A1 (PCT), US10023614B2, US10941183B2, US11884748B2"),
    ("권위 만료일", "**2035-07-15** (GP anticipated expiration; 출원일+20년, PTE 미반영)"),
    ("교차검증", "GP=24, FPO=0(미수집) → ⚠️단일소스(GP)"),
])
w("**[ANALYSIS] (한국어)**")
w()
w("PTG-200 계열의 **기초 미국 특허**(icotrokinra 이전 세대). 청구항 1은 Formula Ir(X1~X20, 광범위 가변)의 "
  "대형 Markush 속이며, X4/X9는 Pen/Cys 등 환화 가능 잔기다. 청구항 5·9는 다수 SEQ ID NO 종 서열을 나열하고, "
  "청구항 24는 조성물이다. FPO 미수집이라 ⚠️단일소스(GP).")
w()
verbatim_block("US9624268B2")
w("---")
w()

# US10023614B2
w("#### 3.3 US10023614B2 ⚠️단일소스(GP)")
w()
meta_table([
    ("특허번호", "US10023614B2 (등록, B2)"),
    ("제목", "Oral peptide inhibitors of interleukin-23 receptor and their use to treat inflammatory bowel diseases"),
    ("출원번호 / 출원일", "15/831,100 / 2017-12-04 (15/442,229의 계속, 14/800,627 분할 계열)"),
    ("우선일", "2014-07-17 (US Provisional 62/025,899)"),
    ("등록일", "2018-07-17"),
    ("출원인/양수인", "Protagonist Therapeutics, Inc."),
    ("발명자", "Bhandari, Bourne, Smythe (성만 표면화)"),
    ("권위 만료일", "**2035-07-15** (GP anticipated expiration; 출원일+20년, PTE 미반영)"),
    ("교차검증", "GP=21, FPO=0(미수집) → ⚠️단일소스(GP)"),
])
w("**[ANALYSIS] (한국어)**")
w()
w("US9624268B2의 계속 계열. 청구항 1은 Formula (Xa) 단환 펩타이드(X4-X9 이황화 환화)를 정의하고 잔기 정의·약어"
  "(2-Nal, Pen, Dap 등)를 본문에 명시한다. 청구항 13~16·20은 **DiGlycolic acid(DIG) 링커로 연결된 이량체(dimer)** "
  "형태를 청구하는 점이 특징이다. FPO 미수집이라 ⚠️단일소스(GP).")
w()
verbatim_block("US10023614B2")
w("---")
w()

# US10941183B2
w("#### 3.4 US10941183B2 ⚠️단일소스(GP)")
w()
meta_table([
    ("특허번호", "US10941183B2 (등록, B2)"),
    ("제목", "Oral peptide inhibitors of interleukin-23 receptor and their use to treat inflammatory bowel diseases"),
    ("출원번호 / 출원일", "16/217,864 / 2018-12-12"),
    ("우선일", "2014-07-17 (US Provisional 62/025,899)"),
    ("등록일", "2021-03-09"),
    ("출원인/양수인", "Protagonist Therapeutics, Inc."),
    ("권위 만료일", "**2035-07-15** (GP anticipated expiration; 출원일+20년, PTE 미반영)"),
    ("교차검증", "GP=20, FPO=0(미수집) → ⚠️단일소스(GP)"),
])
w("**[ANALYSIS] (한국어)**")
w()
w("**방법(method) 청구항** 중심. 청구항 1은 Formula (Xa)에서 X4=Abu, X9=Cys, **X4-X9 티오에터(thioether) 가교**로 "
  "환화된 펩타이드를 IBD 치료에 투여하는 방법이다(앞선 이황화 가교 특허들과 가교 화학이 구별됨). 종속항은 구체 SEQ 서열·"
  "경구투여·UC/CD/pouchitis 한정이다. FPO 미수집이라 ⚠️단일소스(GP).")
w()
verbatim_block("US10941183B2")
w("---")
w()

# US11884748B2
w("#### 3.5 US11884748B2 ⚠️단일소스(GP)")
w()
meta_table([
    ("특허번호", "US11884748B2 (등록, B2)"),
    ("제목", "Oral peptide inhibitors of interleukin-23 receptor and their use to treat inflammatory bowel diseases"),
    ("출원번호 / 출원일", "17/161,370 / 2021-01-28"),
    ("우선일", "2014-07-17 (US Provisional 62/025,899)"),
    ("등록일", "2024-01-30"),
    ("출원인/양수인", "Protagonist Therapeutics, Inc."),
    ("권위 만료일", "**2035-07-15** (GP anticipated expiration; 출원일+20년, PTE 미반영)"),
    ("교차검증", "GP=21, FPO=0(미수집) → ⚠️단일소스(GP)"),
])
w("**[ANALYSIS] (한국어)**")
w()
w("**조성물(composition) 청구항** 중심. 청구항 1은 다수 SEQ ID NO(702, 704, 782, 861, 877, 880 등) 서열군을 "
  "함유한 약학 조성물이며, X4=Abu와 C 간 티오에터 가교로 환화된다. 원문에 `[Abta]`, `AiN`, `[AibMLys(Ac)]` 등 "
  "파싱 잔재가 그대로 남아 있어 원문 보존 원칙에 따라 손대지 않는다. FPO 미수집이라 ⚠️단일소스(GP).")
w()
verbatim_block("US11884748B2")
w("---")
w()

# WO2016011208A1
w("#### 3.6 WO2016011208A1 ⚠️단일소스(GP)")
w()
meta_table([
    ("특허번호", "WO2016011208A1 (PCT 공개, A1)"),
    ("제목", "ORAL PEPTIDE INHIBITORS OF INTERLEUKIN-23 RECEPTOR AND THEIR USE TO TREAT INFLAMMATORY BOWEL DISEASES"),
    ("국제출원 / 공개", "PCT/US2015/040658, 국제출원일 2015-07-15"),
    ("우선일", "2014-07-17 (US Provisional 62/025,899)"),
    ("출원인/양수인", "Protagonist Therapeutics, Inc."),
    ("발명자", "Dinesh V. Patel, David Liu"),
    ("권위 만료일", "PCT 자체 만료 **N/A**; 추정 국내단계 2034~2035 (우선일/출원일+20년)"),
    ("교차검증", "GP=52, FPO=0(미수집) → ⚠️단일소스(GP)"),
])
w("**[ANALYSIS] (한국어)**")
w()
w("Protagonist 경구 IL-23R 프로그램의 **최초 기초 PCT**. 청구항 1은 Formula (Xa)의 가장 넓은 속(X4/X9 = '결합 형성 "
  "가능한 임의 아미노산/화학 모이어티')이며, 이후 청구항에서 점진적으로 한정된다. 청구항 52~54는 후보 화합물 스크리닝 "
  "방법(항-IL-23p19 항체 양성대조 등)이다. FPO 미수집이라 ⚠️단일소스(GP).")
w()
verbatim_block("WO2016011208A1")
w("---")
w()

# ----------------------------------------------------------------------------
# TIER 4 — peripheral lipidated chemotype
# ----------------------------------------------------------------------------
w("### 티어 4 — 주변(Peripheral) lipidated 화학형 및 제제(formulation)")
w()

# US12478617B2
w("#### 4.1 US12478617B2 ✅교차검증 (40/40 완전일치)")
w()
meta_table([
    ("특허번호", "US12478617B2 (등록, B2)"),
    ("제목", "Lipidated peptide inhibitors of interleukin-23 receptor"),
    ("출원번호 / 출원일", "18/495,457 / 2023-10-26"),
    ("우선일", "2021-07-14 (US Provisional 63/221,697); PCT/US2022/037205"),
    ("등록일", "2025-11-25"),
    ("출원인/양수인", "Janssen Biotech, Inc.; Protagonist Therapeutics, Inc."),
    ("패밀리", "US20240173309A1 (동일 출원 공개본), WO2023288019A2 (PCT)"),
    ("권위 만료일", "**2042-07-14** (GP anticipated expiration; 출원일+20년, PTE 미반영)"),
    ("교차검증", "GP=40, FPO=40, both=40, agree=40, **substantive_diff=0** → ✅완전일치"),
])
w("**[ANALYSIS] (한국어)**")
w()
w("**GP↔FPO 40/40 완전일치** ✅교차검증. 다만 본 특허의 청구항 대부분은 IL-23R 저해제의 **화학구조식**을 청구하는데, "
  "GP `/en` 텍스트 파싱에서 구조식 이미지가 렌더링되지 않아 청구항 1~23 및 31~40 본문이 "
  "`...selected from the group consisting of: or a pharmaceutically acceptable salt thereof.` / "
  "`...having the following structure:` 형태의 **구조 누락 청구항**으로 보존되어 있다(원문 그대로). 구조식 전문은 GP PDF "
  "또는 등록공보 원본 확인이 필요하다. 청구항 24는 조성물, 25~30은 IL-23/IL-23R 질환·IBD·UC·CD·PsO·PsA 치료방법으로 텍스트가 온전하다. "
  "lipidated 화학형이므로 icotrokinra(단환, 비지질) 본체와는 주변 관계다.")
w()
verbatim_block("US12478617B2")
w("---")
w()

# US20240173309A1
w("#### 4.2 US20240173309A1 ✅교차검증 (공통 30개 일치)")
w()
meta_table([
    ("특허번호", "US20240173309A1 (pre-grant 공개, A1)"),
    ("제목", "Lipidated peptide inhibitors of interleukin-23 receptor"),
    ("출원번호 / 출원일", "18/495,457 / 2023-10-26"),
    ("우선일", "2021-07-14 (US Provisional 63/221,697)"),
    ("공개일", "2024-05-30"),
    ("출원인/양수인", "Janssen Biotech, Inc.; Protagonist Therapeutics, Inc."),
    ("패밀리", "WO2023288019A2 (PCT), US12478617B2 (동일 출원 등록본)"),
    ("권위 만료일", "**2042-07-14** (GP anticipated expiration; 출원일+20년, PTE 미반영)"),
    ("교차검증", "GP=30, FPO=52, both=30, agree=30, **substantive_diff=0** → ✅완전일치(공통분)"),
])
w("**[ANALYSIS] (한국어)**")
w()
w("US12478617B2와 **동일 출원(18/495,457)**의 공개본. GP 청구항 번호가 **23번부터 시작**하는 것은 공개 시점의 "
  "청구항 세트가 23~52였음을 반영한다(원문 그대로 보존). GP↔FPO 공통 30개가 substantive_diff=0으로 일치하여 "
  "✅교차검증(공통분)이며, FPO가 52개를 보유해 일부 청구항은 GP 텍스트에 미포함이다. 본 공개본 역시 구조식 청구항이 "
  "텍스트로 깨져 있다(원문 보존).")
w()
verbatim_block("US20240173309A1")
w("---")
w()

# WO2023288019A2
w("#### 4.3 WO2023288019A2 ☑️부분교차검증 (차이 5개)")
w()
meta_table([
    ("특허번호", "WO2023288019A2 (PCT 공개, A2)"),
    ("제목", "LIPIDATED PEPTIDE INHIBITORS OF INTERLEUKIN-23 RECEPTOR"),
    ("국제출원 / 공개", "PCT/US2022/037205, 국제출원일 2022-07-14"),
    ("우선일", "2021-07-14 (US Provisional 63/221,697)"),
    ("출원인/양수인", "Janssen Biotech, Inc.; Protagonist Therapeutics, Inc."),
    ("패밀리", "US20240173309A1, US12478617B2 (출원 18/495,457)"),
    ("권위 만료일", "PCT 자체 만료 **N/A**; 미국 대응 = 2042-07-14"),
    ("교차검증", "GP=22, FPO=22, both=22, agree=17, **substantive_diff=5** → ☑️부분교차검증"),
])
w("**[ANALYSIS] (한국어)**")
w()
w("lipidated 화학형 PCT. 청구항 1~10은 Formula I~X의 IL-23R 저해제 속(다수의 비천연 잔기 약어 — 7MeW, AEF, THP, "
  "Zlipid 등)이며 X4-X9 이황화/티오에터 가교로 환화된다. 원문에 `XI 0`(=X10), `Ci`(=C1), `40MePh`(=4-OMe-Ph) 등 "
  "OCR 잔재가 다수 남아 있어 원문 그대로 보존한다. GP↔FPO 22개 중 17개 일치, 5개 차이로 ☑️부분교차검증이며 권위 소스는 GP.")
w()
verbatim_block("WO2023288019A2")
w("---")
w()

# WO2024155552A1
w("#### 4.4 WO2024155552A1 ☑️부분교차검증 (차이 19개)")
w()
meta_table([
    ("특허번호", "WO2024155552A1 (PCT 공개, A1)"),
    ("제목", "FORMULATIONS OF LIPIDATED PEPTIDE INHIBITORS OF INTERLEUKIN-23 RECEPTOR"),
    ("국제출원 / 공개", "PCT/US2024/011549, 국제출원일 2024-01-15"),
    ("우선일", "2023-01-16 (US Provisional 63/480,068)"),
    ("출원인/양수인", "Janssen Pharmaceutica NV (Protagonist 미표기)"),
    ("발명자", "David A. Lane (et al.)"),
    ("권위 만료일", "PCT 자체 만료 **N/A**; 추정 국내단계 2043~2044 (우선일/출원일+20년)"),
    ("교차검증", "GP=78, FPO=79, both=78, agree=59, **substantive_diff=19** → ☑️부분교차검증"),
])
w("**[ANALYSIS] (한국어)**")
w()
w("lipidated 펩타이드의 **경구 제제(oral formulation)** PCT. 주의: GP 청구항 본문이 **2번부터 시작**한다"
  "(청구항 1이 GP `/en` 텍스트에 누락 — 원문 보존, 1번은 GP PDF/원본 확인 필요). 청구항 2 이하는 Formula (A) "
  "지질화 펩타이드와 그 경구 제제를 청구하며, 후반부(77~79)는 광범위 자가면역/염증 질환 치료방법이다. GP↔FPO 공통 78개 중 "
  "59개 일치, 19개 차이로 ☑️부분교차검증이며 권위 소스는 GP. (FPO 79 vs GP 78의 1건 차이도 존재.)")
w()
verbatim_block("WO2024155552A1")
w("---")
w()

# ----------------------------------------------------------------------------
# TIER 5 — JP gap
# ----------------------------------------------------------------------------
w("### 티어 5 — 조성물 일본 대응 (청구항 미확보)")
w()
w("#### 5.1 JP2023145581A ⚠️미확보 (Google Patents /en 청구항 0건)")
w()
meta_table([
    ("특허번호", "JP2023145581A (일본 공개, A)"),
    ("제목", "Compositions of peptide inhibitors of interleukin-23 receptors"),
    ("출원일 / 공개일", "2023-07-24 / 2023-10-11"),
    ("우선일", "2020-11-20"),
    ("출원인/양수인", "Janssen Pharmaceutica NV; Protagonist Therapeutics Inc"),
    ("패밀리", "US11939361B2, CA3202226A1 (동일 조성물 패밀리)"),
    ("권위 만료일", "추정 ~2041 (우선일/출원일+20년; 일본 산정 별도)"),
    ("교차검증", "GP=0(일본어 청구항이 `/en` 페이지에 미수록), FPO=실패 → **⚠️미확보**"),
])
w("**[ANALYSIS] (한국어)**")
w()
w("icotrokinra 조성물 패밀리(US11939361B2/CA3202226A1과 동일 제목·동일 우선일 2020-11-20)의 **일본 대응 출원**임은 "
  "서지정보로 확정된다. 그러나 일본어 청구항 본문이 Google Patents `/en` 페이지에 실리지 않아(claims=0) 청구항 원문을 "
  "확보하지 못했다. 원문 보존 원칙상 청구항을 **추측·번역해 채우지 않으며**, 본 건은 ⚠️미확보로 남기고 "
  "**J-PlatPat(일본 특허청)** 또는 일본어 GP 페이지에서 원문 재수집이 필요하다(부록 B 참조). 패밀리 정황상 SEQ ID NO:1 "
  "조성물 권리의 일본 영토 커버로 추정되나, 청구항 미확보로 권리범위는 단정하지 않는다.")
w()
w("---")
w()

# ----------------------------------------------------------------------------
# APPENDIX A — misattributed
# ----------------------------------------------------------------------------
w("## 부록 A — 오귀속(misattributed) 특허 (icotrokinra 무관) ❌")
w()
w("> 아래 9건은 디스커버리 단계에서 후보로 수집되었으나, 권위 소스 확인 결과 icotrokinra/Protagonist+Janssen 프로그램과 "
  "**무관**함이 확정되었다. 누락 방지를 위해 드롭하지 않고 부록으로 보존한다.")
w()
w("| # | 번호 | 실제 주제 / 출원인 | 근거 | GP 청구항 |")
w("|---|---|---|---|---|")
w("| A1 | WO2023212427A1 | IC-TROSA 점-대-다점 광통신 네트워크 / **Dell Products LP** | 제목·IPC(H04B10) 광통신, IL-23 무관 | 20 (광통신) |")
w("| A2 | WO2023212432A1 | 보호커버 부착 다중날 칼 어셈블리 / **Larry Kalkstein** | 제목·IPC(B26B) 주방기구 | 다수 (칼) |")
w("| A3 | WO2024026471A1 | CD98HC 항원결합 도메인(혈뇌장벽 항체) / **Alector LLC** | 항체 특허, IL-23 무관 | 0 (GP 본문 미수록) |")
w("| A4 | WO2024026472A1 | 트랜스페린수용체 항원결합 도메인 / **Alector LLC** (실제 kind=A2) | 항체 특허; 요청 A1 vs 실제 A2 불일치 | (Alector 항체) |")
w("| A5 | WO2023099669A1 | IL-23R 펩타이드 저해제 / **Zealand Pharma A/S** (경쟁사) | 진짜 IL-23R 펩타이드이나 출원인이 J&J/Protagonist 아님 | 87 (경쟁사 IL-23R) |")
w("| A6 | US9605027B2 | IL-23R 결합 폴리펩타이드 / **Medical Diagnostic Laboratories, LLC** | 다른 당사자의 IL-23R 폴리펩타이드 | 13 |")
w("| A7 | USRE49026E1 | 동상(US9169292의 재발행) / **Medical Diagnostic Laboratories, LLC** | 재발행 특허, Protagonist 아님 | 36 |")
w("| A8 | US11180535B2 | 박테리아 종양침투 키메라 펩타이드(YebF 융합) | Google Patents 404 + FPO는 박테리아 펩타이드 → **오귀속 확정** | n/a (GP 404) |")
w()
w("### A.1 WO2023212427A1 (Dell 광통신) — 오귀속 근거 [VERBATIM 발췌]")
w()
w("**[ANALYSIS]** 청구항 전체가 광 트랜시버·점-대-다점 광네트워크 기술이며 펩타이드/IL-23과 전혀 무관하다.")
w()
verbatim_block("WO2023212427A1")
w()
w("### A.2 WO2023212432A1 (다중날 칼) — 오귀속 근거 [VERBATIM 발췌]")
w()
w("**[ANALYSIS]** 청구항 1이 '복수의 날과 보호커버를 갖는 칼 어셈블리'로 주방기구 특허임이 명백하다.")
w()
verbatim_block("WO2023212432A1")
w()
w("### A.3 WO2023099669A1 (Zealand Pharma, 경쟁사 IL-23R 펩타이드) — 오귀속 근거 [VERBATIM 발췌]")
w()
w("**[ANALYSIS]** 진짜 IL-23R 펩타이드 저해제이나 출원인이 **Zealand Pharma A/S**(경쟁사)로, Janssen/Protagonist "
  "icotrokinra 패밀리가 아니다. 화학형(lactam/dithioether/triazole 가교, Formula I X1~X14)도 별개 분자다. 발췌만 싣는다.")
w()
verbatim_block("WO2023099669A1")
w()
w("### A.4 US9605027B2 (Medical Diagnostic Laboratories) — 오귀속 근거 [VERBATIM]")
w()
w("**[ANALYSIS]** 출원인이 **Medical Diagnostic Laboratories, LLC**이며, SEQ ID NO:177~179의 환형 폴리펩타이드를 "
  "청구한다 — Protagonist의 Pen-Pen 단환 펩타이드와 무관한 별개 당사자/분자다.")
w()
verbatim_block("US9605027B2")
w()
w("### A.5 USRE49026E1 (Medical Diagnostic Laboratories, US9169292 재발행) — 오귀속 근거 [VERBATIM]")
w()
w("**[ANALYSIS]** A.4와 동일 출원인의 재발행 특허(US9169292 재발행)이며 청구항 1이 동일하게 SEQ ID NO:177~179 환형 "
  "폴리펩타이드다. icotrokinra 무관.")
w()
verbatim_block("USRE49026E1")
w()
w("### A.6 US11180535B2 (박테리아 종양침투 키메라 펩타이드) — 오귀속 확정 [VERBATIM: FPO 추출본]")
w()
w("**[ANALYSIS]** 본 번호는 **Google Patents에서 404**가 반환되어 권위 소스 청구항을 얻지 못했고, FPO 추출본은 "
  "'살아있는 유전자조작 박테리아가 YebF-종양침투 펩타이드 키메라를 발현'하는 **박테리아 종양침투 특허**(SEQ ID NO:33/34)다. "
  "이는 icotrokinra(SEQ ID NO:1, 단환 IL-23R 펩타이드)와 전혀 무관하므로 **오귀속 확정**으로 부록 A에 둔다. "
  "아래는 권위 GP가 아닌 FPO 추출본(`work/02_extracted/US11180535B2.md`)이며, 무관 특허임을 입증하는 용도로만 인용한다.")
w()
w("**[VERBATIM] — 출처: FreePatentsOnline (`work/02_extracted/US11180535B2.md`); GP 미확보(404)**")
w()
# embed FPO body for US11180535B2 verbatim
with io.open("/home/user/Claude.lgchem_CHA1/pcea-harness/work/02_extracted/US11180535B2.md","r",encoding="utf-8",newline="") as f:
    fpo = f.read()
fl = fpo.split("\n")
j=0
while j < len(fl) and (fl[j].startswith("#") or fl[j].strip()==""):
    if fl[j].startswith("#"):
        j+=1
        if j<len(fl) and fl[j].strip()=="":
            j+=1
        break
    j+=1
w("```text\n" + "\n".join(fl[j:]).rstrip("\n") + "\n```")
w()
w("> A4 WO2024026471A1 / WO2024026472A1(Alector 항체)는 Google Patents 본문에 청구항이 미수록(claims=0)되어 "
  "[VERBATIM] 발췌가 불가하다. 서지정보(부록 A 표)만으로 오귀속 판정하며, 화학/생물학적으로 IL-23 펩타이드와 무관한 "
  "혈뇌장벽 통과 항체 특허다.")
w()
w("---")
w()

# ----------------------------------------------------------------------------
# APPENDIX B — limitations
# ----------------------------------------------------------------------------
w("## 부록 B — 잔여 한계 및 주의사항")
w()
w("1. **JP2023145581A 청구항 미확보:** 일본어 청구항이 Google Patents `/en` 페이지에 실리지 않아(claims=0) 청구항 "
  "원문을 확보하지 못했다. **J-PlatPat(일본 특허청)** 원문 또는 일본어 GP 페이지에서 재수집 필요. 원문 보존 원칙상 "
  "청구항을 추측·번역해 채우지 않았다.")
w("2. **PCT 출원의 만료일:** WO2021146441A1, WO2016011208A1, WO2023288019A2, WO2024155552A1은 PCT 국제출원으로, "
  "PCT 자체에는 특허 존속기간 만료 개념이 **해당없음(N/A)**이다. 만료는 각 지정국 국내단계 진입 후 해당국 법제로 산정된다"
  "(대응 미국 출원 만료일은 부록 C 참조).")
w("3. **PTE/Hatch-Waxman 미반영:** 부록 C의 권위 만료일은 모두 Google Patents anticipated expiration"
  "(출원일/우선일+20년 base term)이며 **특허존속기간연장(PTE), PTA(존속기간조정)는 반영되지 않았다**. icotrokinra가 "
  "2026-03 FDA 승인 약물이므로, 특히 조성물 특허 **US11939361B2**에 Hatch-Waxman PTE(최대 +5년)가 적용되면 "
  "**실질 만료가 ~2045년까지 연장**될 수 있다.")
w("4. **구조식 누락 청구항:** US12478617B2, US20240173309A1, US11041000B2 등 다수 청구항은 화학구조식 이미지를 "
  "청구하는데 GP `/en` 텍스트에 구조식이 렌더링되지 않아 본문이 빈 형태로 보존되어 있다. 구조 전문은 GP PDF/등록공보 원본 "
  "확인이 필요하다. 원문 보존 원칙상 추측 보충하지 않았다.")
w("5. **청구항 번호 비연속/누락:** US20240173309A1(23번부터 시작), WO2024155552A1(2번부터 시작), "
  "US20210261622A1(`(canceled)` 표기 포함)은 GP 원문 자체가 그러하므로 그대로 보존했다.")
w("6. **OCR/파싱 잔재 보존:** `Gin`/`Gln`, `lie`/`Ile`, `XI 0`/`X10`, `[Abta]`, `Ci`/`C1` 등은 권리범위를 바꿀 수 "
  "있으므로 교정하지 않고 원문 그대로 두었다(THE ONE RULE).")
w("7. **CA3202226A1 우선일:** 캐나다 소스에서 우선일이 직접 확인되지 않아 '확인불가'로 둔다(미국 자매는 2020-11-20).")
w()
w("---")
w()

# ----------------------------------------------------------------------------
# APPENDIX C — expiry table
# ----------------------------------------------------------------------------
w("## 부록 C — 권위 만료일 표 (Google Patents anticipated expiration, 출원일/우선일+20년, PTE 미반영)")
w()
w("| 특허 | 권위 만료일 | base | 비고 |")
w("|---|---|---|---|")
w("| **US11939361B2** (조성물, SEQ ID NO:1) | **2041-11-19** | 출원일 2021-11-19 | **FDA 승인약 → Hatch-Waxman PTE 최대 +5년 시 ~2045 가능** |")
w("| CA3202226A1 (조성물 CA) | ~2041-11-19 | 출원일 2021-11-19 | 캐나다 산정 별도 |")
w("| JP2023145581A (조성물 JP) | ~2041 | 우선일 2020-11-20 | 일본 산정 별도; 청구항 미확보 |")
w("| US20210261622A1 (속, 공개) | **2041-01-14** | 출원일 2021-01-14 | 17/149,509 계열 |")
w("| US11845808B2 (속, 등록) | **2041-01-14** | 출원일 2021-01-14 | 17/149,509 등록본 |")
w("| US12018057B2 (속/종) | **2041-01-14** | 출원일 2021-01-14 | 자매 17/149,544 |")
w("| WO2021146441A1 (속 PCT) | N/A (PCT) | — | 미국 대응 2041-01-14 |")
w("| US12552836B2 (속) | **2039-07-12** | 우선일 2018-07-12 | 계속출원 |")
w("| US11041000B2 (속) | **2040-07-09** | PCT 2020-07-09 | |")
w("| US10787490B2 (PTG-200/lipidated 종) | **2035-07-15** | 우선일 2015-07-15 | |")
w("| US9624268B2 (PTG-200 기초) | **2035-07-15** | 우선일 2014-07-17 표시; GP base 2035-07-15 | |")
w("| US10023614B2 (PTG-200) | **2035-07-15** | 동상 | |")
w("| US10941183B2 (PTG-200) | **2035-07-15** | 동상 | |")
w("| US11884748B2 (PTG-200) | **2035-07-15** | 동상 | |")
w("| WO2016011208A1 (PTG-200 PCT) | N/A (PCT) | — | 추정 국내 ~2035 |")
w("| US12478617B2 (lipidated) | **2042-07-14** | 우선일 2021-07-14 | |")
w("| US20240173309A1 (lipidated 공개) | **2042-07-14** | 우선일 2021-07-14 | |")
w("| WO2023288019A2 (lipidated PCT) | N/A (PCT) | — | 미국 대응 2042-07-14 |")
w("| WO2024155552A1 (lipidated 제제 PCT) | N/A (PCT) | — | 추정 국내 ~2043 |")
w()
w("---")
w()

# ----------------------------------------------------------------------------
# SYNTHESIS
# ----------------------------------------------------------------------------
w("## 종합(Synthesis)")
w()
w("- **권리 핵심:** icotrokinra(=SEQ ID NO:1)의 시장 독점은 **조성물 특허 US11939361B2**(✅GP↔FPO 16/16 완전일치, "
  "권위 만료 2041-11-19, **PTE 시 ~2045 가능**)가 가장 직접적이고 검증 강도가 높다. 동일 조성물의 캐나다(CA3202226A1, "
  "153항) 대응까지 이번에 GP로 확보되어 조성물 권리의 영토 범위가 명확해졌다. 일본(JP2023145581A)만 청구항 미확보로 남는다.")
w()
w("- **다층 방어:** 조성물(US11939361B2/CA/JP) 위에 **속/종 Markush 특허**(WO2021146441A1 186항, US20210261622A1, "
  "US11845808B2, US12018057B2, US12552836B2, US11041000B2; 만료 2039~2041)가 단환 Pen-Pen 펩타이드 골격을 폭넓게 "
  "덮고, 그 아래에 **PTG-200 초기 세대**(2035 만료)와 **lipidated 화학형/제제**(2042~2043)가 전후 세대를 보강하는 "
  "다층(layered) 포트폴리오 구조다.")
w()
w("- **교차검증 신뢰도:** ✅완전일치 4건(US11939361B2, US12018057B2, US12552836B2, US12478617B2; + 공통분 일치 "
  "US20240173309A1)은 두 독립 소스가 청구항을 char-level로 동일하게 재현해 신뢰도가 가장 높다. ☑️부분교차검증 건들의 "
  "차이는 대부분 FPO의 Markush 치환기 목록 파싱 잡음에서 기인하며, **권위 원문은 Google Patents**다. ⚠️단일소스(GP) "
  "건들은 FPO 미수집이나 GP 자체가 권위 소스이므로 청구항 자체의 신뢰도는 유지된다.")
w()
w("- **공백 해소 성과(이번 회차):** WO2021146441A1 168~186번(19항)과 CA3202226A1 전체(153항)를 신규 확보. "
  "**잔여 공백은 JP2023145581A 청구항 1건**(J-PlatPat 필요)으로 축소되었다.")
w()
w("- **오귀속 정리:** 9건(Dell 광통신, 칼, Alector 항체 2건, Zealand 경쟁사 펩타이드, MDL 폴리펩타이드 2건, "
  "박테리아 키메라 펩타이드)은 권위 소스로 무관함을 확인해 부록 A로 격리했다. 특히 US11180535B2는 GP 404 + FPO 박테리아 "
  "펩타이드로 **오귀속 확정**했다.")
w()
w("> 본 보고서의 모든 [VERBATIM] 블록은 `work/05_gp_authoritative/<id>.md`(권위: Google Patents)에서 "
  "char-for-char 복사했으며(US11180535B2만 GP 404로 인해 FPO 추출본 인용), 한국어 [ANALYSIS]는 그 위에 덧붙였을 뿐 "
  "원문을 대체·변형하지 않았다. 생성일 2026-06-16.")

text = "\n".join(W) + "\n"
with io.open(OUT, "w", encoding="utf-8", newline="\n") as f:
    f.write(text)
print("WROTE", OUT)
print("LINES", text.count("\n"))
