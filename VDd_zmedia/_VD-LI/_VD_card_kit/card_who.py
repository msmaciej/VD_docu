import vd_card as vd
EYEBROW  = "WHO IT'S FOR"
TITLE    = ["TOO CAUTIOUS FOR AUTOPILOT.", "TOO BUSY TO DIY."]
SUBTITLE = "This is probably you if \u2014"
ITEMS    = [("Repetitive admin quietly eats your team's week",""),
            ("You want AI's help \u2014 not its autonomy",""),
            ("You won't hand your data to a black box",""),
            ("You don't have time to build it yourself","")]
TAKEAWAY = "that in-between is exactly what we build"
FOOTER   = "vortexdeep.ch"
OUTNAME  = "VD_LI_who-its-for"
inner=vd.head(EYEBROW)
for k,ln in enumerate(TITLE):
    col=vd.ACC if k==1 else vd.TXT
    inner+=f"<text x='600' y='{312+k*62}' text-anchor='middle' font-family='{vd.F}' font-size='48' fill='{col}' letter-spacing='3'>{vd.esc(ln)}</text>"
y=470
if SUBTITLE: inner+=f"<text x='600' y='{y}' text-anchor='middle' font-family='{vd.F}' font-size='24' fill='{vd.MUT}'>{vd.esc(SUBTITLE)}</text>"; y+=78
for lead,sub in ITEMS:
    inner+=vd.tick(300,y-7)+f"<text x='340' y='{y}' font-family='{vd.F}' font-size='27' fill='{vd.TXT}'>{vd.esc(lead)}</text>"
    y+=70
inner+=f"<text x='600' y='905' text-anchor='middle' font-family='{vd.F}' font-size='26' fill='{vd.ACC}' letter-spacing='1'>{vd.esc(TAKEAWAY)}</text>"
inner+=vd.divider(970)+vd.footer(FOOTER)
vd.render(inner,OUTNAME)
