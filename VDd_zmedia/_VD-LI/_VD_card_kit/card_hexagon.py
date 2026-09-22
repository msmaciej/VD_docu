# =========================================================
#  HEXAGON card — 6 nodes + 6 connector bars.  EDIT ONLY THIS BLOCK.
# =========================================================
EYEBROW = "A FIRST PROJECT"
TITLE   = ["SIX PHASES", "YOU SIGN OFF ON EACH"]     # 1 or 2 short lines (line 2 = teal)
NODES   = ["Discovery","Scope","Solution","Build","Validation","Live"]  # 6 stages, top then clockwise
BARS    = ["","","","","",""]                        # 6 transitions; "" = blank bar (no clutter)
HOT     = []                                          # node indices to highlight (0-based). [] = none
CLOSE   = "You approve every phase."
FOOTER  = "vortexdeep.ch"
OUTNAME = "VD_LI_six-phases"
# =========================================================
import math, vd_card as vd
cx,cy,R=600,660,205; ang=[-90,-30,30,90,150,210]
V=[(cx+R*math.cos(math.radians(a)),cy+R*math.sin(math.radians(a))) for a in ang]
inner=vd.head(EYEBROW)
for k,ln in enumerate(TITLE):
    col = vd.ACC if k==1 else vd.TXT
    inner+=f"<text x='600' y='{312+k*62}' text-anchor='middle' font-family='{vd.F}' font-size='50' fill='{col}' letter-spacing='5'>{vd.esc(ln)}</text>"
poly=" ".join(f"{x:.1f},{y:.1f}" for x,y in V)
inner+=f"<polygon points='{poly}' fill='none' stroke='{vd.NET}' stroke-width='1.6' opacity='0.55'/>"
for i in range(6):
    lab=BARS[i] if i<len(BARS) else ""
    x1,y1=V[i]; x2,y2=V[(i+1)%6]; mx,my=(x1+x2)/2,(y1+y2)/2
    inner+=f"<circle cx='{mx:.0f}' cy='{my:.0f}' r='4' fill='{vd.ACC}' opacity='0.7'/>"   # gate dot on every edge
    if lab:
        dx,dy=cx-mx,cy-my; L=math.hypot(dx,dy); ux,uy=dx/L,dy/L; lx,ly=mx+ux*46,my+uy*46
        inner+=f"<text x='{lx:.0f}' y='{ly+7:.0f}' text-anchor='middle' font-family='{vd.F}' font-size='23' fill='{vd.SUB}' font-style='italic'>{vd.esc(lab)}</text>"
for i,(x,y) in enumerate(V):
    hot=i in HOT
    inner+= vd.glow(x,y,11,30) if hot else f"<circle cx='{x:.0f}' cy='{y:.0f}' r='9' fill='{vd.NODE}'/>"
    a=ang[i]; anchor="middle"; ox,oy=x,y
    if a==-90: oy=y-32
    elif a==90: oy=y+44
    elif a in (-30,30): anchor="start"; ox=x+26; oy=y+7
    else: anchor="end"; ox=x-26; oy=y+7
    col=vd.ACC if hot else vd.BODY
    inner+=f"<text x='{ox:.0f}' y='{oy:.0f}' text-anchor='{anchor}' font-family='{vd.F}' font-size='28' fill='{col}' letter-spacing='1'>{i+1}. {vd.esc(NODES[i])}</text>"
inner+=vd.divider()+f"<text x='600' y='996' text-anchor='middle' font-family='{vd.F}' font-size='27' fill='{vd.BODY}' letter-spacing='1'>{vd.esc(CLOSE)}</text>"+vd.footer(FOOTER)
vd.render(inner, OUTNAME)
