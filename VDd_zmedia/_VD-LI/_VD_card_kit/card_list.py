# =========================================================
#  LIST card — eyebrow + 2 title lines + tick list + takeaway.  EDIT ONLY THIS BLOCK.
# =========================================================
EYEBROW  = "WHAT VORTEXDEEP IS"
TITLE    = ["AI HANDLES THE ADMIN.", "YOU KEEP THE DECISIONS."]   # line 2 = teal
SUBTITLE = ""                                                     # optional grey line under title; "" = none
ITEMS    = [                                                      # (lead, sub) ; sub "" = single line
    ("AI takes the repetitive admin", "the copying, chasing, re-formatting, retyping"),
    ("You approve every step that matters", "nothing is sent or filed on its own"),
    ("Built for teams who won't hand over control", "too cautious for autopilot, too busy for DIY"),
]
TAKEAWAY = "automation you stay in control of"                    # teal line above footer; "" = none
FOOTER   = "vortexdeep.ch"
OUTNAME  = "VD_LI_what-vortexdeep-is"
# =========================================================
import vd_card as vd
inner=vd.head(EYEBROW)
for k,ln in enumerate(TITLE):
    col = vd.ACC if k==1 else vd.TXT
    inner+=f"<text x='600' y='{312+k*62}' text-anchor='middle' font-family='{vd.F}' font-size='50' fill='{col}' letter-spacing='4'>{vd.esc(ln)}</text>"
y=470
if SUBTITLE:
    inner+=f"<text x='600' y='{y}' text-anchor='middle' font-family='{vd.F}' font-size='24' fill='{vd.MUT}'>{vd.esc(SUBTITLE)}</text>"; y+=70
# items: center the block; ticks left of text
gap = 92 if any(s for _,s in ITEMS) else 74
y += 20
for lead,sub in ITEMS:
    inner+=vd.tick(300,y-7)
    inner+=f"<text x='340' y='{y}' font-family='{vd.F}' font-size='27' fill='{vd.TXT}'>{vd.esc(lead)}</text>"
    if sub: inner+=f"<text x='340' y='{y+32}' font-family='{vd.F}' font-size='20' fill='{vd.MUT}'>{vd.esc(sub)}</text>"
    y+=gap
if TAKEAWAY:
    inner+=f"<text x='600' y='905' text-anchor='middle' font-family='{vd.F}' font-size='26' fill='{vd.ACC}' letter-spacing='1'>{vd.esc(TAKEAWAY)}</text>"
inner+=vd.divider(970)+vd.footer(FOOTER)
vd.render(inner, OUTNAME)
