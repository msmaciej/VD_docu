# =========================================================
#  ENGINEERING BREATH card — PID tuning comparison, real sim data.
#  Follows the VD kit convention: imports vd_card, edit the block below only.
#  Data comes from curves.json (t/pv arrays per config) — regenerate via
#  the PID simulator (classic ZN / Tyreus-Luyben / no-overshoot ZN, E5+E6).
# =========================================================
EYEBROW = "20 YEARS IN PROCESS ENGINEERING"
TITLE   = ["SAME LOOP.", "THREE PERSONALITIES."]
SUBTITLE = "Same gain, lag and delay. Three tuning rules from the same simulator."
CLOSE   = "Same process, same PID structure \u2014 the tuning philosophy is the whole difference."
FOOTER  = "vortexdeep.ch"
OUTNAME = "VD_engineering_breath_pid"
CURVES_JSON = "curves.json"   # {key: {t:[...], pv:[...]}}
CURVES = [
    # key,       label,                      color,    width, dash,    tag
    ("classic", "Classic Ziegler-Nichols", "SUB",  2.2, "none", "aggressive"),
    ("tyreus",  "Tyreus-Luyben",           "BODY", 2.6, "8,6",  "balanced"),
    ("nov",     "No-overshoot ZN",         "ACC",  4.0, "none", "conservative"),
]
TMAX, YMAX = 100, 2.6
PX0, PX1, PY0, PY1 = 195, 1005, 560, 860
# =========================================================
import json, vd_card as vd

with open(CURVES_JSON) as f:
    series = json.load(f)

COLORMAP = {"SUB": vd.SUB, "BODY": vd.BODY, "ACC": vd.ACC, "MUT": vd.MUT, "NODE": vd.NODE}

def build_path(t, pv, ymax):
    pts = []
    for ti, vi in zip(t, pv):
        if ti is None or vi is None or ti < 0 or ti > TMAX: continue
        x = PX0 + (ti/TMAX)*(PX1-PX0); y = PY1 - (vi/ymax)*(PY1-PY0)
        pts.append((x, y))
    return "M " + " L ".join(f"{x:.1f},{y:.1f}" for x, y in pts)

inner = vd.head(EYEBROW)
for k, ln in enumerate(TITLE):
    col = vd.ACC if k == 1 else vd.TXT
    inner += f"<text x='600' y='{312+k*62}' text-anchor='middle' font-family='{vd.F}' font-size='50' fill='{col}' letter-spacing='4'>{vd.esc(ln)}</text>"
if SUBTITLE:
    inner += f"<text x='600' y='430' text-anchor='middle' font-family='{vd.F}' font-size='23' fill='{vd.MUT}'>{vd.esc(SUBTITLE)}</text>"

leg_y, leg_x = 490, [230, 590, 870]
for (key, label, colname, lw, dash, tag), lx in zip(CURVES, leg_x):
    color = COLORMAP[colname]
    d_attr = f" stroke-dasharray='{dash}'" if dash != "none" else ""
    inner += f"<line x1='{lx-34}' y1='{leg_y-6}' x2='{lx-4}' y2='{leg_y-6}' stroke='{color}' stroke-width='{lw}'{d_attr} stroke-linecap='round'/>"
    inner += f"<text x='{lx}' y='{leg_y}' font-family='{vd.F}' font-size='21' fill='{vd.BODY}'>{vd.esc(label)}</text>"
    inner += f"<text x='{lx}' y='{leg_y+22}' font-family='{vd.F}' font-size='16' fill='{vd.MUT}' font-style='italic'>{vd.esc(tag)}</text>"

sp_y = PY1 - (1.0/YMAX)*(PY1-PY0)
inner += f"<line x1='{PX0}' y1='{sp_y:.1f}' x2='{PX1}' y2='{sp_y:.1f}' stroke='{vd.SUB}' stroke-width='1.2' stroke-dasharray='2,6' opacity='0.5'/>"
inner += f"<text x='{PX1+8}' y='{sp_y+6:.1f}' font-family='{vd.F}' font-size='17' fill='{vd.SUB}' font-style='italic'>setpoint</text>"
inner += f"<line x1='{PX0}' y1='{PY1}' x2='{PX1}' y2='{PY1}' stroke='{vd.NET}' stroke-width='1' opacity='0.35'/>"

for key, label, colname, lw, dash, tag in CURVES:
    color = COLORMAP[colname]
    d = build_path(series[key]['t'], series[key]['pv'], YMAX)
    d_attr = f" stroke-dasharray='{dash}'" if dash != "none" else ""
    op = "1" if key == "nov" else "0.8"
    inner += f"<path d='{d}' fill='none' stroke='{color}' stroke-width='{lw}' opacity='{op}'{d_attr} stroke-linejoin='round' stroke-linecap='round'/>"

inner += vd.divider(905) + f"<text x='600' y='945' text-anchor='middle' font-family='{vd.F}' font-size='25' fill='{vd.BODY}' letter-spacing='0.5'>{vd.esc(CLOSE)}</text>"
inner += vd.footer(FOOTER)
vd.render(inner, OUTNAME)
