export const meta = {
  name: 'mtg-research',
  description: 'mTG crosslinker research: landscape scouts -> evidence collectors (Q1/Q2/Q3) -> adversarial verify -> synthesize',
  phases: [
    { title: 'Landscape', detail: 'web-scout each candidate crosslinker' },
    { title: 'Q1', detail: 'rank dominant crosslinker + verify' },
    { title: 'Q2', detail: '9-axis mTG vs dominant + verify' },
    { title: 'Q3', detail: '5-avenue mTG potential + verify' },
    { title: 'Synthesize', detail: 'compose Q1/Q2/Q3 answers from verified ledger' },
  ],
}

const AS_OF = '2026-07-01'

const SRC = {
  type: 'object',
  properties: {
    title: { type: 'string' },
    url: { type: 'string' },
    type: { type: 'string', enum: ['regulatory','systematic_review','peer_reviewed','market_report','manufacturer','news_secondary','other'] },
  },
  required: ['url','type'],
}
const CLAIM = {
  type: 'object',
  properties: {
    id: { type: 'string' },
    question: { type: 'string', enum: ['Q1','Q2','Q3'] },
    topic: { type: 'string' },
    axis: { type: ['string','null'] },
    avenue: { type: ['string','null'] },
    stance: { type: 'string', enum: ['pro','con','neutral','finding'] },
    claim: { type: 'string' },
    evidence: { type: 'string' },
    sources: { type: 'array', items: SRC, minItems: 1 },
    confidence: { type: 'string', enum: ['high','medium','low'] },
  },
  required: ['id','question','topic','stance','claim','evidence','sources','confidence'],
}
const CLAIMS_SCHEMA = { type: 'object', properties: { claims: { type: 'array', items: CLAIM } }, required: ['claims'] }

const LANDSCAPE_SCHEMA = {
  type: 'object',
  properties: {
    topic: { type: 'string' },
    products: { type: 'array', items: { type: 'object', properties: {
      name: { type: 'string' }, maker: { type: 'string' }, approval: { type: 'string' }, indication: { type: 'string' } }, required: ['name'] } },
    mechanism: { type: 'string' },
    market_signals: { type: 'array', items: { type: 'object', properties: { note: { type: 'string' }, url: { type: 'string' } }, required: ['note'] } },
    limitations: { type: 'array', items: { type: 'string' } },
    sources: { type: 'array', items: SRC },
  },
  required: ['topic','products','mechanism','sources'],
}

const VERDICT = {
  type: 'object',
  properties: {
    verified: { type: 'array', items: {
      type: 'object',
      properties: {
        id: { type: 'string' },
        status: { type: 'string', enum: ['confirmed','plausible','refuted','unverified'] },
        confidence: { type: 'string', enum: ['high','medium','low'] },
        note: { type: 'string' },
        extra_sources: { type: 'array', items: SRC },
      },
      required: ['id','status','confidence','note'],
    } },
  },
  required: ['verified'],
}

const CANDIDATES = [
  { id: 'fibrin', desc: 'fibrin sealant: fibrinogen + thrombin, Factor XIIIa crosslink. Products: Tisseel, Evicel, Evarrest, Artiss.' },
  { id: 'gelatin_thrombin', desc: 'flowable gelatin-thrombin hemostat. Products: Floseal, Surgiflo.' },
  { id: 'peg_nhs', desc: 'multi-arm PEG NHS-ester amine crosslink sealant. Products: CoSeal, DuraSeal, Progel, Adherus.' },
  { id: 'glutaraldehyde_albumin', desc: 'BSA + glutaraldehyde surgical adhesive. Product: BioGlue.' },
  { id: 'cyanoacrylate', desc: 'n-butyl / 2-octyl cyanoacrylate tissue adhesive. Products: Dermabond, Histoacryl, Omnex.' },
  { id: 'grf_grfg', desc: 'gelatin-resorcinol-formaldehyde/glutaraldehyde (GRF/GRFG) glue, mainly aortic surgery.' },
]

phase('Landscape')
const landscapes = (await parallel(CANDIDATES.map(c => () =>
  agent(
    `You are a landscape-scout for the crosslinker chemistry "${c.id}" (${c.desc}) used in surgical sealants/hemostats/tissue-adhesives.\n` +
    `Use WebSearch and WebFetch to gather EVIDENCE (real URLs). Collect: (1) leading commercial products + maker, (2) regulatory approvals (FDA 510(k)/PMA number+year, CE, PMDA) and approved indication, (3) the crosslinking mechanism in 1-2 sentences, (4) usage/market-share signals with source URLs (do not assert a single number as fact), (5) known limitations/contraindications.\n` +
    `Prefer regulatory > systematic_review > peer_reviewed > market_report > manufacturer > news_secondary. Do NOT invent facts or URLs; leave unknowns empty. Return the structured object.`,
    { label: `scout:${c.id}`, phase: 'Landscape', schema: LANDSCAPE_SCHEMA, effort: 'medium' }
  )
))).filter(Boolean)

const digest = landscapes.map(l =>
  `## ${l.topic}\nproducts: ${(l.products||[]).map(p => `${p.name}(${p.maker||'?'}; ${p.approval||'?'}; ${p.indication||'?'})`).join('; ')}\nmechanism: ${l.mechanism}\nmarket: ${(l.market_signals||[]).map(m=>m.note).join(' | ')}\nlimits: ${(l.limitations||[]).join(' | ')}`
).join('\n\n')
log(`Landscape done: ${landscapes.length}/${CANDIDATES.length} candidates scouted`)

phase('Q1')
const q1raw = await agent(
  `You are evidence-collector for Q1: "Which crosslinker chemistry is MOST used in sealants/hemostats/tissue-adhesives, by commercial products, regulatory approvals, and market share?"\n\n` +
  `Landscape digest (reuse, verify with WebSearch/WebFetch as needed):\n${digest}\n\n` +
  `Produce ATOMIC claims (question="Q1", topic=the crosslinker chemistry id like fibrin/peg_nhs/cyanoacrylate/gelatin_thrombin/glutaraldehyde_albumin/grf_grfg). For each candidate give claims on breadth of approvals, indications, clinical usage, and market signals. Then produce a small number of comparative/ranking claims (topic="ranking") that triangulate the #1 (do NOT rely on one market number). Every claim needs >=1 real source URL. id format Q1-C001. stance=finding. Be honest about confidence. Return {claims:[...]}.`,
  { label: 'collect:Q1', phase: 'Q1', schema: CLAIMS_SCHEMA, effort: 'high' }
)
const q1claims = (q1raw?.claims || []).map(c => ({ ...c, question: 'Q1' }))
const q1verd = await agent(
  `You are claim-verifier. Adversarially re-check these Q1 claims (independent re-collection, try to REFUTE, downgrade manufacturer-only evidence). For EACH claim id return status(confirmed|plausible|refuted|unverified), confidence, a 1-sentence note, and any extra_sources.\n\nClaims:\n${JSON.stringify(q1claims.map(c=>({id:c.id,claim:c.claim,sources:c.sources})))}`,
  { label: 'verify:Q1', phase: 'Q1', schema: VERDICT, effort: 'high' }
)

const q1Headline = (() => {
  const conf = new Map((q1verd?.verified||[]).map(v => [v.id, v.status]))
  const score = {}
  for (const c of q1claims) {
    if (c.topic === 'ranking') continue
    const st = conf.get(c.id)
    const w = st === 'confirmed' ? 3 : st === 'plausible' ? 1 : 0
    score[c.topic] = (score[c.topic]||0) + w + (c.confidence==='high'?1:0)
  }
  const top = Object.entries(score).sort((a,b)=>b[1]-a[1])[0]
  return top ? top[0] : 'fibrin'
})()
log(`Q1 leading crosslinker (evidence-weighted): ${q1Headline}`)

const AXES = [
  ['gelation','gelation trigger/conditions/speed'],
  ['mechanical','tensile/shear/adhesive strength, burst pressure'],
  ['cytotoxicity','cytotoxicity & biocompatibility'],
  ['blood_dependency','dependence on blood-derived components (fibrinogen/thrombin)'],
  ['immunogenicity','immunogenicity incl. mimicry of tissue tTG (autoantigen) / anti-mTG antibody debate'],
  ['degradation','absorption/degradation behavior'],
  ['gmp_supply','GMP raw-material supply, purity, food-grade vs medical-grade'],
  ['regulatory','regulatory pathway (enzyme-as-material issues)'],
  ['cost','cost of goods / manufacturing cost'],
]
const q2results = await pipeline(
  AXES,
  ([axis, d]) => agent(
    `You are evidence-collector for Q2 axis "${axis}" (${d}). Compare microbial transglutaminase (mTG) AGAINST the dominant surgical crosslinkers (leading one is ~"${q1Headline}"; also reference fibrin, PEG-NHS, cyanoacrylate as relevant).\n` +
    `Use WebSearch/WebFetch. Produce ATOMIC claims (question="Q2", topic="mtg", axis="${axis}") capturing BOTH pro (stance=pro) and con (stance=con) of mTG on this axis, each vs a named comparator, each with >=1 real source URL. For immunogenicity include BOTH sides of the tTG-mimicry debate as separate claims. id format Q2-${axis}-C01. Return {claims:[...]}.`,
    { label: `collect:Q2:${axis}`, phase: 'Q2', schema: CLAIMS_SCHEMA, effort: 'high' }
  ).then(r => (r?.claims||[]).map(c => ({ ...c, question:'Q2', topic:'mtg', axis }))),
  (claims, [axis]) => claims.length ? agent(
    `You are claim-verifier. Adversarially re-check these Q2 (${axis}) mTG claims. Try to refute; downgrade manufacturer-only or weak single-source claims. For each id return status/confidence/note/extra_sources.\n\n${JSON.stringify(claims.map(c=>({id:c.id,stance:c.stance,claim:c.claim,sources:c.sources})))}`,
    { label: `verify:Q2:${axis}`, phase: 'Q2', schema: VERDICT, effort: 'medium' }
  ).then(v => ({ claims, verd: v?.verified||[] })) : { claims, verd: [] }
)

const AVENUES = [
  ['enzyme_engineering','low-immunogenicity / site-specific mTG variants, zymogen, recombinant production'],
  ['dual_crosslink','dual crosslinking e.g. GelMA photo + mTG, PEG/mTG combinations'],
  ['biomimetic_clotting','biomimetic Factor XIIIa clot-mimicking design'],
  ['indication_fit','fit for resorbable/topical/temporary vs permanent indications'],
  ['supply_scaleup','supply chain, scale-up, cost competitiveness'],
]
const q3results = await pipeline(
  AVENUES,
  ([av, d]) => agent(
    `You are evidence-collector for Q3 avenue "${av}" (${d}): the technical POTENTIAL of microbial transglutaminase (mTG) for surgical sealants/hemostats/adhesives.\n` +
    `Use WebSearch/WebFetch. Produce ATOMIC claims (question="Q3", topic="mtg", avenue="${av}") with real source URLs, honest confidence, no hype. Note both promise and open problems. id format Q3-${av}-C01. stance=finding|pro|con. Return {claims:[...]}.`,
    { label: `collect:Q3:${av}`, phase: 'Q3', schema: CLAIMS_SCHEMA, effort: 'high' }
  ).then(r => (r?.claims||[]).map(c => ({ ...c, question:'Q3', topic:'mtg', avenue: av }))),
  (claims, [av]) => claims.length ? agent(
    `You are claim-verifier. Adversarially re-check these Q3 (${av}) mTG-potential claims. Distinguish demonstrated vs speculative. For each id return status/confidence/note/extra_sources.\n\n${JSON.stringify(claims.map(c=>({id:c.id,claim:c.claim,sources:c.sources})))}`,
    { label: `verify:Q3:${av}`, phase: 'Q3', schema: VERDICT, effort: 'medium' }
  ).then(v => ({ claims, verd: v?.verified||[] })) : { claims, verd: [] }
)

function applyVerd(claims, verdList) {
  const m = new Map((verdList||[]).map(v => [v.id, v]))
  return claims.map(c => {
    const v = m.get(c.id)
    const extra = (v?.extra_sources||[]).filter(s => s && s.url)
    return {
      ...c,
      avenue: c.avenue ?? null,
      axis: c.axis ?? null,
      confidence: v?.confidence || c.confidence,
      sources: [...(c.sources||[]), ...extra],
      verification: { status: v?.status || 'unverified', note: v?.note || '' },
      collected_at: AS_OF,
    }
  })
}

const allClaims = [
  ...applyVerd(q1claims, q1verd?.verified),
  ...q2results.filter(Boolean).flatMap(r => applyVerd(r.claims, r.verd)),
  ...q3results.filter(Boolean).flatMap(r => applyVerd(r.claims, r.verd)),
]

phase('Synthesize')
const forSynth = allClaims.filter(c => c.verification.status !== 'refuted')
const answers = await agent(
  `You are synthesizer. Using ONLY the verified claim ledger below (do not add outside facts), compose conclusions for three questions. Prefer confirmed>plausible; note conflicts (esp. immunogenicity) and lower confidence accordingly. Write headline/body/bullets in KOREAN (product/regulatory/chemical names in original).\n\n` +
  `Q1: which crosslinker chemistry is MOST used (triangulate approvals+indications+clinical practice+market; the evidence-weighted lead is "${q1Headline}").\n` +
  `Q2: mTG's pros/cons vs the dominant crosslinker across 9 axes (say where mTG wins and loses).\n` +
  `Q3: mTG's technical potential across 5 avenues (promise vs open problems).\n\n` +
  `LEDGER (${forSynth.length} claims):\n${JSON.stringify(forSynth.map(c=>({id:c.id,q:c.question,topic:c.topic,axis:c.axis,avenue:c.avenue,stance:c.stance,claim:c.claim,conf:c.confidence,ver:c.verification.status})))}\n\n` +
  `Return an object with as_of="${AS_OF}" and Q1/Q2/Q3 each {headline, body, bullets:[...], confidence} plus a top-level caveats string. Where evidence is thin, say "근거 불충분" and lower confidence.`,
  {
    label: 'synthesize', phase: 'Synthesize', effort: 'high',
    schema: {
      type: 'object',
      properties: {
        as_of: { type: 'string' },
        Q1: { type: 'object', properties: { headline:{type:'string'}, body:{type:'string'}, bullets:{type:'array',items:{type:'string'}}, confidence:{type:'string'} }, required:['headline','body','bullets','confidence'] },
        Q2: { type: 'object', properties: { headline:{type:'string'}, body:{type:'string'}, bullets:{type:'array',items:{type:'string'}}, confidence:{type:'string'} }, required:['headline','body','bullets','confidence'] },
        Q3: { type: 'object', properties: { headline:{type:'string'}, body:{type:'string'}, bullets:{type:'array',items:{type:'string'}}, confidence:{type:'string'} }, required:['headline','body','bullets','confidence'] },
        caveats: { type: 'string' },
      },
      required: ['as_of','Q1','Q2','Q3','caveats'],
    },
  }
)

return { as_of: AS_OF, q1Headline, landscape_count: landscapes.length, claims: allClaims, answers }
