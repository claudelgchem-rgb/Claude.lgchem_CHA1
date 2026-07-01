#!/usr/bin/env python3
"""build_report.py — 원장(claims.jsonl) + 합성(answers.json) → report/index.html.

사람이 아니라 코드가 원장을 렌더한다. 모든 claim 은 근거·출처·신뢰도·검증상태와
함께 표시되고, 세 질문의 결론(answers.json)이 상단 요약으로 붙는다.

  python scripts/build_report.py \
      --ledger ledger/claims.jsonl \
      --answers work/03_synthesis/answers.json \
      --out report/index.html
"""
from __future__ import annotations
import argparse, html, json
from pathlib import Path
from collections import defaultdict

CONF_BADGE = {"high": ("높음", "#0a7d28"), "medium": ("중간", "#b58100"),
              "low": ("낮음", "#b53535")}
VER_BADGE  = {"confirmed": ("검증됨", "#0a7d28"), "plausible": ("개연적", "#2b6cb0"),
              "refuted": ("반증됨", "#b53535"), "unverified": ("미검증", "#777")}
SRC_LABEL  = {"regulatory": "규제", "systematic_review": "메타분석",
              "peer_reviewed": "논문", "market_report": "시장", "manufacturer": "제조사",
              "news_secondary": "2차보도", "other": "기타"}


def esc(x) -> str:
    return html.escape(str(x if x is not None else ""))


def load_ledger(path: str) -> list[dict]:
    p = Path(path)
    if not p.exists():
        return []
    out = []
    for line in p.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            out.append(json.loads(line))
    return out


def load_answers(path: str) -> dict:
    p = Path(path)
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}


def badge(text, color):
    return (f'<span style="display:inline-block;padding:1px 7px;border-radius:9px;'
            f'font-size:11px;font-weight:600;color:#fff;background:{color}">{esc(text)}</span>')


def sources_html(srcs):
    items = []
    for s in srcs or []:
        lbl = SRC_LABEL.get(s.get("type"), s.get("type") or "출처")
        title = esc(s.get("title") or s.get("url"))
        url = esc(s.get("url"))
        items.append(f'<li><span class="stype">{esc(lbl)}</span> '
                     f'<a href="{url}" target="_blank" rel="noopener">{title}</a></li>')
    return '<ul class="srcs">' + "".join(items) + "</ul>" if items else ""


def claim_card(r):
    cb = CONF_BADGE.get(r.get("confidence"), ("?", "#777"))
    vb = VER_BADGE.get((r.get("verification") or {}).get("status"), ("?", "#777"))
    axis = r.get("axis") or r.get("avenue") or r.get("topic") or ""
    stance = r.get("stance", "")
    stance_col = {"pro": "#0a7d28", "con": "#b53535",
                  "neutral": "#555", "finding": "#2b6cb0"}.get(stance, "#555")
    vnote = (r.get("verification") or {}).get("note")
    return f"""
    <div class="claim">
      <div class="chead">
        <code>{esc(r.get('id'))}</code>
        <span class="axis">{esc(axis)}</span>
        {badge(stance.upper(), stance_col)}
        {badge("신뢰 "+cb[0], cb[1])}
        {badge(vb[0], vb[1])}
      </div>
      <div class="ctext">{esc(r.get('claim'))}</div>
      {f'<div class="eviden">근거: {esc(r.get("evidence"))}</div>' if r.get('evidence') else ''}
      {f'<div class="vnote">검증 메모: {esc(vnote)}</div>' if vnote else ''}
      {sources_html(r.get('sources'))}
    </div>"""


def answer_block(ans: dict, qkey: str, title: str):
    a = ans.get(qkey) or {}
    headline = a.get("headline") or a.get("answer") or "(합성 결과 없음)"
    body = a.get("body") or ""
    bullets = a.get("bullets") or []
    bl = "".join(f"<li>{esc(b)}</li>" for b in bullets)
    conf = a.get("confidence")
    cb = CONF_BADGE.get(conf)
    conf_html = f' {badge("결론 신뢰 "+cb[0], cb[1])}' if cb else ""
    return f"""
    <section class="answer">
      <h3>{esc(title)}{conf_html}</h3>
      <p class="headline">{esc(headline)}</p>
      {f'<p>{esc(body)}</p>' if body else ''}
      {f'<ul>{bl}</ul>' if bl else ''}
    </section>"""


def q1_table(claims):
    """Q1 후보별 랭킹 표 (topic 단위 집계)."""
    rows = [c for c in claims if c.get("question") == "Q1"]
    by_topic = defaultdict(list)
    for c in rows:
        by_topic[c.get("topic")].append(c)
    if not by_topic:
        return ""
    trs = []
    for topic, cs in sorted(by_topic.items(),
                            key=lambda kv: -len(kv[1])):
        n = len(cs)
        hi = sum(1 for c in cs if c.get("confidence") == "high")
        trs.append(f"<tr><td><b>{esc(topic)}</b></td><td>{n}</td>"
                   f"<td>{hi}</td></tr>")
    return ("<table class='tbl'><thead><tr><th>가교 화학(topic)</th>"
            "<th>claim 수</th><th>high 신뢰</th></tr></thead><tbody>"
            + "".join(trs) + "</tbody></table>")


def render(claims, answers):
    by_q = defaultdict(list)
    for c in claims:
        by_q[c.get("question")].append(c)

    n = len(claims)
    n_hi = sum(1 for c in claims if c.get("confidence") == "high")
    n_conf = sum(1 for c in claims
                 if (c.get("verification") or {}).get("status") == "confirmed")
    generated = answers.get("as_of") or answers.get("generated") or ""

    def q_section(qkey, title):
        cs = by_q.get(qkey, [])
        # Q2 는 축, Q3 는 방면으로 그룹
        group_key = {"Q2": "axis", "Q3": "avenue"}.get(qkey, "topic")
        groups = defaultdict(list)
        for c in cs:
            groups[c.get(group_key) or c.get("topic") or "기타"].append(c)
        blocks = []
        for g, gcs in groups.items():
            cards = "".join(claim_card(c) for c in gcs)
            blocks.append(f'<div class="grp"><h4>{esc(g)} '
                          f'<span class="gn">({len(gcs)})</span></h4>{cards}</div>')
        extra = q1_table(cs) if qkey == "Q1" else ""
        return f"""
        <section id="{qkey}">
          <h2>{esc(title)} <span class="gn">· claim {len(cs)}건</span></h2>
          {extra}
          {''.join(blocks)}
        </section>"""

    return f"""<!doctype html>
<html lang="ko"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>mTG 가교제 리서치 보고서</title>
<style>
 :root {{ --fg:#1a1a1a; --mut:#666; --line:#e2e2e2; --bg:#fafafa; }}
 * {{ box-sizing:border-box; }}
 body {{ font-family:-apple-system,'Segoe UI',Roboto,'Noto Sans KR',sans-serif;
   color:var(--fg); background:var(--bg); margin:0; line-height:1.6; }}
 .wrap {{ max-width:960px; margin:0 auto; padding:32px 20px 80px; }}
 header.top {{ border-bottom:3px solid #111; padding-bottom:16px; margin-bottom:8px; }}
 header.top h1 {{ margin:0 0 4px; font-size:26px; }}
 .meta {{ color:var(--mut); font-size:13px; }}
 .stat {{ display:inline-block; margin:14px 14px 0 0; font-size:13px;
   background:#fff; border:1px solid var(--line); border-radius:8px; padding:8px 12px; }}
 .stat b {{ font-size:18px; }}
 nav a {{ margin-right:14px; font-size:13px; text-decoration:none; color:#2b6cb0; }}
 h2 {{ margin-top:40px; border-bottom:2px solid var(--line); padding-bottom:6px; }}
 h3 {{ margin:18px 0 6px; }}
 h4 {{ margin:22px 0 4px; color:#333; }}
 .gn {{ color:var(--mut); font-weight:400; font-size:13px; }}
 section.answer {{ background:#fff; border:1px solid var(--line); border-left:4px solid #111;
   border-radius:8px; padding:14px 18px; margin:14px 0; }}
 .headline {{ font-weight:700; font-size:16px; margin:4px 0; }}
 .claim {{ background:#fff; border:1px solid var(--line); border-radius:8px;
   padding:12px 14px; margin:10px 0; }}
 .chead {{ display:flex; gap:8px; align-items:center; flex-wrap:wrap; margin-bottom:6px; }}
 .chead code {{ background:#f0f0f0; padding:1px 6px; border-radius:5px; font-size:12px; }}
 .axis {{ font-size:12px; color:var(--mut); text-transform:uppercase; letter-spacing:.03em; }}
 .ctext {{ font-size:15px; }}
 .eviden {{ font-size:13px; color:#444; margin-top:6px; }}
 .vnote {{ font-size:12px; color:#8a5a00; margin-top:4px; }}
 ul.srcs {{ margin:8px 0 0; padding-left:18px; font-size:12.5px; }}
 ul.srcs .stype {{ display:inline-block; min-width:44px; color:var(--mut);
   font-size:11px; text-transform:uppercase; }}
 table.tbl {{ border-collapse:collapse; width:100%; margin:12px 0; font-size:14px; background:#fff; }}
 table.tbl th, table.tbl td {{ border:1px solid var(--line); padding:6px 10px; text-align:left; }}
 table.tbl thead {{ background:#f2f2f2; }}
 footer {{ margin-top:60px; color:var(--mut); font-size:12px; border-top:1px solid var(--line); padding-top:14px; }}
</style></head>
<body><div class="wrap">
 <header class="top">
   <h1>mTG 가교제 리서치 보고서</h1>
   <div class="meta">실런트·지혈재·조직접착제 산업의 가교 화학, mTG 대비 우열, 그리고 잠재력 · 생성일 {esc(generated)}</div>
   <div>
     <span class="stat"><b>{n}</b> claim</span>
     <span class="stat"><b>{n_hi}</b> 高신뢰</span>
     <span class="stat"><b>{n_conf}</b> 검증완료</span>
   </div>
 </header>
 <nav>
   <a href="#summary">요약(결론)</a><a href="#Q1">Q1 지배 가교제</a>
   <a href="#Q2">Q2 mTG 대비</a><a href="#Q3">Q3 잠재력</a>
 </nav>

 <section id="summary">
   <h2>Executive Summary — 세 질문의 결론</h2>
   {answer_block(answers, 'Q1', 'Q1. 가장 많이 쓰이는 가교제')}
   {answer_block(answers, 'Q2', 'Q2. 대표 가교제 대비 mTG 장단점')}
   {answer_block(answers, 'Q3', 'Q3. mTG의 기술적 잠재력')}
   {f'<p class="meta">{esc(answers.get("caveats"))}</p>' if answers.get('caveats') else ''}
 </section>

 {q_section('Q1', 'Q1 · 지배적 가교 화학의 근거 원장')}
 {q_section('Q2', 'Q2 · mTG vs 대표 가교제 (다축 비교)')}
 {q_section('Q3', 'Q3 · mTG 잠재력 (기술 방면별)')}

 <footer>
   본 보고서는 mTG 리서치 하니스가 웹 근거를 claim 단위로 수집·검증해 자동 생성했다.
   각 claim 의 신뢰도/검증상태 배지와 출처 링크를 함께 검토하라. 시장 수치는 2차 출처
   비중이 높아 방향성 근거로만 사용한다.
 </footer>
</div></body></html>"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ledger", default="ledger/claims.jsonl")
    ap.add_argument("--answers", default="work/03_synthesis/answers.json")
    ap.add_argument("--out", default="report/index.html")
    a = ap.parse_args()
    claims = load_ledger(a.ledger)
    answers = load_answers(a.answers)
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(render(claims, answers), encoding="utf-8")
    print(f"wrote {a.out}  ({len(claims)} claims)")


if __name__ == "__main__":
    main()
