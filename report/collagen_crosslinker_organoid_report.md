# 콜라겐 가교제 & 오가노이드 지지체 분석 보고서

> 주제: 콜라겐을 오가노이드 지지체(scaffold)로 사용 시 부족한 점탄성(viscoelasticity)을 보완하기 위한 가교(crosslinking) 전략 분석 — 화학적/물리적/효소적 방법 비교, mTG 심층 분석, 임상 적용 관점, alginate 대안 평가
> 작성일: 2026-06-30 | 다중 에이전트 리서치 하니스(5개 전문 에이전트 + QA 교차검증) 산출물
> 규칙: 모든 사실 진술에 (출처 URL | 신뢰도[상/중/하]) 표기. 신뢰도 기준은 RELIABILITY_RUBRIC.md.

---

## 0. 핵심 요약 (Executive Summary)

1. 콜라겐 지지체의 근본 한계는 기계적 취약성·빠른 분해와 더불어 **부족한 점탄성**이며, 가교는 필수이나 대부분의 영구 공유 가교는 강성(stiffness)을 올리는 대신 응력완화(stress relaxation)를 억제하여 오가노이드 형태형성에는 오히려 불리할 수 있다. (출처: https://www.nature.com/articles/nmat4489 | 신뢰도: [상]; https://www.nature.com/articles/s44341-025-00014-6 | 신뢰도: [상])
2. **화학적 가교** 중 glutaraldehyde(GA)는 기계적 강화가 가장 크고 생체보철 심장판막의 사실상 임상 표준이나, 세포독성·유리 알데히드 잔류·석회화로 세포 봉입(in-situ)에는 부적합하다. (출처: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6563958/ | 신뢰도: [상]; https://www.mdpi.com/1999-4923/13/6/832 | 신뢰도: [상])
3. **저독성 화학 대안**으로 EDC/NHS(zero-length, 단 integrin 접착부위 소모), genipin(GA 대비 5,000~10,000배 저독성, 단 청색 착색)이 유효하며, polyepoxide는 유연성·점탄성 보존에 유리하다. (출처: https://pubmed.ncbi.nlm.nih.gov/10091923/ | 신뢰도: [상]; https://www.sciencedirect.com/science/article/pii/S1742706116306559 | 신뢰도: [상])
4. **물리적 가교** 중 riboflavin(비타민 B2) 광가교는 세포 존재 하 in-situ 가교가 가능하고 외인성 가교제 잔류가 없으며, 각막 콜라겐 가교용으로 **FDA 승인(Photrexa + KXL, 2016년)** 이력이 있다. UV·DHT는 세포 담지 불가(acellular 전처리 전용)다. (출처: https://www.accessdata.fda.gov/drugsatfda_docs/nda/2016/203324Orig1s000Lbl.pdf | 신뢰도: [상])
5. **효소적 가교** mTG는 온화한 조건(생리 pH·37℃, Ca²⁺ 비의존)에서 세포를 살린 채 가교하며 점탄성을 튜닝할 수 있어, 화학가교 대비 저독성이라는 명확한 장점을 갖는다. 단, 천연 삼중나선 콜라겐에는 반응성이 낮아 실무상 **젤라틴/부분변성 콜라겐**을 전제로 한다. (출처: https://pubs.acs.org/doi/10.1021/bm901284x | 신뢰도: [상]; https://pmc.ncbi.nlm.nih.gov/articles/PMC12835111/ | 신뢰도: [상])
6. mTG는 **종양 오가노이드(강성 구동 기계신호 모델링), 주입형 in-situ 봉입 지지체, 근/심근·신경근 등 장기·동적 자극 배양**에서 최대 강점을 발휘하나, 기저막(라미닌) 의존 상피 오가노이드와 고속 gelation 요구 공정에는 불리하다. (출처: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4136878/ | 신뢰도: [중]; https://pmc.ncbi.nlm.nih.gov/articles/PMC7825108/ | 신뢰도: [상])
7. **임상(이식형) 관점**에서 mTG의 결정적 리스크는 미생물 유래 효소가 인간 tissue transglutaminase(셀리악 자가항원)를 기능적으로 모방하는 **면역원성**이며, 임상등급 GMP mTG 상용 제품이 사실상 부재하다. 식품용 GRAS 안전성을 이식 적용으로 일반화해서는 안 된다. (출처: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6297833/ | 신뢰도: [상]; https://pmc.ncbi.nlm.nih.gov/articles/PMC8537092/ | 신뢰도: [중])
8. **Alginate**는 온화한 이온성 가교·우수한 면역격리(immunoisolation)·인체 임상 선례(islet 캡슐화)·GMP 등급 공급을 갖춘 거의 유일한 천연 세포봉입 소재이나, 세포 비부착성(RGD 미함유)·포유류 비분해성·불순물 면역원성/섬유화 캡슐화(FBR)가 핵심 단점이다. 실무는 alginate–collagen/GelMA 복합 또는 RGD-alginate로 수렴한다. (출처: https://www.nature.com/articles/nmat4489 | 신뢰도: [상]; https://clinicaltrials.gov/study/NCT01736228 | 신뢰도: [상]; https://pubmed.ncbi.nlm.nih.gov/9916770/ | 신뢰도: [상])

---

## 1. 콜라겐 가교 방법 비교 분석 (Q1)

### 1.0 왜 점탄성이 선택 기준인가
천연 ECM은 점탄성을 가지며 응력완화를 보이지만 3D 배양용 합성 하이드로젤은 대개 탄성(elastic)이다. 응력완화 속도를 독립적으로 튜닝하면 줄기세포의 spreading·증식·골분화가 빠른 완화 젤에서 향상된다. (출처: https://www.nature.com/articles/nmat4489 | 신뢰도: [상]) 응력완화는 이온/물리 가교 같은 약한 가교에서 촉진되고, 공유결합으로 강하게 가교된 ECM에서는 억제된다. (출처: https://www.nature.com/articles/s44341-025-00014-6 | 신뢰도: [상]) 장(intestinal) 오가노이드는 강성·점탄성이 자기조직화에 결정적이어서 1.3 kPa에서는 crypt가 형성되나 0.3 kPa에서는 형성되지 않는다. (출처: https://www.nature.com/articles/s41563-026-02519-4 | 신뢰도: [상]) → **시사점**: 영구 공유 가교(GA/EDC/genipin)를 강하게 단독 적용하면 강성은 오르나 응력완화가 억제되어 morphogenesis에 불리하므로, 약한 튜닝·동적 가역 결합·IPN(alginate/HA + collagen) 병용이 권장된다. (출처: https://pubs.acs.org/doi/10.1021/acscentsci.8b00170 | 신뢰도: [상])

### 1.1 화학적 가교 (Chemical)

**Glutaraldehyde (GA)** — 알데히드기가 라이신 ε-아미노기와 Schiff base를 형성하고 알돌 축합으로 분자간 공유 가교를 형성한다. 수축온도를 약 60→85~91℃까지 올리고 인장강도를 ~10배 향상시키나, 가수분해로 유리되는 잔류 알데히드가 세포독성(섬유아세포 99% 억제 ~3 ppm)·석회화를 유발한다. (출처: https://pubmed.ncbi.nlm.nih.gov/10150174/ | 신뢰도: [상]; https://onlinelibrary.wiley.com/doi/abs/10.1002/jbm.820140607 | 신뢰도: [상]) 세포 존재 하 in-situ 가교는 불가하다. (출처: https://www.sciencedirect.com/science/article/am/pii/S2352492819302107 | 신뢰도: [상])

**EDC/NHS (carbodiimide)** — EDC가 카복실기(Asp/Glu)를 활성화하고 NHS가 안정화하여 라이신과 아마이드 결합을 형성하는 zero-length 가교(가교제 분자가 매트릭스에 잔류하지 않음)이다. 부산물은 수용성 isourea로 세척 제거된다. 인장모듈러스를 약 6배 올리고 GA보다 저독성(cytocompatible)이나, **카복실기(GFOGER/RGD) 소모로 integrin 매개 세포접착을 저해**하는 것이 오가노이드 적용의 주의점이다. (출처: https://pmc.ncbi.nlm.nih.gov/articles/PMC11123180/ | 신뢰도: [상]; https://www.sciencedirect.com/science/article/pii/S1742706116306559 | 신뢰도: [상]) 통상 사용농도가 기계적 안정에 필요한 양보다 최대 100배 과량인 경우가 있어 감량 여지가 크다. (출처: https://www.sciencedirect.com/science/article/pii/S1742706115300325 | 신뢰도: [상])

**Genipin** — 치자(gardenia) 유래 천연 가교제로, 라이신/하이드록시라이신 아미노기가 genipin C-3 탄소를 친핵공격하여 고리 개환형 헤테로고리 가교를 형성한다. 강성을 약 0.03~50 kPa 범위로 튜닝 가능하며, **GA 대비 약 5,000~10,000배 저독성**(MTT 기준)으로 세포 존재 하 가교가 가능하다. 반응이 느리고(24~72h, 약알칼리 pH 최적) 특유의 청색 착색이 단점이다. (출처: https://pubmed.ncbi.nlm.nih.gov/10091923/ | 신뢰도: [상]; https://pmc.ncbi.nlm.nih.gov/articles/PMC9957210/ | 신뢰도: [상]; https://pmc.ncbi.nlm.nih.gov/articles/PMC3189483/ | 신뢰도: [상])

**Formaldehyde** — 모노알데히드로 메틸렌 가교(-CH₂-)를 형성하나 GA보다 가교가 약·불안정하고, **IARC Group 1 인체 발암물질**(비인두암)이어서 세포봉입·신규 임상 적용에 부적합하다. 초기 Hancock 돼지판막에 쓰였으나 이후 GA로 대체되었다. (출처: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1280402/ | 신뢰도: [상]; https://academic.oup.com/ejcts/article/38/2/141/516911 | 신뢰도: [상])

**Polyepoxide (Denacol EX-810/EX-313, BDDE 등)** — 에폭사이드 고리 개환으로 아미노/카복실기와 ether 가교를 형성(pH 의존: 염기성→아민·강성, 산성→카복실·유연). Td는 GA와 동등하나 **GA보다 부드럽고 유연하여 점탄성 보존에 유리**하고 세포독성이 낮다(di-/penta-epoxide ≤15% 생존감소 vs GA 20~33%). GA-free 항석회화 판막의 유망 대안이나 미반응 에폭시 잔류 세척이 필요하다. (출처: https://pubmed.ncbi.nlm.nih.gov/10147176/ | 신뢰도: [상]; https://pmc.ncbi.nlm.nih.gov/articles/PMC8482832/ | 신뢰도: [상])

**기타** — Acyl azide(DPPA)는 zero-length 아마이드 가교로 GA보다 세포적합성이 우수하나 인장강도가 낮고 다공구조 붕괴 위험이 있으며, HMDI는 GA급 기계강도와 함께 **FDA 510(k) 제품(Permacol, 돼지 진피 콜라겐)** 선례가 있으나 잔류 isocyanate/diamine 감작 부담이 있다. Tannic acid(비공유 우세)는 모듈러스를 50 kPa→~1.5 MPa로 올리며 세포 담지가 가능하다. (출처: https://pubmed.ncbi.nlm.nih.gov/14566791 | 신뢰도: [상]; https://pmc.ncbi.nlm.nih.gov/articles/PMC4006564/ | 신뢰도: [상]; https://pubmed.ncbi.nlm.nih.gov/21244722/ | 신뢰도: [상])

### 1.2 물리적 가교 (Physical)

**UV (254 nm)** — 타이로신/페닐알라닌 잔기에 라디칼을 생성해 dityrosine 가교를 형성(동시에 사슬 절단도 유발). **세포접착 부위가 아닌 방향족 잔기를 사용하므로 integrin 결합부위가 보존**되어 EDC의 단점을 회피하고, 멸균을 겸한다. 저장모듈러스를 ~150% 올리나 과조사 시 backbone scission으로 물성이 저하되고, UV 자체가 세포에 유해해 세포 담지는 불가하다. (출처: https://link.springer.com/article/10.1007/s10856-015-5627-8 | 신뢰도: [상]; https://onlinelibrary.wiley.com/doi/abs/10.1002/jbm.820291108 | 신뢰도: [상])

**DHT (탈수열처리)** — 진공·고온(105~140℃, 24h~수일)에서 탈수 축합으로 아마이드 가교를 형성한다. 인장강도를 최대 3배 이상 올리나 ≥145℃에서 심한 denaturation이 발생하고, fibrillar 구조 변성·integrin masking으로 세포 이동·접착을 저해할 수 있어 acellular 전처리 전용이다. 화학 잔류가 없어 규제상 유리하다. (출처: https://pmc.ncbi.nlm.nih.gov/articles/PMC7013574/ | 신뢰도: [상]; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11398025/ | 신뢰도: [상])

**Riboflavin(비타민 B2) 광가교 (청색광/UVA)** — 리보플라빈이 광촉매로 작용하여 ROS를 생성하고 주로 타이로신 잔기에서 dityrosine 가교를 형성한다. **세포 존재 하 in-situ 가교가 가능하고 외인성 가교제 잔류가 없는 것이 최대 장점**이며, 광량으로 강성을 튜닝한다. 단 고광량에서 ROS 산화손상으로 생존율이 저하될 수 있다(조건 의존). 임상적으로 **Photrexa Viscous/Photrexa(리보플라빈 5'-인산 0.146%) + KXL UVA 시스템이 진행성 원추각막용으로 2016년 FDA 승인**되었다. (출처: https://pmc.ncbi.nlm.nih.gov/articles/PMC8510499/ | 신뢰도: [상]; https://www.accessdata.fda.gov/drugsatfda_docs/nda/2016/203324Orig1s000Lbl.pdf | 신뢰도: [상])

> 참고: Gamma irradiation은 저선량서 가교, 고선량서 사슬 절단이 지배하며 25 kGy가 멸균 표준선량이나 세포 담지는 불가(치사)하다. (출처: https://www.sciencedirect.com/science/article/abs/pii/S0141391025006007 | 신뢰도: [상])

### 1.3 효소적 가교 (Enzymatic)

**Microbial transglutaminase (mTG)** — glutamine γ-carboxyamide와 lysine ε-amino 간 acyl transfer로 ε-(γ-glutamyl)lysine 이소펩타이드 공유결합을 형성한다. 칼슘 비의존이고 넓은 pH·온도에서 안정하며, 농도·시간으로 강성과 완화시간(응력완화)을 튜닝할 수 있다. 화학/광화학법과 달리 세포·사이토카인을 무해하게 봉입하며 세포접착·증식·분화가 우수하다. (출처: https://pubs.acs.org/doi/10.1021/bm901284x | 신뢰도: [상]; https://pmc.ncbi.nlm.nih.gov/articles/PMC5045885/ | 신뢰도: [상]) 다만 **천연 삼중나선 콜라겐에는 반응성이 낮아** 변성(젤라틴/부분변성) 기질이 전제되며, 잔류 효소의 면역원성이 의료 적용의 관건이다(상세 2·4장). (출처: https://pubs.acs.org/doi/10.1021/bm901284x | 신뢰도: [상]; https://pmc.ncbi.nlm.nih.gov/articles/PMC6297833/ | 신뢰도: [상])

**Lysyl oxidase (LOX/LOXL2)** — lysine을 산화적 탈아미노화하여 allysine을 만들고 자발적 Schiff base로 성숙 가교를 형성하는 **생리적(native) 가교**로, 생체모방형·세포봉입 친화적이다. 단 구리 의존·느린 동역학·고가·부산물 H₂O₂ 관리로 실용화는 mTG보다 제한적이며 승인 제품이 없다. (출처: https://reactome.org/content/detail/R-HSA-2243919 | 신뢰도: [상]; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6050231/ | 신뢰도: [상])

> 참고: Tyrosinase는 페놀→퀴논 라디칼 커플링으로 봉입 직후 세포생존이 HRP보다 우수하고, HRP/H₂O₂는 빠른 겔화가 가능하나 H₂O₂가 세포생존을 저하시켜 catalase 등 완화전략이 필요하다. (출처: https://onlinelibrary.wiley.com/doi/full/10.1002/app.51887 | 신뢰도: [상]; https://link.springer.com/article/10.1186/s40824-016-0077-z | 신뢰도: [상])

### 1.4 [표] 방법별 장단점 비교

| 방법 | 메커니즘 | 점탄성 효과 | 세포독성 | 임상적합성 | 잔류이슈 | 대표신뢰도 |
|---|---|---|---|---|---|---|
| **Glutaraldehyde** | 알데히드–Lys Schiff base + 알돌축합(영구 공유) | 강성·인장 최고, 응력완화 억제(탄성화) | 높음(유리 알데히드) | 매우 높음(심장판막 사실상 표준, FDA) | 유리 알데히드·석회화 | [상] |
| **EDC/NHS** | 카복실 활성화→아마이드(zero-length) | 강성·효소저항↑(중간), 점탄성↓ | 낮음(cytocompatible) | 양호(잔류 적음, FDA 510(k) 드레싱) | isourea(수세 제거), integrin부위 소모 | [상] |
| **Genipin** | Lys 아미노기 가교(천연) | G'/G'' 농도의존(~0.03–50 kPa), tan δ<1 | 매우 낮음(GA의 1/5,000~1/10,000) | 유망(식품안전), 의료기기 실적 적음 | 청색 착색, 미반응 중간체 | [상] |
| **Formaldehyde** | 메틸렌 가교 | 약·불안정 | 높음(IARC Group 1 발암) | 낮음(GA로 대체) | 휘발성 알데히드·석회화 | [상] |
| **Polyepoxide(Denacol/BDDE)** | 에폭사이드–아미노/카복실 ether | 강성↓ 유연·점탄성 보존 우수 | GA보다 낮음(미반응 에폭시 주의) | GA-free 항석회화 판막 유망 | 미반응 에폭시기 | [상] |
| **Tannic acid** | 수소결합·소수성(비공유 우세) | 모듈러스 50 kPa→~1.5 MPa, 세포담지 가능 | 낮음 | 상처드레싱 등 | 페놀 잔류·산화 | [상] |
| **UV(254 nm)** | dityrosine 라디칼 가교(+사슬절단) | G' ~150%↑, 과조사 시 저하 | 가교 비독성, UV 자체 유해(세포담지 불가) | 멸균 겸용 | 가교제 無, 단편화/denaturation | [상] |
| **DHT** | 탈수·열 축합 아마이드 가교 | 인장 최대 3배+, ≥145℃ 변성 | 비독성이나 대사↓·integrin masking(세포담지 불가) | 잔류 無로 규제 유리 | 화학잔류 無, 부분 denaturation | [상] |
| **Riboflavin 광가교** | ROS 매개 dityrosine 가교(청색/UVA) | 강성 광량의존 튜닝, **in situ 가능** | 낮음(세포존재 가교 가능), 고광량 시 저하 | **FDA 승인(Photrexa+KXL, 각막 CXL)** | 가교제 잔류 無, ROS 산화손상 | [상] |
| **mTG** | Gln–Lys isopeptide(효소) | 농도의존 강성·완화시간↑, 응력완화 튜닝 | 매우 낮음(세포봉입 우수) | food-grade 광범위, 의료는 **면역원성(셀리악) 관건** | 잔류 효소·neoepitope 면역원성 | [상] |
| **Lysyl oxidase** | allysine→Schiff base(생리적 가교) | native 가교, 인장·안정성↑(느림) | 매우 낮음(생체모방) | 연구단계, 승인제품 無 | H₂O₂·잔류 효소 | [상]/[중] |
| **Tyrosinase / HRP** | 페놀/퀴논 라디칼 커플링 | 빠른 겔화·튜닝 | Tyrosinase 양호 / HRP는 H₂O₂로 생존 저하 | 연구단계 | H₂O₂(HRP)·페놀 잔류 | [상] |

---

## 2. mTG의 장점 분석 (Q2)

핵심 전제: mTG는 native 콜라겐 삼중나선에는 반응성이 낮고 변성된 젤라틴/콜라겐에서 가교 효율이 높다(열변성 콜라겐 monomer당 최대 5.4개 가교). 따라서 실무의 "mTG-콜라겐 가교"는 대부분 젤라틴 또는 부분변성 콜라겐 시스템을 의미하며, 이 사실이 장단점을 모두 규정한다. (출처: https://pubs.acs.org/doi/10.1021/bm901284x | 신뢰도: [상]; https://www.sciencedirect.com/science/article/abs/pii/S0308814618313827 | 신뢰도: [상])

### [표] mTG 장점 / 한계

| 구분 | 항목 | 핵심 내용 | 출처 | 신뢰도 |
|---|---|---|---|---|
| **장점** | 온화한 반응조건 | 생리 pH·37℃, Ca²⁺ 비의존, 무독성 생촉매 → 세포 존재 하 in-situ 가교 가능 | https://pmc.ncbi.nlm.nih.gov/articles/PMC3971462/ | [중] |
| | 기질 특이성 | Gln γ-carboxamide ↔ Lys ε-amino 간 ε-(γ-glutamyl)lysine 이소펩타이드 공유결합, 부반응 적음 | https://pmc.ncbi.nlm.nih.gov/articles/PMC12610575/ | [상] |
| | 세포친화성·저독성 | 화학가교 부산물 없음. 콜라겐피브릴 하이드로젤 40 U/g 이하서 우수한 세포 성장 | https://pmc.ncbi.nlm.nih.gov/articles/PMC6682156/ | [상] |
| | 점탄성/물성 튜닝 | 효소량·시간·전구체 농도로 G'/G''·강성·완화시간 조절. 열가역→비가역 전환 | https://www.sciencedirect.com/science/article/abs/pii/S0268005X0100025X | [상] |
| | 조직 통합성·광학 투명성 | in-situ 젤이 숙주조직과 일체화(주입형 유리), Col-Tgel 투명→이미징 적합 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4136878/ | [중] |
| **한계** | 천연 콜라겐 저효율 | 삼중나선 내 Gln 접근 불가 → 변성(젤라틴화) 필요 (가장 중요한 한계) | https://pubs.acs.org/doi/10.1021/bm901284x | [상] |
| | 느린 반응속도 | 가교가 분~시간 단위 → 정밀 gelation 제어 필요, 고처리량 불리 | https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0105616 | [중] |
| | 온도 민감성 | 50℃↑ 활성 급감, 60℃ 완전 실활, 50℃·30분 활성 50% 상실 → 공정창 좁음 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10543708/ | [중] |
| | 효소 잔류·면역원성 | 잔류 mTG가 tTG 모방 → (경구·셀리악 맥락) 면역원성 우려, 이식 시 주의 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6297833/ | [상] |
| | 과가교 역효과 | 효소 과량 시 입체장애로 네트워크가 오히려 느슨해질 수 있음(메커니즘 추론) | (단독 출처 부재 — 보수적 해석) | [하] |

---

## 3. mTG가 가장 유리한 오가노이드 목적·유형 (Q3)

mTG의 차별적 강점(세포 존재 하 온화한 비가역 가교, 강성·점탄성 정밀 튜닝, 저독성, 광학 투명성·조직 통합성)과 한계(천연 삼중나선 저효율, 느린 반응)를 종합하면 다음 용도에서 가장 큰 장점을 낸다. (아래 적용 사례는 in-vitro 연구 단계이며 이식 임상 승인 선례가 아님에 유의 — QA 단서.)

- **(A) 종양/암 오가노이드 — 강성 구동 기계신호 모델링 (최우선 적합)**: Col-Tgel(mTG 가교 젤라틴/콜라겐)이 고형종양 미세환경 재현에 채택되며, 젤라틴 농도로 강성을 광범위 튜닝하고 투명하여 이미징 스크리닝에 적합하다. 높은 기질강성이 오가노이드 성장에 영향을 주므로 강성 변수를 능동적으로 다뤄야 하는 종양 연구에 mTG 튜닝성이 직접 부합한다. (출처: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4136878/ | 신뢰도: [중]; https://pubmed.ncbi.nlm.nih.gov/31398570/ | 신뢰도: [상])
- **(B) 주입형(injectable)/in-situ 형성 지지체 — 세포 봉입·조직 통합 (강력 적합)**: mTG는 단백질 하이드로젤 in-situ 가교의 가장 잘 연구된 효소로, 액상→비가역 젤로 전환해 세포를 봉입하고 숙주조직과 일체화한다. (출처: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0105616 | 신뢰도: [중]; https://pmc.ncbi.nlm.nih.gov/articles/PMC5045885/ | 신뢰도: [상])
- **(C) 근/심근·신경근 — 장기배양·기계자극·성숙 유도 (적합)**: mTG 가교 젤라틴-라미닌 젤에서 골격근세포가 28일까지 박리 없이 장기배양·성숙하며, 비가역 공유 네트워크의 기계적 안정성이 동적 자극 배양에 유리하다. (출처: https://pmc.ncbi.nlm.nih.gov/articles/PMC7825108/ | 신뢰도: [상]; https://pubs.rsc.org/en/content/articlelanding/2020/bm/c9bm01430f | 신뢰도: [상])
- **(D) 줄기세포 확장·간엽계 분화 (적합)**: mTG 가교 젤라틴 기반 젤이 치수줄기세포 골형성 잠재력을 증진한다. (출처: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8240633/ | 신뢰도: [상])
- **(E) Matrigel 대체 — 정의성·재현성 요구 (전략적 적합)**: 미정의·배치 변동성이 큰 Matrigel 대비, 정의된 젤라틴 기반 튜닝성 하이드로젤을 mTG가 세포 친화적으로 굳히는 수단으로 부합한다. (출처: https://www.nature.com/articles/s41578-020-0199-8 | 신뢰도: [중])

**부적합/주의 케이스**: ① 순수 천연 삼중나선 콜라겐 지지체(저효율, 변성 필요) (출처: https://pubs.acs.org/doi/10.1021/bm901284x | 신뢰도: [상]); ② 기저막(라미닌) 의존 상피 오가노이드(장·신장 등) — mTG-젤라틴은 RGD는 제공하나 라미닌/기저막 단백질은 비제공 (출처: https://www.nature.com/articles/s41578-020-0199-8 | 신뢰도: [중]); ③ 고속·대량/즉각 gelation 공정(광가교·click이 유리); ④ 장/이식형에서 잔류효소 제거 곤란; ⑤ 정밀 항온이 어려운 고온 공정(50℃↑ 실활). (출처: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10543708/ | 신뢰도: [중])

**한 줄 결론**: mTG는 변성 젤라틴/부분변성 콜라겐 기반으로, **강성·점탄성을 능동적으로 다뤄야 하고(종양), 세포를 in-situ 봉입·조직과 통합해야 하며(주입형), 장기·동적 기계자극 하 성숙을 유도하는(근·심근·신경근) 오가노이드**에서 최대 강점을 낸다.

---

## 4. 임상 활용 관점 — mTG 장단점 및 Selling-point (Q4)

mTG는 *Streptomyces mobaraensis* 유래 Ca²⁺ 비의존 가교효소다. (출처: https://pmc.ncbi.nlm.nih.gov/articles/PMC12835111/ | 신뢰도: [상]) **임상중개 결론**: 식품용(GRAS)으로는 확립되었고 조직공학 연구에서 우수한 가교제이지만, "임상용/GMP-grade 직접 치료 적용" 등급의 상용 제품은 사실상 부재하며, 미생물 유래 면역원성(특히 셀리악/자가면역 mimicry)이 임상 오가노이드의 가장 큰 리스크다.

### [표] 임상 장점 / 단점·리스크

| 구분 | 항목 | 내용 | 출처 | 신뢰도 |
|---|---|---|---|---|
| **장점** | 칼슘 비의존·온화 가교 | 포유류 tTG/FXIII와 달리 Ca²⁺ 없이 작동 → 배양환경서 사용 간편 | https://pmc.ncbi.nlm.nih.gov/articles/PMC12835111/ | [상] |
| | 우수한 세포적합성 | 화학가교 대비 비독성, 가교가 기계·단백분해 저항 | https://pmc.ncbi.nlm.nih.gov/articles/PMC5045885/ | [상] |
| | 재조합 시 동물유래성분 배제 | 재조합 mTG는 *E. coli* 생산, 동물유래물질 미사용(예: Zedira Andracon) | https://zedira.com/Microbial-Transglutaminase-Andracon | [중] |
| | in-situ 조직 통합 | in-situ 젤이 숙주조직(연골·간 등)에 공유결합으로 통합 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8757843/ | [상] |
| | 식품 안전성 선례 | 1998년 이후 GRAS, 13주 랫드 372 mg TOS/kg/d까지 무해, 비변이원성 | https://www.fda.gov/media/178428/download | [상] |
| | 의료 sealant 인체 선례 | 젤라틴+mTG+thrombin sealant, 신경외과 20명 first-in-human 100% 지혈 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4486749/ | [상] |
| **단점·리스크** | **면역원성/tTG mimicry** | mTG가 human tissue TG(셀리악 자가항원)를 기능적으로 모방, neo-epitope 항체 형성 | https://pmc.ncbi.nlm.nih.gov/articles/PMC6297833/ | [상] |
| | GMP/임상등급 상용제품 부재 | cGMP-grade는 ADC용 "upon request"만, 치료용 승인 제품 미시판, 다수 "research use only" | https://www.sigmaaldrich.com/US/en/product/sigma/sae0217 | [중] |
| | 부산물 암모니아(NH₃) | 가교 1회당 NH₃ 1분자 방출, 아민 공여체 부재 시 deamidation | https://pmc.ncbi.nlm.nih.gov/articles/PMC12835111/ | [상] |
| | 식품용≠의료용 규제격차 | GRAS는 가공보조제 분류로 전면 독성평가 면제, 경구 안전성이 이식 안전성 보증 아님 | https://pmc.ncbi.nlm.nih.gov/articles/PMC8537092/ | [중] |
| | 식품용 제제 동물유래 캐리어 | Activa RM = sodium caseinate(우유)+maltodextrin → 식품용 그대로 쓰면 xeno-free 위배 | https://modernistpantry.com/products/activa-rm-transglutaminase.html | [중] |
| | 잔류 효소 제거 제약 | 열불활성화(60~70℃)는 살아있는 세포·오가노이드와 양립 어려움 | https://pubmed.ncbi.nlm.nih.gov/17719777/ | [중] |
| | 멸균 제약 | 효소는 열·방사선 멸균에 취약 → 무균여과 의존, 밸리데이션 부담 | https://www.amerigoscientific.com/microbial-transglutaminase-production-grade-characterized-for-endotoxin-hcp-dna-sterility-item-55294.html | [중] |
| | 규제 독립제품 승인 선례 없음 | mTG 단독 의료기기/약물의 FDA/EMA 직접 승인 선례 확인 불가 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4486749/ | [중] |

> **규제 충돌 명시**: mTG 면역원성에 대해 ① 제조사·식품안전 평가(GRAS)는 "무해", ② 다수 peer-reviewed 임상연구진은 "면역원성·잠재 병원성"을 경고한다. 양측 모두 [상] 등급이나 맥락이 다르다(GRAS=경구·식품, 셀리악 연구=면역학적 mimicry). **임상 오가노이드(이식형)에는 면역원성 경고가 더 직접 관련되므로 보수적으로 면역원성 리스크를 우선시**해야 한다. (출처: https://www.fda.gov/media/178428/download | 신뢰도: [상] vs https://pmc.ncbi.nlm.nih.gov/articles/PMC6297833/ | 신뢰도: [상])

### [표] Selling-point (검증된 사실 vs. 마케팅 주장 구분)

| 주장 | 판정 | 근거 출처 · 신뢰도 |
|---|---|---|
| "비독성·천연 효소 가교제" | **부분 검증** — 식품 경구 비독성은 사실, 이식 일반화는 마케팅 과장(면역원성과 충돌) | https://www.fda.gov/media/178428/download [상] vs https://pmc.ncbi.nlm.nih.gov/articles/PMC6297833/ [상] |
| "Animal-origin-free / xeno-free" | **조건부 검증** — 재조합 제품은 검증, 식품용 Activa RM은 caseinate 함유로 거짓 | https://zedira.com/Microbial-Transglutaminase-Andracon [중]; https://modernistpantry.com/products/activa-rm-transglutaminase.html [중] |
| "GMP-grade 가용" | **마케팅 과장** — cGMP는 ADC용 맞춤 공급, 치료용 기성품 부재 | https://www.sigmaaldrich.com/US/en/product/sigma/sae0217 [중] |
| "배치 일관성·고순도" | **검증된 사실** — 재조합 >95% 순도, endotoxin/HCP/DNA/sterility 특성화 제품 실재 | https://www.amerigoscientific.com/microbial-transglutaminase-production-grade-characterized-for-endotoxin-hcp-dna-sterility-item-55294.html [중] |
| "칼슘 비의존·온화 생리조건 가교" | **검증된 사실** | https://pmc.ncbi.nlm.nih.gov/articles/PMC12835111/ [상] |
| "임상검증된 조직공학 적용" | **부분 검증** — sealant 소규모 인체 O, 오가노이드 이식 승인 선례 X | https://pubmed.ncbi.nlm.nih.gov/19360881/ [상] |
| "잔류물 없이 제거 가능" | **부분 검증** — 열불활성화 가능하나 생세포 양립 곤란, NH₃ 제거 필요 | https://pubmed.ncbi.nlm.nih.gov/17719777/ [중] |

---

## 5. Alginate의 임상 오가노이드 적용 장단점 (Q5)

Alginate는 M/G 다당류로, Ca²⁺ 등 다가 양이온이 연속된 G-block에 결합하는 "egg-box" 이온성·가역적 가교를 형성한다. (출처: https://pubs.acs.org/doi/abs/10.1021/bm060550a | 신뢰도: [상]) 이 가역성이 장점(점탄성)과 단점(불안정성) 양쪽의 근원이다.

### [표] Alginate 임상 적용 장단점

| 구분 | 항목 | 내용 | 출처 | 신뢰도 |
|---|---|---|---|---|
| **장점** | 온화한 세포친화 가교 | 상온·수계 CaCl₂ 이온 가교로 봉입 시 세포 생존 보존 | https://www.mdpi.com/2310-2861/11/1/16 | [중] |
| | 점탄성/stress relaxation 튜닝 | 탄성률 고정 상태서 응력완화 독립 조절 → MSC spreading·증식·골분화 촉진 | https://www.nature.com/articles/nmat4489 | [상] |
| | 검증된 면역격리 캡슐 | 영양·인슐린 교환 허용, 면역세포·항체 차단 | https://clinicaltrials.gov/study/NCT01736228 | [상] |
| | 인체 임상 선례 | DIABECELL(봉입 돼지 islet) Phase IIb(NCT01736228, COMPLETED), islet 9.5년 후 생존 확인 | https://clinicaltrials.gov/study/NCT01736228 | [상] |
| | GMP-grade 상용화 | NovaMatrix/Pronova가 임상등급 alginate·RGD-alginate 공급(벤더 1차자료, lot CoA 확인 필요) | https://novamatrix.biz/ | [중] |
| | anti-fibrotic 변형 | triazole/TMTD·zwitterion 변형이 설치류·영장류서 섬유화 저항(전임상, 인체 효능 미확립) | https://www.nature.com/articles/s41467-019-13238-7 | [상] |
| **단점** | 세포 비부착성(RGD 미함유) | integrin 결합 부재로 부착·spreading·분화 신호 결핍 → RGD 펩타이드 공유결합으로 보완 | https://pubmed.ncbi.nlm.nih.gov/9916770/ | [상] |
| | 포유류 비분해성 | alginase 부재로 화학 분해 안됨, Ca²⁺ 용출에 의한 비제어 용해만 → 산화 alginate로 보완 | https://pmc.ncbi.nlm.nih.gov/articles/PMC12940349/ | [중] |
| | 이온가교 불안정 | 생리환경 Na⁺ 교환·chelator로 Ca²⁺ 이탈→겔 약화·붕괴 → Ba²⁺/Sr²⁺·이중가교로 보완 | https://pmc.ncbi.nlm.nih.gov/articles/PMC12940349/ | [중] |
| | 불순물 면역원성 | polyphenol·protein·endotoxin·fucoidan 잔류가 생체적합성 저해(단백 저감 어려움) | https://www.sciencedirect.com/science/article/abs/pii/S0142961205007969 | [상] |
| | 섬유화 캡슐화/FBR | 임상 핵심 실패요인 — pericapsular 과성장→영양 차단→이식체 사멸 | https://pmc.ncbi.nlm.nih.gov/articles/PMC4123607/ | [중] |
| | 표준화 부재·생물학적 불활성 | lot간 재현성 문제, 부착·분해·리모델링 신호 부재 | https://pubmed.ncbi.nlm.nih.gov/20225212/ | [상] |

### [표] Alginate vs. 콜라겐+mTG 비교

| 항목 | Alginate (이온가교, ±RGD) | 콜라겐 + mTG (효소 가교) |
|---|---|---|
| 가교 메커니즘 | Ca²⁺ 이온성·가역적 egg-box | 공유 isopeptide, Ca²⁺ 비의존 |
| 세포 부착성 | 본질적 비부착(RGD 필요) | 콜라겐 천연 부착 리간드 보유 |
| 생분해성 | 비분해(Ca²⁺ 용출 의존) | 본질적 생분해·세포 리모델링 |
| 점탄성/물성 | 응력완화 정밀 튜닝·자가치유 | 공유 가교로 강성↑, 튜닝폭 상대적 제한 |
| 생리환경 안정성 | chelation·단가이온에 취약 | isopeptide로 이온환경 변화에 안정 |
| 면역원성/순도 | 해조 유래 불순물 잔류(ultrapure로 저감) | mTG 셀리악 면역원성 우려 + 동물유래 콜라겐 리스크 |
| 임상/면역격리 선례 | islet 캡슐화 임상 다수 + GMP 상용 | sealant 소규모/오가노이드 연구단계 |
| 오가노이드 적합성 | 점탄성·온화공정 강점, 부착 신호 부재(기능화 필요) | 천연 ECM 부착·리모델링 신호, 온화·저독성 가교 |

(출처: https://www.nature.com/articles/nmat4489 | 신뢰도: [상]; https://pmc.ncbi.nlm.nih.gov/articles/PMC5045885/ | 신뢰도: [상]; https://pubmed.ncbi.nlm.nih.gov/9916770/ | 신뢰도: [상]; https://pmc.ncbi.nlm.nih.gov/articles/PMC12940349/ | 신뢰도: [중])

**종합 판단**: 임상 면역격리 캡슐화(세포치료·당뇨 islet)에는 검증된 선례·GMP 공급·점탄성 튜닝을 갖춘 **alginate(ultrapure, low M/G, RGD/anti-fibrotic 변형)**가 우위. 반면 세포 부착·ECM 리모델링·생분해가 필요한 **오가노이드 성숙**에는 **콜라겐(±mTG)**이 생물학적으로 유리하다. 실무는 **alginate–collagen/GelMA 복합 또는 RGD-alginate**로 양쪽 장점을 절충하는 방향으로 수렴한다.

---

## 6. 종합 비교 & 권고

### [표] 화학가교(GA 대표) vs mTG vs Alginate (임상 오가노이드 기준)

| 평가 축 | 화학가교 (GA 대표) | mTG (효소) | Alginate (이온) |
|---|---|---|---|
| 세포 존재 하 in-situ 가교 | 불가(독성) | 가능(온화) | 가능(온화) |
| 점탄성/응력완화 | 강성↑, 응력완화 억제 | 농도로 튜닝 가능 | 응력완화 정밀 튜닝 우수 |
| 세포 부착·ECM 신호 | 콜라겐 유래 부착 O(단 GA 독성) | 콜라겐/젤라틴 부착 O | 비부착(RGD 기능화 필요) |
| 생분해·리모델링 | 가교로 분해 저항↑ | 생분해·리모델링 O | 비분해(Ca 용출 의존) |
| 세포독성 | 높음(유리 알데히드) | 매우 낮음 | 낮음 |
| 면역원성(이식형) | 잔류 알데히드·석회화 | tTG mimicry 면역원성(핵심 리스크) | 불순물·FBR(핵심 리스크) |
| GMP/임상 선례 | 강함(심장판막 표준) | 약함(치료용 상용 부재) | 강함(islet 캡슐화·GMP) |

### 권고 (임상 오가노이드 기준)
1. **점탄성 보존이 1순위**라면 영구 공유 가교(GA/EDC/genipin) 단독·고가교는 부적합. 약한 튜닝 또는 동적/가역 결합·IPN(alginate/HA + collagen) 병용으로 응력완화를 별도 부여한다. (출처: https://www.nature.com/articles/nmat4489 | 신뢰도: [상]; https://pubs.acs.org/doi/10.1021/acscentsci.8b00170 | 신뢰도: [상])
2. **세포 존재 하 in-situ 가교**가 필요하면 우선순위는 (a) riboflavin 광가교(FDA 이력·잔류물 적음·ROS만 관리), (b) mTG(온화·Ca²⁺ 비의존, 단 의료는 면역원성 평가 필수), (c) tyrosinase/저-H₂O₂ HRP. UV·DHT·GA·formaldehyde·gamma는 acellular 전처리 전용.
3. **mTG를 임상에 채택할 경우**: ① 정제 재조합 GMP 등급만 사용(식품용 제제 금지), ② 자체 cGMP 공급망·CoA·ancillary material 등급화, ③ 잔류 효소·NH₃ 정량 및 면역원성/항원성 평가를 IND 필수 항목으로 설정, ④ FDA/EMA 독립제품 승인 선례 부재를 전제로 de novo 규제 경로 설계. (출처: https://pmc.ncbi.nlm.nih.gov/articles/PMC6297833/ | 신뢰도: [상]; https://pmc.ncbi.nlm.nih.gov/articles/PMC8537092/ | 신뢰도: [중])
4. **면역격리·세포치료형** 임상이면 alginate(ultrapure·low M/G·RGD/anti-fibrotic 변형)가 선례·GMP 측면에서 우위이며, **오가노이드 성숙·ECM 신호**가 중요하면 콜라겐(±mTG) 또는 alginate–collagen 복합이 합리적이다.

---

## 7. 출처 목록

1. Chaudhuri et al., Hydrogels with tunable stress relaxation regulate stem cell fate — Nature Materials — https://www.nature.com/articles/nmat4489 — [상]
2. Role of ECM viscoelasticity in development/disease — npj — https://www.nature.com/articles/s44341-025-00014-6 — [상]
3. Stress-relaxing bioprinting materials enable organoid self-organization — Nature Materials — https://www.nature.com/articles/s41563-026-02519-4 — [상]
4. Modulating viscoelasticity via covalent vs dynamic crosslinking — ACS Cent Sci — https://pubs.acs.org/doi/10.1021/acscentsci.8b00170 — [상]
5. GA crosslinking of collagen (shrinkage temp, time/temp/conc) — PubMed 10150174 — https://pubmed.ncbi.nlm.nih.gov/10150174/ — [상]
6. Speer, Biological effects of residual GA — J Biomed Mater Res — https://onlinelibrary.wiley.com/doi/abs/10.1002/jbm.820140607 — [상]
7. Chemical cross-linking methods for cell encapsulation (review) — ScienceDirect — https://www.sciencedirect.com/science/article/am/pii/S2352492819302107 — [상]
8. Effect of cyclic deformation on xenogeneic heart valve biomaterials (GA 판막) — PMC6563958 — https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6563958/ — [상]
9. Optimization of Collagen Chemical Crosslinking to Restore Biocompatibility — Pharmaceutics/PMC8229326 — https://www.mdpi.com/1999-4923/13/6/832 — [상]
10. EDC/NHS crosslinking of fish collagen film — PMC11123180 — https://pmc.ncbi.nlm.nih.gov/articles/PMC11123180/ — [상]
11. Carbodiimide crosslinking & cellular recognition of collagen (integrin) — Acta Biomater — https://www.sciencedirect.com/science/article/pii/S1742706116306559 — [상]
12. Control of crosslinking for collagen scaffold stability (EDC 과량) — Acta Biomater — https://www.sciencedirect.com/science/article/pii/S1742706115300325 — [상]
13. FDA 510(k) K112580 — EDC-crosslinked porcine collagen wound dressing — https://www.accessdata.fda.gov/cdrh_docs/pdf11/K112580.pdf — [상]
14. Sung et al., In vitro cytotoxicity of genipin vs glutaraldehyde — PubMed 10091923 — https://pubmed.ncbi.nlm.nih.gov/10091923/ — [상]
15. Stiffness-modulation of collagen gels by genipin — Gels/PMC9957210 — https://pmc.ncbi.nlm.nih.gov/articles/PMC9957210/ — [상]
16. Genipin crosslinking optical/structural properties of collagen — PMC3189483 — https://pmc.ncbi.nlm.nih.gov/articles/PMC3189483/ — [상]
17. IARC Monographs summary — Formaldehyde Group 1 — PMC1280402 — https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1280402/ — [상]
18. Hancock II porcine valve 25-yr (formalin→glutaraldehyde) — EJCTS — https://academic.oup.com/ejcts/article/38/2/141/516911 — [상]
19. Polyepoxy compound fixed porcine heart valve — PubMed 10147176 — https://pubmed.ncbi.nlm.nih.gov/10147176/ — [상]
20. Cytotoxicity of epoxy-crosslinked pericardium (≤15% vs GA 20-33%) — PMC8482832 — https://pmc.ncbi.nlm.nih.gov/articles/PMC8482832/ — [상]
21. Marinucci, biocompatibility of GA- vs DPPA-crosslinked membranes — PubMed 14566791 — https://pubmed.ncbi.nlm.nih.gov/14566791 — [상]
22. Permacol (HMDI) pediatric abdominal wall reconstruction — PMC4006564 — https://pmc.ncbi.nlm.nih.gov/articles/PMC4006564/ — [상]
23. Tannic acid cross-linked collagen scaffolds — PubMed 21244722 — https://pubmed.ncbi.nlm.nih.gov/21244722/ — [상]
24. UV irradiation as binding-site-conserving crosslinking — J Mater Sci Mater Med — https://link.springer.com/article/10.1007/s10856-015-5627-8 — [상]
25. Physical crosslinking of collagen: UV vs DHT (Weadock 1995) — J Biomed Mater Res — https://onlinelibrary.wiley.com/doi/abs/10.1002/jbm.820291108 — [상]
26. DHT effect on structure/mechanics of collagen — PMC7013574 — https://pmc.ncbi.nlm.nih.gov/articles/PMC7013574/ — [상]
27. Comparative DHT crosslinking of electrospun collagen — PMC11398025 — https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11398025/ — [상]
28. Blue light-activated riboflavin phosphate collagen crosslinking — PMC8510499 — https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8510499/ — [상]
29. FDA NDA 203324 label (Photrexa) — https://www.accessdata.fda.gov/drugsatfda_docs/nda/2016/203324Orig1s000Lbl.pdf — [상]
30. Avedro/Glaukos Photrexa + KXL FDA approval (2016) — Businesswire — https://www.businesswire.com/news/home/20160418006610/en/ — [상]
31. Regulatory effects of γ-irradiation on collagen gels — ScienceDirect — https://www.sciencedirect.com/science/article/abs/pii/S0141391025006007 — [상]
32. Cross-Linking of Type I Collagen with mTG: sites — Biomacromolecules — https://pubs.acs.org/doi/10.1021/bm901284x — [상]
33. TG-modified collagen fibers tailored by denaturation temp — Food Chem — https://www.sciencedirect.com/science/article/abs/pii/S0308814618313827 — [상]
34. Enzymatically crosslinked gelatin hydrogel promotes ADSC proliferation — PMC5045885 — https://pmc.ncbi.nlm.nih.gov/articles/PMC5045885/ — [상]
35. mTG in food biotech: mechanisms & applications — PMC12835111 — https://pmc.ncbi.nlm.nih.gov/articles/PMC12835111/ — [상]
36. Feasibility of TGase for self-catalytic collagen fibril hydrogel — PMC6682156 — https://pmc.ncbi.nlm.nih.gov/articles/PMC6682156/ — [상]
37. TG crosslinking enhances properties of fish gelatins — PMC12610575 — https://pmc.ncbi.nlm.nih.gov/articles/PMC12610575/ — [상]
38. Influence of TG on thermoreversible gelation of gelatin — Food Hydrocoll — https://www.sciencedirect.com/science/article/abs/pii/S0268005X0100025X — [상]
39. Tumor bioengineering using TG crosslinked hydrogel (Col-Tgel) — PMC4136878 — https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4136878/ — [중]
40. mTG controlled crosslinking of GelMA for 3D printing — Biofabrication/IOP — https://iopscience.iop.org/article/10.1088/1758-5090/ab063f — [상]
41. Defined hydrogel matrices for patient-derived colorectal tumor organoids — PubMed 31398570 — https://pubmed.ncbi.nlm.nih.gov/31398570/ — [상]
42. Tumor bioengineering TG hydrogel (PLOS One) — https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0105616 — [중]
43. Gelatin hydrogels crosslinked with mTG as skeletal muscle substrates (28d) — PMC7825108 — https://pmc.ncbi.nlm.nih.gov/articles/PMC7825108/ — [상]
44. Enzymatically crosslinked gelatin-laminin hydrogels (neuromuscular) — RSC Biomater Sci — https://pubs.rsc.org/en/content/articlelanding/2020/bm/c9bm01430f — [상]
45. Gelatin-GAG semi-IPN via mTG enhances osteogenic potential of DPSCs — PMC8240633 — https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8240633/ — [상]
46. Synthetic alternatives to Matrigel — Nature Reviews Materials — https://www.nature.com/articles/s41578-020-0199-8 — [중]
47. mTG immunogenic & potentially pathogenic in pediatric celiac disease — PMC6297833 — https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6297833/ — [상]
48. mTG frequently used food additive, autoimmune inducer — PMC8537092 — https://pmc.ncbi.nlm.nih.gov/articles/PMC8537092/ — [중]
49. FDA GRAS Notice 1139, Transglutaminase — https://www.fda.gov/media/178428/download — [상]
50. mTG improves ex vivo adhesion of GelMA to cartilage — PMC8757843 — https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8757843/ — [상]
51. First-in-human trial of gelatin-TG vascular sealant — PMC4486749 — https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4486749/ — [상]
52. Biomimetic gelatin-mTG sealant in vivo — PubMed 19360881 — https://pubmed.ncbi.nlm.nih.gov/19360881/ — [상]
53. Zedira Andracon recombinant mTG (벤더) — https://zedira.com/Microbial-Transglutaminase-Andracon — [중]
54. Amerigo Scientific mTG production grade (벤더) — https://www.amerigoscientific.com/microbial-transglutaminase-production-grade-characterized-for-endotoxin-hcp-dna-sterility-item-55294.html — [중]
55. Sigma-Aldrich eMTG (cGMP upon request, 벤더) — https://www.sigmaaldrich.com/US/en/product/sigma/sae0217 — [중]
56. Modernist Pantry Activa RM 성분(caseinate) (소매) — https://modernistpantry.com/products/activa-rm-transglutaminase.html — [중]
57. Thermal stability/inactivation of mTG — PubMed 17719777 — https://pubmed.ncbi.nlm.nih.gov/17719777/ — [중]
58. mTG application in food industry (온도 안정성) — PMC10543708 — https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10543708/ — [중]
59. Reexamining egg-box model in Ca-alginate gels (XRD) — Biomacromolecules — https://pubs.acs.org/doi/abs/10.1021/bm060550a — [상]
60. Metal ion crosslinking alginate gels (egg-box, 이온가교) — MDPI Gels — https://www.mdpi.com/2310-2861/11/1/16 — [중]
61. Rowley/Mooney, alginate hydrogels as synthetic ECM (RGD) — PubMed 9916770 — https://pubmed.ncbi.nlm.nih.gov/9916770/ — [상]
62. DIABECELL Phase IIb (NCT01736228) — ClinicalTrials.gov — https://clinicaltrials.gov/study/NCT01736228 — [상]
63. Immunological/technical considerations in alginate microencapsulation — PMC4123607 — https://pmc.ncbi.nlm.nih.gov/articles/PMC4123607/ — [중]
64. Residual contamination & purified alginate biofunction — Biomaterials — https://www.sciencedirect.com/science/article/abs/pii/S0142961205007969 — [상]
65. Protein contaminants in alginate immunogenicity — PubMed 20225212 — https://pubmed.ncbi.nlm.nih.gov/20225212/ — [상]
66. Alginate-based hydrogels: 비분해·chelation·bioinertness 리뷰 — PMC12940349 — https://pmc.ncbi.nlm.nih.gov/articles/PMC12940349/ — [중]
67. NovaMatrix/Pronova GMP alginate (벤더) — https://novamatrix.biz/ — [중]
68. Zwitterionically modified alginates mitigate overgrowth — Nature Communications — https://www.nature.com/articles/s41467-019-13238-7 — [상]
69. Reactome — Crosslinking of collagen fibrils (LOX) — https://reactome.org/content/detail/R-HSA-2243919 — [상]
70. LOX + BMP-1 enhance collagen deposition/crosslink — PMC6050231 — https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6050231/ — [상]
71. Tyrosinase-mediated hydrogel crosslinking — J Appl Polym Sci — https://onlinelibrary.wiley.com/doi/full/10.1002/app.51887 — [상]
72. Enzyme initiators (HRP vs tyrosinase) for cell encapsulation — Biomater Res — https://link.springer.com/article/10.1186/s40824-016-0077-z — [상]
73. Cross-linking methods of type I collagen scaffolds (cartilage) — PMC8902548 — https://pmc.ncbi.nlm.nih.gov/articles/PMC8902548/ — [상]
74. Genipin and EDC crosslinking of ECM hydrogel (neural) — Sci Rep — https://www.nature.com/articles/s41598-019-47059-x — [상]

---

## 8. 미해결·불확실 항목 (교차검증 충돌 포함)

1. **mTG 평가 충돌 (가장 중요)**: 식품/조직공학계는 mTG를 "무독성·세포친화 우수"로, 면역학계는 "tTG 모방·셀리악 면역원성·잠재 병원성"으로 평가한다. 양측 모두 [상] 출처이나 맥락이 다르며(GRAS=경구·식품 가공보조제, 셀리악=면역학적 mimicry), **임상 오가노이드(이식형)에는 면역원성 경고가 더 직접 관련**된다. 본 보고서는 이를 채택하여 mTG 임상적합성을 "면역원성 평가 전제"로 표기했다. (출처: https://www.fda.gov/media/178428/download | [상] vs https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6297833/ | [상])
2. **Riboflavin 광가교 세포생존**: "높은 생존 유지"(다수)와 "청색광/고광량 가교 후 생존 감소"(일부) 보고가 공존한다. 광량·콜라겐 농도·세포종에 의존하므로 조건 최적화가 필요하다(양측 모두 명시). (출처: https://pmc.ncbi.nlm.nih.gov/articles/PMC11857272/ | [상])
3. **Polyepoxide 항석회화 효과 불일치**: Denacol-fixed 판막은 in-vivo 석회화 개선이 뚜렷하지 않았으나 triglycidylamine은 GA 대비 석회화 감소를 보였다 — 화합물·조건 의존적이다. (출처: https://pubmed.ncbi.nlm.nih.gov/10634948/ | [상])
4. **GMP-grade mTG 정량 스펙**: 재조합 제품의 순도·endotoxin 수치는 벤더 1차자료([중])에 의존하며, 임상 사용 시 lot별 CoA·ancillary material 등급화로 독립 검증이 필요하다. (출처: https://www.amerigoscientific.com/microbial-transglutaminase-production-grade-characterized-for-endotoxin-hcp-dna-sterility-item-55294.html | [중])
5. **Alginate islet 임상 최종 효능**: NCT01736228은 등록·완료가 확인되나(임상 선례 근거 [상]), 최종 효능 수치는 본 검색 범위에서 확정 인용하지 못했다 — 향후 결과 논문 확인 필요. (출처: https://clinicaltrials.gov/study/NCT01736228 | [상])
6. **NovaMatrix anti-fibrotic alginate 인체 효능**: TMTD/zwitterion 변형의 FBR 저감은 설치류·영장류 전임상 데이터([상])이며 **인체 임상 장기 효능은 미확립**이다. (출처: https://www.nature.com/articles/s41467-019-13238-7 | [상])
7. **정량값 원문 재확인 권고**: 일부 정량 수치(예: genipin G' 배수, UV 모듈러스 +150%, DHT 130→355 kPa, Col-Tgel 강성 kPa)는 프록시의 전문(全文) 접근 제한으로 검색 발췌에 의존했으며, 의사결정에 결정적이라면 1차 원문 재확인을 권고한다.

> **QA 주기 결과**: 7개 load-bearing 규제/과학 주장(Photrexa FDA 승인, genipin 5,000~10,000배 저독성, mTG 셀리악 면역원성, GA 판막 표준, alginate islet 임상, EDC 510(k)+integrin 소모, formaldehyde IARC Group 1)이 모두 독립 재검증을 통과했다. Photrexa 1차 승인일은 2016-04-15이며, "모든 시판 판막이 GA"라는 표현은 "GA가 생체판막 가교의 사실상 표준(소 심막·돼지 판엽)"으로 정정·완화하여 반영했다. 본문의 모든 사실 진술은 (출처 URL | 신뢰도) 표기를 충족한다(메커니즘 추론 1건은 [하]로 명시).
