# Additional writing-system references

Reviewed 2026-10-18. `extended.py` builds the seven additional tabs from these records and `briefs/*.html`. Page generation is offline; it does not refresh reference data automatically.

## Data records

- `hentaigana.json`: all 293 rows of https://cid.ninjal.ac.jp/kana/list/ (research ID, modern reading, parent kanji, listed code point). 265 rows have unique listed code points and 28 do not. The page supplements these with the other 21 code points in U+1B001–U+1B11E for 286 encoded forms total. The additional 21 use Unicode character names for readings and do not invent parent-kanji values. Sources: https://www.unicode.org/charts/PDF/U1B000.pdf and https://www.unicode.org/charts/PDF/U1B100.pdf. The catalog intentionally does not treat a missing assignment field as proof that a form has no possible encoding.
- `manyogana.json`: two selected character–reading examples per non-N group from https://art-tags.net/manyo/kana/manyokana.html. 45 modern reading groups, 90 pairs. Not an exhaustive Old Japanese inventory; no claim to include voiced series or historical WI/WE. Examples are plain characters, not copied source artwork or descriptive prose.
- `extra-glyph-sources.json`: original image URLs in source order, plus their exact chart pages. Ahiru includes two 47-sign variants (the second uses `y_` filenames); Ahiru cursive has 47; Izumo and both Toyokuni charts have 50 each; the Tatsu/Ryutai reference chart has 51. Contemporary 48-character Ryutai teaching is documented separately and not silently substituted into that chart.

## Artwork and font

The added jindai-moji images are externally hosted reference graphics from the linked collection at https://miko.org/~uraki/kuon/furu/text/sindaimonji/. No open reuse license is asserted for that collection, and these images are not redistributed in this repository. They require internet access and depend on the publisher's availability. Glyph backgrounds preserve the white-on-dark source graphics without recoloring or cropping.

NINJAL's unencoded-form examples likewise load from the institute. Encoded hentaigana use the bundled Noto Serif Hentaigana font, obtained from https://github.com/google/fonts/tree/main/ofl/notoserifhentaigana and distributed under the SIL Open Font License in `assets/fonts/OFL.txt`. Modern font shapes are not facsimiles of historical manuscript hands.

## Editorial source roles

Each brief separates source descriptions/claims, legends/transmission narratives, and documentation/provenance. Legends have attributed tellers; a legendary date is never used as the date of a surviving witness. Comparative surveys, institutional explanations, chart publishers, scholarly discussions, and practitioner announcements are identified by role. Publisher descriptions of books are not presented as reviews of the entire books.

The comparative survey at https://www.chikyukotobamura.org/muse/wr_column_8.html supplies short attributed transmission summaries for Ahiru, Ahiru cursive, Toyokuni, and Izumo. The broader history of debate comes from Mori Mizue's Encyclopedia of Shinto entry, https://d-museum.kokugakuin.ac.jp/eos/detail/?id=8651. Neither replaces examination of the individual manuscripts.

Ryutai's modern claims are summarized from Tokuma Shoten's publisher-supplied record https://www.hanmoto.com/bd/isbn/9784198657734 and the promotion organization's own announcement https://www.atpress.ne.jp/releases/328547/att_328547_1.pdf. These document advertised claims and contemporary transmission, rather than establish the claimed effects.

Kana founder legends are described through Yada Tsutomu's NINJAL explanation https://kotoba.ninjal.ac.jp/qa/yokuaru/qa-72/. Woshite's Awauta and Motoake stories are attributed to the practitioner page https://awauta.happydolphin-k.com/index.html. Katakamuna's legends retain the already-linked authors and publishers.
