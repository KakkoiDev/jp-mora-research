"""Build the standalone chart. Run from any directory with Python 3."""
from pathlib import Path
from html import escape, unescape
from research import panels, brief

ROOT = Path(__file__).resolve().parent.parent
PROPOSED = {
    0x1B129: 'Hiragana YI', 0x1B12A: 'Hiragana WU',
    0x1B12C: 'Katakana YI', 0x1B12D: 'Katakana YE',
    0x1B12E: 'Katakana WU', 0x1B163: 'Katakana small WU',
}

def glyph(value, small=False):
    value = unescape(value)
    point = ord(value) if len(value) == 1 else 0
    if point in PROPOSED or point == 0x1B001:
        name = PROPOSED.get(point, 'Hiragana YE')
        size_class = ' small-glyph' if small else ''
        if small:
            name += ' (small display variant)'
        # Proposal glyph images avoid unsupported characters and PDF subset fonts.
        return f'<span class="mora proposed-glyph{size_class}" role="img" aria-label="{name}" title="{name} · U+{point:X}" style="--glyph: url(assets/glyphs/{point:x}.png)"></span>'
    return f'<span class="mora" lang="ja">{escape(value)}</span>'

def generate():
    tables = []
    for line in (ROOT / 'data/data.md').read_text().splitlines():
        if line.startswith('## '):
            name = line[3:]
            tables.append(f'<section class="chart"><h2>{name}</h2><table><caption>{name} vowel columns</caption><thead><tr><th scope="col">Row</th>' + ''.join(f'<th scope="col">{v}</th>' for v in 'AIUEO') + '</tr></thead><tbody>')
            row = 0
        elif line.startswith('- '):
            cells = [v.strip() for v in line[2:].split(',')]
            if len(cells) == 3:
                yi, ye = ('&#x1B129;', '&#x1B001;') if name == 'Hiragana' else ('&#x1B12C;', '&#x1B12D;')
                cells = [cells[0], yi, cells[1], ye, cells[2]]
                label = 'Small Y'
            else:
                label = ['Vowels','K','S','T','N','H','M','Y','R','W'][row]
            tables.append(f'<tr><th scope="row">{label}</th>' + ''.join(f'<td>{glyph(c, small=label == "Small Y") if c else "—"}</td>' for c in cells) + '</tr>')
            row += 1
        elif not line.strip() and tables and not tables[-1].endswith('</section>'):
            tables.append('</tbody></table></section>')
    if tables and not tables[-1].endswith('</section>'):
        tables.append('</tbody></table></section>')
    catalog = ''.join(f'<li>{glyph(chr(cp))}<h3>{name}</h3><code>U+{cp:X}</code></li>' for cp, name in {**PROPOSED, 0x1B001: 'Hiragana YE (historical)'}.items())
    page = '''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Japanese Script Research · Kana, Woshite &amp; Katakamuna</title>
<link rel="stylesheet" href="assets/research.css?v=3">
<style>
:root{color-scheme:light;--ink:#272d35;--accent:#a33434;--line:#e0ded9}*{box-sizing:border-box}body{margin:0;background:#f6f5f1;color:var(--ink);font-family:system-ui,sans-serif;line-height:1.6}main{max-width:1100px;margin:auto;padding:48px 24px}header{max-width:720px;margin-bottom:36px}.eyebrow{color:var(--accent);text-transform:uppercase;letter-spacing:.14em;font-size:.75rem;font-weight:700}h1{font-size:clamp(2rem,5vw,3.2rem);line-height:1.15;margin:12px 0 20px}h2{font-size:1.3rem;margin:0 0 20px}p{color:#5b626b}a{color:var(--accent)}.charts{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:24px}.chart{padding:24px;background:white;border:1px solid var(--line);border-radius:12px}table{width:100%;border-collapse:collapse;table-layout:fixed}caption{position:absolute;width:1px;height:1px;overflow:hidden;clip-path:inset(50%)}th,td{text-align:center;border-bottom:1px solid var(--line);height:62px;padding:4px}thead th{height:36px;color:#68707a;font-size:.8rem}tbody th{font-size:.7rem;font-weight:500;color:#68707a;width:48px}td{font-family:'Hiragino Kaku Gothic ProN','Yu Gothic',sans-serif;font-size:32px;font-weight:400}.mora{display:inline-flex;align-items:center;justify-content:center;width:36px;height:36px;vertical-align:middle;font-weight:400;font-synthesis:none;line-height:1}.proposed-glyph{background:currentColor;mask-image:var(--glyph);mask-size:contain;mask-repeat:no-repeat;mask-position:center;-webkit-mask-image:var(--glyph);-webkit-mask-size:contain;-webkit-mask-repeat:no-repeat;-webkit-mask-position:center}.small-glyph{mask-size:85%;-webkit-mask-size:85%;mask-position:60% 65%;-webkit-mask-position:60% 65%}.highlight-control{display:flex;align-items:center;gap:8px;margin-top:24px;font-size:.9rem;cursor:pointer}.highlight-control input{width:18px;height:18px;accent-color:var(--accent)}body:has(#highlight-mora:checked) .proposed-glyph{color:#c52d35}.catalog{margin:40px 0}ul{padding:0;list-style:none;display:grid;grid-template-columns:repeat(3,1fr);gap:16px}li{background:white;border:1px solid var(--line);border-top:3px solid var(--accent);border-radius:8px;padding:24px;text-align:center}li .proposed-glyph{width:36px;height:36px}h3{font-size:.95rem;margin:12px 0 4px}code{font-size:.8rem;color:#68707a}footer{border-top:1px solid var(--line);padding-top:20px;font-size:.85rem}.note{font-size:.9rem}@media(max-width:760px){.charts{grid-template-columns:1fr}main{padding:28px 16px}.chart{padding:16px}ul{grid-template-columns:repeat(2,1fr)}li{padding:16px}}@media(max-width:360px){.chart{padding:10px}th,td{padding:2px}}
</style></head><body><main><header><div class="eyebrow">Japanese kana research</div><h1>Japanese script research</h1><p>Explore kana, Woshite, and Katakamuna through sound tables, glyph references, and the 80 utahi.</p><label class="highlight-control"><input type="checkbox" id="highlight-mora"> Highlight historical and proposed mora in red</label></header><nav class="tabs" role="tablist" aria-label="Writing system"><button id="tab-kana" role="tab" aria-selected="true" aria-controls="panel-kana" data-panel="kana">Hiragana / Katakana</button><button id="tab-woshite" role="tab" aria-selected="false" aria-controls="panel-woshite" data-panel="woshite" tabindex="-1">Woshite</button><button id="tab-katakamuna" role="tab" aria-selected="false" aria-controls="panel-katakamuna" data-panel="katakamuna" tabindex="-1">Katakamuna</button></nav><section id="panel-kana" class="tab-panel" role="tabpanel" aria-labelledby="tab-kana" tabindex="0"><p class="note">The six proposed characters and historical hiragana YE use glyph images from the original document so they display without a special font. Code points below are the proposal’s suggested assignments.</p><a href="docs/missing-japanese-kana-proposal.pdf">Read the original proposal ↗</a><div class="charts">'''
    page += ''.join(tables) + f'</div><section class="catalog"><h2>Proposed glyph catalog</h2><ul>{catalog}</ul></section>'
    page += brief('kana') + '</section>' + panels()
    page += '<footer>Kana proposal by Abraham Gross · January 5, 2020. English briefs and comparative source records are editorial additions.<br>Glyphs reproduced from the bundled proposal, page 2. Hiragana YE is included in the chart as an existing historical kana.</footer></main><script src="assets/research.js"></script></body></html>\n'
    (ROOT / 'index.html').write_text(page, encoding='utf-8')

if __name__ == '__main__':
    generate()
