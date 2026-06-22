# Trans-splicing 기반 Exon Editor — 청구항 범위 비교 분석
## (Ascidian vs ViGeneron vs SpliceBio)

| 항목 | 값 |
|---|---|
| 분석 범위 | **RNA trans-splicing 기반 exon editor에 한정** (요청 스코프) |
| 핵심 질문 | (1) Ascidian이 "novel exon editor molecules"를 청구항에서 어디까지 일반화하는가 (2) ViGeneron·SpliceBio와 청구항이 어디서 겹치고 갈리는가 |
| 대상 3사 | Ascidian Therapeutics(주), ViGeneron/VeonGen, SpliceBio(비교군) |
| 소스 | Google Patents 청구항 원문(verbatim, 결정론적 파싱) — 번역·교정 없음 |
| 생성일 | 2026-06-16 |
| 한계 | WO2023220742A3(Ascidian ABCA4/Stargardt)는 Google 503으로 미확보(부록); ViGeneron PCT WO 번호 미확정; SpliceBio WO2021191447A1은 GP에서 독립항 claim 1 미파싱(US20230116688A1로 대체 확인) |

---
## Executive Summary — 한눈에

- **Ascidian의 일반화 수준:** Ascidian은 **exon-editor 분자의 "아키텍처"를 일반화**하되, **청구항은 항상 표적 유전자·인트론에 고정**한다. 즉 모든 독립 조성물 청구항이 *(a) 표적 인트론에 결합하는 binding domain + (b) splicing domain(또는 artificial intron) + (c) 기능성 exon을 담은 coding domain* 의 **삼분(三分) 구조**를 반복하지만, **유전자-비특이적(gene-agnostic) '임의의 exon editor 분자' 청구항은 존재하지 않는다**. 공개출원 US20210155938A1은 이 아키텍처를 **ABCA4(인트론 19/22/23/24)와 CEP290(인트론 26~30)** 두 유전자에 걸쳐 청구하고, 등록특허(US11993776B2·US12442003B2)는 **ABCA4 인트론 22로 더 좁혀** 등록됐으며, HTT는 **별도 패밀리(WO2024173719A1)**로 같은 아키텍처를 확장한다.
- **겹침(overlap):** **Ascidian ↔ ViGeneron**은 동일 메커니즘(RNA pre-mRNA trans-splicing)으로, 둘 다 *binding domain + 스플라이싱 요소 + payload(exon/관심서열)* 를 갖는 **"(pre-mRNA) trans-splicing molecule" 속(genus)** 을 청구한다 → **개념적 권리범위가 겹치는 영역이 실재**한다.
- **갈림(divergence):** 두 회사는 **서로 다른 한정 축**으로 권리를 그었다 — **Ascidian = 표적 유전자/인트론·기능성 exon** 으로 한정, **ViGeneron = 엔지니어링된 acceptor splice region 서열**(SEQ ID NO:3/4, 피리미딘 트랙 TTTTTT/TCTTTT, CAGG acceptor)로 한정하되 **payload는 유전자-비특이적**. 따라서 정면 충돌은 *"ABCA4 표적 + ViGeneron 특정 acceptor 서열"* 이 동시에 성립하는 좁은 교집합에서만 발생한다.
- **SpliceBio는 메커니즘이 다르다:** split-intein **단백질** trans-splicing(인테인 매개)으로, 청구 대상이 **인테인-융합 단백질을 코딩하는 폴리뉴클레오타이드**다. RNA trans-splicing exon editor와 **청구항 차원에서는 거의 겹치지 않으며**, 겹치는 지점은 오직 **치료 전략 수준**(대형 유전자 ABCA4를 dual-AAV로 전달해 Stargardt 치료)뿐이다.

---
## 제1장. Ascidian Therapeutics (주 타깃) — RNA trans-splicing exon editor

### 1.1 "exon editor molecule" 일반화 수준 — 결론
Ascidian의 독립항을 전수 확인한 결과, **일반화는 '플랫폼 아키텍처' 수준에서만** 이뤄지고 **권리 외연은 표적 유전자에 묶여 있다**:

| 일반화된 요소(아키텍처) | 청구항에서 고정된 요소(한정) |
|---|---|
| 삼분 구조: binding domain + splicing domain + coding domain(기능성 exon) | **표적 유전자/인트론**(ABCA4 19·22·23·24, CEP290 26~30, HTT 1~3) |
| 양방향 모두 청구(3′→5′ 및 5′→3′) | 인트론 내 **구체적 binding-site 뉴클레오타이드 범위**(SEQ ID NO:28/29/32 기준) |
| "functional exon(s)" 로 exon을 포괄 표현 | 교체 대상 **구체적 exon 범위**(예: exons 1-22, 23-50, CEP290 exons 2-26) |
| 다(多)유전자로 확장(공개출원에 ABCA4+CEP290; 별도 패밀리에 HTT) | **유전자-비특이적 '임의의 trans-splicing exon editor' 독립항은 없음** |

즉 *"novel exon editor molecules"* 라는 표현의 외연은 **표적 유전자별 청구항의 합집합**으로 구현되며, ViGeneron식의 '유전자 불문 + 스플라이싱 모듈 서열' 같은 **단일 포괄 청구항 형태는 채택(또는 확보)되지 않았다**. 이는 권리 일반화 폭은 좁지만(설계적 회피가 상대적으로 쉬움), 표적 유전자(특히 ABCA4)에 대해서는 **양방향·다수 binding-site·exon 범위까지 촘촘히** 둘러친 형태다.

### 1.2 공개출원 US20210155938A1 — 다유전자 genus (ABCA4 + CEP290)
독립항: 1, 28, 30, 42–47(ABCA4), 66–67(CEP290) 등 11개. 대표 독립항:

**[VERBATIM] US20210155938A1 (claims 1=ABCA4, 66=CEP290) — 출처: Google Patents (`runs/exon_editor_trans_splicing/05_gp_authoritative/US20210155938A1.md`)**

```text
1. A nucleic acid trans-splicing molecule comprising, operatively linked in either a 3′-to-5′ direction or a 5′-to-3′ direction: (a) a binding domain configured to bind a target ABCA4 intron selected from the group consisting of introns 19, 23, or 24; (b) a splicing domain configured to mediate trans-splicing; and (c) a coding domain comprising a functional ABCA4 exon; wherein the nucleic acid trans-splicing molecule is configured to trans-splice the coding domain to an endogenous ABCA4 exon adjacent to the target ABCA4 intron, thereby replacing the endogenous ABCA4 exon with the functional ABCA4 exon and correcting a mutation in ABCA4.

66. A nucleic acid trans-splicing molecule comprising, operatively linked in a 3′-to-5′ direction: (a) a binding domain configured to bind CEP290 intron 26 at a binding site comprising any one or more of nucleotides 4,800 to 5,838 of SEQ ID NO: 32; (b) a splicing domain configured to mediate trans-splicing; and (c) a coding domain comprising functional CEP290 exons 2-26; wherein the nucleic acid trans-splicing molecule is configured to trans-splice the coding domain to endogenous CEP290 exon 27, thereby replacing endogenous CEP290 exons 2-26 with the functional CEP290 exons 2-26 and correcting a pathogenic point mutation.

```

**[ANALYSIS]** 청구항 1은 ABCA4 인트론 19/23/24를 표적하며 **양방향(3′→5′ 및 5′→3′)** 을 모두 포섭하는, 본 패밀리에서 **가장 넓은 독립항**이다. 그러나 여전히 *ABCA4* 에 고정된다. 청구항 66/67은 동일 아키텍처를 **CEP290**(LCA10)으로 옮긴 것으로, *플랫폼을 다유전자로 일반화하되 청구항 단위로는 유전자-특이* 라는 전략을 그대로 보여준다.

### 1.3 등록특허 — ABCA4 인트론 22로 좁혀 등록 (양방향 각각)
**[VERBATIM] US11993776B2 (등록, 3′→5′, exons 1-22) — 출처: Google Patents (`runs/exon_editor_trans_splicing/05_gp_authoritative/US11993776B2.md`)**

```text
1. A nucleic acid trans-splicing molecule comprising, operatively linked in a 3′-to-5′ direction: (a) a binding domain, wherein the binding domain comprises a sequence ranging from 50-300 nucleotides in length and is configured to bind ABCA4 intron 22 at a binding site within nucleotides 880 to 1,350 of SEQ ID NO: 28; (b) a splicing domain configured to mediate trans-splicing; and (c) a coding domain comprising functional ABCA4 exons 1-22; wherein the nucleic acid trans-splicing molecule is configured to trans-splice the coding domain to endogenous ABCA4 exon 23, thereby replacing endogenous ABCA4 exons 1-22 with the functional ABCA4 exons 1-22.

```

**[VERBATIM] US12442003B2 (등록, 5′→3′, exons 23-50) — 출처: Google Patents (`runs/exon_editor_trans_splicing/05_gp_authoritative/US12442003B2.md`)**

```text
1. A nucleic acid trans-splicing molecule comprising, operatively linked in a 5′-to-3′ direction: (a) a binding domain, wherein the binding domain comprises a sequence ranging from 50-300 nucleotides in length and is configured to bind ABCA4 intron 22 at a binding site within nucleotides 60 to 570, 600 to 800, or 900 to 1,350 of SEQ ID NO: 28; (b) a splicing domain configured to mediate trans-splicing; and (c) a coding domain comprising functional ABCA4 exons 23-50; wherein the nucleic acid trans-splicing molecule is configured to trans-splice the coding domain to endogenous ABCA4 exon 22, thereby replacing endogenous ABCA4 exons 23-50 with the functional ABCA4 exons 23-50.

```

**[ANALYSIS]** 등록 단계에서 권리는 **ABCA4 인트론 22 결합 + 50~300nt binding domain + 구체적 binding-site 범위(SEQ ID NO:28의 특정 뉴클레오타이드) + 기능성 exon 1-22(3′→5′) 또는 23-50(5′→3′)** 으로 좁혀졌다. 공개출원의 '인트론 19/23/24·양방향 단일항'이 심사를 거치며 **인트론 22 중심·방향별 분리·binding-site 한정**으로 구체화된 것 — 전형적 '넓은 출원 → 좁은 등록' 패턴이며, **ACDN-01(Stargardt) 제품에 정조준**된 청구다.

### 1.4 별도 패밀리로 유전자 확장 — HTT (Huntington)
**[VERBATIM] WO2024173719A1 (HTT, 독립항 다수) — 출처: Google Patents (`runs/exon_editor_trans_splicing/05_gp_authoritative/WO2024173719A1.md`)**

```text
1. An HTT nucleic acid trans-splicing molecule comprising: (a) a coding domain comprising HTT exon 1 and HTT exon 2; (b) a splicing domain; and (c) a binding domain that binds a target intron of an HTT pre-mRNA, wherein the target intron comprises intron 2.

3. An HTT nucleic acid trans-splicing molecule comprising: (a) a coding domain comprising HTT exons 1-3; (b) a splicing domain; and (c) a binding domain that binds a target intron of an HTT pre-mRNA, wherein the target intron comprises intron 3.

```

**[ANALYSIS]** HTT 패밀리(독립항 22개: 1,3,5,6,…)는 동일 삼분 아키텍처를 **HTT 인트론 1/2/3 + HTT exon 1~3 coding domain** 으로 옮긴 것. *아키텍처 재사용·유전자별 신규 패밀리* 라는 Ascidian의 일반화 방식을 재확인한다(헌팅턴병으로 적응증 확장).

---
## 제2장. ViGeneron / VeonGen — REVeRT (RNA pre-mRNA trans-splicing)

**[VERBATIM] US12502438B2 (등록) — 출처: Google Patents (`runs/exon_editor_trans_splicing/05_gp_authoritative/US12502438B2.md`)**

```text
1. A pre-mRNA trans-splicing molecule comprising, (i) an acceptor splice region, comprising a sequence of at least 80% sequence identity to SEQ ID NO: 3 or SEQ ID NO: 4, further comprising (ia) a pyrimidine tract, wherein the pyrimidine tract comprises (iaa) 5 to 25 nucleotides; (iab) wherein at least 60% of the nucleotides within these 5 to 25 nucleotides are cytosine (C), thymine (T) and/or uracil (U); (iac) wherein the 5 to 25 nucleotides of the pyrimidine tract comprise the sequence TTTTTT or TCTTTT; and (ib) an acceptor splice site, (iba) wherein the acceptor splice site is located 3′ to the pyrimidine tract; and (ibb) wherein the acceptor splice site comprises from 5′ to 3′ a sequence of CAGG; (ii) a nucleotide sequence of interest or a portion thereof, wherein the acceptor splice region is localized 3′ or 5′ to the nucleotide sequence of interest or the portion thereof; (iii) a binding domain targeting pre-mRNA, which is localized 3′ or 5′ to the nucleotide sequence of interest or the portion thereof, and (iv) optionally a spacer sequence, wherein the spacer sequence is localized between the binding domain and the acceptor splice region.

12. An adeno-associated virus (AAV) vector comprising at least two inverted terminal repeats comprising a nucleic acid sequence between these two inverted terminal repeats, wherein said nucleic acid sequence comprises from 5′ to 3′ (i) a promoter; (ii) a binding domain; (iii) optionally a spacer sequence; (iv) an acceptor splice region sequence comprising a sequence of at least 80% sequence identity to SEQ ID NO: 3 or SEQ ID NO: 4, further comprising (a) a pyrimidine tract, wherein the pyrimidine tract comprises (aa) 5 to 25 nucleotides; (ab) wherein at least 60% of the nucleotides within these 5 to 25 nucleotides are cytosine (C), thymine (T) and/or uracil (U); (ac) wherein the 5 to 25 nucleotides of the pyrimidine tract comprise the sequence TTTTTT or TCTTTT; and (b) an acceptor splice site, ba) wherein the acceptor splice site is located 3′ to the pyrimidine tract; and bb) wherein the acceptor splice site comprises from 5′ to 3′ a sequence of CAGG; (v) a nucleotide sequence of interest or a portion thereof, and (vi) optionally a poly A sequence.

```

**[ANALYSIS] — 일반화 축이 Ascidian과 다르다.** ViGeneron의 독립항 1은 *(i) acceptor splice region(SEQ ID NO:3/4와 ≥80% 동일, 피리미딘 트랙 5~25nt·≥60% C/T/U·TTTTTT 또는 TCTTTT, CAGG acceptor) + (ii) 임의의 nucleotide sequence of interest + (iii) binding domain* 으로 정의되는 **pre-mRNA trans-splicing molecule** 이다. 결정적으로 **payload(관심서열)는 유전자-비특이**이고, **한정의 핵심은 '엔지니어링된 acceptor splice 모듈 서열'** 이다. AAV 벡터 독립항(claim 12)으로 dual-AAV 전달까지 포섭. 즉 ViGeneron은 *어느 유전자든* 자사 최적화 splice 모듈을 쓰면 걸리도록 **유전자 축으로는 넓게, 스플라이싱-서열 축으로는 좁게** 권리를 그었다.

---
## 제3장. SpliceBio (비교군) — split-intein **단백질** trans-splicing

**[VERBATIM] US20230116688A1 (SpliceBio) — 출처: Google Patents (`runs/exon_editor_trans_splicing/05_gp_authoritative/US20230116688A1.md`)**

```text
1. A composition comprising a. a first polynucleotide encoding a polypeptide comprising a Split intein N-fragment, wherein the Split intein N-fragment is selected from the list consisting of the CfaN of SEQ ID NO 27, the CatN of SEQ ID NO 30 and the Gp41N of SEQ ID NO 38, or any functionally equivalent variants thereof such as ConN of SEQ ID NO 39, directly linked via a peptide bond, optionally through a peptide linker, to the N-terminal fragment of a protein to be reconstituted; and b. a second polynucleotide encoding a polypeptide comprising a Split intein C-fragment, wherein the Split intein C-fragment is selected from the list consisting of the CfaC of SEQ ID NO 28, the CatC of SEQ ID NO 31 and the Gp41C of SEQ ID NO 104, or any functionally equivalent variants thereof such as CfaCmut (SEQ ID NO 29) or ConC (SEQ ID NO 105), directly linked via a peptide bond, optionally through a peptide linker, to the C-terminal fragment of the protein to be reconstituted; wherein both polynucleotides of the composition may be packed together in a single formulation or separately in different formulations; wherein the first and the second polynucleotides, respectively, encode the N-terminal fragment and the C-terminal fragment of the protein to be reconstituted, in such a way that when both fragments are combined, the N-terminal fragment of the protein is linked to the C-terminal fragment of the protein generating the whole protein; wherein the protein to be reconstituted is of more than 25 KDa; and wherein the composition is further characterized in that: the split intein N-fragment is further directly linked via a peptide bond to a degron, wherein the degron is linked to the intein N-fragment via the C-terminus of the intein, with or without a linker between the intein N-fragment and the degron, and wherein the N-terminus of the Split intein N-fragment is directly linked via a peptide bond to the N-terminal fragment of the protein to be reconstituted; and/or the split intein C-fragment is further directly linked via a peptide bond to a degron, wherein the degron is linked to the intein C-fragment via the N-terminus of the intein, with or without a linker between the intein C-fragment and the degron, and wherein the C-terminus of the Split intein C-fragment is directly linked via a peptide bond to the C-terminal fragment of the protein to be reconstituted

```

**[ANALYSIS] — 메커니즘이 다르다(스코프 주의).** SpliceBio 독립항 1은 *split-intein N-fragment(CfaN/CatN/Gp41N…)와 C-fragment(CfaC/CatC/Gp41C…)를 각각 단백질 단편에 융합해 코딩하는 두 폴리뉴클레오타이드의 조성물* 이다. 작동은 **단백질 수준(인테인 매개 protein trans-splicing)** 으로, **RNA exon editor 분자(trans-splicing RNA molecule) 자체를 청구하지 않는다.** 한정의 핵심은 **특정 split intein(Cfa/Cat/Gp41)** 이다. 본 분석의 trans-splicing exon-editor 스코프와는 **청구 대상(statutory subject)이 다른** 인접 기술이다.

---
## 제4장. 청구항 Overlap / Divergence 비교 (핵심)

### 4.1 한 장 비교표
| 비교 축 | **Ascidian** | **ViGeneron** | **SpliceBio** |
|---|---|---|---|
| 메커니즘 | RNA trans-splicing (exon 교체) | RNA pre-mRNA trans-splicing | **단백질** split-intein splicing |
| 청구되는 '분자' | nucleic acid trans-splicing molecule (binding+splicing+coding exon 삼분) | pre-mRNA trans-splicing molecule (acceptor splice region 모듈 + 관심서열 + binding) | 인테인-융합 단백질을 코딩하는 폴리뉴클레오타이드 조성물 |
| 한정의 주축 | **표적 유전자/인트론 + 기능성 exon** (ABCA4·CEP290·HTT) | **엔지니어링된 acceptor splice 서열**(SEQ ID NO:3/4, CAGG, 피리미딘 TTTTTT/TCTTTT) | **특정 split intein**(Cfa/Cat/Gp41) |
| 유전자 축 폭 | 좁음(유전자별 청구, gene-agnostic 청구항 없음) | **넓음**(payload 유전자 불문) | 넓음(재구성 대상 단백질 불문) |
| 스플라이싱-요소 축 폭 | 넓음("splicing domain"/"artificial intron" 포괄) | **좁음**(특정 acceptor 서열에 고정) | 좁음(특정 인테인에 고정) |
| 방향성 | 3′→5′ 및 5′→3′ 모두 명시 | acceptor region이 관심서열의 3′ 또는 5′ | 단백질 N-/C-fragment |
| AAV/dual-AAV | 후속 청구·명세 | AAV 벡터 독립항(claim 12) | dual-AAV 단백질 재구성 |

### 4.2 어디서 겹치나 (overlap)
- **Ascidian ∩ ViGeneron (실질 겹침):** 둘 다 **RNA pre-mRNA trans-splicing molecule** 라는 같은 속을 청구하고, 공통 구성요소(*표적 결합 도메인 + 스플라이싱 요소 + payload + AAV 전달*)를 공유한다. 따라서 **"ABCA4를 표적하면서 ViGeneron의 특정 acceptor splice 서열을 사용하는 분자"** 처럼 **두 한정이 동시에 성립하는 영역에서는 양사 청구항이 충돌**할 수 있다. (양사 모두 ABCA4/Stargardt를 dual-AAV로 노린다는 점에서 이 교집합은 가설이 아니라 현실적 위험 지대.)
- **3사 공통(전략 수준):** 대형 유전자(ABCA4 등 AAV 적재한계 초과)를 **분할·재조립**해 전달한다는 *치료 컨셉* 은 공유 — 단, 이는 청구항 겹침이 아니라 **적응증/전략 겹침**이다.

### 4.3 어디서 갈리나 (divergence)
- **Ascidian vs ViGeneron:** 한정 축이 **직교**한다(유전자/인트론 vs 스플라이싱-서열). 그래서 *다른 유전자를 노리는 ViGeneron 분자* 는 Ascidian의 유전자-특이 청구항을 침해하지 않고, *ViGeneron 특정 acceptor 서열을 쓰지 않는 Ascidian ABCA4 분자* 는 ViGeneron 청구항을 침해하지 않는다 → **상당 부분 상호 회피 가능한 보완적 영지**를 형성, 충돌은 좁은 교집합에 국한.
- **vs SpliceBio:** **메커니즘·청구 대상 자체가 다르다**(RNA trans-splicing 분자 vs 인테인-융합 단백질 코딩 폴리뉴클레오타이드). 청구항 차원의 직접 겹침은 **사실상 없음**; 겹치는 건 *같은 질환(Stargardt/ABCA4)을 dual-AAV로 푼다* 는 **목표**뿐. 따라서 SpliceBio는 **자유실시(FTO) 관점의 우회 경로**에 가깝다(RNA가 아니라 단백질을 쪼갬).

---
## 부록 A. 데이터 출처·한계
- 모든 청구항은 Google Patents 원문에서 **결정론적 파싱**으로 verbatim 추출(번역·교정 없음). 추출본: `runs/exon_editor_trans_splicing/05_gp_authoritative/`.
- **WO2023220742A3**(Ascidian, ABCA4/Stargardt, ACDN-01 기반): Google Patents 503 반복으로 청구항 미확보 → ABCA4 권리는 등록 US11993776B2/US12442003B2 및 공개 US20210155938A1로 충분히 대표됨(재시도 또는 WIPO 권장).
- **ViGeneron PCT WO 번호**: 신뢰 가능한 출처로 확정 못 함(추측 금지). 등록 US12502438B2 + 공개 US20220160898A1로 권리 확인.
- **SpliceBio WO2021191447A1**: GP에서 독립항 claim 1 미파싱(종속항만 잡힘) → 동일 패밀리 US20230116688A1 독립항 1로 대표. EP3885440A1도 동일 패밀리.
- 등록·만료·PTA 등 법적 상태는 본 비교 분석 범위 밖(요청 스코프=청구항 범위 비교).
- **면책:** 본 문서는 청구항 문언 기반 기술/범위 분석이며 침해·유효성에 대한 법적 자문이 아니다.
