# Unicode Proposal: Missing Japanese Kana

This repository contains research and documentation regarding the Unicode proposal to encode missing Japanese kana characters to complete the 50-sound (Gojuon) chart.

## Documentation

- [**Download the Original Proposal (PDF)**](./docs/missing-japanese-kana-proposal.pdf)

## Proposal Details

- **Title:** Proposal to Encode Missing Japanese Kana
- **Author:** Abraham Gross (<a href="mailto:abrahambgross@gmail.com">abrahambgross@gmail.com</a>)
- **Date:** 2020-01-05

## Summary

The proposal aims to add several missing characters to the Hiragana and Katakana Unicode blocks to reach the coveted 50-character mark of the "50-sound chart" (五十音図) and to facilitate the transcription of historical Japanese sounds.

### Proposed Characters

| Codepoint (Suggested) | Character Name |
| :--- | :--- |
| 1B129 | HIRAGANA LETTER YI |
| 1B12A | HIRAGANA LETTER WU |
| 1B12C | KATAKANA LETTER YI |
| 1B12D | KATAKANA LETTER YE |
| 1B12E | KATAKANA LETTER WU |
| 1B163 | KATAKANA LETTER SMALL WU |

### Key Motivations

1.  **Completing the Gojuon Chart:** Providing the characters needed to represent the full 50-sound system.
2.  **Historical/Linguistic Accuracy:** Representing historical sounds (like *wu*) that were present in ancient Japanese but are often omitted in modern orthography.
3.  **Transcription and Digitization:** Assisting scholars in transcribing old books and digitalizing historical Japanese texts.

## Credit

Full credit for the research, data, and proposal is given to **Abraham Gross**. This work is shared for research and archival purposes. 
The original proposal can also be found on the official Unicode website: [http://www.unicode.org/L2/2019/19381-missing-kana.pdf](http://www.unicode.org/L2/2019/19381-missing-kana.pdf)

## Research website

The original three tabs are Hiragana / Katakana, Woshite, and Katakamuna; seven additional research tabs are documented below.
Run `python3 data/generate_site.py` to regenerate `index.html`.

- Woshite: 48 locally bundled glyph crops by MOTOI Kenkichi, CC BY-SA 3.0. See `assets/glyphs/woshite/ATTRIBUTION.md`.
- Katakamuna: 48 glyph images referenced from their creator at https://katakamuna-note.com/katakamuna-phontlist/26/ (requires internet access).
- Utahi: all 80 numbered entries in `data/utahi.json`, with individual source links and a selectable external PDF reader. The PDF remains at https://hajime.online/download/KATAKAMUNAUTAI80SHU.pdf; no full verse transcription or modern commentary is redistributed.

The 48 sound symbols and the 80 utahi are different collections. WI, WE, and N labels follow the cited charts; the tables do not invent YI, YE, or WU mappings. Prehistoric-origin and spiritual/scientific claims are not established historical conclusions of this project.

## Expanded script catalog and legends

The site now also includes Hentaigana, Man’yōgana, Ahiru, Ahiru cursive, Toyokuni (both old and new styles), Izumo, and Ryūtai. Each has an English brief, attributed legends or transmission narratives, a separate provenance section, and a character reference. The existing three tabs also include legend sections.

Hentaigana includes a searchable 314-record comparison catalog: 286 encoded forms plus 28 additional institute entries. Noto Serif Hentaigana is bundled under the SIL Open Font License for reliable rendering. Additional traditional-script graphics remain on their original publisher's server. See [reference sources and scope](data/REFERENCE_SOURCES.md) for inventories, citations, display provenance, and limits.
