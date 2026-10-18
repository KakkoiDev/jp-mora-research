"""Additional script panels. Data preserves each cited chart's own inventory."""
import json
import unicodedata
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SYSTEMS = [('hentaigana','Hentaigana'),('manyogana','Man’yōgana'),('ahiru','Ahiru'),('ahiru-cursive','Ahiru cursive'),('toyokuni','Toyokuni'),('izumo','Izumo'),('ryutai','Ryūtai')]
ROMAN = ['a','i','u','e','o','ka','ki','ku','ke','ko','sa','si','su','se','so','ta','ti','tu','te','to','na','ni','nu','ne','no','ha','hi','hu','he','ho','ma','mi','mu','me','mo','ya','yi','yu','ye','yo','ra','ri','ru','re','ro','wa','wi','wu','we','wo']
KANA = list('あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめも') + ['や','YI','ゆ','YE','よ'] + list('らりるれろ') + ['わ','ゐ','WU','ゑ','を']
SOURCES = json.loads((ROOT/'data/extra-glyph-sources.json').read_text())

def extra_tabs():
    return ''.join(f'<button id="tab-{key}" role="tab" aria-selected="false" aria-controls="panel-{key}" data-panel="{key}" tabindex="-1">{name}</button>' for key,name in SYSTEMS)

def reference_table(key,title,variant=0):
    record=SOURCES[key]
    # Ahiru's page contains two chart variants, each with 47 symbols.
    images=record['images'][variant*47:(variant+1)*47] if key=='ahiru' else record['images']
    mapping={Path(url).stem.lower().removeprefix('y_'):url for url in images}
    out=f'<section class="reference-chart"><h3>{title}</h3><div class="chart script-chart legacy-chart"><table><caption>{title}: source chart sound labels</caption><thead><tr><th scope="col">Row</th>'+''.join(f'<th scope="col">{v}</th>' for v in 'AIUEO')+'</tr></thead><tbody>'
    for row,label in enumerate(['Vowels','K','S','T','N','H','M','Y','R','W']):
        out+=f'<tr><th scope="row">{label}</th>'
        for i in range(row*5,row*5+5):
            url=mapping.get(ROMAN[i]);kana=KANA[i]
            out+=f'<td><span class="legacy-glyph"><img src="{escape(url,quote=True)}" alt="{escape(title)} {kana}" width="40" height="40" loading="lazy" referrerpolicy="no-referrer"></span><small>{kana}</small></td>' if url else '<td class="empty" aria-label="Unfilled in source chart">—</td>'
        out+='</tr>'
    if 'n' in mapping:
        out+=f'<tr><th scope="row">N</th><td><span class="legacy-glyph"><img src="{mapping["n"]}" alt="{title} ん" width="40" height="40" loading="lazy" referrerpolicy="no-referrer"></span><small>ん</small></td><td colspan="4"></td></tr>'
    return out+f'</tbody></table></div><p class="source-note"><a href="{record["source"]}">Source chart and original images ↗</a>. Images load from the publisher; each table preserves its labels and gaps. If an image is unavailable, follow the source link.</p></section>'

def hentaigana_catalog():
    entries=json.loads((ROOT/'data/hentaigana.json').read_text())
    encoded={e['codepoint'] for e in entries if e['codepoint']}
    for cp in range(0x1B001,0x1B11F):
        point=f'{cp:X}'
        if point not in encoded:
            name=unicodedata.name(chr(cp));reading=name.removeprefix('HENTAIGANA LETTER ').rsplit('-',1)[0].lower()
            entries.append({'id':None,'reading':reading,'parent':'—','codepoint':point})
    cards=[]
    for e in entries:
        cp=e['codepoint'];name=unicodedata.name(chr(int(cp,16))) if cp else 'Source form without a listed Unicode assignment'
        source=f'https://cid.ninjal.ac.jp/kana/detail/{e["id"]}/' if e['id'] else ('https://www.unicode.org/charts/PDF/U1B000.pdf' if int(cp,16)<0x1B100 else 'https://www.unicode.org/charts/PDF/U1B100.pdf')
        glyph=f'<span class="hentaigana-letter" lang="ja">{chr(int(cp,16))}</span>' if cp else f'<img src="https://cid.ninjal.ac.jp/kana/images/kana/{e["id"]}.webp" alt="Institute form {e["id"]}" width="52" height="52" loading="lazy">'
        search=escape(f'{e["reading"]} {e["parent"]} {cp or ""} {name} {e["id"] or ""}'.lower(),quote=True)
        cards.append(f'<div class="glyph-card" data-search="{search}">{glyph}<span>Reading: {escape(e["reading"])}</span><span>Parent kanji: {escape(e["parent"])}</span><code>{"U+"+cp if cp else "No assignment listed"}</code><a href="{source}">{"Institute record "+e["id"] if e["id"] else "Unicode chart"} ↗</a></div>')
    return f'<p>286 encoded forms, including E-1 / archaic YE, plus 28 additional forms without a code point in the institute’s catalog. Parent kanji are shown where supplied by that catalog; a dash means this combined record does not supply one.</p><label class="catalog-filter">Find a form by reading, parent kanji, code point, or record number<input type="search" data-filter="hentaigana-cards" placeholder="For example: あ, 安, 1B002, or na"></label><p class="filter-count" aria-live="polite" data-count="hentaigana-cards">{len(cards)} forms</p><div class="glyph-cards" id="hentaigana-cards">'+''.join(cards)+'</div>'

def manyogana_table():
    records=json.loads((ROOT/'data/manyogana.json').read_text())
    return '<div class="chart reading-table"><table><caption>Selected Man’yōgana examples, grouped by modern kana reading</caption><thead><tr><th scope="col">Reading</th><th scope="col">Selected sound-writing examples</th></tr></thead><tbody>'+''.join(f'<tr><th scope="row">{r["reading"]}</th><td lang="ja">{" · ".join(r["examples"])}</td></tr>' for r in records)+'</tbody></table></div><p class="source-note">Selected examples, not a complete inventory or a reconstruction of all Old Japanese sound distinctions. <a href="https://art-tags.net/manyo/kana/manyokana.html">Educational source and expanded examples ↗</a>.</p>'

def extra_panels():
    out=''
    for key,name in SYSTEMS:
        brief=(ROOT/f'data/briefs/{key}.html').read_text()
        if key=='hentaigana':chart=hentaigana_catalog()
        elif key=='manyogana':chart=manyogana_table()
        elif key=='toyokuni':chart=reference_table('toyokuni-old','Toyokuni: old-style chart')+reference_table('toyokuni-new','Toyokuni: new-style chart')
        elif key=='ahiru':chart=reference_table(key,'Ahiru: chart variant 1')+f'<details class="research-note"><summary>Compare the source’s second Ahiru variant</summary>{reference_table(key,"Ahiru: chart variant 2",1)}</details>'
        else:chart=reference_table(key,name)
        out+=f'<section id="panel-{key}" class="tab-panel" role="tabpanel" aria-labelledby="tab-{key}" tabindex="0" hidden><div class="panel-heading"><div class="eyebrow">Writing-system research</div><h2>{name}</h2><p>Read the English brief, then explore the source-specific character reference below.</p></div>{brief}{chart}</section>'
    return out
