#!/usr/bin/env python3
"""One-slide 16:9 overview of Stanford Park Youth Sports (flyer/overview.html)."""
import os
import build as b

IMG = "../assets/img/"
OUT = os.path.join(b.SITE, "flyer", "overview.html")

formats = "".join(f'<li>{b.icon(ic, sw=1.8)}<span>{t}</span></li>' for ic, t, *_ in b.SCHOOL_FORMATS)
sports = " · ".join(n for _, n, _ in b.SPORTS)
why = [("shield", "Trained, background-checked coaches"),
       ("clipboard", "Programs built around your schedule and space"),
       ("users", "Reliable staffing: the same coaches every week"),
       ("heart", "Scholarships through our 501(c)(3) Foundation")]
why_html = "".join(f'<li>{b.icon(ic, sw=1.8)}<span>{t}</span></li>' for ic, t in why)

html = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<title>Stanford Park Youth Sports Overview</title>
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Figtree:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
@page {{ size: 1920px 1080px; margin: 0; }}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
:root {{ --maroon:#8e1316; --maroon-900:#3f0809; --cream:#fbf5ec; --paper:#fffdf9; --ink:#1d1213; --ink-2:#4a3b3b; --line:#e7dac8; --blush:#f6e3de; --pink:#f6b3ac; }}
html, body {{ width: 1920px; height: 1080px; }}
body {{ background: var(--cream); color: var(--ink); font-family: Figtree, sans-serif; -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
.slide {{ width: 1920px; height: 1080px; display: grid; grid-template-columns: 700px 1fr; overflow: hidden; }}
.display {{ font-family: Anton, Impact, sans-serif; text-transform: uppercase; font-weight: 400; line-height: .92; }}
.eyebrow {{ display: inline-flex; align-items: center; gap: 12px; color: var(--maroon); font-weight: 800; font-size: 18px; letter-spacing: .16em; text-transform: uppercase; }}
.eyebrow::before {{ content: ""; width: 40px; height: 3px; background: currentColor; }}

/* left */
.left {{ position: relative; color: var(--cream); padding: 60px 56px; display: flex; flex-direction: column; }}
.left > img {{ position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: 55% 40%; z-index: -2; }}
.left::after {{ content: ""; position: absolute; inset: 0; z-index: -1; background: linear-gradient(180deg, rgba(63,8,9,.25) 0%, rgba(63,8,9,.15) 35%, rgba(63,8,9,.85) 68%, rgba(63,8,9,.97) 100%); }}
.left {{ isolation: isolate; }}
.logo {{ background: var(--cream); border-radius: 14px; padding: 12px 18px; align-self: flex-start; }}
.logo img {{ height: 70px; display: block; }}
.left h1 {{ margin-top: auto; font-size: 56px; white-space: nowrap; font-style: italic; transform: skewX(-7deg); transform-origin: left; }}
.left h1 em {{ font-style: inherit; color: var(--pink); }}
.left .sub {{ margin-top: 22px; font-size: 24px; line-height: 1.45; color: #f6e4e0; max-width: 560px; }}
.left .np {{ margin-top: 26px; display: inline-flex; align-items: center; gap: 10px; align-self: flex-start; background: var(--cream); color: var(--maroon); font-weight: 800; font-size: 15px; letter-spacing: .12em; text-transform: uppercase; padding: 9px 16px; border-radius: 8px; }}
.left .np svg {{ width: 20px; height: 20px; }}

/* right */
.right {{ padding: 60px 64px 50px 64px; display: flex; flex-direction: column; }}
.right h2 {{ font-size: 64px; margin-top: 10px; }}
.right h2 span {{ color: var(--maroon); }}
.lede {{ margin-top: 16px; font-size: 23px; line-height: 1.45; color: var(--ink-2); max-width: 1040px; }}
.stats {{ margin-top: 30px; display: grid; grid-template-columns: repeat(4, 1fr); gap: 18px; }}
.stat {{ background: var(--paper); border: 3px solid var(--maroon); box-shadow: 7px 7px 0 var(--maroon); border-radius: 14px; padding: 16px 20px; }}
.stat b {{ display: block; font-family: Anton, Impact, sans-serif; font-weight: 400; font-size: 54px; line-height: 1; color: var(--maroon); }}
.stat span {{ display: block; margin-top: 6px; font-size: 17px; font-weight: 700; color: var(--ink-2); }}
.cols {{ margin-top: 36px; display: grid; grid-template-columns: 1fr 1fr; gap: 40px; }}
.cols h3 {{ font-size: 32px; margin: 8px 0 16px; }}
.cols ul {{ list-style: none; display: grid; gap: 11px; }}
.cols li {{ display: flex; align-items: center; gap: 14px; font-weight: 700; font-size: 21px; background: var(--blush); border-radius: 10px; padding: 11px 16px; }}
.cols li svg {{ width: 26px; height: 26px; color: var(--maroon); flex: none; }}
.sports {{ margin-top: 26px; background: var(--maroon); color: var(--cream); border-radius: 14px; padding: 18px 24px; display: flex; align-items: center; gap: 20px; }}
.sports strong {{ font-family: Anton, Impact, sans-serif; font-weight: 400; text-transform: uppercase; font-size: 26px; white-space: nowrap; }}
.sports span {{ font-size: 21px; font-weight: 600; color: #f6e4e0; }}
.foot {{ margin-top: auto; display: flex; justify-content: space-between; align-items: center; padding-top: 22px; border-top: 2px solid var(--line); font-size: 20px; font-weight: 700; color: var(--ink-2); }}
.foot .c {{ display: flex; gap: 32px; }}
.foot .c span {{ display: inline-flex; align-items: center; gap: 10px; }}
.foot svg {{ width: 22px; height: 22px; color: var(--maroon); }}
</style></head>
<body><div class="slide">

<section class="left">
  <img src="{IMG}pn23-1600.webp" alt="">
  <div class="logo"><img src="{IMG}logo.png" alt="Stanford Park Youth Sports"></div>
  <h1 class="display">We do more than <em>coach.</em><br>We build <em>character.</em></h1>
  <p class="sub">Professional sports programs run on school campuses across the Bay Area, by our own trained coaches.</p>
  <span class="np">{b.icon("shield")} 501(c)(3) nonprofit · Since 2021</span>
</section>

<section class="right">
  <span class="eyebrow">Who we are</span>
  <h2 class="display">School sports, <span>done right.</span></h2>
  <p class="lede">We partner with public and private schools to run fun, safe, skill-focused sports programs on campus, from PE and recess to after school and camps. School programs are all we do.</p>

  <div class="stats">
    <div class="stat"><b>50+</b><span>Bay Area partner schools</span></div>
    <div class="stat"><b>1,000+</b><span>Students every week</span></div>
    <div class="stat"><b>7+</b><span>Sports offered</span></div>
    <div class="stat"><b>5</b><span>Program formats</span></div>
  </div>

  <div class="cols">
    <div><span class="eyebrow">What we run</span><h3 class="display">Program formats</h3><ul>{formats}</ul></div>
    <div><span class="eyebrow">Why schools choose us</span><h3 class="display">Our difference</h3><ul>{why_html}</ul></div>
  </div>

  <div class="sports"><strong>Sports</strong><span>{sports} · and more</span></div>

  <div class="foot">
    <span>stanfordparksports.com</span>
    <div class="c"><span>{b.icon("mail")} info@stanfordparksports.com</span><span>{b.icon("phone")} (650) 785-9029</span></div>
  </div>
</section>

</div></body></html>
'''

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w") as f:
    f.write(html)
print("wrote", OUT)
