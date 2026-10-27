#!/usr/bin/env python3
"""Khan Lab School full day sports schedule for families (A4 portrait, blue/green accents)."""
import os
import build as b

OUT = os.path.join(b.SITE, "flyer", "khan-schedule.html")

# (start, end, title, description, icon key, kind)  kind: drop|play|food|calm
DAY = [
    ("8:00", "8:30", "Drop off &amp; free play", "Flexible drop off. Kids check in and play while friends arrive.", "users", "drop"),
    ("8:30", "9:00", "Welcome circle &amp; warm up", "Meet the coaches, learn the plan and get moving together.", "sun", "play"),
    ("9:00", "10:15", "Sport block 1", "Soccer for ages 7 to 10. Ball skills and tag games for ages <span class=\"nw\">4 to 6</span>.", "soccer", "play"),
    ("10:15", "10:35", "Snack &amp; water", "Refuel time.", "heart", "food"),
    ("10:35", "11:45", "Sport block 2", "Basketball and flag football, grouped by age.", "basketball", "play"),
    ("11:45", "12:30", "Lunch with coaches", "Packed lunch together on the field.", "heart", "food"),
    ("12:30", "1:15", "Quiet time", "Rest and calm games for ages 4 to 6. Low key skill challenges for ages 7 to 10.", "clock", "calm"),
    ("1:15", "2:30", "Sports gymkhana", "Stations and relays. Every kid gets a turn at everything.", "star", "play"),
    ("2:30", "2:45", "Snack &amp; water", "One more refuel.", "heart", "food"),
    ("2:45", "3:30", "Mini tournament", "Favorite games, a friendly tournament and cool down.", "football", "play"),
    ("3:30", "4:00", "Pick up", "Flexible pick up from the field.", "users", "drop"),
]

KIND = {"drop": ("var(--maroon-900)", "#efe6e4"), "play": ("var(--maroon)", "var(--blush)"),
        "food": ("#c9862a", "#fbf0dd"), "calm": ("#8a6f6c", "#f1ebe6")}

rows = ""
for s, e, t, d, ic, k in DAY:
    fg, bg = KIND[k]
    rows += f'''<li class="row">
      <div class="time"><b>{s}</b><span>to {e}</span></div>
      <div class="dot" style="background:{fg}"><span>{b.icon(ic, sw=2)}</span></div>
      <div class="card" style="background:{bg}"><h3>{t}</h3><p>{d}</p></div>
    </li>'''

bring = ["Packed lunch and 2 snacks", "Water bottle with a name", "Sneakers", "A layer, hat and sunscreen", "Any medication, with a note"]
bring_html = "".join(f'<li>{b.icon("check", sw=3)}<span>{x}</span></li>' for x in bring)

html = f'''<!doctype html><html lang="en"><head><meta charset="utf-8">
<title>Full Day Sports at Khan Lab School</title>
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Figtree:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
@page {{ size: A4; margin: 0; }}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
:root {{ --maroon:#8e1316; --maroon-900:#3f0809; --cream:#fbf5ec; --paper:#fffdf9; --blush:#f6e3de; --blue:#8e1316; --blue-900:#3f0809; --blue-50:#f6e3de; --green:#8e1316; --green-50:#fbf5ec; --ink:#1d1213; --ink-2:#4a3b3b; --line:#e7dac8; }}
html, body {{ width: 210mm; height: 297mm; }}
body {{ background: var(--cream); color: var(--ink); font-family: Figtree, sans-serif; -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
.page {{ width: 210mm; height: 297mm; display: flex; flex-direction: column; padding: 11mm 13mm 0; }}
.display {{ font-family: Anton, Impact, sans-serif; text-transform: uppercase; font-weight: 400; line-height: .95; }}

header {{ display: flex; justify-content: space-between; align-items: flex-start; gap: 6mm; }}
.brand {{ display: flex; align-items: center; gap: 3mm; }}
.brand img {{ height: 12mm; }}
.x {{ color: var(--ink-2); font-weight: 700; font-size: 10pt; }}
.school {{ font-weight: 800; font-size: 11pt; color: var(--maroon); }}
.date {{ text-align: right; }}
.date b {{ display: block; font-family: Anton, Impact, sans-serif; font-weight: 400; font-size: 17pt; color: var(--maroon); line-height: 1; text-transform: uppercase; }}
.date span {{ font-size: 9pt; font-weight: 700; color: var(--ink-2); }}

.hero {{ margin-top: 6mm; display: flex; align-items: flex-end; justify-content: space-between; gap: 6mm; }}
.hero h1 {{ font-size: 46pt; color: var(--ink); }}
.hero h1 span {{ color: var(--maroon); }}
.hero .sub {{ margin-top: 2mm; font-size: 10.5pt; color: var(--ink-2); font-weight: 600; }}
.chips {{ display: flex; flex-wrap: wrap; gap: 2mm; margin-top: 3.5mm; }}
.chip {{ display: inline-flex; align-items: center; gap: 1.6mm; font-size: 8.6pt; font-weight: 800; padding: 1.6mm 3mm; border-radius: 99px; background: var(--maroon); color: var(--cream); }}
.chip svg {{ width: 3.8mm; height: 3.8mm; }}
.chip.g {{ background: var(--paper); color: var(--maroon); border: .35mm solid var(--line); }}
.times {{ display: grid; gap: 2mm; flex: none; }}
.tbox {{ background: var(--paper); border: .5mm solid var(--line); border-radius: 3mm; padding: 2.4mm 3.4mm; min-width: 44mm; }}
.tbox small {{ display: block; font-size: 7pt; font-weight: 800; letter-spacing: .14em; text-transform: uppercase; color: var(--ink-2); }}
.tbox b {{ font-size: 12pt; }}
.tbox.d b, .tbox.p b {{ color: var(--maroon); }}
.tbox.d {{ border-color: var(--maroon); box-shadow: 1.2mm 1.2mm 0 var(--maroon); }} .tbox.p {{ border-color: var(--maroon); box-shadow: 1.2mm 1.2mm 0 var(--maroon); }}

.main {{ margin-top: 6mm; display: grid; grid-template-columns: 1fr 56mm; gap: 7mm; }}
.tl h2, .side h2 {{ font-size: 15pt; margin-bottom: 3mm; }}
.tl ol {{ list-style: none; position: relative; }}
.tl ol::before {{ content: ""; position: absolute; left: 25.6mm; top: 3mm; bottom: 3mm; width: .7mm; background: var(--line); border-radius: 1mm; }}
.row {{ display: grid; grid-template-columns: 19mm 13mm 1fr; align-items: center; margin-bottom: 2.9mm; }}
.nw {{ white-space: nowrap; }}
.time {{ text-align: right; padding-right: 2mm; line-height: 1.05; }}
.time b {{ display: block; font-size: 11.5pt; font-weight: 800; }}
.time span {{ font-size: 7.6pt; color: var(--ink-2); font-weight: 600; }}
.dot {{ width: 8.6mm; height: 8.6mm; border-radius: 50%; display: grid; place-items: center; color: #fff; justify-self: center; position: relative; z-index: 1; box-shadow: 0 0 0 1.2mm var(--cream); }}
.dot svg {{ width: 4.6mm; height: 4.6mm; display: block; }}
.card {{ border-radius: 2.6mm; padding: 2.8mm 3.4mm; }}
.card h3 {{ font-size: 10.6pt; font-weight: 800; }}
.card p {{ font-size: 8.4pt; line-height: 1.35; color: var(--ink-2); margin-top: .4mm; }}

.side {{ display: flex; flex-direction: column; gap: 5mm; }}
.box {{ border-radius: 3.4mm; padding: 4mm; }}
.bring {{ background: var(--paper); border: .5mm solid var(--maroon); box-shadow: 1.4mm 1.4mm 0 var(--maroon); }}
.bring ul {{ list-style: none; display: grid; gap: 2mm; }}
.bring li {{ display: flex; gap: 2mm; font-size: 9pt; font-weight: 700; line-height: 1.3; }}
.bring li svg {{ width: 4mm; height: 4mm; color: var(--maroon); flex: none; margin-top: .3mm; }}
.bring .note {{ margin-top: 3mm; padding-top: 2.6mm; border-top: .4mm dashed var(--line); font-size: 8.6pt; color: var(--maroon); font-weight: 700; display: flex; gap: 2mm; }}
.bring .note svg {{ width: 4.4mm; height: 4.4mm; flex: none; }}
.groups {{ background: var(--maroon); color: var(--cream); border: 0; }}
.groups h2 {{ color: var(--cream); }} .groups p {{ color: #f2dcd7 !important; }}
.groups p {{ font-size: 8.8pt; line-height: 1.4; color: var(--ink-2); }}
.groups .g2 {{ display: grid; grid-template-columns: 1fr 1fr; gap: 2mm; margin-top: 2.4mm; }}
.groups .g2 div {{ background: var(--cream); border-radius: 2mm; padding: 2mm; text-align: center; }}
.groups .g2 b {{ display: block; font-family: Anton, Impact, sans-serif; font-weight: 400; font-size: 15pt; color: var(--maroon); }}
.groups .g2 span {{ font-size: 7.6pt; font-weight: 700; color: var(--ink-2); }}
.blank {{ background: var(--paper); border: .6mm dashed #cdb9a4; border-radius: 3.4mm; padding: 3.4mm 4mm; }}
.blank small {{ display: block; font-size: 7pt; font-weight: 800; letter-spacing: .14em; text-transform: uppercase; color: var(--ink-2); margin-bottom: 1.6mm; }}
.blank .ln {{ height: 6.5mm; border-bottom: .4mm solid var(--line); }}

footer {{ margin: auto -13mm 0; background: var(--maroon); color: #fff; padding: 4.4mm 13mm; display: flex; justify-content: space-between; align-items: center; font-size: 9.6pt; font-weight: 700; }}
footer .dotsep {{ color: #f6b3ac; margin: 0 2.4mm; }}
footer .tag {{ color: #9fe0b8; }}
</style></head><body><div class="page">

<header>
  <div class="brand"><img src="../assets/img/logo.png" alt="Stanford Park Sports"><span class="x">at</span><span class="school">Khan Lab School</span></div>
  <div class="date"><b>Tuesday, Nov 3</b><span>2026 · On the Khan Lab School field</span></div>
</header>

<section class="hero">
  <div>
    <h1 class="display">Full Day <span>Sports</span></h1>
    <p class="sub">A full day of games, sports and friends, led by our coaches.</p>
    <div class="chips">
      <span class="chip">{b.icon("users", sw=2)} Ages 4 to 10</span>
      <span class="chip g">{b.icon("soccer", sw=2)} Soccer · Basketball · Flag football</span>
    </div>
  </div>
  <div class="times">
    <div class="tbox d"><small>Drop off</small><b>8:00 to 8:30 AM</b></div>
    <div class="tbox p"><small>Pick up</small><b>3:30 to 4:00 PM</b></div>
  </div>
</section>

<section class="main">
  <div class="tl">
    <h2 class="display">The day</h2>
    <ol>{rows}</ol>
  </div>
  <aside class="side">
    <div class="box groups">
      <h2 class="display">Two groups</h2>
      <p>Kids play with their own age group, so every game fits.</p>
      <div class="g2"><div><b>4 to 6</b><span>years old</span></div><div><b>7 to 10</b><span>years old</span></div></div>
    </div>
    <div class="box bring">
      <h2 class="display">What to bring</h2>
      <ul>{bring_html}</ul>
      <p class="note">{b.icon("star", sw=2)}<span>We bring all the sports equipment.</span></p>
    </div>
    <div class="blank">
      <small>Price</small><div class="ln"></div>
      <small style="margin-top:3mm">Register at</small><div class="ln"></div>
    </div>
  </aside>
</section>

<footer>
  <span>Stanford Park Sports<span class="dotsep">|</span>650.289.8040<span class="dotsep">|</span>stanfordparksports.com</span>
</footer>

</div></body></html>
'''

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w") as f:
    f.write(html)
print("wrote", OUT)
