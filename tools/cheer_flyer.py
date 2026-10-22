#!/usr/bin/env python3
"""Builds the A4 cheerleading program flyer (flyer/cheer.html) in the site's brand."""
import os
import build as b

IMG = "../assets/img/"
OUT = os.path.join(b.SITE, "flyer", "cheer.html")

learn = [
    ("cheer", "Cheers &amp; chants", "Loud, proud and in sync, with clear voices and sharp motions."),
    ("star", "Stunts", "Age-appropriate stunts taught step by step, always spotted by our coaches."),
    ("users", "Jumps &amp; teamwork", "Toe touches, timing and trusting your teammates."),
    ("heart", "Dance &amp; confidence", "Rhythm, energy and the confidence to perform in front of a crowd."),
]
learn_html = "".join(f'<div class="lc"><span class="lc__ic">{b.icon(ic, sw=1.8)}</span><div><h3>{t}</h3><p>{d}</p></div></div>' for ic, t, d in learn)

html = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<title>Stanford Park Youth Sports Cheerleading Flyer</title>
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Figtree:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
@page {{ size: A4; margin: 0; }}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
:root {{ --maroon:#8e1316; --maroon-900:#3f0809; --cream:#fbf5ec; --paper:#fffdf9; --ink:#1d1213; --ink-2:#4a3b3b; --line:#e7dac8; --blush:#f6e3de; --pink:#f6b3ac; }}
html, body {{ width: 210mm; height: 297mm; }}
body {{ background: var(--cream); color: var(--ink); font-family: Figtree, sans-serif; -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
.page {{ width: 210mm; height: 297mm; display: flex; flex-direction: column; overflow: hidden; }}
.page > * {{ flex: none; }}
.display {{ font-family: Anton, Impact, sans-serif; text-transform: uppercase; font-weight: 400; line-height: .92; }}
.eyebrow {{ display: inline-flex; align-items: center; gap: 2mm; color: var(--maroon); font-weight: 800; font-size: 7.5pt; letter-spacing: .16em; text-transform: uppercase; }}
.eyebrow::before {{ content: ""; width: 7mm; height: .5mm; background: currentColor; }}

/* hero */
.hero {{ position: relative; height: 92mm; overflow: hidden; color: var(--cream); }}
.hero > img {{ position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: 50% 35%; }}
.hero::after {{ content: ""; position: absolute; inset: 0; background: linear-gradient(180deg, rgba(63,8,9,.35) 0%, rgba(63,8,9,.05) 30%, rgba(63,8,9,.55) 62%, rgba(63,8,9,.96) 100%); }}
.hero__in {{ position: relative; z-index: 1; height: 100%; padding: 9mm 12mm 8mm; display: flex; flex-direction: column; }}
.logo {{ background: var(--cream); border-radius: 3mm; padding: 2.2mm 3.4mm; align-self: flex-start; }}
.logo img {{ height: 12mm; display: block; }}
.kicker {{ margin-top: auto; align-self: flex-start; background: var(--cream); color: var(--maroon); font-weight: 800; font-size: 8pt; letter-spacing: .14em; text-transform: uppercase; padding: 1.4mm 3mm; border-radius: 1.4mm; }}
.hero h1 {{ margin-top: 2.5mm; font-size: 56pt; font-style: italic; transform: skewX(-7deg); transform-origin: left; letter-spacing: .01em; }}
.hero .sub {{ margin-top: 2.5mm; font-size: 13pt; font-weight: 700; color: var(--pink); letter-spacing: .02em; }}

/* learn */
.learn {{ padding: 6mm 12mm 0; }}
.learn h2 {{ font-size: 22pt; margin: 1.5mm 0 3mm; }}
.learn h2 span {{ color: var(--maroon); }}
.lgrid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 3mm; }}
.lc {{ display: flex; gap: 3mm; align-items: flex-start; background: var(--paper); border: .35mm solid var(--line); border-radius: 2.6mm; padding: 2.8mm 3.4mm; }}
.lc__ic {{ width: 10mm; height: 10mm; flex: none; border-radius: 2.2mm; background: var(--maroon); color: var(--cream); display: grid; place-items: center; }}
.lc__ic svg {{ width: 5.6mm; height: 5.6mm; }}
.lc h3 {{ font-family: Anton, Impact, sans-serif; font-weight: 400; text-transform: uppercase; font-size: 13pt; line-height: 1; }}
.lc p {{ margin-top: 1.2mm; font-size: 8.4pt; line-height: 1.4; color: var(--ink-2); }}

/* showcase */
.show {{ margin: 5mm 12mm 0; display: grid; grid-template-columns: 1fr 1.05fr; border-radius: 3.4mm; overflow: hidden; background: var(--maroon); color: var(--cream); box-shadow: 1.6mm 1.6mm 0 var(--maroon-900); }}
.show__copy {{ padding: 5mm 6mm 5mm 7mm; display: flex; flex-direction: column; justify-content: center; }}
.show .eyebrow {{ color: var(--pink); }}
.show h2 {{ font-size: 25pt; margin-top: 2mm; }}
.show h2 span {{ color: var(--pink); }}
.show p {{ margin-top: 3mm; font-size: 9.6pt; line-height: 1.5; color: #f6e4e0; }}
.show__photo {{ min-height: 52mm; }}
.show__photo img {{ width: 100%; height: 100%; object-fit: cover; object-position: 50% 55%; display: block; }}

/* why */
.why {{ padding: 4mm 12mm 5mm; display: grid; grid-template-columns: repeat(3, 1fr); gap: 3mm; }}
.why div {{ display: flex; align-items: center; gap: 2.4mm; font-weight: 700; font-size: 8.8pt; background: var(--blush); border-radius: 1.8mm; padding: 2.6mm 3mm; }}
.why svg {{ width: 5mm; height: 5mm; color: var(--maroon); flex: none; }}

/* cta */
.cta {{ margin-top: auto; background: var(--maroon); color: var(--cream); padding: 6.5mm 12mm 6mm; display: grid; grid-template-columns: 1.1fr 1fr; gap: 6mm; align-items: center; }}
.cta h2 {{ font-size: 22pt; }}
.cta h2 span {{ color: var(--pink); }}
.cta p {{ margin-top: 2mm; font-size: 9pt; line-height: 1.45; color: #f2dcd7; }}
.contact {{ list-style: none; display: grid; gap: 2mm; }}
.contact li {{ display: flex; align-items: center; gap: 2.4mm; font-weight: 700; font-size: 10pt; }}
.contact svg {{ width: 5mm; height: 5mm; flex: none; }}
.tag {{ background: var(--maroon-900); padding: 2.6mm 12mm; display: flex; justify-content: space-between; align-items: center; font-size: 6.8pt; color: #e8c9c4; }}
.tag strong {{ font-family: Anton, Impact, sans-serif; font-weight: 400; font-style: italic; font-size: 11pt; text-transform: uppercase; color: var(--cream); }}
</style></head>
<body><div class="page">

<section class="hero">
  <img src="{IMG}pcheerhd.jpg" alt="">
  <div class="hero__in">
    <div class="logo"><img src="{IMG}logo.png" alt="Stanford Park Youth Sports"></div>
    <span class="kicker">New program · Stanford Park Youth Sports</span>
    <h1 class="display">Cheerleading</h1>
    <p class="sub">Cheers, jumps, stunts &amp; a big finale for families</p>
  </div>
</section>

<section class="learn">
  <span class="eyebrow">What your child will learn</span>
  <h2 class="display">Big energy. <span>Real skills.</span></h2>
  <div class="lgrid">{learn_html}</div>
</section>

<section class="show">
  <div class="show__copy">
    <span class="eyebrow">The grand finale</span>
    <h2 class="display">A show <span>for parents</span></h2>
    <p>At the end of the program, our cheerleaders put everything together and perform their full choreographed routine live for families. Bring your cameras!</p>
  </div>
  <div class="show__photo"><img src="{IMG}pcheergroup-1600.webp" alt=""></div>
</section>

<section class="why">
  <div>{b.icon("shield")} Trained, background-checked coaches</div>
  <div>{b.icon("users")} All levels welcome, no experience needed</div>
  <div>{b.icon("star")} Builds confidence &amp; teamwork</div>
</section>

<section class="cta">
  <div>
    <h2 class="display">Ready to <span>cheer?</span></h2>
    <p>Spots are limited. Ask your school about our cheer program or register online at stanfordparksports.org.</p>
  </div>
  <ul class="contact">
    <li>{b.icon("external")} stanfordparksports.org</li>
    <li>{b.icon("mail")} info@stanfordparksports.com</li>
    <li>{b.icon("phone")} (650) 785-9029</li>
  </ul>
</section>
<div class="tag"><span>Stanford Park Youth Sports · Bay Area school sports since 2021</span><strong>We do more than coach. We build character.</strong></div>

</div></body></html>
'''

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w") as f:
    f.write(html)
print("wrote", OUT)
