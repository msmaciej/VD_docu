VortexDeep LinkedIn card kit
============================
vd_card.py     - shared base (background, VD logo, colours, footer, render). Do NOT edit per card.
card_hexagon.py- HEXAGON cards (6 nodes + optional bar labels). Edit the top block, run: python card_hexagon.py
card_list.py   - LIST cards (2 title lines + tick list + takeaway). Edit the top block, run: python card_list.py
card_who.py    - example: a second list card (who it's for).

Every card imports vd_card, so all share the exact same background/logo/footer by construction.
Rendering: uses cairosvg if present, else rsvg-convert. Output: <OUTNAME>.svg + .png (1200x1200) next to the scripts.
Edit ONLY the CAPS block at the top of a card script (EYEBROW/TITLE/NODES or ITEMS/etc.), then re-run.
