# =========================================================
#  VortexDeep — Week 1 card  "Should you automate it?"
#  Native 1200x1200. Fixes clipped line + lifts contrast.
# =========================================================
import math, cairosvg, os

W = 1200
BG   = "#0a0e12"; TXT="#eef0eb"; BODY="#e6e8e3"
MUT  = "#9aa2ab"      # subtitle / footer (was #8b939c — lifted)
ANS  = "#aab3bc"      # check answers    (was #828a93 — lifted for legibility)
Q    = "#eaece7"      # check questions
ACC  = "#7fd8c4"; NET="#8fa0aa"; NODE="#9fb0ba"
F    = "DejaVu Serif"

# --- background constellation (same node field as hex_template.py) ---
BGNODES=[(120,150),(360,80),(600,60),(1080,120),(950,300),(1120,520),(90,430),
         (200,760),(110,980),(360,1110),(620,1140),(900,1010),(1090,900),
         (1010,700),(700,1080),(240,300)]
BGEDGES=[(0,1),(1,2),(2,3),(3,4),(4,5),(5,13),(13,12),(12,11),(11,10),(10,9),
         (9,8),(8,7),(7,6),(6,0),(1,15),(15,6),(4,13),(9,14),(14,10)]

def esc(t): return t.replace("&","&amp;")

def bg():
    s=[f'<g stroke="{NET}" stroke-width="1" fill="none" opacity="0.12">']
    for a,b in BGEDGES:
        x1,y1=BGNODES[a]; x2,y2=BGNODES[b]
        s.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"/>')
    s.append(f'</g><g fill="{NODE}" opacity="0.4">')
    for x,y in BGNODES: s.append(f'<circle cx="{x}" cy="{y}" r="3"/>')
    return "".join(s)+"</g>"

def hexmark(cx=600, cy=168, R=30):
    pts=[(cx+R*math.cos(math.radians(a)), cy+R*math.sin(math.radians(a))) for a in (-90,-30,30,90,150,210)]
    poly=" ".join(f"{x:.1f},{y:.1f}" for x,y in pts)
    dots="".join(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3" fill="{NODE}"/>' for x,y in pts)
    return (f'<polygon points="{poly}" fill="none" stroke="{NODE}" stroke-width="2.1" '
            f'stroke-linejoin="round"/>{dots}'
            f'<text x="{cx}" y="{cy+8}" text-anchor="middle" font-family="{F}" '
            f'font-size="24" fill="{TXT}">VD</text>')

def glow(cx,cy,r=9,hr=26):
    return (f'<circle cx="{cx}" cy="{cy}" r="{hr}" fill="url(#halo)"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{ACC}"/>')

# --- three checks: (question, [answer lines]) ---
CHECKS=[
    ("Is it repetitive and rule-based?",
     ["If it needs judgment every time,",
      "automate the prep — not the decision."]),
    ("What's the cost of a mistake?",
     ["High stakes? Keep a human on the approval step."]),
    ("Does the data need to stay in-house?",
     ["If yes, no black boxes. Your data stays yours."]),
]

DOT_X, TXT_X = 232, 286   # left-aligned check column
inner  = ("<defs>"
  f"<radialGradient id='halo'><stop offset='0' stop-color='{ACC}' stop-opacity='0.85'/>"
  f"<stop offset='38%' stop-color='{ACC}' stop-opacity='0.30'/>"
  f"<stop offset='100%' stop-color='{ACC}' stop-opacity='0'/></radialGradient>"
  f"<radialGradient id='vig' cx='50%' cy='0%' r='95%'>"
  f"<stop offset='0' stop-color='#12181f'/><stop offset='72%' stop-color='{BG}'/>"
  "</radialGradient></defs>")
inner += f"<rect width='{W}' height='{W}' fill='url(#vig)'/>" + bg() + hexmark()

# centered header
inner += (f"<text x='600' y='270' text-anchor='middle' font-family='{F}' font-size='25' "
          f"fill='{ACC}' letter-spacing='9'>A QUICK CHECK</text>")
for k,ln in enumerate(["SHOULD YOU","AUTOMATE IT?"]):
    inner += (f"<text x='600' y='{356+k*80}' text-anchor='middle' font-family='{F}' "
              f"font-size='74' fill='{BODY}' letter-spacing='6'>{ln}</text>")
inner += (f"<text x='600' y='530' text-anchor='middle' font-family='{F}' font-size='27' "
          f"fill='{MUT}' font-style='italic'>Three checks before you hand a task to AI.</text>")

# left-aligned checks
y = 626
for question, ans_lines in CHECKS:
    inner += glow(DOT_X, y-13, 9, 26)
    inner += (f"<text x='{TXT_X}' y='{y}' font-family='{F}' font-size='34' "
              f"fill='{Q}' letter-spacing='0.4'>{esc(question)}</text>")
    ay = y + 42
    for ln in ans_lines:
        inner += (f"<text x='{TXT_X}' y='{ay}' font-family='{F}' font-size='26' "
                  f"fill='{ANS}'>{esc(ln)}</text>")
        ay += 36
    y = ay + (40 if len(ans_lines) > 1 else 44)

# divider + footer
inner += (f"<line x1='390' y1='1018' x2='810' y2='1018' stroke='#ffffff' stroke-opacity='0.09'/>"
          f"{glow(600,1018,7,20)}")
inner += (f"<text x='600' y='1082' text-anchor='middle' font-family='{F}' font-size='24' "
          f"fill='{MUT}' letter-spacing='2'>vortexdeep.ch · human-in-the-loop AI automation</text>")

svg=f"<svg xmlns='http://www.w3.org/2000/svg' width='{W}' height='{W}' viewBox='0 0 {W} {W}'>{inner}</svg>"
out="/home/claude/week01-26KW32_should_you_automate_v2"
open(out+".svg","w").write(svg)
cairosvg.svg2png(bytestring=svg.encode(), write_to=out+".png", output_width=1200, output_height=1200)
print("built", out+".png")
