#!/usr/bin/env python3
"""Generates the static Stanford Park Youth Sports pages (shared header/footer/icons)."""
import os
from PIL import Image

SITE = "/Users/javieralcaraz/com.apple.Maps.Suggestions/Claude/stanford-park-sports-site"
IMG = os.path.join(SITE, "assets/img")

# ---------------------------------------------------------------- icons
UI = {
    "arrow": '<path d="M5 12h14"/><path d="m12 5 7 7-7 7"/>',
    "pin": '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/>',
    "clock": '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
    "calendar": '<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>',
    "calendar-x": '<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/><path d="m14 14-4 4M10 14l4 4"/>',
    "mail": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/>',
    "phone": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/>',
    "check": '<path d="M20 6 9 17l-5-5"/>',
    "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/>',
    "heart": '<path d="M19 14c1.5-1.5 3-3.2 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.8 0-3 .5-4.5 2-1.5-1.5-2.7-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4 3 5.5l7 7Z"/>',
    "school": '<path d="M14 22v-4a2 2 0 1 0-4 0v4"/><path d="m18 10 4 2v8a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2v-8l4-2"/><path d="M18 5v17M6 5v17"/><path d="m4 6 8-4 8 4"/><circle cx="12" cy="9" r="2"/>',
    "sunrise": '<path d="M12 2v8M4.9 10.9l1.4 1.4M2 18h2M20 18h2M19.1 10.9l-1.4 1.4M22 22H2M8 6l4-4 4 4M16 18a4 4 0 0 0-8 0"/>',
    "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M6.3 17.7l-1.4 1.4M19.1 4.9l-1.4 1.4"/>',
    "backpack": '<path d="M4 10a4 4 0 0 1 4-4h8a4 4 0 0 1 4 4v10a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2Z"/><path d="M8 22v-6a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v6M9 6V4a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v2"/>',
    "tent": '<path d="M3.5 21 14 3M20.5 21 10 3M15.5 21 12 15l-3.5 6M2 21h20"/>',
    "info": '<circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/>',
    "plus": '<path d="M12 5v14M5 12h14"/>',
    "users": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8"/>',
    "star": '<path d="M12 2l3.1 6.3 6.9 1-5 4.9 1.2 6.8L12 17.8 5.8 21l1.2-6.8-5-4.9 6.9-1z"/>',
    "grad": '<path d="M22 10 12 5 2 10l10 5 10-5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/>',
    "external": '<path d="M15 3h6v6M10 14 21 3M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/>',
    "clipboard": '<rect x="8" y="2" width="8" height="4" rx="1"/><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><path d="M12 11h4M12 16h4M8 11h.01M8 16h.01"/>',
    "send": '<path d="m22 2-7 20-4-9-9-4Z"/><path d="M22 2 11 13"/>',
}
SPORT = {
    "basketball": '<circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2v20"/><path d="M4.9 4.9c2.8 2.8 2.8 11.4 0 14.2M19.1 4.9c-2.8 2.8-2.8 11.4 0 14.2"/>',
    "soccer": '<circle cx="12" cy="12" r="10"/><path d="m12 7 4.2 3-1.6 5H9.4L7.8 10z"/><path d="M12 7V2.5M16.2 10l4.3-1.4M14.6 15l2.7 3.7M9.4 15l-2.7 3.7M7.8 10 3.5 8.6"/>',
    "volleyball": '<circle cx="12" cy="12" r="10"/><path d="M11.1 7.1a16.5 16.5 0 0 1 10.9 4"/><path d="M12 12a12.6 12.6 0 0 1-8.7 5"/><path d="M16.8 13.6a16.5 16.5 0 0 1-9 7.5"/><path d="M20.7 17a12.8 12.8 0 0 0-8.7-5 13.3 13.3 0 0 1 0-10"/><path d="M6.3 3.8a16.5 16.5 0 0 0 1.9 11.5"/>',
    "tennis": '<circle cx="12" cy="12" r="10"/><path d="M5 4.9a10 10 0 0 1 0 14.2M19 4.9a10 10 0 0 0 0 14.2"/>',
    "football": '<ellipse cx="12" cy="12" rx="10.5" ry="6" transform="rotate(-45 12 12)"/><path d="M8.5 15.5l7-7M9.6 12.6l1.8 1.8M11.1 11.1l1.8 1.8M12.6 9.6l1.8 1.8"/>',
    "cheer": '<path d="m3 11 18-5v12L3 14v-3z"/><path d="M11.6 16.8a3 3 0 1 1-5.8-1.6"/>',
    "run": '<circle cx="12" cy="14" r="8"/><path d="M12 14l3-3M10 2h4M12 2v4M19 6l1.5-1.5"/>',
}


def icon(name, cls="", sw=2):
    paths = UI.get(name) or SPORT[name]
    c = f' class="{cls}"' if cls else ""
    return (f'<svg{c} viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{sw}" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">{paths}</svg>')


ARROW = icon("arrow")
CUR = ' aria-current="page"'
OUTC = ' class="outline"'

# ---------------------------------------------------------------- images
_dims = {}


def dims(n):
    if n not in _dims:
        with Image.open(os.path.join(IMG, f"p{n}-1600.webp")) as im:
            _dims[n] = im.size
    return _dims[n]


def img(n, alt, sizes="(max-width: 960px) 100vw, 50vw", eager=False, cls="", extra=""):
    w, h = dims(n)
    load = 'fetchpriority="high" loading="eager"' if eager else 'loading="lazy"'
    c = f' class="{cls}"' if cls else ""
    return (f'<img{c} src="assets/img/p{n}-1600.webp" srcset="assets/img/p{n}-800.webp 800w, assets/img/p{n}-1600.webp {w}w" '
            f'sizes="{sizes}" width="{w}" height="{h}" alt="{alt}" {load} decoding="async"{extra}>')


# ---------------------------------------------------------------- data
DONATE_URL = "https://donorbox.org/stanford-park-sports-foundation"
EIN = "33-2148759"
SITE_URL = "https://www.stanfordparksports.com"
# Where the Wix registration pages live after the domain moves (Petr's free Wix URL, no trailing slash)
REG_BASE = "https://REPLACE-WITH-WIX-FREE-URL"
EMAIL = "info@stanfordparksports.com"
PHONE_DISPLAY = "(650) 785-9029"
PHONE_TEL = "+16507859029"
ADDRESS = "825 Live Oak Ave, Unit E, Menlo Park, CA 94025"

NAV = [("schools.html", "For Schools"), ("about.html", "About"), ("programs.html", "Programs"),
       ("get-involved.html", "Get Involved"), ("donate.html", "Foundation"), ("contact.html", "Contact")]

SPORTS = [
    ("basketball", "Basketball", "Dribbling, passing and real game play on the court."),
    ("soccer", "Soccer", "Footwork, small-sided games and a whole lot of goals."),
    ("volleyball", "Volleyball", "Bumps, sets, serves and learning to talk as a team."),
    ("tennis", "Tennis", "Racquet skills, footwork and focus, one rally at a time."),
    ("football", "Flag Football", "Routes, throws and teamwork without the tackles."),
    ("cheer", "Cheerleading", "Chants, jumps and confidence in front of a crowd."),
    ("run", "Run Club", "Track and field basics and the joy of just running."),
]

FORMATS = [
    ("backpack", "After School", "Right after the final bell, on the school campus. Kids go straight from class to coach.", "After the bell"),
    ("clipboard", "Physical Education", "A done-for-you PE program with experienced coaches and age-based progressions.", "During the school day"),
    ("sun", "Recess", "Coach-led games during recess or lunch, so every break is an active one.", "Recess &amp; lunch"),
    ("sunrise", "Before School", "Get the wiggles out first thing, before the school day begins, on campus.", "Before the bell"),
    ("tent", "Camps", "Full or half-day camps over summer, winter and holiday breaks.", "Summer · Winter · Holiday"),
]

SCHOOLS = ["Synapse School", "YCIS", "Taft", "Silicon Valley International School", "Adelante", "St. Simon Parish School", "Hillbrook School",
           "Acton Academy", "Keys School", "Las Lomitas Elementary", "Phillips Brooks School", "Oak Knoll Elementary",
           "San Miguel Elementary", "Hoover Elementary", "La Entrada Middle School", "Garfield Elementary",
           "The Carey School", "Woodland School", "Herbert Hoover Elementary", "Vargas Elementary", "Barron Park",
           "Addison Elementary", "Henry Ford", "Lakeside", "Duveneck Elementary", "North Star Academy",
           "White Oaks", "Ponderosa", "Bowman", "Gabriela Mistral Elementary"]

LOGOS = [("01", "Taft Community School"), ("02", "Synapse School"), ("03", "Silicon Valley International School"),
         ("04", "Adelante Selby Spanish Immersion School"), ("05", "Bowman School"), ("06", "Saint Simon Parish School"),
         ("07", "Hillbrook School"), ("08", "YCIS"), ("09", "Acton Academy"), ("10", "Keys School"),
         ("11", "Ponderosa Elementary School"), ("12", "Las Lomitas Elementary"), ("13", "Phillips Brooks School"),
         ("14", "Oak Knoll School"), ("15", "San Miguel School"), ("16", "Hoover Community School"),
         ("17", "La Entrada Middle School"), ("18", "Garfield Elementary"), ("19", "Gabriela Mistral Elementary"),
         ("20", "The Carey School"), ("21", "Woodland School"), ("22", "Herbert Hoover Elementary"),
         ("23", "Vargas Elementary"), ("24", "Barron Park Elementary"), ("25", "Addison Elementary"),
         ("26", "Henry Ford Elementary"), ("27", "Lakeside"), ("28", "Duveneck Elementary")]

PROGRAMS = [  # Fall 2026, from stanfordparksports.com/current-programs
    ("North Star Academy", "run", "Run Club / Track &amp; Field", "Mondays", "Aug 24 – Nov 9", "3:10 – 4:10 PM", "Grass field", "No class 9/7, 9/28, 10/12", "$360", "reg-north-star-run-club"),
    ("Addison Elementary", "soccer", "Soccer", "Wednesdays", "Sep 9 – Dec 9", "1:30 – 2:30 PM", "Grass field", "No class 11/11", "$420", "reg-addison-soccer"),
    ("Lakeside", "soccer", "Soccer", "Mondays", "Sep 14 – Dec 14", "2:40 – 3:40 PM", "Grass field", "No class 10/12, 11/23", "$480", "reg-lakeside-soccer"),
    ("White Oaks", "basketball", "Basketball", "Thursdays", "Sep 10 – Oct 29", "2:40 – 3:40 PM", "Basketball court", "", "$360", "reg-whiteoaks-basketball"),
    ("White Oaks", "soccer", "Soccer", "Mondays", "Sep 14 – Nov 9", "2:40 – 3:40 PM", "Grass field", "No class 10/12", "$360", "reg-whiteoaks-soccer"),
    ("San Miguel", "basketball", "Basketball", "Tuesdays", "Sep 22 – Nov 17", "2:20 – 3:20 PM", "Basketball court", "No class 10/6", "$180", "reg-sanmiguel-bball"),
    ("Ponderosa", "soccer", "Soccer", "Thursdays", "Sep 17 – Nov 5", "2:40 – 3:40 PM", "Grass field", "Supervision begins at 2:00 PM", "$360", "reg-ponderosa-soccer"),
    ("Bowman", "basketball", "Basketball", "Tuesdays", "Sep 29 – Dec 1", "4:00 – 5:00 PM", "Basketball court", "", "$449", "reg-bowman-basketball"),
    ("Gabriela Mistral", "soccer", "Soccer", "Tuesdays", "Sep 15 – Nov 3", "2:40 – 3:40 PM", "Grass field", "", "$320", "reg-gabriela-mistral-soccer"),
    ("Gabriela Mistral", "basketball", "Basketball", "Mondays", "Sep 14 – Nov 2", "2:40 – 3:30 PM", "Basketball court", "", "$320", "reg-gabrielamistral-basketball"),
]

SAFETY = [
    ("Supervised at all times", "Every session is run by trained coaches and staff who stay with the group from check-in to pick-up."),
    ("Screened, trained coaches", "Our coaches go through rigorous screening, background checks and specialized coach training before they lead a group."),
    ("Clear rules &amp; routines", "Every session has the same expectations and structure, so kids know exactly what to expect and can focus on playing."),
    ("Built for their age", "Activities are developmentally appropriate and structured to reduce risk, with kids grouped so everyone is matched well."),
    ("Everyone belongs", "Coaches actively watch group dynamics and participation, and our programs are designed around positive behavior and inclusion."),
]

TESTIMONIALS = [
    ("We have been partnered with Stanford Park Sports since last school year and it has been a really great experience with them. All the sports programs they’ve brought onto our campus have been delivered with a lot of high energy and because of this we have increased the amount of classes they have to offer.",
     "Silicon Valley International School", "Partner school", "SV", "03"),
    ("We’ve been working with Stanford Park Sports at Acton Academy, and it has been a very positive partnership. They’ve supported us with reliable recess solutions, consistently bringing coaches over to run structured games and activities. They’ve also run strong soccer and basketball programs for our students, as well as multiple camps throughout 2025.",
     "Acton Academy SV", "Partner school", "AA", "09"),
]

SCHOOL_FORMATS = [
    ("backpack", "After School", "Enrichment right after the final bell, on your campus. Students go straight from class to coach.", "After the bell"),
    ("clipboard", "Physical Education", "Fully outsourced PE with experienced coaches and age-based progressions for every grade.", "During the school day"),
    ("sun", "Recess", "Structured, coach-led games during recess or lunch, so breaks are active and well supervised.", "Recess &amp; lunch"),
    ("sunrise", "Before School", "Morning sessions before the school day starts, held right on your campus.", "Before the bell"),
    ("tent", "Camps", "Full or half-day camps for your school during summer, winter and holiday breaks.", "Summer · Winter · Holiday"),
]

STEPS = [("Reach out", "Tell us about your school, your students and what you\u2019re looking for."),
         ("We tailor it", "We build a program around your schedule, space and goals: after school, PE, recess, before school or camps."),
         ("Families sign up", "Parents register online, or through your school if you prefer to manage enrollment."),
         ("Students play", "Our trained coaches arrive ready to go, and students get active, confident and excited to come back.")]

FAQ = [
    ("What ages and grades do you work with?", "Our programs serve elementary and middle school students. Groups are organized so kids are matched with others their age and ability."),
    ("Where do programs take place?", "Most programs run right on your school’s campus, on its field or basketball court, so there’s no extra drop-off. Camps run during school breaks."),
    ("Which sports do you offer?", "Basketball, soccer, volleyball, tennis, flag football, cheerleading and run club, plus multi-sport programs that rotate through games and PE-style activities."),
    ("How do you keep students safe?", "Programs are supervised at all times by trained coaches and staff. Every coach goes through screening, background checks and specialized training, and each session follows clear rules and routines."),
    ("Can the program be customized for our school?", "Yes. We build every program around your school’s schedule, space and needs: after school, PE, recess, before school or camps."),
    ("How do families register?", "Families register online through our Programs page. Some schools manage registration themselves, and we can work either way."),
    ("Do you offer financial aid?", "Yes. Through the Stanford Park Sports Foundation, our 501(c)(3) nonprofit, we offer scholarships and free programs so every child can take part regardless of financial circumstances."),
]

# ---------------------------------------------------------------- shared chrome
FIELD_SVG = '''<div class="hero__field" aria-hidden="true"><svg viewBox="0 0 1440 900" preserveAspectRatio="xMidYMid slice" fill="none" stroke="currentColor" stroke-width="2">
<rect x="40" y="60" width="1360" height="780" rx="6"/><line x1="720" y1="60" x2="720" y2="840"/><circle cx="720" cy="450" r="130"/><circle cx="720" cy="450" r="5"/>
<rect x="40" y="250" width="200" height="400"/><rect x="40" y="350" width="70" height="200"/><path d="M240 380a110 110 0 0 1 0 140"/>
<rect x="1200" y="250" width="200" height="400"/><rect x="1330" y="350" width="70" height="200"/><path d="M1200 380a110 110 0 0 0 0 140"/></svg></div>'''


NOINDEX = '<meta name="robots" content="noindex, nofollow">\n'


def head(title, desc, page):
    return f'''<!doctype html>
<html lang="en" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
{NOINDEX if page in ("options.html", "hero-options.html") else ""}<meta name="theme-color" content="#8e1316">
<meta name="format-detection" content="telephone=no">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<link rel="canonical" href="{SITE_URL}/{"" if page == "index.html" else page}">
<meta property="og:image" content="assets/img/p5063-1600.webp">
<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Figtree:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/styles.css?v=20261023">
</head>
<body data-page="{page}">
<a class="skip-link" href="#main">Skip to content</a>
'''


def header(page):
    links = "".join(f'<a href="{h}"{CUR if h == page else ""}>{t}</a>' for h, t in NAV)
    mlinks = "".join(f'<li><a class="m-link" href="{h}"{CUR if h == page else ""}>{t}</a></li>' for h, t in [("index.html", "Home")] + NAV)
    return f'''<header class="site-header">
  <div class="container nav">
    <a class="brand" href="index.html" aria-label="Stanford Park Youth Sports home"><img src="assets/img/logo.png" alt="Stanford Park Youth Sports" width="640" height="184"></a>
    <nav class="nav-links" aria-label="Main">{links}</nav>
    <div class="nav-cta">
      <a class="btn btn--sm nav-donate" href="donate.html">{icon("heart")} Donate</a>
      <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="mobile-menu" aria-label="Open menu"><span></span></button>
    </div>
  </div>
</header>
<div class="mobile-menu" id="mobile-menu" aria-hidden="true">
  <nav aria-label="Mobile"><ul>{mlinks}</ul></nav>
  <div class="mobile-menu__foot">
    <a href="mailto:{EMAIL}">{EMAIL}</a>
    <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>
  </div>
</div>
'''


def footer():
    return f'''<footer class="site-footer on-dark">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <a class="logo-chip" href="index.html" aria-label="Stanford Park Youth Sports home"><img src="assets/img/logo.png" alt="Stanford Park Youth Sports" width="640" height="184" loading="lazy"></a>
        <p>After-school, PE, recess, before-school and camp sports programs for Bay Area schools since 2021.</p>
        <p class="footer-np">{icon("shield")} <span>Stanford Park Sports Foundation is a registered 501(c)(3) nonprofit. EIN {EIN}. Donations are tax-deductible.</span></p>
      </div>
      <div>
        <h4>Explore</h4>
        <ul class="footer-links">
          <li><a href="about.html">About us</a></li>
          <li><a href="programs.html">Current programs</a></li>
          <li><a href="schools.html">For schools</a></li>
          <li><a href="get-involved.html">Get involved</a></li>
          <li><a href="donate.html">Donate</a></li>
        </ul>
      </div>
      <div>
        <h4>Programs</h4>
        <ul class="footer-links">
          <li><a href="about.html#offerings">After school</a></li>
          <li><a href="about.html#offerings">Physical education</a></li>
          <li><a href="about.html#offerings">Recess</a></li>
          <li><a href="about.html#offerings">Before school</a></li>
          <li><a href="about.html#offerings">Camps</a></li>
        </ul>
      </div>
      <div>
        <h4>Get in touch</h4>
        <ul class="footer-contact">
          <li>{icon("mail")}<a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li>{icon("phone")}<a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-word" aria-hidden="true">We build character</div>
    <div class="footer-bottom">
      <span>&copy; <span data-year>2026</span> Stanford Park Sports Foundation · 501(c)(3) nonprofit · EIN {EIN}</span>
      <span class="footer-tagline">We do more than coach. We build character.</span>
    </div>
  </div>
</footer>
<script src="assets/js/site.js?v=20261023" defer></script>
</body>
</html>
'''


def mpic(mphoto, photo, alt):
    return (f'<picture><source media="(max-width: 960px)" srcset="assets/img/p{mphoto}-800.webp 800w, assets/img/p{mphoto}-1600.webp 1600w" sizes="100vw">'
            + img(photo, alt, eager=True) + '</picture>')


def page_hero(crumb, lines, lede, photo, alt, actions="", mphoto=None, note="", msmall=False):
    title = "".join(f'<span class="line"><span{OUTC if o else ""}>{t}</span></span>' for t, o in lines)
    return f'''<section class="page-hero{' page-hero--msmall' if msmall else ''}">
  {FIELD_SVG}
  <div class="container page-hero__grid">
    <div class="page-hero__copy">
      <nav class="crumbs fade-up" aria-label="Breadcrumb"><a href="index.html">Home</a><span aria-hidden="true">/</span><span aria-current="page">{crumb}</span></nav>
      <h1 class="display page-hero__title text-maroon">{title}</h1>
      <p class="lede fade-up d2">{lede}</p>
      {f'<p class="page-hero__note m-only">{note}</p>' if note else ""}
      {f'<div class="btn-row fade-up d3">{actions}</div>' if actions else ""}
    </div>
    <div class="page-hero__media">{mpic(mphoto, photo, alt) if mphoto else img(photo, alt, eager=True)}</div>
  </div>
</section>
'''


def sports_band(reverse=False):
    items = ""
    for i, (k, name, _) in enumerate(SPORTS):
        items += f'<span class="{"o" if i % 2 else ""}">{name}</span>{icon(k, sw=1.6)}'
    track = f'<div class="marquee__track">{items}</div>'
    return f'''<div class="band-clip"><div class="band{" band--flat" if reverse else ""}" aria-label="Sports we offer: {", ".join(s[1] for s in SPORTS)}">
  <div class="marquee{" marquee--reverse" if reverse else ""}" aria-hidden="true">{track}{track}</div>
</div></div>'''


def foundation_section():
    return f'''<section class="section" aria-labelledby="fdn-title">
  <div class="container">
    <div class="fdn reveal-scale">
      <div class="fdn__brand">
        <div class="fdn__logo"><img src="assets/img/foundation-logo.png" alt="Stanford Park Sports Foundation" width="1515" height="513" loading="lazy"></div>
        <dl class="fdn__facts">
          <div><dt>Status</dt><dd>Registered 501(c)(3) nonprofit</dd></div>
          <div><dt>EIN</dt><dd>{EIN}</dd></div>
          <div><dt>Donations</dt><dd>Tax-deductible</dd></div>
        </dl>
      </div>
      <div class="fdn__copy">
        <span class="eyebrow">We’re a nonprofit</span>
        <h2 id="fdn-title" class="display h-lg">Every kid <span class="outline">gets to play.</span></h2>
        <p class="lede">Stanford Park Sports is run by the Stanford Park Sports Foundation, a registered 501(c)(3) nonprofit. Too many children in underserved Bay Area schools are left out of sports because of cost or access. We change that with scholarships, free programs and new school partnerships.</p>
        <ul class="checks">
          <li>{icon("check", sw=3)} Scholarships and free programs for families who need them</li>
          <li>{icon("check", sw=3)} Programs for schools affected by funding cuts</li>
          <li>{icon("check", sw=3)} Gifts fund coaching, equipment and programs in underserved communities</li>
        </ul>
        <div class="btn-row">
          <a class="btn" href="{DONATE_URL}" target="_blank" rel="noopener">Donate now {icon("heart")}</a>
          <a class="btn btn--ghost" href="donate.html">About the Foundation</a>
        </div>
      </div>
    </div>
  </div>
</section>'''


def donate_band():
    return f'''<section class="section" aria-labelledby="donate-title">
  <div class="container">
    <div class="donate-band on-dark reveal-scale">
      {icon("basketball", "donate-band__art", 0.6)}
      <div class="donate-band__copy">
        <span class="eyebrow">Stanford Park Sports Foundation</span>
        <h2 id="donate-title" class="display h-lg">Every kid<br><span class="outline">gets to play.</span></h2>
        <p class="lede">Help us bring our programs to more schools serving under-resourced kids and families. Your gift goes directly to scholarships and free programs.</p>
      </div>
      <div class="donate-band__side">
        <span class="pill-note">{icon("shield")} <span>501(c)(3) nonprofit · Tax-deductible<span class="np-ein"><span class="np-sep"> · </span>EIN {EIN}</span></span></span>
        <div class="btn-row">
          <a class="btn btn--cream" href="{DONATE_URL}" target="_blank" rel="noopener">Donate now {icon("heart")}</a>
          <a class="btn btn--outline-cream" href="donate.html">Ways to give</a>
        </div>
      </div>
    </div>
  </div>
</section>'''


def quotes_section():
    cards = ""
    for i, (q, who, role, ini, logo) in enumerate(TESTIMONIALS):
        cards += f'''<figure class="quote reveal">
        <div class="quote__mark" aria-hidden="true">&ldquo;</div>
        <blockquote><p>{q}</p></blockquote>
        <figcaption>{logo_tile(logo, who, "quote__logo")}<span><strong>{who}</strong><span>{role}</span></span></figcaption>
      </figure>'''
    return f'''<section class="section" aria-labelledby="quotes-title">
  <div class="container">
    <div class="section-head section-head--center reveal">
      <span class="eyebrow">In their words</span>
      <h2 id="quotes-title" class="display h-lg">What schools <span class="outline">say</span></h2>
    </div>
    <div class="quotes" data-stagger="0.12">{cards}</div>
  </div>
</section>'''


def logo_tile(n, name, cls="logo-tile"):
    return f'<span class="{cls}" title="{name}"><img src="assets/img/logos/school-{n}.webp" alt="{name} logo" loading="lazy" decoding="async"></span>'


FORMAT_PHOTOS = {"backpack": ("flagcard", "Flag football team in Stanford Park Sports Foundation shirts smiling on their school field after school"),
                 "clipboard": ("tenniscard", "Stanford Park Sports coach taking a selfie with uniformed students holding up tennis rackets during PE"),
                 "sun": ("cheer", "Girls cheerleading with arms raised in Stanford Park Sports Foundation shirts at summer camp"),
                 "sunrise": ("n22", "Stanford Park Sports coach and students with basketballs on the school blacktop"),
                 "tent": ("i6941", "Large camp group in red and white jerseys with four Stanford Park Sports coaches in a gym")}
STEP_ICONS = ["phone", "clipboard", "users", "soccer"]


def format_cards(items):
    out = ""
    for i, (ic, t, d, w) in enumerate(items):
        n, alt = FORMAT_PHOTOS[ic]
        out += f'''<article class="format format--photo reveal">
        {img(n, alt, sizes="(max-width: 640px) 100vw, (max-width: 1100px) 50vw, 33vw", cls="format__bg")}
        <div class="format__top"><span class="format__no">0{i+1}</span><span class="format__when">{w}</span></div>
        <div class="format__body">
          <div class="format__icon">{icon(ic, sw=1.8)}</div>
          <h3>{t}</h3><p>{d}</p>
        </div>
      </article>'''
    return out


def step_cards():
    return "".join(f'''<div class="step reveal"><div class="step__card"><span class="step__icon">{icon(STEP_ICONS[i], sw=1.8)}</span><h3>{t}</h3><p>{d}</p></div></div>''' for i, (t, d) in enumerate(STEPS))


def schools_marquee(top=False):
    half = (len(LOGOS) + 1) // 2
    def row(items, rev):
        tiles = "".join(logo_tile(n, name) for n, name in items)
        return f'<div class="marquee{" marquee--reverse" if rev else ""}" aria-hidden="true"><div class="marquee__track">{tiles}</div><div class="marquee__track">{tiles}</div></div>'
    return f'''<section class="section" aria-labelledby="schools-title" style="padding-top:{'clamp(56px,7vw,96px)' if top else '0'}">
  <div class="container">
    <div class="section-head section-head--split reveal">
      <div style="display:grid;gap:18px">
        <span class="eyebrow">{"Our partner schools" if top else "Our partners"}</span>
        <h2 id="schools-title" class="display h-lg">Trusted by <span class="text-maroon">50+</span><br><span class="outline">Bay Area schools</span></h2>
      </div>
      <p class="lede">Public and private schools across San Francisco, San Mateo, Santa Clara, and Alameda counties.</p>
    </div>
  </div>
  <p class="sr-only">Partner schools include: {", ".join(SCHOOLS)}.</p>
  <div class="schools-marquee logos-marquee reveal">{row(LOGOS[:half], False)}{row(LOGOS[half:], True)}</div>
</section>'''


def write(name, html):
    with open(os.path.join(SITE, name), "w") as f:
        f.write(html)
    print("wrote", name)


# ================================================================= HOME
def home():
    formats = format_cards(SCHOOL_FORMATS)

    formats += f'''<a class="format format--more reveal" href="contact.html">
        <span class="format__no">06</span>
        <div class="format__icon">{icon("plus", sw=2)}</div>
        <h3>And more</h3><p>Clinics, special events or something custom. Tell us what your school needs and we\u2019ll build it.</p><span class="format__when">Let\u2019s talk {ARROW}</span>
      </a>'''
    sports = "".join(f'''<article class="sport reveal">{icon(k, "sport__icon", 1.6)}<div><h3>{n}</h3><p>{d}</p></div></article>''' for k, n, d in SPORTS)
    sports += f'''<a class="sport sport--more reveal" href="contact.html">{icon("plus", "sport__icon", 1.6)}<div><h3>And more</h3><p>Have something specific in mind? Ask us.</p></div></a>'''
    trust = "".join(f'<li class="trust__item reveal"><div><h3>{t}</h3><p>{d}</p></div></li>' for t, d in SAFETY)
    steps = step_cards()

    gal = [("5063", "Smiling students holding soccer balls with their coach on a school field"),
           ("cheergroup", "Summer camp cheerleading team in Stanford Park Sports Foundation shirts"),
           ("i2301", "Coach with a group of smiling students after school by the fence"),
           ("5190", "Group of young players at the goal with their coach"),
           ("i1035", "Students in Foundation shirts having fun at soccer with their coach"),
           ("i3476", "Three smiling girls in Stanford Park Sports Foundation shirts"),
           ("5224", "Coach smiling with a soccer ball on the school field"),
           ("i1034", "Students with basketballs and their coach on the school blacktop"),
           ("flag", "Flag football team in Foundation shirts holding footballs"),
           ("i4053", "Students gathered around their coach on a bright teal outdoor court"),
           ("i1028", "Group of students with basketballs on an outdoor school court")]
    items = ""
    for i, g in enumerate(gal):
        if isinstance(g, str):
            items += f'<div class="gallery__item gallery__item--word{" o" if i % 2 else ""}" aria-hidden="true">{g}</div>'
        else:
            gimg = img(g[0], g[1], sizes="(max-width: 960px) 80vw, 560px")
            items += f'<figure class="gallery__item" style="margin:0">{gimg}</figure>'

    body = f'''<main id="main">
<section class="hero" aria-labelledby="hero-title">
  {FIELD_SVG}
  <div class="container hero__grid">
    <div class="hero__copy">
      <div class="hero__mbg">{img("5220", "Stanford Park Sports coach blowing a whistle while coaching", sizes="100vw", eager=True)}<span class="hero__mchip">{icon("shield")}501(c)(3) nonprofit · Bay Area · Since 2021</span></div>
      <span class="np-badge fade-up">{icon("shield")} Registered 501(c)(3) nonprofit</span>
      <span class="eyebrow fade-up">School sports programs · Bay Area · Since 2021</span>
      <h1 id="hero-title" class="display hero__title">
        <span class="line"><span>We do more than <em>coach.</em></span></span>
        <span class="line"><span>We build <em>character.</em></span></span>
      </h1>
      <p class="lede fade-up d1">Professional after-school, PE, recess, before-school and camp sports programs for Bay Area schools. School programs are all we do, run on your campus by our own trained coaches.</p>
      <div class="btn-row fade-up d2">
        <a class="btn" href="contact.html">Partner with us {ARROW}</a>
        <a class="btn btn--ghost" href="schools.html">How it works</a>
      </div>
      <p class="hero__alt fade-up d3">Parent at a partner school?<a class="link-arrow" href="programs.html">Find your program {ARROW}</a></p>
    </div>

    <div class="collage" aria-label="Photos from our programs">
      <div class="collage__layer collage__main" data-depth="0.4">{img("n23", "Stanford Park Sports coach in a shirt reading We do more than coach. We build character, leading a group of students with basketballs on a school court", sizes="(max-width: 960px) 90vw, 45vw", eager=True, extra=' style="object-position:28% 50%"')}</div>
      <div class="collage__layer collage__b" data-depth="1.1"><figure class="polaroid" style="margin:0;position:relative">{img("n544", "Stanford Park Sports coaching team smiling together on a school blacktop", sizes="260px", eager=True)}<figcaption>Coach-led</figcaption></figure></div>
      <div class="collage__layer collage__a" data-depth="1.4"><figure class="polaroid" style="margin:0;position:relative">{img("gym", "Students cheering with their Stanford Park Sports coach in the school gym", sizes="260px", eager=True)}<figcaption>On your campus</figcaption></figure></div>
      <div class="collage__layer badge-spin" data-depth="0.9" aria-hidden="true">
        <svg class="ring" viewBox="0 0 200 200"><defs><path id="circ" d="M100,100 m-78,0 a78,78 0 1,1 156,0 a78,78 0 1,1 -156,0"/></defs><text><textPath href="#circ" textLength="486" lengthAdjust="spacing">TRUSTED BY BAY AREA SCHOOLS · 1,000+ KIDS EVERY WEEK ·</textPath></text></svg>
        <span class="badge-spin__center"><b>50+</b><small>Schools</small></span>
      </div>
      <div class="collage__layer sticker" data-depth="1.6" aria-hidden="true">Since 2021</div>
    </div>
  </div>
  <div class="container hero-stats" aria-label="By the numbers">
    <div class="stats" data-stagger="0.08">
      <div class="stat reveal">{icon("school", "corner", 1.5)}<span class="stat__num" data-count="50" data-suffix="+">50+</span><span class="stat__label">Bay Area partner schools, public and private</span></div>
      <div class="stat reveal">{icon("users", "corner", 1.5)}<span class="stat__num" data-count="1000" data-suffix="+">1,000+</span><span class="stat__label">Students playing every week</span></div>
      <div class="stat reveal">{icon("soccer", "corner", 1.5)}<span class="stat__num" data-count="7" data-suffix="+">7+</span><span class="stat__label">Sports your students can play</span></div>
      <div class="stat reveal">{icon("clock", "corner", 1.5)}<span class="stat__num" data-count="5">5</span><span class="stat__label">Program formats, from PE to camps</span></div>
    </div>
  </div>
</section>

{sports_band()}

{schools_marquee(top=True)}


<section class="section" aria-labelledby="intro-title">
  <div class="container intro">
    <div class="intro__media reveal">
      <div class="frame"><picture><source media="(max-width: 960px)" srcset="assets/img/pn544-800.webp 800w, assets/img/pn544-1600.webp 1600w" sizes="100vw">{img("5220", "Stanford Park Sports coach with a whistle directing a session", extra=' data-parallax="0.12" style="object-position:42% 50%"')}</picture></div>
      <div class="tag"><strong>Reliable staffing</strong><span>The same trained coaches on your campus, every week.</span></div>
    </div>
    <div class="intro__copy">
      <span class="eyebrow reveal">Why schools choose us</span>
      <h2 id="intro-title" class="display h-lg reveal">A sports partner <span class="outline">your school can count on</span></h2>
      <p class="lede reveal">We specialize in school programs. Our expert, caring coaches bring high-energy, skill-focused sessions to your campus every week, and we take care of the program so your team doesn’t have to.</p>
      <ul class="checks reveal">
        <li>{icon("check", sw=3)} Reliable staffing: the same trained coaches, every week</li>
        <li>{icon("check", sw=3)} Programs built around your bell schedule, space and goals</li>
        <li>{icon("check", sw=3)} Long-term partnerships: many schools add more programs over time</li>
        <li>{icon("check", sw=3)} Scholarships through our 501(c)(3), so no student is left out</li>
      </ul>
      <div class="btn-row reveal"><a class="btn" href="contact.html">Start a program {ARROW}</a><a class="link-arrow" href="about.html" style="align-self:center">Our story {ARROW}</a></div>
    </div>
  </div>
</section>




<section class="section" style="padding-top:0" aria-labelledby="formats-title">
  <div class="container">
    <div class="section-head section-head--split reveal">
      <div style="display:grid;gap:18px">
        <span class="eyebrow">What we run for schools</span>
        <h2 id="formats-title" class="display h-lg"><span class="d-only">Five ways</span><span class="m-only">Ways</span> <span class="outline">to partner</span></h2>
      </div>
      <p class="lede">Choose one format or combine them. Every program fits into your school day and runs on your campus.</p>
    </div>
    <div class="formats" data-stagger="0.1">{formats}</div>
  </div>
</section>

<section class="section steps-band on-dark" aria-labelledby="how-title">
  <div class="container">
    <div class="section-head section-head--split reveal">
      <div style="display:grid;gap:18px">
        <span class="eyebrow">How it works</span>
        <h2 id="how-title" class="display h-lg">Up and running <span class="outline">in four steps</span></h2>
      </div>
      <p class="lede">From the first call to the first whistle, we make starting a program simple for your team.</p>
    </div>
    <div class="steps reveal-line" data-stagger="0.14">{steps}</div>
    <div class="steps-cta reveal"><a class="btn btn--cream" href="contact.html">Contact us {ARROW}</a><span>Or call <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></span></div>
  </div>
</section>

<section class="section" aria-labelledby="trust-title">
  <div class="container trust">
    <figure class="trust__media reveal" style="margin:0">
      <div class="frame">{img("coaches", "Five smiling Stanford Park Youth Sports coaches in matching caps and shirts on a school blacktop")}</div>
      <figcaption>Trained, background-checked coaches</figcaption>
    </figure>
    <div>
      <div class="section-head reveal" style="margin-bottom:32px">
        <span class="eyebrow">Safety &amp; supervision</span>
        <h2 id="trust-title" class="display h-lg">Active supervision, <span class="outline">not passive care</span></h2>
      </div>
      <ol class="trust__list">{trust}</ol>
    </div>
  </div>
</section>

<section class="section sports-wrap" aria-labelledby="sports-title">
  <div class="container sports-split">
    <div class="sports-split__head reveal">
      <span class="eyebrow">Our sports</span>
      <h2 id="sports-title" class="display h-lg sports-split__title"><span>One partner.</span><span class="outline">Every sport.</span></h2>
      <p class="lede">Seven sports and counting, all taught by the same trained coaches, so your school only needs one partner.</p>
      <a class="btn" href="contact.html">Ask about a sport {ARROW}</a>
    </div>
    <div class="sports sports--compact" data-stagger="0.05">{sports}</div>
  </div>
</section>

<section class="gallery gallery--light gallery--photos" aria-label="Photos from our school programs">
  <div class="marquee photo-marquee"><div class="marquee__track">{items}</div><div class="marquee__track" aria-hidden="true">{items}</div></div>
</section>

{foundation_section()}

<section class="section" style="padding-top:0" aria-label="Get started">
  <div class="container cta-split" data-stagger="0.12">
    <a class="cta-card reveal" href="contact.html">
      {img("i5196", "", sizes="(max-width: 960px) 100vw, 50vw")}
      <span class="who">For schools</span>
      <h3>Bring SPS to your campus</h3>
      <p>Tell us about your school and we’ll put together a program that fits your schedule and students.</p>
      <span class="btn btn--cream" style="align-self:flex-start">Partner with us {ARROW}</span>
    </a>
    <a class="cta-card reveal" href="programs.html">
      {img("5055", "", sizes="(max-width: 960px) 100vw, 50vw")}
      <span class="who">For parents</span>
      <h3>Find your school’s program</h3>
      <p>Already at a partner school? See current programs, schedules and pricing, and register online.</p>
      <span class="btn btn--cream" style="align-self:flex-start">View programs {ARROW}</span>
    </a>
  </div>
</section>
</main>
'''
    write("index.html", head("Stanford Park Youth Sports | Sports Programs for Bay Area Schools",
                             "Professional after-school, recess, before-school and camp sports programs for Bay Area schools. Trusted by 50+ schools with 1,000+ students every week.",
                             "index.html") + header("index.html") + body + footer())


# ================================================================= ABOUT
def about():
    offers = format_cards(FORMATS)

    offers += f'''<a class="format format--more reveal" href="contact.html">
        <span class="format__no">06</span>
        <div class="format__icon">{icon("plus", sw=2)}</div>
        <h3>And more</h3><p>Clinics, special events or something custom. Tell us what your school needs and we\u2019ll build it.</p><span class="format__when">Let\u2019s talk {ARROW}</span>
      </a>'''
    body = f'''<main id="main">
{page_hero("About us", [("Our", False), ("story", True)],
            "Since 2021, Stanford Park Sports has brought professional coaching directly onto school campuses across the Bay Area: after school, PE, recess, before school and camps.",
            "4993", "Stanford Park Sports coach on a school field under a blue sky",
            f'<a class="btn" href="contact.html">Partner with us {ARROW}</a><a class="btn btn--ghost" href="programs.html">Current programs</a>', mphoto="coaches")}

{sports_band(True)}

<section class="section" aria-labelledby="story-title">
  <div class="container story">
    <div class="reveal">
      <span class="eyebrow">Who we are</span>
      <h2 id="story-title" class="display h-lg" style="margin-top:18px">Built on <span class="outline">what sport teaches</span></h2>
    </div>
    <div class="story__body">
      <p class="story__big reveal">Sports can change lives, and not just by creating athletes, but by building <em>confident, disciplined and resilient</em> young people.</p>
      <p class="reveal">Our founder, Petr Ropek, grew up in Prague, Czech Republic. Through soccer and later basketball, he learned early that discipline, hard work and accountability could open doors that financial resources could not. Those lessons earned him the opportunity to move to the United States to play college basketball, and shaped the person he would become.</p>
      <p class="reveal">After graduating, Petr founded Stanford Park Sports to deliver professional sports programs to schools across the Bay Area. When funding cuts eliminated programs at some local school districts, families from underserved communities lost something their children loved and relied on. Seeing that firsthand made the mission clear: access to high-quality sports training should not depend on income or opportunity. That led to the Stanford Park Sports Foundation, a registered 501(c)(3) nonprofit.</p>
      <p class="reveal">Today we partner with 50+ schools and serve 1,000+ students every week, from TK through high school and across all skill levels, including public schools, underserved schools, low-income families and juvenile programs.</p>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0" aria-labelledby="approach-title">
  <div class="container">
    <div class="section-head section-head--split reveal">
      <div style="display:grid;gap:18px">
        <span class="eyebrow">Our approach</span>
        <h2 id="approach-title" class="display h-lg">Serious coaching. <span class="outline">Real growth.</span></h2>
      </div>
      <p class="lede">We train athletes seriously, but we focus on development over winning, because character, confidence and resilience matter far more than the scoreboard.</p>
    </div>
    <div class="impact" data-stagger="0.1">
      <article class="impact__card reveal"><div class="format__icon">{icon("clipboard", sw=1.8)}</div><h3>European-style coaching</h3><p>Our coaching emphasizes fundamentals, discipline and pushing beyond comfort zones.</p></article>
      <article class="impact__card reveal"><div class="format__icon">{icon("star", sw=1.8)}</div><h3>Development over winning</h3><p>Every session builds skills, confidence, teamwork and positive habits, for every level of player.</p></article>
      <article class="impact__card reveal"><div class="format__icon">{icon("grad", sw=1.8)}</div><h3>SPS Academy pathway</h3><p>For motivated athletes, higher-level SPS Academy programs offer serious training while still putting character first.</p></article>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0" aria-label="Photos">
  <div class="container photo-row" data-stagger="0.1">
    <figure class="reveal">{img("i1038", "Students holding a Stanford Park Youth Sports banner on a school court", sizes="(max-width: 960px) 100vw, 40vw")}</figure>
    <figure class="reveal">{img("i1033", "Young players lined up with basketballs in the gym", sizes="(max-width: 960px) 50vw, 30vw")}</figure>
    <figure class="reveal">{img("i1026", "Coach taking a selfie with laughing students", sizes="(max-width: 960px) 50vw, 30vw")}</figure>
  </div>
</section>

<section class="section" style="padding-top:0" aria-labelledby="mission-title">
  <div class="container">
    <div class="mission on-dark reveal-scale">
      {icon("soccer", "mission__art", 0.6)}
      <span class="eyebrow" style="justify-content:center">Our mission</span>
      <h2 id="mission-title" class="display" style="margin-top:22px">Not every child will become a pro. <span class="outline">That’s not how we measure success.</span></h2>
      <p class="lede" style="margin:22px auto 0;text-align:center">Our goal is to help young people succeed in life by teaching the values sports naturally develop.</p>
      <ul class="values">
        <li>Hard work</li><li>Accountability</li><li>Teamwork</li><li>Self-belief</li>
      </ul>
      <p class="mission__vision"><strong>Our vision:</strong> every child in the Bay Area and beyond has the opportunity to grow, compete and succeed through the power of sports.</p>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0" id="offerings" aria-labelledby="offer-title">
  <div class="container">
    <div class="section-head section-head--split reveal">
      <div style="display:grid;gap:18px">
        <span class="eyebrow">Offerings</span>
        <h2 id="offer-title" class="display h-lg">How we <span class="outline">play</span></h2>
      </div>
      <p class="lede">Every format runs on or near your school campus, so getting kids moving never adds to a family’s commute.</p>
    </div>
    <div class="formats" data-stagger="0.1">{offers}</div>
  </div>
</section>

<section class="section sports-wrap" aria-labelledby="aid-title">
  <div class="container intro">
    <div class="intro__media reveal">
      <div class="frame">{img("i3476", "Three smiling girls in Stanford Park Sports Foundation shirts", extra=' data-parallax="0.12"')}</div>
      <div class="tag"><strong>501(c)(3)</strong><span>Stanford Park Sports Foundation</span></div>
    </div>
    <div class="intro__copy">
      <span class="eyebrow reveal">Scholarships &amp; financial aid</span>
      <h2 id="aid-title" class="display h-lg reveal">No kid <span class="outline">sits out</span></h2>
      <p class="lede reveal">Through our nonprofit, the Stanford Park Sports Foundation, we offer scholarships and free programs to under-resourced families and schools. Our goal is to make sure every child can take part, whatever their financial circumstances.</p>
      <div class="btn-row reveal">
        <a class="btn" href="donate.html">Support the Foundation {icon("heart")}</a>
        <a class="btn btn--ghost" href="contact.html">Ask about aid</a>
      </div>
    </div>
  </div>
</section>

</main>
'''
    write("about.html", head("About Us | Stanford Park Youth Sports",
                             "Since 2021, Stanford Park Sports has provided after-school, recess, before-school and camp sports programs for elementary and middle school students across the Bay Area.",
                             "about.html") + header("about.html") + body + footer())


# ================================================================= PROGRAMS
def programs():
    counts = {}
    for p in PROGRAMS:
        counts[p[1]] = counts.get(p[1], 0) + 1
    labels = {"soccer": "Soccer", "basketball": "Basketball", "run": "Run Club"}
    filt = f'<button class="filter" type="button" data-filter="all" aria-pressed="true">All <span class="count">{len(PROGRAMS)}</span></button>'
    for k in ["soccer", "basketball", "run"]:
        filt += f'<button class="filter" type="button" data-filter="{k}" aria-pressed="false">{icon(k, sw=1.8)}{labels[k]} <span class="count">{counts.get(k, 0)}</span></button>'
    cards = ""
    for school, k, sport, day, dates, time, loc, note, price, slug in PROGRAMS:
        n = f'<p class="note">{note}</p>' if note else ""
        cards += f'''<article class="program reveal" data-sport="{k}">
        <div class="program__top"><span class="program__sport">{icon(k, sw=1.8)}{sport}</span><span class="program__price">{price}</span></div>
        <h3>{school}</h3>
        <dl>
          <div><dt>{icon("calendar")}<span class="sr-only">Day</span></dt><dd>{day} · {dates}</dd></div>
          <div><dt>{icon("clock")}<span class="sr-only">Time</span></dt><dd>{time}</dd></div>
          <div><dt>{icon("pin")}<span class="sr-only">Location</span></dt><dd>{loc}</dd></div>
        </dl>
        {n}
        <a class="btn btn--sm" href="{REG_BASE}/{slug}" target="_blank" rel="noopener">Register <span class="sr-only">for {school} {sport.replace("&amp;", "and")}</span>{ARROW}</a>
      </article>'''
    body = f'''<main id="main">
{page_hero("Programs", [("Find your", False), ("school", True)],
            "Current programs, schedules and pricing for Fall 2026. Find your child’s school, pick a sport and register online in a few minutes.",
            "5018", "Young player sprinting toward a soccer ball on the school field",
            mphoto="n23", msmall=True, note="<strong>Please note:</strong> Not every school program is listed here, as many schools manage their own registrations through their internal systems. For the most accurate and up-to-date information, please check with your school’s administration or contact us directly.")}

<section class="section" style="padding-top:clamp(24px,4vw,48px)" aria-labelledby="programs-title">
  <div class="container">
    <div class="section-head section-head--split reveal">
      <div style="display:grid;gap:18px">
        <span class="eyebrow">Fall 2026</span>
        <h2 id="programs-title" class="display h-lg">Current <span class="outline">programs</span></h2>
      </div>
      <p class="lede">Filter by sport, then tap Register to save your spot.</p>
    </div>
    <div class="filters" role="group" aria-label="Filter programs by sport">{filt}</div>
    <p id="filter-status" class="sr-only" aria-live="polite"></p>
    <div class="programs-grid" data-stagger="0.05">{cards}</div>
    <div class="callout reveal">{icon("info")}<p><strong>Don’t see your school?</strong> Not every program is listed here, because many schools manage their own registration. Check with your school’s office, or <a class="link-arrow" href="contact.html" style="font-size:0.8rem">ask us {ARROW}</a></p></div>
  </div>
</section>

{schools_marquee()}

{donate_band()}
</main>
'''
    write("programs.html", head("Current Programs | Stanford Park Youth Sports",
                                "Find your school's Stanford Park Sports program: soccer, basketball and run club schedules, pricing and online registration.",
                                "programs.html") + header("programs.html") + body + footer())


# ================================================================= SCHOOLS
def schools():
    step_html = step_cards()
    grid = "".join(f'<div class="school school--logo reveal">{logo_tile(n, name, "school__logo")}<span>{name if name != "Partner school" else ""}</span></div>' for n, name in LOGOS)
    trust = "".join(f'<li class="trust__item reveal"><div><h3>{t}</h3><p>{d}</p></div></li>' for t, d in SAFETY)
    faq = "".join(f'<details class="reveal"><summary>{q}<span class="plus">{icon("plus", sw=2.5)}</span></summary><div class="answer"><p>{a}</p></div></details>' for q, a in FAQ)
    body = f'''<main id="main">
{page_hero("Schools", [("For", False), ("schools", True)],
            "We partner with public and private schools across the Bay Area to bring high-quality sports programs directly to students, on and off campus.",
            "i1038", "Large group of students holding a Stanford Park Youth Sports banner on a school court",
            f'<a class="btn" href="contact.html">Request a program {ARROW}</a><a class="btn btn--ghost" href="programs.html">Current programs</a>')}

{sports_band(True)}

<section class="section steps-band on-dark" aria-labelledby="how-title">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">How it works</span>
      <h2 id="how-title" class="display h-lg">Up and running <span class="outline">in four steps</span></h2>
    </div>
    <div class="steps reveal-line" data-stagger="0.14">{step_html}</div>
    <div class="steps-cta reveal"><a class="btn btn--cream" href="contact.html">Contact us {ARROW}</a><span>Or call <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></span></div>
  </div>
</section>

<section class="section sports-wrap" aria-labelledby="safe-title">
  <div class="container trust">
    <figure class="trust__media reveal" style="margin:0">
      <div class="frame">{img("5098", "Coach guiding players through a drill on the school field")}</div>
      <figcaption>Active supervision, not passive care</figcaption>
    </figure>
    <div>
      <div class="section-head reveal" style="margin-bottom:32px">
        <span class="eyebrow">Safety &amp; supervision</span>
        <h2 id="safe-title" class="display h-lg">Peace of mind <span class="outline">for your team</span></h2>
      </div>
      <ol class="trust__list">{trust}</ol>
    </div>
  </div>
</section>


<section class="section" aria-labelledby="partner-title">
  <div class="container">
    <div class="section-head section-head--split reveal">
      <div style="display:grid;gap:18px">
        <span class="eyebrow">Partnerships</span>
        <h2 id="partner-title" class="display h-lg">Partnerships <span class="outline">built around you</span></h2>
      </div>
      <p class="lede">Whether you’re a school looking for on-campus programming, a nonprofit seeking collaboration or a company interested in community impact, we tailor partnerships to shared goals.</p>
    </div>
    <div class="plists" data-stagger="0.1">
      <div class="plist reveal"><h3>Who we partner with</h3><ul>
        <li>Public and private schools</li><li>School districts</li><li>Community and youth organizations</li><li>Cities and recreation departments</li><li>Mission-aligned companies and sponsors</li><li>Families and supportive individuals</li></ul></div>
      <div class="plist reveal"><h3>What partnership can look like</h3><ul>
        <li>On-campus sports programming</li><li>Program sponsorships or scholarships</li><li>Joint community initiatives</li><li>Equipment or facility support</li><li>Corporate volunteer engagement</li></ul></div>
      <div class="plist reveal"><h3>Why partner with us</h3><ul>
        <li>Proven, development-first sports programs</li><li>Professional, trained coaches</li><li>Experience serving underserved communities</li><li>Flexible, customized partnership models</li><li>A registered 501(c)(3) nonprofit</li></ul></div>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0" aria-labelledby="list-title">
  <div class="container">
    <div class="section-head section-head--split reveal">
      <div style="display:grid;gap:18px">
        <span class="eyebrow">Our partners</span>
        <h2 id="list-title" class="display h-lg">Trusted by <span class="outline">50+ schools</span></h2>
      </div>
      <p class="lede">A few of the schools where you’ll find us every week.</p>
    </div>
    <div class="school-grid" data-stagger="0.03">{grid}</div>
  </div>
</section>

<section class="section sports-wrap" aria-labelledby="faq-title">
  <div class="container">
    <div class="section-head section-head--center reveal">
      <span class="eyebrow">FAQ</span>
      <h2 id="faq-title" class="display h-lg">Questions, <span class="outline">answered</span></h2>
    </div>
    <div class="faq" data-stagger="0.05">{faq}</div>
  </div>
</section>

<section class="section" aria-labelledby="req-title">
  <div class="container">
    <div class="donate-band on-dark reveal-scale">
      {icon("school", "donate-band__art", 0.6)}
      <div class="donate-band__copy">
        <span class="eyebrow">We’re always adding schools</span>
        <h2 id="req-title" class="display h-lg">Want us at <span class="outline">your school?</span></h2>
        <p class="lede">Tell us a little about your campus and we’ll put together a program that fits.</p>
      </div>
      <div class="donate-band__side">
        <a class="btn btn--cream" href="contact.html">Request a program {ARROW}</a>
        <a class="pill-note" href="tel:{PHONE_TEL}">{icon("phone")} {PHONE_DISPLAY}</a>
      </div>
    </div>
  </div>
</section>
</main>
'''
    write("schools.html", head("For Schools | Stanford Park Youth Sports",
                               "Bring Stanford Park Sports to your campus. After-school, recess, before-school and camp sports programs for Bay Area schools, with trained, background-checked coaches.",
                               "schools.html") + header("schools.html") + body + footer())


# ================================================================= DONATE
def donate():
    tiers = [("$50", "Equipment & supplies", "Balls, cones, pinnies and gear for a program."),
             ("$250", "A full semester", "Covers one student\u2019s full semester of school-based programming."),
             ("$2,500", "An academy season", "A season of professional training for a group of students."),
             ("$5,000", "A new school", "Launches a brand-new program at a school that needs one.")]
    tier_html = "".join(f'''<a class="tier reveal" href="{DONATE_URL}" target="_blank" rel="noopener">
        <span class="tier__amt">{a}</span><h3>{t}</h3><p>{d}</p><span class="tier__cta">Give {a} {ARROW}</span></a>''' for a, t, d in tiers)
    ways = [("heart", "Give online", "One-time or monthly, by card or bank, through our secure Donorbox page.", f'<a class="btn btn--sm" href="{DONATE_URL}" target="_blank" rel="noopener">Donate now {icon("external")}</a>'),
            ("send", "Bank transfer", "ACH or wire transfer. Email us and we\u2019ll send instructions.", f'<a class="btn btn--sm btn--ghost" href="mailto:{EMAIL}?subject=Bank%20transfer%20donation">Email us</a>'),
            ("mail", "Mail a check", f"Payable to Stanford Park Sports Foundation, {ADDRESS}.", ""),
            ("users", "Sponsor a program", "Sponsor a child, a team or a whole school program, or fund scholarships for underserved youth.", f'<a class="btn btn--sm btn--ghost" href="mailto:{EMAIL}?subject=Sponsorship">Talk to us</a>'),
            ("star", "Spread the word", "Share our mission with your network, your school community or your company.", f'<a class="btn btn--sm btn--ghost" href="get-involved.html">Get involved</a>')]
    ways_html = "".join(f'''<article class="way reveal"><span class="way__icon">{icon(ic, sw=1.8)}</span><h3>{t}</h3><p>{d}</p>{btn}</article>''' for ic, t, d, btn in ways)
    impact = [("grad", "Scholarships", "Financial aid so kids from every background can join a program at their school."),
              ("heart", "Free programs", "Fully free sports programs for families and schools that need them most."),
              ("school", "More schools", "Bringing our programs to more schools serving under-resourced kids and families.")]
    cards = "".join(f'<article class="impact__card reveal"><div class="format__icon">{icon(ic, sw=1.8)}</div><h3>{t}</h3><p>{d}</p></article>' for ic, t, d in impact)
    body = f'''<main id="main">
{page_hero("Foundation", [("Give kids", False), ("the game", True)],
            f"Stanford Park Sports is run by the Stanford Park Sports Foundation, a registered 501(c)(3) nonprofit (EIN {EIN}). Your tax-deductible gift helps make sure every child can play.",
            "i3476", "Three smiling girls in Stanford Park Sports Foundation shirts",
            f'<a class="btn" href="{DONATE_URL}" target="_blank" rel="noopener">Donate now {icon("heart")}</a><a class="btn btn--ghost" href="#ways">Other ways to give</a>')}

<section class="section" aria-labelledby="tiers-title" style="padding-top:clamp(24px,4vw,48px)">
  <div class="container">
    <div class="section-head section-head--split reveal">
      <div style="display:grid;gap:18px">
        <span class="eyebrow">Your impact</span>
        <h2 id="tiers-title" class="display h-lg">Every gift <span class="outline">gets kids playing</span></h2>
      </div>
      <p class="lede">Pick an amount to see what it makes possible, or give any amount you like.</p>
    </div>
    <div class="tiers" data-stagger="0.08">{tier_html}</div>
    <p class="match reveal">{icon("users")} <span><strong>Double your gift:</strong> many employers match donations to 501(c)(3) nonprofits. Check with your HR team.</span></p>
  </div>
</section>

<section class="section sports-wrap" id="ways" aria-labelledby="ways-title">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">Ways to give</span>
      <h2 id="ways-title" class="display h-lg">Give the way <span class="outline">that works for you</span></h2>
    </div>
    <div class="ways" data-stagger="0.1">{ways_html}</div>
    <div class="np-facts reveal">
      <div><small>Legal name</small><strong>Stanford Park Sports Foundation</strong></div>
      <div><small>Tax status</small><strong>501(c)(3) nonprofit</strong></div>
      <div><small>Federal Tax ID (EIN)</small><strong>{EIN}</strong></div>
      <div><small>Mailing address</small><strong>{ADDRESS}</strong></div>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="impact-title">
  <div class="container">
    <div class="section-head section-head--split reveal">
      <div style="display:grid;gap:18px">
        <span class="eyebrow">Where your gift goes</span>
        <h2 id="impact-title" class="display h-lg">No kid <span class="outline">sits out</span></h2>
      </div>
      <p class="lede">Financial circumstances should never decide who gets to play. The Foundation closes that gap.</p>
    </div>
    <div class="impact" data-stagger="0.1">{cards}</div>
  </div>
</section>

<section class="section sports-wrap" aria-labelledby="why-title">
  <div class="container intro">
    <div class="intro__media reveal">
      <div class="frame">{img("i7367", "Students and coaches in front of the Stanford Park Sports Foundation bus", extra=' data-parallax="0.12"')}</div>
      <div class="tag"><strong>501(c)(3)</strong><span>EIN {EIN} · Tax-deductible</span></div>
    </div>
    <div class="intro__copy">
      <span class="eyebrow reveal">One organization</span>
      <h2 id="why-title" class="display h-lg reveal">More than a game. <span class="outline">A team.</span></h2>
      <p class="lede reveal">Stanford Park Sports and the Stanford Park Sports Foundation are one team. The same coaches and programs you see at 50+ Bay Area schools are run by a nonprofit whose mission is to help every child stay active, build confidence and love sports.</p>
      <ul class="checks reveal">
        <li>{icon("check", sw=3)} Registered 501(c)(3) nonprofit organization</li>
        <li>{icon("check", sw=3)} Scholarships and free programs for families who need them</li>
        <li>{icon("check", sw=3)} Expanding to more schools serving under-resourced kids</li>
      </ul>
      <div class="btn-row reveal"><a class="btn" href="{DONATE_URL}" target="_blank" rel="noopener">Donate to the Foundation {icon("external")}</a></div>
    </div>
  </div>
</section>
</main>
'''
    write("donate.html", head("Donate | Stanford Park Sports Foundation, a 501(c)(3) Nonprofit",
                              f"Support the Stanford Park Sports Foundation, a registered 501(c)(3) nonprofit (EIN {EIN}) bringing sports programs to 50+ Bay Area schools. Donations are tax-deductible.",
                              "donate.html") + header("donate.html") + body + footer())


# ================================================================= GET INVOLVED
def get_involved():
    roles = [("coach", "clipboard", "Coach", "Coach applicant",
              ["Coaches are the heart of the Stanford Park Sports Foundation. Each season, our coaches mentor and inspire young athletes while leading them through structured, development-focused programs.",
               "You don\u2019t need to be a former professional athlete. What matters most is a positive attitude, a passion for working with kids and a commitment to helping them grow. We provide training, curriculum and ongoing support."],
              "Apply to coach", "5220", "Stanford Park Sports coach with a whistle"),
             ("volunteer", "heart", "Volunteer", "Volunteer",
              ["Volunteers make our programs possible: assisting coaches, supporting practices and helping with events, camps and program operations.",
               "No sports experience is required, just a willingness to help and support kids. Whether you can give one hour or a full season, your time makes a real difference."],
              "Volunteer with us", "i3476", "Smiling girls in Stanford Park Sports Foundation shirts"),
             ("supporter", "star", "Supporter", None,
              ["Supporters make our mission possible. Your support funds coaching, equipment, scholarships and programs in underserved communities.",
               "Make a one-time or recurring donation, sponsor a child, team or program, support scholarships, or share our mission with your network. You don\u2019t need to be on the court to change a child\u2019s life."],
              "Donate now", "i7367", "Students and coaches in front of the Stanford Park Sports Foundation bus")]
    cards = ""
    for i, (rid, ic, title, role, paras, cta, photo, alt) in enumerate(roles):
        href = f"contact.html?role={role.replace(' ', '+')}#form-title" if role else DONATE_URL
        ext = '' if role else ' target="_blank" rel="noopener"'
        ps = "".join(f'<p>{p}</p>' for p in paras)
        cards += f'''<article class="gi-card{" gi-card--mnophoto" if i else ""} reveal" id="{rid}" aria-labelledby="gi-{rid}">
      <div class="gi-card__photo">{img(photo, alt, sizes="(max-width: 960px) 100vw, 33vw")}</div>
      <div class="gi-card__body">
        <span class="gi-card__kicker"><span class="way__icon">{icon(ic, sw=1.8)}</span>Get involved as a</span>
        <h2 id="gi-{rid}" class="display">{title}</h2>
        {ps}
        <a class="btn" href="{href}"{ext}>{cta} {ARROW}</a>
      </div>
    </article>'''
    body = f'''<main id="main">
{page_hero("Get involved", [("Join", False), ("the team", True)],
            "Coaches, volunteers and supporters make it possible for more kids to grow, compete and succeed through sports. Find the way that fits you.",
            "i1038", "Big group of students holding a Stanford Park Youth Sports banner")}
<section class="section" style="padding-top:0" aria-label="Ways to get involved"><div class="container gi-cards" data-stagger="0.1">{cards}</div></section>
{donate_band()}
</main>
'''
    write("get-involved.html", head("Get Involved | Coach, Volunteer or Support Stanford Park Sports",
                                    "Coach, volunteer or support the Stanford Park Sports Foundation, a 501(c)(3) nonprofit bringing sports programs to 50+ Bay Area schools.",
                                    "get-involved.html") + header("get-involved.html") + body + footer())


# ================================================================= CONTACT
def contact():
    body = f'''<main id="main">
{page_hero("Contact", [("Let’s", False), ("talk", True)],
            "Want to start a sports program at your school? Tell us about your campus and we’ll put together a program that fits. Parents and future coaches, we’d love to hear from you too.",
            "4996", "Smiling Stanford Park Sports coach on the school field", mphoto="gym", msmall=True)}

<section class="section" style="padding-top:clamp(24px,4vw,48px)" aria-labelledby="form-title">
  <div class="container contact-grid">
    <div class="form-card reveal">
      <!-- To receive messages without opening the visitor's email app, create a free form at formspree.io
           and add its URL here: data-endpoint="https://formspree.io/f/XXXXXXX" -->
      <form class="form" name="contact" method="POST" data-netlify="true" netlify-honeypot="bot-field" data-contact data-endpoint="/" novalidate>
        <input type="hidden" name="form-name" value="contact"><p hidden><label>Don’t fill this out: <input name="bot-field"></label></p>
        <div>
          <h2 id="form-title" class="display h-md">Start the conversation</h2>
          <p style="color:var(--muted);margin-top:8px">We usually reply within one business day.</p>
        </div>
        <fieldset class="field">
          <legend>I am a…</legend>
          <div class="seg">
            <label><input type="radio" name="role" value="School" checked><span>School</span></label>
            <label><input type="radio" name="role" value="Parent"><span>Parent</span></label>
            <label><input type="radio" name="role" value="Coach applicant"><span>Coach</span></label>
            <label><input type="radio" name="role" value="Volunteer"><span>Volunteer</span></label>
            <label><input type="radio" name="role" value="Partner organization"><span>Partner</span></label>
            <label><input type="radio" name="role" value="Other"><span>Other</span></label>
          </div>
        </fieldset>
        <div class="form-row">
          <div class="field"><label for="f-name">Name</label><input id="f-name" name="name" autocomplete="name" required aria-describedby="e-name"><span class="error" id="e-name">Please enter your name.</span></div>
          <div class="field"><label for="f-email">Email</label><input id="f-email" name="email" type="email" autocomplete="email" required aria-describedby="e-email"><span class="error" id="e-email">Please enter a valid email.</span></div>
        </div>
        <div class="form-row">
          <div class="field"><label for="f-phone">Phone <span class="opt">(optional)</span></label><input id="f-phone" name="phone" type="tel" autocomplete="tel"></div>
          <div class="field"><label for="f-school">School <span class="opt">(optional)</span></label><input id="f-school" name="school" autocomplete="organization"></div>
        </div>
        <div class="field"><label for="f-msg">Message</label><textarea id="f-msg" name="message" required aria-describedby="e-msg"></textarea><span class="error" id="e-msg">Please add a short message.</span></div>
        <button class="btn" type="submit" style="justify-self:start"><span>Send message</span>{icon("send")}</button>
      </form>
      <div class="form-success" tabindex="-1" role="status">
        <div class="tick">{icon("check", sw=3)}</div>
        <h2 class="display h-md">Thanks!</h2>
        <p class="lede" style="text-align:center">Your message is on its way. We’ll get back to you soon.</p>
      </div>
    </div>
    <div class="info-cards" data-stagger="0.1">
      <a class="info-card reveal" href="mailto:{EMAIL}"><span class="ic">{icon("mail")}</span><span><small>Email</small><strong>{EMAIL}</strong></span></a>
      <a class="info-card reveal" href="tel:{PHONE_TEL}"><span class="ic">{icon("phone")}</span><span><small>Phone</small><strong>{PHONE_DISPLAY}</strong></span></a>
      <a class="info-card reveal" href="programs.html"><span class="ic">{icon("calendar")}</span><span><small>Parents</small><strong>Looking to register? See current programs</strong></span></a>
      <a class="info-card reveal" href="schools.html"><span class="ic">{icon("school")}</span><span><small>Schools</small><strong>Learn how partnering works</strong></span></a>
    </div>
  </div>
</section>

{donate_band()}
</main>
'''
    write("contact.html", head("Contact | Stanford Park Youth Sports",
                               "Contact Stanford Park Sports about programs, school partnerships or coaching. info@stanfordparksports.com · (650) 785-9029.",
                               "contact.html") + header("contact.html") + body + footer())


# ---------------------------------------------------------------- favicon
def favicon():
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="8" fill="#8e1316"/>'
           '<g transform="translate(4 4)" fill="none" stroke="#fbf5ec" stroke-width="1.8" stroke-linecap="round">'
           + SPORT["basketball"] + '</g></svg>')
    with open(os.path.join(IMG, "favicon.svg"), "w") as f:
        f.write(svg)


# ---------------------------------------------------------------- launch files
def launch_files():
    pages = ["", "about.html", "programs.html", "schools.html", "get-involved.html", "donate.html", "contact.html"]
    redirects = f"""# Old Wix addresses -> new pages (301 keeps Google rankings)
/about-us            /about.html          301
/schools             /schools.html        301
/contact             /contact.html        301
/current-programs    /programs.html       301
/donate              /donate.html         301
/donate-spsf         /donate.html         301
/get-involved        /get-involved.html   301
# Registration pages still live on Wix (free Wix URL)
/reg-*               {REG_BASE}/reg-:splat   301
"""
    robots = f"""User-agent: *
Disallow: /tools/
Disallow: /flyer/
Disallow: /options.html
Disallow: /hero-options.html
Sitemap: {SITE_URL}/sitemap.xml
"""
    urls = "".join(f"  <url><loc>{SITE_URL}/{p}</loc></url>\n" for p in pages)
    sitemap = f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n'
    for name, body in [("_redirects", redirects), ("robots.txt", robots), ("sitemap.xml", sitemap)]:
        with open(os.path.join(SITE, name), "w") as f:
            f.write(body)
        print("wrote", name)


if __name__ == "__main__":
    favicon()
    home(); about(); programs(); schools(); donate(); get_involved(); contact()
    launch_files()
