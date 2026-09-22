# =========================================================
#  vd_card.py — shared VortexDeep card base (DO NOT EDIT per-card).
#  Background, logo, colours, footer + render. Both card scripts import this,
#  so every card is byte-identical underneath by construction.
# =========================================================
import os, re, math
W = 1200
BG="#0a0e12"; TXT="#e6e8e3"; BODY="#dfe1dc"; MUT="#8b939c"; SUB="#828a93"
ACC="#7fd8c4"; NET="#8fa0aa"; NODE="#9fb0ba"; FOOT="#7e868f"; F="DejaVu Serif"
BGNODES=[(120,150),(360,80),(600,60),(1080,120),(950,300),(1120,520),(90,430),(200,760),(110,980),(360,1110),(620,1140),(900,1010),(1090,900),(1010,700),(700,1080),(240,300)]
BGEDGES=[(0,1),(1,2),(2,3),(3,4),(4,5),(5,13),(13,12),(12,11),(11,10),(10,9),(9,8),(8,7),(7,6),(6,0),(1,15),(15,6),(4,13),(9,14),(14,10)]

def esc(t): return re.sub(r"&(?!(?:amp|lt|gt|quot|apos|#\d+);)","&amp;",str(t))
def defs():
    d="<defs><radialGradient id='halo'><stop offset='0' stop-color='%s' stop-opacity='0.85'/><stop offset='38%%' stop-color='%s' stop-opacity='0.30'/><stop offset='100%%' stop-color='%s' stop-opacity='0'/></radialGradient>"%(ACC,ACC,ACC)
    d+="<radialGradient id='vig' cx='50%%' cy='2%%' r='95%%'><stop offset='0' stop-color='#12181f'/><stop offset='72%%' stop-color='%s'/></radialGradient></defs>"%BG
    return d
def bg():
    s=[f'<g stroke="{NET}" stroke-width="1" fill="none" opacity="0.12">']
    for a,b in BGEDGES: x1,y1=BGNODES[a]; x2,y2=BGNODES[b]; s.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"/>')
    s.append('</g><g fill="'+NODE+'" opacity="0.4">')
    for x,y in BGNODES: s.append(f'<circle cx="{x}" cy="{y}" r="3"/>')
    return "\n".join(s)+'</g>'
def glow(cx,cy,r=8,hr=24): return f"<circle cx='{cx}' cy='{cy}' r='{hr}' fill='url(#halo)'/><circle cx='{cx}' cy='{cy}' r='{r}' fill='{ACC}'/>"
def tick(cx,cy):
    return (f"<circle cx='{cx}' cy='{cy}' r='15' fill='url(#halo)'/>"
            f"<path d='M {cx-7} {cy+1} L {cx-1} {cy+7} L {cx+8} {cy-6}' fill='none' stroke='{ACC}' stroke-width='2.6' stroke-linecap='round' stroke-linejoin='round'/>")
def hexmark(cx=600,cy=150,R=24):
    pts=[(cx+R*math.cos(math.radians(a)),cy+R*math.sin(math.radians(a))) for a in (-90,-30,30,90,150,210)]
    poly=" ".join(f"{x:.1f},{y:.1f}" for x,y in pts)
    return f"<polygon points='{poly}' fill='none' stroke='{NODE}' stroke-width='2.1' stroke-linejoin='round'/><text x='{cx}' y='{cy+7}' text-anchor='middle' font-family='{F}' font-size='21' fill='{TXT}'>VD</text>"
def head(eyebrow):
    return (f"<rect width='{W}' height='{W}' fill='url(#vig)'/>"+bg()+hexmark()
            +f"<text x='600' y='228' text-anchor='middle' font-family='{F}' font-size='24' fill='{MUT}' letter-spacing='7'>{esc(eyebrow)}</text>")
def footer(text="vortexdeep.ch"):
    return f"<text x='600' y='1050' text-anchor='middle' font-family='{F}' font-size='22' fill='{FOOT}' letter-spacing='3'>{esc(text)}</text>"
def divider(y=948): return f"<line x1='390' y1='{y}' x2='810' y2='{y}' stroke='#ffffff' stroke-opacity='0.08'/>"
def render(inner, outname):
    svg=f"<svg xmlns='http://www.w3.org/2000/svg' width='{W}' height='{W}' viewBox='0 0 {W} {W}'>{defs()}{inner}</svg>"
    out=os.path.dirname(os.path.abspath(__file__))
    sp=os.path.join(out,outname+".svg"); pp=os.path.join(out,outname+".png")
    open(sp,"w").write(svg)
    try:
        import cairosvg; cairosvg.svg2png(url=sp, write_to=pp, output_width=W, output_height=W)
    except Exception:
        try:
            import subprocess; subprocess.run(["rsvg-convert","-w",str(W),"-h",str(W),sp,"-o",pp],check=True)
        except Exception as e: print("  (png render skipped:", e, "\u2014 SVG still written)")
    print("built", outname)
