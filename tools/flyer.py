#!/usr/bin/env python3
"""Builds the A4 promotional flyer (flyer.html) using the site's brand, icons and photos."""
import os
import build as b

IMG = "../assets/img/"
OUT = os.path.join(b.SITE, "flyer", "flyer.html")

sports = "".join(f'''<div class="sp">{b.icon(k, sw=1.7)}<div><h3>{n}</h3><p>{d}</p></div></div>'''
                 for k, n, d in b.SPORTS)
sports += f'''<div class="sp sp--more">{b.icon("plus", sw=2)}<div><h3>And more</h3><p>Clinics, events or something custom for your school.</p></div></div>'''

formats = "".join(f'<li>{b.icon(ic, sw=1.8)}<span>{t}</span></li>' for ic, t, *_ in b.SCHOOL_FORMATS)

photos = [("pcheer", "Cheerleading"), ("pflagcard", "Flag football"), ("pflyertennis", "Tennis"), ("pflyerbball", "Basketball")]
CAPTR = ' class="cap-tr"'
strip = "".join(f'<figure{CAPTR if p == "pflyertennis" else ""}><img src="{IMG}{p}-800.webp" alt=""><figcaption>{c}</figcaption></figure>' for p, c in photos)

html = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<title>Stanford Park Youth Sports Flyer</title>
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Figtree:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
@page {{ size: A4; margin: 0; }}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
:root {{ --maroon:#8e1316; --maroon-900:#3f0809; --cream:#fbf5ec; --cream-2:#f4eadb; --paper:#fffdf9; --ink:#1d1213; --ink-2:#4a3b3b; --line:#e7dac8; --blush:#f6e3de; }}
html, body {{ width: 210mm; height: 297mm; }}
body {{ background: var(--cream); color: var(--ink); font-family: Figtree, sans-serif; -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
.page {{ width: 210mm; height: 297mm; display: flex; flex-direction: column; overflow: hidden; }}
.page > * {{ flex: none; }}
.display {{ font-family: Anton, Impact, sans-serif; text-transform: uppercase; line-height: .95; }}

/* hero */
.hero {{ position: relative; height: 80mm; overflow: hidden; color: var(--cream); }}
.hero > img {{ position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: 50% 40%; }}
.hero::after {{ content: ""; position: absolute; inset: 0; background: linear-gradient(100deg, rgba(63,8,9,.95) 0%, rgba(63,8,9,.85) 42%, rgba(63,8,9,.25) 72%, rgba(63,8,9,.05) 100%); }}
.hero__in {{ position: relative; z-index: 1; height: 100%; padding: 9mm 12mm 7mm; display: flex; flex-direction: column; }}
.logo {{ background: var(--cream); border-radius: 3mm; padding: 2.2mm 3.4mm; align-self: flex-start; }}
.logo img {{ height: 13mm; display: block; }}
.np {{ margin-top: auto; display: inline-flex; align-items: center; gap: 1.6mm; align-self: flex-start; background: var(--cream); color: var(--maroon);
  font-weight: 800; font-size: 7.4pt; letter-spacing: .12em; text-transform: uppercase; padding: 1.4mm 2.6mm; border-radius: 1.4mm; }}
.np svg {{ width: 3.4mm; height: 3.4mm; }}
.hero h1 {{ margin-top: auto; font-size: 33pt; font-style: italic; transform: skewX(-6deg); transform-origin: left; max-width: 120mm; }}
.hero h1 em {{ font-style: inherit; color: #f6b3ac; }}
.hero .sub {{ margin-top: 3mm; font-size: 10.5pt; line-height: 1.45; max-width: 104mm; color: #f6e4e0; }}

/* sports */
.sports {{ padding: 6mm 12mm 0; }}
.head {{ display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 3mm; }}
.eyebrow {{ display: inline-flex; align-items: center; gap: 2mm; color: var(--maroon); font-weight: 800; font-size: 7.5pt; letter-spacing: .16em; text-transform: uppercase; }}
.eyebrow::before {{ content: ""; width: 7mm; height: .5mm; background: currentColor; }}
.head h2 {{ font-size: 25pt; }}
.head h2 span {{ color: var(--maroon); }}
.grid {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 2.6mm; }}
.sp {{ background: var(--paper); border: .35mm solid var(--line); border-radius: 2.6mm; padding: 2.6mm 3mm; display: flex; flex-direction: column; gap: 1.4mm; }}
.sp svg {{ width: 7mm; height: 7mm; color: var(--maroon); }}
.sp h3 {{ font-family: Anton, Impact, sans-serif; text-transform: uppercase; font-weight: 400; font-size: 12.5pt; line-height: 1; }}
.sp p {{ margin-top: 1mm; font-size: 7.6pt; line-height: 1.35; color: var(--ink-2); }}
.sp--more {{ background: var(--maroon); border-color: var(--maroon); color: var(--cream); }}
.sp--more svg {{ color: var(--cream); }}
.sp--more p {{ color: #f2dcd7; }}

/* photo strip */
.strip {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 2.6mm; padding: 3mm 12mm 0; }}
.strip figure {{ position: relative; height: 33mm; border-radius: 2.6mm; overflow: hidden; }}
.strip img {{ width: 100%; height: 100%; object-fit: cover; }}
.strip .cap-tr figcaption {{ left: auto; right: 2mm; top: 2mm; bottom: auto; }}
.strip figcaption {{ position: absolute; left: 2mm; bottom: 2mm; background: var(--cream); color: var(--maroon); font-weight: 800; font-size: 6.6pt; letter-spacing: .1em; text-transform: uppercase; padding: .8mm 1.8mm; border-radius: 1mm; }}

/* formats + stats */
.mid {{ display: grid; grid-template-columns: 1.25fr 1fr; gap: 6mm; padding: 4mm 12mm 6mm; align-items: start; }}
.formats h2, .stats h2 {{ font-size: 15pt; margin: 1.5mm 0 2.5mm; }}
.formats ul {{ list-style: none; display: grid; grid-template-columns: 1fr 1fr; gap: 1.8mm; }}
.formats li {{ display: flex; align-items: center; gap: 2mm; font-weight: 700; font-size: 8.8pt; background: var(--blush); border-radius: 1.6mm; padding: 1.8mm 2.2mm; }}
.formats li svg {{ width: 4.6mm; height: 4.6mm; color: var(--maroon); flex: none; }}
.stats .nums {{ display: grid; grid-template-columns: 1fr 1fr; gap: 2mm; }}
.stat {{ background: var(--paper); border: .45mm solid var(--maroon); box-shadow: 1.2mm 1.2mm 0 var(--maroon); border-radius: 2mm; padding: 2.4mm 3mm; }}
.stat b {{ display: block; font-family: Anton, Impact, sans-serif; font-weight: 400; font-size: 18pt; color: var(--maroon); line-height: 1; }}
.stat span {{ font-size: 7.2pt; font-weight: 700; color: var(--ink-2); }}

/* footer band */
.cta {{ margin-top: auto; background: var(--maroon); color: var(--cream); padding: 6mm 12mm 5mm; display: grid; grid-template-columns: 1.15fr 1fr; gap: 6mm; align-items: center; }}
.cta h2 {{ font-size: 21pt; }}
.cta h2 span {{ color: #f6b3ac; }}
.cta p {{ margin-top: 2mm; font-size: 8.8pt; line-height: 1.45; color: #f2dcd7; }}
.contact {{ list-style: none; display: grid; gap: 2mm; }}
.contact li {{ display: flex; align-items: center; gap: 2.4mm; font-weight: 700; font-size: 10pt; }}
.contact svg {{ width: 5mm; height: 5mm; flex: none; }}
.tag {{ background: var(--maroon-900); color: var(--cream); text-align: center; padding: 2.6mm 12mm; display: flex; justify-content: space-between; align-items: center; font-size: 6.8pt; color: #e8c9c4; }}
.tag strong {{ font-family: Anton, Impact, sans-serif; font-weight: 400; font-style: italic; font-size: 11pt; letter-spacing: .02em; text-transform: uppercase; color: var(--cream); }}
</style></head>
<body><div class="page">

<section class="hero">
  <img src="{IMG}p5063-2600.webp" alt="">
  <div class="hero__in">
    <div class="logo"><img src="{IMG}logo.png" alt="Stanford Park Youth Sports"></div>
    <h1 class="display">We do more than <em>coach.</em><br>We build <em>character.</em></h1>
    <p class="sub">Professional after-school, PE, recess, before-school and camp sports programs, run on your campus by our own trained, background-checked coaches.</p>
  </div>
</section>

<section class="sports">
  <div class="head">
    <div><span class="eyebrow">Sports we offer</span><h2 class="display">One partner. <span>Every sport.</span></h2></div>
  </div>
  <div class="grid">{sports}</div>
</section>

<div class="strip">{strip}</div>

<div class="mid">
  <section class="formats"><span class="eyebrow">Program formats</span><h2 class="display">Ways to partner</h2><ul>{formats}<li>{b.icon("plus", sw=2)}<span>Custom programs</span></li></ul></section>
  <section class="stats"><span class="eyebrow">By the numbers</span><h2 class="display">Trusted locally</h2>
    <div class="nums">
      <div class="stat"><b>50+</b><span>Bay Area partner schools</span></div>
      <div class="stat"><b>1,000+</b><span>Students every week</span></div>
      <div class="stat"><b>7+</b><span>Sports to choose from</span></div>
      <div class="stat"><b>2021</b><span>Coaching since</span></div>
    </div>
  </section>
</div>

<section class="cta">
  <div>
    <h2 class="display">Bring SPS to <span>your school</span></h2>
    <p>Tell us about your campus and we’ll build a program around your schedule, space and students. Scholarships available through the Stanford Park Sports Foundation.</p>
  </div>
  <ul class="contact">
    <li>{b.icon("mail")} info@stanfordparksports.com</li>
    <li>{b.icon("phone")} (650) 785-9029</li>
    <li>{b.icon("external")} stanfordparksports.com</li>
  </ul>
</section>
<div class="tag"><span>Stanford Park Sports Foundation · 501(c)(3) · EIN 33-2148759</span><strong>We do more than coach. We build character.</strong></div>

</div></body></html>
'''

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w") as f:
    f.write(html)
print("wrote", OUT)
