# =========================================================
#  VortexDeep hexagon template  —  6 nodes + 6 connector bars
#  EDIT ONLY THIS BLOCK, then re-run.  Keep labels SHORT.
# =========================================================
EYEBROW = "A 6-STAGE PROCESS"
TITLE   = ["FROM REQUEST", "TO RESULT"]          # 1 or 2 short lines
NODES   = ["Intake","Routing","Execution","Approval","Record","Trust"]   # 6 stages, top then clockwise
BARS    = ["structure","assign","prep","sign off","capture","rely"]      # 6 transitions (Vi->Vi+1); "" = blank bar
HOT     = [3, 5]                                  # node indices to highlight (0-based). [] = none
CLOSE   = "Where does yours break?"
FOOTER  = "vortexdeep.ch"
OUTNAME = "hex_template_example"
# =========================================================

import subprocess, os, re, math
OUT=os.path.dirname(os.path.abspath(__file__)); W=1200
BG="#0a0e12"; TXT="#e6e8e3"; BODY="#dfe1dc"; MUT="#8b939c"; SUB="#828a93"; ACC="#7fd8c4"; NET="#8fa0aa"; NODE="#9fb0ba"; F="DejaVu Serif"
BGNODES=[(120,150),(360,80),(600,60),(1080,120),(950,300),(1120,520),(90,430),(200,760),(110,980),(360,1110),(620,1140),(900,1010),(1090,900),(1010,700),(700,1080),(240,300)]
BGEDGES=[(0,1),(1,2),(2,3),(3,4),(4,5),(5,13),(13,12),(12,11),(11,10),(10,9),(9,8),(8,7),(7,6),(6,0),(1,15),(15,6),(4,13),(9,14),(14,10)]
def bg():
    s=[f'<g stroke="{NET}" stroke-width="1" fill="none" opacity="0.12">']
    for a,b in BGEDGES: x1,y1=BGNODES[a]; x2,y2=BGNODES[b]; s.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"/>')
    s.append('</g><g fill="'+NODE+'" opacity="0.4">'); 
    for x,y in BGNODES: s.append(f'<circle cx="{x}" cy="{y}" r="3"/>')
    return "\n".join(s)+'</g>'
def glow(cx,cy,r=8,hr=24): return f'<circle cx="{cx}" cy="{cy}" r="{hr}" fill="url(#halo)"/><circle cx="{cx}" cy="{cy}" r="{r}" fill="{ACC}"/>'
def hexmark(cx=600,cy=150,R=24):
    pts=[(cx+R*math.cos(math.radians(a)),cy+R*math.sin(math.radians(a))) for a in (-90,-30,30,90,150,210)]
    poly=" ".join(f"{x:.1f},{y:.1f}" for x,y in pts)
    return f'<polygon points="{poly}" fill="none" stroke="{NODE}" stroke-width="2.1" stroke-linejoin="round"/><text x="{cx}" y="{cy+7}" text-anchor="middle" font-family="{F}" font-size="21" fill="{TXT}">VD</text>'
def esc(t): return re.sub(r"&(?!(?:amp|lt|gt|quot|apos|#\d+);)","&amp;",t)

cx,cy,R=600,660,205
ang=[-90,-30,30,90,150,210]
V=[(cx+R*math.cos(math.radians(a)),cy+R*math.sin(math.radians(a))) for a in ang]
inner="<defs><radialGradient id='halo'><stop offset='0' stop-color='%s' stop-opacity='0.85'/><stop offset='38%%' stop-color='%s' stop-opacity='0.30'/><stop offset='100%%' stop-color='%s' stop-opacity='0'/></radialGradient>"%(ACC,ACC,ACC)
inner+="<radialGradient id='vig' cx='50%%' cy='2%%' r='95%%'><stop offset='0' stop-color='#12181f'/><stop offset='72%%' stop-color='%s'/></radialGradient></defs>"%BG
inner+=f"<rect width='{W}' height='{W}' fill='url(#vig)'/>"+bg()
inner+=hexmark()
inner+=f"<text x='600' y='228' text-anchor='middle' font-family='{F}' font-size='24' fill='{MUT}' letter-spacing='7'>{esc(EYEBROW)}</text>"
for k,ln in enumerate(TITLE):
    inner+=f"<text x='600' y='{312+k*62}' text-anchor='middle' font-family='{F}' font-size='50' fill='{TXT}' letter-spacing='5'>{esc(ln)}</text>"
# hexagon outline (the bars)
poly=" ".join(f"{x:.1f},{y:.1f}" for x,y in V)
inner+=f"<polygon points='{poly}' fill='none' stroke='{NET}' stroke-width='1.6' opacity='0.55'/>"
# bar labels: midpoint of each edge, nudged toward centre
for i in range(6):
    lab=BARS[i] if i<len(BARS) else ""
    if not lab: continue
    x1,y1=V[i]; x2,y2=V[(i+1)%6]; mx,my=(x1+x2)/2,(y1+y2)/2
    dx,dy=cx-mx,cy-my; L=math.hypot(dx,dy); ux,uy=dx/L,dy/L
    lx,ly=mx+ux*46,my+uy*46
    inner+=f"<circle cx='{mx:.0f}' cy='{my:.0f}' r='4' fill='{ACC}' opacity='0.7'/>"
    inner+=f"<text x='{lx:.0f}' y='{ly+7:.0f}' text-anchor='middle' font-family='{F}' font-size='23' fill='{SUB}' font-style='italic'>{esc(lab)}</text>"
# nodes + outside labels
for i,(x,y) in enumerate(V):
    hot=i in HOT
    inner+= glow(x,y,11,30) if hot else f"<circle cx='{x:.0f}' cy='{y:.0f}' r='9' fill='{NODE}'/>"
    a=ang[i]; anchor="middle"; ox,oy=x,y
    if a==-90: oy=y-32
    elif a==90: oy=y+44
    elif a in (-30,30): anchor="start"; ox=x+26; oy=y+7
    else: anchor="end"; ox=x-26; oy=y+7
    col=ACC if hot else BODY
    inner+=f"<text x='{ox:.0f}' y='{oy:.0f}' text-anchor='{anchor}' font-family='{F}' font-size='28' fill='{col}' letter-spacing='1'>{i+1}. {esc(NODES[i])}</text>"
# close + footer
inner+=f"<line x1='390' y1='948' x2='810' y2='948' stroke='#ffffff' stroke-opacity='0.08'/>"
inner+=f"<text x='600' y='996' text-anchor='middle' font-family='{F}' font-size='27' fill='{BODY}' letter-spacing='1'>{esc(CLOSE)}</text>"
inner+=f"<text x='600' y='1050' text-anchor='middle' font-family='{F}' font-size='22' fill='#7e868f' letter-spacing='3'>{esc(FOOTER)}</text>"
svg=f"<svg xmlns='http://www.w3.org/2000/svg' width='{W}' height='{W}' viewBox='0 0 {W} {W}'>{inner}</svg>"
sp=os.path.join(OUT,OUTNAME+".svg"); pp=os.path.join(OUT,OUTNAME+".png")
open(sp,"w").write(svg); subprocess.run(["rsvg-convert","-w","1200","-h","1200",sp,"-o",pp],check=True)
print("built",OUTNAME)
