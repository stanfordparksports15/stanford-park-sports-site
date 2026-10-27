#!/usr/bin/env python3
"""Bentley School (Oakland) Winter 2026/2027 parent flyers: Volleyball and Cheer (A4)."""
import os
import build as b

IMG = "../assets/img/"
OUTDIR = os.path.join(b.SITE, "flyer")

FLYERS = {
    "bentley-volleyball": {
        "sport": "Volleyball", "icon": "volleyball", "grades": "Grades 3 to 5", "who": "Students in grades 3 to 5. This program was requested by Bentley families in these grades.",
        "photo": "pi3476-1600.webp", "photo_pos": "50% 35%",
        "tagline": "Bumps, sets, serves and a whole lot of fun!",
        "intro": "Bentley families asked for volleyball, so this winter we are bringing an after school volleyball program to students in grades 3 to 5. Our coaches teach real volleyball skills in a fun, encouraging way, and students build confidence and teamwork every week.",
        "learn": [
            ("volleyball", "Passing &amp; setting", "Bumps and sets with good form, so the ball goes where they want it to."),
            ("star", "Serving", "Underhand serves first, then building up as skills and confidence grow."),
            ("run", "Footwork", "Ready position, quick feet and moving to the ball."),
            ("users", "Teamwork", "Calling the ball, cheering on teammates and playing real games."),
        ],
        "rain": "Volleyball is a low maintenance sport that works great in a classroom with just a little open space. On wet days the class moves indoors, and no net is needed:",
        "rain_list": ["Passing with soft volleyballs", "Volleyball trivia", "Fun team games that fit the room"],
    },
    "bentley-cheer": {
        "sport": "Cheer", "icon": "cheer", "grades": "Grades K through 4th or 5th", "who": "Students from kindergarten through 4th or 5th grade, all together in one fun class.",
        "photo": "pcheerhd.jpg", "photo_pos": "50% 30%",
        "tagline": "Chants, jumps and big smiles!",
        "intro": "This winter we are bringing an after school cheer program to Bentley students from kindergarten through 4th or 5th grade. Our coaches lead fun, high energy sessions where students learn cheers, motions and routines while building confidence, teamwork and school spirit.",
        "learn": [
            ("cheer", "Cheers &amp; chants", "Loud, proud and in sync, with clear voices and sharp motions."),
            ("star", "Jumps", "Fun jumps taught step by step with good technique."),
            ("heart", "Routines", "Learning and practicing a cheer routine together as a team."),
            ("users", "Confidence &amp; teamwork", "Performing with energy and supporting every teammate."),
        ],
        "rain": "Cheer is a low maintenance sport that works great in a classroom with just a little open space. On wet days the class moves indoors, with dance and choreography as the main focus:",
        "rain_list": ["Dance and choreography", "Sharp arm motions", "Jumps in place", "Chants and cheers"],
    },
}

CSS = '''
@page { size: A4; margin: 0; }
* { box-sizing: border-box; margin: 0; padding: 0; }
:root { --maroon:#8e1316; --maroon-900:#3f0809; --cream:#fbf5ec; --paper:#fffdf9; --ink:#1d1213; --ink-2:#4a3b3b; --line:#e7dac8; --blush:#f6e3de; --pink:#f6b3ac; --hl:#ffe9a8; }
html, body { width: 210mm; height: 297mm; }
body { background: var(--cream); color: var(--ink); font-family: Figtree, sans-serif; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
.page { width: 210mm; height: 297mm; display: flex; flex-direction: column; overflow: hidden; }
.page > * { flex: none; }
.display { font-family: Anton, Impact, sans-serif; text-transform: uppercase; font-weight: 400; line-height: .92; }
.eyebrow { display: inline-flex; align-items: center; gap: 2mm; color: var(--maroon); font-weight: 800; font-size: 7.5pt; letter-spacing: .16em; text-transform: uppercase; }
.ph { background: var(--hl); color: var(--ink); border-radius: 1mm; padding: 0 1.4mm; font-weight: 800; }

.hero { position: relative; height: 70mm; overflow: hidden; color: var(--cream); }
.hero > img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; }
.hero::after { content: ""; position: absolute; inset: 0; background: linear-gradient(100deg, rgba(63,8,9,.96) 0%, rgba(63,8,9,.86) 45%, rgba(63,8,9,.25) 78%, rgba(63,8,9,.1) 100%); }
.hero__in { position: relative; z-index: 1; height: 100%; padding: 9mm 12mm 8mm; display: flex; flex-direction: column; }
.top { display: flex; justify-content: space-between; align-items: flex-start; }
.logo { background: var(--cream); border-radius: 3mm; padding: 2mm 3.2mm; }
.logo img { height: 11mm; display: block; }
.school { background: var(--cream); color: var(--maroon); border-radius: 2mm; padding: 2mm 3.2mm; text-align: right; }
.school b { display: block; font-family: Anton, Impact, sans-serif; font-weight: 400; text-transform: uppercase; font-size: 13pt; line-height: 1; }
.school span { font-size: 7.6pt; font-weight: 700; letter-spacing: .08em; text-transform: uppercase; }
.kick { margin-top: auto; font-weight: 800; font-size: 8.4pt; letter-spacing: .14em; text-transform: uppercase; color: var(--pink); }
.hero h1 { margin-top: 2mm; font-size: 58pt; font-style: italic; transform: skewX(-7deg); transform-origin: left; display: flex; align-items: center; gap: 4mm; }
.hero h1 svg { width: 15mm; height: 15mm; transform: skewX(7deg); }
.hero .tag { margin-top: 2.5mm; display: flex; gap: 2.5mm; align-items: center; }
.pill { background: var(--cream); color: var(--maroon); font-weight: 800; font-size: 9pt; padding: 1.4mm 3mm; border-radius: 1.6mm; letter-spacing: .04em; }
.hero .tagline { font-size: 11pt; font-weight: 700; color: #f6e4e0; }

.body { padding: 6mm 12mm 0; display: grid; grid-template-columns: 1.15fr 1fr; gap: 6mm; }
.intro { font-size: 10pt; line-height: 1.5; color: var(--ink-2); }
h2 { font-size: 17pt; margin: 1.5mm 0 3mm; }
h2 span { color: var(--maroon); }
.learn { display: grid; gap: 2.2mm; margin-top: 4mm; }
.lc { display: flex; gap: 2.8mm; align-items: flex-start; background: var(--paper); border: .35mm solid var(--line); border-radius: 2.4mm; padding: 2.6mm 3mm; }
.lc__ic { width: 8.5mm; height: 8.5mm; flex: none; border-radius: 2mm; background: var(--maroon); color: var(--cream); display: grid; place-items: center; }
.lc__ic svg { width: 5mm; height: 5mm; }
.lc h3 { font-family: Anton, Impact, sans-serif; font-weight: 400; text-transform: uppercase; font-size: 11.5pt; line-height: 1; }
.lc p { margin-top: 1mm; font-size: 8.2pt; line-height: 1.35; color: var(--ink-2); }

.details { background: var(--paper); border: .5mm solid var(--maroon); box-shadow: 1.4mm 1.4mm 0 var(--maroon); border-radius: 3mm; padding: 4mm 4.4mm; }
.details dl { display: grid; gap: 2.2mm; margin-top: 1mm; }
.details dl div { display: grid; grid-template-columns: 6mm 1fr; gap: 2.4mm; align-items: start; font-size: 9.4pt; }
.details dt svg { width: 5mm; height: 5mm; color: var(--maroon); }
.details dd b { display: block; font-size: 7pt; letter-spacing: .12em; text-transform: uppercase; color: var(--ink-2); }
.details dd { font-weight: 700; line-height: 1.35; }

.rain { margin-top: 5mm; background: var(--blush); border-radius: 3mm; padding: 4mm 4.4mm; }
.rain h3 { font-family: Anton, Impact, sans-serif; font-weight: 400; text-transform: uppercase; font-size: 14pt; display: flex; align-items: center; gap: 2mm; color: var(--maroon); }
.rain h3 svg { width: 6mm; height: 6mm; }
.rain p { margin-top: 2mm; font-size: 8.6pt; line-height: 1.45; color: var(--ink-2); }
.rain ul { list-style: none; margin-top: 2.4mm; display: grid; gap: 1.6mm; }
.rain li { display: flex; gap: 2mm; align-items: flex-start; font-size: 8.8pt; font-weight: 700; }
.rain li svg { width: 4mm; height: 4mm; color: var(--maroon); flex: none; margin-top: .4mm; }

.why2 { margin: 5mm 12mm 6mm; display: flex; gap: 3mm; align-items: center; background: var(--paper); border: .35mm solid var(--line); border-radius: 2.4mm; padding: 3.4mm 4mm; font-size: 9.4pt; line-height: 1.45; color: var(--ink-2); }
.why2 svg { width: 7mm; height: 7mm; color: var(--maroon); flex: none; }
.why2 b { color: var(--ink); }
.why { padding: 5mm 12mm 6mm; display: grid; grid-template-columns: repeat(4, 1fr); gap: 2.6mm; }
.why div { display: flex; flex-direction: column; gap: 1.4mm; background: var(--paper); border: .35mm solid var(--line); border-radius: 2.4mm; padding: 3mm; font-size: 8.4pt; font-weight: 700; line-height: 1.3; }
.why svg { width: 6mm; height: 6mm; color: var(--maroon); }

.cta { margin-top: auto; background: var(--maroon); color: var(--cream); padding: 6mm 12mm 5.5mm; display: grid; grid-template-columns: 1.2fr 1fr; gap: 6mm; align-items: center; }
.cta h2 { font-size: 22pt; margin: 0; }
.cta h2 span { color: var(--pink); }
.cta .reg { margin-top: 2.6mm; font-size: 10pt; font-weight: 700; }
.cta .reg .ph { font-size: 10pt; }
.contact { list-style: none; display: grid; gap: 1.8mm; }
.contact li { display: flex; align-items: center; gap: 2.4mm; font-weight: 700; font-size: 9.6pt; }
.contact svg { width: 4.6mm; height: 4.6mm; flex: none; }
.foot { background: var(--maroon-900); padding: 2.6mm 12mm; display: flex; justify-content: space-between; align-items: center; font-size: 6.8pt; color: #e8c9c4; }
.foot strong { font-family: Anton, Impact, sans-serif; font-weight: 400; font-style: italic; font-size: 11pt; text-transform: uppercase; color: var(--cream); }
'''

CLOUD = '<path d="M20 16.6A5 5 0 0 0 18 7h-1.3A8 8 0 1 0 4 15.3"/><path d="M16 14v6M8 14v6M12 16v6"/>'


def flyer(key, f):
    learn = "".join(f'<div class="lc"><span class="lc__ic">{b.icon(ic, sw=1.8)}</span><div><h3>{t}</h3><p>{d}</p></div></div>' for ic, t, d in f["learn"])
    rain = "".join(f'<li>{b.icon("check", sw=3)}<span>{x}</span></li>' for x in f["rain_list"])
    cloud = f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{CLOUD}</svg>'
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8">
<title>Stanford Park Sports {f["sport"]} at Bentley School: Program Overview</title>
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Figtree:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>{CSS}.hero > img {{ object-position: {f["photo_pos"]}; }}</style></head>
<body><div class="page">

<section class="hero">
  <img src="{IMG}{f["photo"]}" alt="">
  <div class="hero__in">
    <div class="top">
      <div class="logo"><img src="{IMG}logo.png" alt="Stanford Park Youth Sports"></div>
      <div class="school"><b>Bentley School</b><span>Oakland</span></div>
    </div>
    <span class="kick">Program overview · Winter Trimester 2026/2027</span>
    <h1 class="display">{f["sport"]} {b.icon(f["icon"], sw=1.6)}</h1>
    <div class="tag"><span class="pill">{f["grades"]}</span><span class="tagline">{f["tagline"]}</span></div>
  </div>
</section>

<section class="body">
  <div>
    <span class="eyebrow">For the Bentley School team</span>
    <p class="intro" style="margin-top:2mm">{f["intro"]}</p>
    <h2 class="display" style="margin-top:4.5mm">What students <span>will learn</span></h2>
    <div class="learn" style="margin-top:0">{learn}</div>
  </div>
  <div>
    <div class="details">
      <span class="eyebrow">Program at a glance</span>
      <dl>
        <div><dt>{b.icon("users")}</dt><dd><b>Who</b>{f["who"]}</dd></div>
        <div><dt>{b.icon("calendar")}</dt><dd><b>When</b>Tuesdays after school, Winter Trimester 2026/2027</dd></div>
        <div><dt>{b.icon("pin")}</dt><dd><b>Where</b>Outdoors on campus when weather allows, in a classroom on rainy days</dd></div>
        <div><dt>{b.icon("check", sw=2.4)}</dt><dd><b>Equipment</b>All equipment provided by Stanford Park Sports</dd></div>
        <div><dt>{b.icon("shield")}</dt><dd><b>Coaches</b>Trained, background checked Stanford Park Sports coaches</dd></div>
      </dl>
    </div>
    <div class="rain">
      <h3>{cloud} Rainy day plan</h3>
      <p>{f["rain"]}</p>
      <ul>{rain}</ul>
    </div>
  </div>
</section>

<section class="why2">{b.icon("school", sw=1.8)}<span>Stanford Park Sports runs fun, safe, skill focused programs at <b>50+ Bay Area schools</b>. Students build skills, confidence and teamwork every week.</span></section>

<section class="cta">
  <div>
    <h2 class="display">Questions? <span>Contact us.</span></h2>
    <p class="reg">Reach out anytime and we will be happy to share more about the program.</p>
  </div>
  <ul class="contact">
    <li>{b.icon("external")} stanfordparksports.com</li>
    <li>{b.icon("mail")} info@stanfordparksports.com</li>
    <li>{b.icon("phone")} (650) 785 9029</li>
  </ul>
</section>
<div class="foot"><span>Stanford Park Sports · Bay Area school sports since 2021</span><strong>We do more than coach. We build character.</strong></div>

</div></body></html>
'''


if __name__ == "__main__":
    os.makedirs(OUTDIR, exist_ok=True)
    for key, f in FLYERS.items():
        with open(os.path.join(OUTDIR, key + ".html"), "w") as fh:
            fh.write(flyer(key, f))
        print("wrote", key)
