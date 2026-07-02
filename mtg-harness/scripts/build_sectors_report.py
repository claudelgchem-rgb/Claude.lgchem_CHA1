#!/usr/bin/env python3
"""build_sectors_report.py — TG 적용 섹터 원장 → report/tg-sectors.html.

생체 조직 접합/점착이 유용한 섹터 + 일반 TG 활용 영역을 claim 단위로 렌더한다.
모든 레코드에 근거(evidence)·출처 링크·신뢰도(상/중/하)·검증상태를 UI 로 명문화한다.

  python scripts/build_sectors_report.py \
      --ledger ledger/tg_sectors.jsonl \
      --synth work/06_sectors_synth/recommendation.json \
      --out report/tg-sectors.html
"""
from __future__ import annotations
import argparse, html, json
from pathlib import Path
from collections import defaultdict

# 신뢰도 상/중/하 (status palette: good/warning/critical) + 아이콘(색 단독 금지)
CONF = {
    "high":   ("상", "#0ca30c", "●●●"),
    "medium": ("중", "#eda100", "●●○"),
    "low":    ("하", "#d03b3b", "●○○"),
}
VER = {
    "confirmed":  ("검증", "#0ca30c"),
    "plausible":  ("개연", "#2a78d6"),
    "refuted":    ("반증", "#d03b3b"),
    "unverified": ("미검", "#898781"),
}
REC = {  # 추천도 (ordinal state)
    "strong":   ("강력 추천", "#2a78d6"),
    "moderate": ("검토 권장", "#1baf7a"),
    "watch":    ("관망", "#898781"),
}
DOMAIN_KO = {
    "medical": "의료·임상 접착",
    "tissue_eng": "조직공학·바이오제작·바이오인터페이스",
    "food_industrial": "식품·산업 바이오접착",
    "hair": "모발 (발모 가설 포함)",
    "biotech": "바이오텍 툴 (ADC·표지·고정)",
    "therapeutic": "치료·진단 (TG2 억제 등)",
}
SRC_LABEL = {"regulatory": "규제", "systematic_review": "메타분석", "peer_reviewed": "논문",
             "market_report": "시장", "manufacturer": "제조사", "patent": "특허",
             "news_secondary": "2차보도", "other": "기타"}
REC_ORDER = {"strong": 3, "moderate": 2, "watch": 1}
CONF_ORDER = {"high": 3, "medium": 2, "low": 1}


def esc(x) -> str:
    return html.escape(str(x if x is not None else ""))


def load_jsonl(path: str) -> list[dict]:
    p = Path(path)
    if not p.exists():
        return []
    return [json.loads(l) for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]


def load_json(path: str) -> dict:
    p = Path(path)
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}


def pill(text, color, fg="#fff"):
    return (f'<span class="pill" style="background:{color};color:{fg}">{esc(text)}</span>')


def outline_pill(text, color):
    return (f'<span class="pill out" style="color:{color};border-color:{color}">{esc(text)}</span>')


def score(r):
    s = REC_ORDER.get(r.get("recommendation"), 1) * CONF_ORDER.get(r.get("confidence"), 1)
    if (r.get("verification") or {}).get("status") == "confirmed":
        s += 2
    if (r.get("verification") or {}).get("status") == "refuted":
        s -= 3
    return s


def sources_html(srcs):
    items = []
    for s in srcs or []:
        lbl = SRC_LABEL.get(s.get("type"), s.get("type") or "출처")
        title = esc(s.get("title") or s.get("url"))
        url = esc(s.get("url"))
        items.append(f'<li><span class="stype">{esc(lbl)}</span> '
                     f'<a href="{url}" target="_blank" rel="noopener">{title}</a></li>')
    return '<ul class="srcs">' + "".join(items) + "</ul>" if items else ""


def card(r):
    conf = CONF.get(r.get("confidence"), ("?", "#898781", "○"))
    ver = VER.get((r.get("verification") or {}).get("status"), ("?", "#898781"))
    rec = REC.get(r.get("recommendation"), ("", "#898781"))
    vnote = (r.get("verification") or {}).get("note")
    mat = r.get("maturity")
    tgt = r.get("tg_type")
    return f"""
    <div class="card">
      <div class="chead">
        <span class="sector">{esc(r.get('sector'))}</span>
        <span class="spacer"></span>
        <span class="conf" title="신뢰도 {esc(conf[0])}" style="color:{conf[1]}">
          <span class="dots">{conf[2]}</span> 신뢰 {esc(conf[0])}</span>
      </div>
      <div class="chips">
        {pill(rec[0], rec[1]) if rec[0] else ''}
        {outline_pill('성숙도: '+esc(mat), '#52514e') if mat else ''}
        {outline_pill('TG: '+esc(tgt), '#4a3aa7') if tgt else ''}
        {pill(ver[0], ver[1])}
        <code class="cid">{esc(r.get('id'))}</code>
      </div>
      <div class="opp"><b>기회</b> · {esc(r.get('opportunity'))}</div>
      <div class="fit"><b>TG 적합성</b> · {esc(r.get('tg_fit'))}</div>
      {f'<div class="evi"><b>근거</b> · {esc(r.get("evidence"))}</div>' if r.get('evidence') else ''}
      {f'<div class="vnote">검증 메모 · {esc(vnote)}</div>' if vnote else ''}
      {sources_html(r.get('sources'))}
    </div>"""


def domain_chart(recs):
    """도메인별 레코드 수를 추천도로 스택한 수평 막대 (범례 + 직접 라벨)."""
    by_dom = defaultdict(lambda: defaultdict(int))
    for r in recs:
        by_dom[r.get("domain")][r.get("recommendation") or "watch"] += 1
    if not by_dom:
        return ""
    maxn = max(sum(v.values()) for v in by_dom.values())
    order = sorted(by_dom.items(), key=lambda kv: -sum(kv[1].values()))
    rows = []
    for dom, counts in order:
        total = sum(counts.values())
        segs = []
        for rk in ("strong", "moderate", "watch"):
            c = counts.get(rk, 0)
            if not c:
                continue
            w = c / maxn * 100
            col = REC[rk][1]
            segs.append(f'<span class="seg" style="width:{w:.2f}%;background:{col}" '
                        f'title="{REC[rk][0]} {c}"></span>')
        rows.append(
            f'<div class="brow"><div class="blabel">{esc(DOMAIN_KO.get(dom, dom))}</div>'
            f'<div class="btrack">{"".join(segs)}<span class="bnum">{total}</span></div></div>')
    legend = "".join(
        f'<span class="lg"><span class="sw" style="background:{REC[k][1]}"></span>{REC[k][0]}</span>'
        for k in ("strong", "moderate", "watch"))
    return (f'<div class="chart"><div class="legend">{legend}</div>{"".join(rows)}</div>')


def rec_block(synth):
    if not synth:
        return ""
    parts = [f'<p class="headline">{esc(synth.get("headline",""))}</p>']
    if synth.get("hair_verdict"):
        parts.append(f'<div class="callout"><h4>🧪 발모 가설 검증 (사용자 질문)</h4>'
                     f'<p>{esc(synth["hair_verdict"])}</p></div>')
    if synth.get("general_tg_summary"):
        parts.append(f'<p><b>일반 TG 활용 지형</b> · {esc(synth["general_tg_summary"])}</p>')
    tops = synth.get("top_sectors") or []
    if tops:
        lis = "".join(f'<li><b>{esc(t.get("sector",""))}</b> — {esc(t.get("why",""))}'
                      f'{" " + pill("신뢰 "+CONF.get(t.get("confidence","medium"),["중"])[0], CONF.get(t.get("confidence","medium"),["","#898781"])[1]) if t.get("confidence") else ""}</li>'
                      for t in tops)
        parts.append(f'<div class="tops"><b>가장 추천하는 섹터</b><ol>{lis}</ol></div>')
    if synth.get("caveats"):
        parts.append(f'<p class="meta">{esc(synth["caveats"])}</p>')
    return "".join(parts)


def render(recs, synth):
    n = len(recs)
    n_hi = sum(1 for r in recs if r.get("confidence") == "high")
    n_strong = sum(1 for r in recs if r.get("recommendation") == "strong")
    n_dom = len({r.get("domain") for r in recs})
    generated = synth.get("as_of") or "2026-07-02"

    # 도메인별 카드 (도메인 내 점수 내림차순)
    by_dom = defaultdict(list)
    for r in recs:
        by_dom[r.get("domain")].append(r)
    dom_sections = []
    for dom in sorted(by_dom, key=lambda d: -sum(score(x) for x in by_dom[d])):
        cs = sorted(by_dom[dom], key=score, reverse=True)
        dom_sections.append(
            f'<section id="dom-{esc(dom)}"><h2>{esc(DOMAIN_KO.get(dom, dom))} '
            f'<span class="gn">· {len(cs)}건</span></h2>{"".join(card(c) for c in cs)}</section>')

    # 전체 상위 추천 (교차 도메인)
    top = sorted([r for r in recs if r.get("recommendation") == "strong"],
                 key=score, reverse=True)[:8]
    top_rows = "".join(
        f'<tr><td>{esc(r.get("sector"))}</td><td>{esc(DOMAIN_KO.get(r.get("domain"),r.get("domain")))}</td>'
        f'<td style="color:{CONF.get(r.get("confidence"),["","#898781"])[1]}">{CONF.get(r.get("confidence"),["?"])[0]}</td>'
        f'<td>{esc(r.get("maturity"))}</td></tr>' for r in top)

    nav = "".join(f'<a href="#dom-{esc(d)}">{esc(DOMAIN_KO.get(d,d))}</a>'
                  for d in sorted(by_dom, key=lambda d: -sum(score(x) for x in by_dom[d])))

    return f"""<!doctype html>
<html lang="ko"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>TG 적용 섹터 지도 — 조직 접합·점착 기회 및 일반 TG 활용</title>
<style>
 :root {{
   --surface:#fcfcfb; --plane:#f9f9f7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
   --line:#e1e0d9; --border:rgba(11,11,11,.10);
 }}
 @media (prefers-color-scheme: dark) {{
   :root {{ --surface:#1a1a19; --plane:#0d0d0d; --ink:#fff; --ink2:#c3c2b7; --muted:#898781;
     --line:#2c2c2a; --border:rgba(255,255,255,.10); }}
 }}
 * {{ box-sizing:border-box; }}
 body {{ font-family:system-ui,-apple-system,"Segoe UI","Noto Sans KR",sans-serif;
   color:var(--ink); background:var(--plane); margin:0; line-height:1.6; }}
 .wrap {{ max-width:1000px; margin:0 auto; padding:32px 20px 90px; }}
 header.top {{ border-bottom:3px solid var(--ink); padding-bottom:16px; }}
 header.top h1 {{ margin:0 0 4px; font-size:25px; }}
 .meta {{ color:var(--muted); font-size:13px; }}
 .kpis {{ display:flex; gap:12px; flex-wrap:wrap; margin:16px 0 4px; }}
 .kpi {{ background:var(--surface); border:1px solid var(--border); border-radius:10px;
   padding:10px 16px; min-width:120px; }}
 .kpi b {{ font-size:22px; display:block; }}
 .kpi span {{ font-size:12px; color:var(--ink2); }}
 nav {{ margin:10px 0 0; }}
 nav a {{ margin:0 12px 6px 0; font-size:12.5px; text-decoration:none; color:#2a78d6;
   display:inline-block; }}
 section.summary {{ background:var(--surface); border:1px solid var(--border);
   border-left:4px solid var(--ink); border-radius:10px; padding:16px 20px; margin:18px 0; }}
 .headline {{ font-weight:700; font-size:17px; }}
 .callout {{ background:var(--plane); border:1px solid var(--line); border-radius:8px;
   padding:10px 14px; margin:12px 0; }}
 .callout h4 {{ margin:0 0 4px; }}
 .tops ol {{ margin:6px 0 0; padding-left:20px; }} .tops li {{ margin:4px 0; }}
 h2 {{ margin:38px 0 8px; border-bottom:2px solid var(--line); padding-bottom:6px; font-size:19px; }}
 .gn {{ color:var(--muted); font-weight:400; font-size:13px; }}
 .chart {{ background:var(--surface); border:1px solid var(--border); border-radius:10px;
   padding:14px 16px; margin:14px 0 6px; }}
 .legend {{ margin-bottom:10px; font-size:12px; color:var(--ink2); }}
 .lg {{ margin-right:14px; }} .sw {{ display:inline-block; width:11px; height:11px; border-radius:3px;
   margin-right:4px; vertical-align:-1px; }}
 .brow {{ display:flex; align-items:center; gap:10px; margin:5px 0; }}
 .blabel {{ width:220px; font-size:12.5px; color:var(--ink2); text-align:right; flex:none; }}
 .btrack {{ flex:1; display:flex; align-items:center; height:18px; }}
 .seg {{ height:18px; margin-right:2px; border-radius:3px; }}
 .bnum {{ font-size:11px; color:var(--muted); margin-left:6px; font-variant-numeric:tabular-nums; }}
 table.top {{ border-collapse:collapse; width:100%; margin:10px 0; font-size:13.5px; background:var(--surface); }}
 table.top th, table.top td {{ border:1px solid var(--line); padding:6px 10px; text-align:left; }}
 table.top thead {{ background:var(--plane); }}
 .card {{ background:var(--surface); border:1px solid var(--border); border-radius:10px;
   padding:13px 16px; margin:11px 0; }}
 .chead {{ display:flex; align-items:baseline; gap:10px; }}
 .sector {{ font-weight:700; font-size:15.5px; }}
 .spacer {{ flex:1; }}
 .conf {{ font-size:12.5px; font-weight:600; white-space:nowrap; }}
 .conf .dots {{ letter-spacing:1px; }}
 .chips {{ display:flex; gap:6px; flex-wrap:wrap; align-items:center; margin:7px 0 8px; }}
 .pill {{ font-size:11px; font-weight:600; padding:1px 8px; border-radius:9px; }}
 .pill.out {{ background:transparent; border:1px solid; font-weight:600; }}
 .cid {{ font-size:11px; color:var(--muted); background:var(--plane); padding:1px 6px; border-radius:5px; }}
 .opp, .fit, .evi {{ font-size:13.5px; margin:3px 0; }}
 .opp b, .fit b, .evi b {{ color:var(--ink2); font-size:12px; }}
 .vnote {{ font-size:12px; color:#8a5a00; margin-top:4px; }}
 @media (prefers-color-scheme: dark) {{ .vnote {{ color:#e0a83a; }} }}
 ul.srcs {{ margin:8px 0 0; padding-left:18px; font-size:12px; }}
 ul.srcs .stype {{ display:inline-block; min-width:44px; color:var(--muted); font-size:11px; }}
 footer {{ margin-top:56px; color:var(--muted); font-size:12px; border-top:1px solid var(--line); padding-top:14px; }}
</style></head>
<body><div class="wrap">
 <header class="top">
   <h1>TG 적용 섹터 지도 — 조직 접합·점착 기회 & 일반 TG 활용 영역</h1>
   <div class="meta">생체 조직을 접합/점착하면 유용한 섹터 추천 + mTG 를 넘어 일반 transglutaminase(TG)가 쓰일 수 있는 영역 · 생성일 {esc(generated)}</div>
   <div class="kpis">
     <div class="kpi"><b>{n}</b><span>조사 섹터/활용 레코드</span></div>
     <div class="kpi"><b>{n_dom}</b><span>도메인</span></div>
     <div class="kpi"><b>{n_strong}</b><span>강력 추천</span></div>
     <div class="kpi"><b>{n_hi}</b><span>신뢰도 상</span></div>
   </div>
   <nav>{nav}</nav>
 </header>

 <section class="summary">
   <h2 style="border:none;margin:0 0 6px">종합 추천 & 결론</h2>
   {rec_block(synth) or '<p class="meta">(합성 요약 없음 — 아래 섹터 원장을 직접 검토)</p>'}
 </section>

 <h2 style="margin-top:26px">도메인별 조사 분포 <span class="gn">(추천도 스택)</span></h2>
 {domain_chart(recs)}

 <h2>교차 도메인 상위 추천 섹터</h2>
 <table class="top"><thead><tr><th>섹터</th><th>도메인</th><th>신뢰도</th><th>성숙도</th></tr></thead>
 <tbody>{top_rows}</tbody></table>

 {"".join(dom_sections)}

 <footer>
   본 보고서는 TG 리서치 하니스가 웹 근거를 섹터/활용 단위로 수집·적대 검증해 자동 생성했다.
   각 레코드의 신뢰도(상/중/하)·검증 배지·출처 링크를 함께 검토하라. '강력 추천/검토 권장/관망'은
   근거 강도와 성숙도에 대한 하니스의 판단이며, 시장·규제는 as_of {esc(generated)} 이후 변동될 수 있다.
 </footer>
</div></body></html>"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ledger", default="ledger/tg_sectors.jsonl")
    ap.add_argument("--synth", default="work/06_sectors_synth/recommendation.json")
    ap.add_argument("--out", default="report/tg-sectors.html")
    a = ap.parse_args()
    recs = load_jsonl(a.ledger)
    synth = load_json(a.synth)
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(render(recs, synth), encoding="utf-8")
    print(f"wrote {a.out}  ({len(recs)} records)")


if __name__ == "__main__":
    main()
