"""Source-backed Woshite and Katakamuna research panels."""
import json
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KATA_SOURCE = 'https://katakamuna-note.com/katakamuna-phontlist/26/'
WOSH_SOURCE = 'https://commons.wikimedia.org/wiki/File:Japanese_Wosite_Base_48_table.svg'
VERSE_PDF = 'https://hajime.online/download/KATAKAMUNAUTAI80SHU.pdf'
ROWS = [('Vowels','アイウエオ'),('K','カキクケコ'),('S','サシスセソ'),('T','タチツテト'),('N','ナニヌネノ'),('H','ハヒフヘホ'),('M','マミムメモ'),('Y / WI / WE','ヤヰユヱヨ'),('R','ラリルレロ'),('W / N','ワ ン ヲ')]

def sound_table(system):
    mapping = json.loads((ROOT/'data/katakamuna-glyphs.json').read_text())
    out = f'<div class="chart script-chart {system}"><table><caption>{system.title()} 48-character sound reference</caption><thead><tr><th scope="col">Row</th>' + ''.join(f'<th scope="col">{v}</th>' for v in 'AIUEO') + '</tr></thead><tbody>'
    for label, sounds in ROWS:
        out += f'<tr><th scope="row">{label}</th>'
        for k in sounds:
            if k == ' ':
                out += '<td class="empty" aria-label="No separate character in this chart">—</td>'
                continue
            url = f'assets/glyphs/woshite/{k}.png?v=2' if system == 'woshite' else mapping[k]
            out += f'<td><img class="script-glyph" src="{escape(url,quote=True)}" alt="{system.title()} {k}" loading="lazy" width="40" height="40"><small lang="ja">{k}</small></td>'
        out += '</tr>'
    return out + '</tbody></table></div>'

def brief(system):
    return (ROOT / f"data/briefs/{system}.html").read_text(encoding="utf-8")

def panels():
    verses = json.loads((ROOT/'data/utahi.json').read_text())
    assert [v['number'] for v in verses] == list(range(1,81))
    buttons = ''.join(f'<button type="button" class="verse-button" data-verse="{v["number"]}" aria-pressed="{str(v["number"] == 1).lower()}">{v["number"]:02}</button>' for v in verses)
    links = ''.join(f'<tr><th scope="row">{v["number"]:02}</th><td><a href="{VERSE_PDF}#page={v["number"]}" target="_blank" rel="noopener">Circular diagram ↗</a></td><td><a href="{escape(v["url"],quote=True)}" target="_blank" rel="noopener">Verse {v["number"]} source ↗</a></td></tr>' for v in verses)
    woshite = f'''<section id="panel-woshite" class="tab-panel" role="tabpanel" aria-labelledby="tab-woshite" tabindex="0" hidden>
<div class="panel-heading"><div class="eyebrow">48 characters · ヲシテ</div><h2>Woshite character table</h2><p>A sound reference with kana labels. The source chart places WI and WE in the Y-family positions and N in the W/U position; these labels do not establish separate YI, YE, or WU characters.</p></div>
{sound_table('woshite')}
<p class="source-note">Glyphs: MOTOI Kenkichi, <a href="{WOSH_SOURCE}" target="_blank" rel="noopener">Japanese Wosite Base 48 table</a>, Wikimedia Commons. Cropped into individual cells; licensed under <a href="https://creativecommons.org/licenses/by-sa/3.0/">CC BY-SA 3.0</a>. The cropped glyph assets use the same license.</p>
{brief('woshite')}</section>'''
    katakamuna = f'''<section id="panel-katakamuna" class="tab-panel" role="tabpanel" aria-labelledby="tab-katakamuna" tabindex="0" hidden>
<div class="panel-heading"><div class="eyebrow">48 sounds · 80 utahi · カタカムナ</div><h2>Katakamuna sound table</h2><p>The 48 sound symbols are the script’s character inventory. The 80 utahi are numbered verses composed with those symbols, rather than 80 different characters.</p></div>
{sound_table('katakamuna')}
<p class="source-note">Character images by <a href="{KATA_SOURCE}" target="_blank" rel="noopener">Katakamuna / ILLUSTRATION＊STORE</a>, loaded from the creator’s site. WI and WE follow that chart’s labels. A dash marks an unfilled position.</p>
<section class="utahi-library" aria-labelledby="utahi-title"><div class="eyebrow">Complete reference index</div><h2 id="utahi-title">All 80 utahi</h2><p>Select a number to view its circular diagram in the external 80-page source. Every verse also has an individual source link below.</p>
<div class="verse-picker" aria-label="Select an utahi">{buttons}</div>
<div class="reader-toolbar"><h3 id="verse-title">Utahi 01 of 80</h3><a id="verse-open" href="{VERSE_PDF}#page=1" target="_blank" rel="noopener">Open diagram in a new tab ↗</a></div>
<p class="source-note">The reader loads an external PDF. If your browser opens page 1 or cannot display the document, use the open link and enter the verse number in its page selector.</p>
<iframe id="verse-reader" title="Katakamuna utahi source PDF, verse 1" data-src="{VERSE_PDF}#page=1" loading="lazy" referrerpolicy="no-referrer"></iframe>
<details class="verse-sources"><summary>Source table · all 80 verses</summary><div class="table-scroll"><table><caption>Numbered utahi diagrams and individual source pages</caption><thead><tr><th scope="col">Utahi</th><th scope="col">Diagram</th><th scope="col">Source page</th></tr></thead><tbody>{links}</tbody></table></div></details>
<p class="source-note">Circular diagrams: <a href="{VERSE_PDF}">Hajime’s 80-page Katakamuna Utai collection</a>. Individual references: <a href="https://katakamuna.themedia.jp/pages/5412396/page_202110120420">カタカムナウタヒ 80首</a>. External works remain hosted by their publishers; English summaries appear in the research brief.</p></section>
{brief('katakamuna')}</section>'''
    return woshite + katakamuna
