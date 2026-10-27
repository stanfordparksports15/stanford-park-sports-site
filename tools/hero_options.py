#!/usr/bin/env python3
"""Prototype page: hero section options."""
import re
import build as b
from options_build import label

IDX = open(b.SITE + "/index.html").read()
CURRENT = re.search(r'<section class="hero".*?</section>', IDX, re.S).group(0)
STATS = re.search(r'<div class="container hero-stats".*?</div>\n  </div>\n', CURRENT, re.S).group(0)
ARROW = b.ARROW


def big(n, alt, w=2600, cls="", eager=False):
    ww, hh = b.dims(n)
    load = 'loading="eager" fetchpriority="high"' if eager else 'loading="lazy"'
    c = f' class="{cls}"' if cls else ""
    return (f'<img{c} src="assets/img/p{n}-{w}.webp" srcset="assets/img/p{n}-1600.webp 1600w, assets/img/p{n}-{w}.webp {w}w" '
            f'sizes="100vw" width="{ww}" height="{hh}" alt="{alt}" {load} decoding="async">')


TITLE = '''<h1 class="display hero__title hx-title">
        <span class="line"><span>We do more than <em>coach.</em></span></span>
        <span class="line"><span>We build <em>character.</em></span></span>
      </h1>'''
LEDE = "Professional after-school, PE, recess, before-school and camp sports programs for Bay Area schools. School programs are all we do, run on your campus by our own trained coaches."


def ctas(light=False):
    g = "btn--outline-cream" if light else "btn--ghost"
    p = "btn--cream" if light else ""
    return f'''<div class="btn-row"><a class="btn {p}" href="contact.html">Bring SPS to your school {ARROW}</a><a class="btn {g}" href="schools.html">How it works</a></div>'''


def badge(extra=""):
    return f'''<div class="badge-spin hx-badge {extra}" aria-hidden="true">
        <svg class="ring" viewBox="0 0 200 200"><defs><path id="circ{extra}" d="M100,100 m-78,0 a78,78 0 1,1 156,0 a78,78 0 1,1 -156,0"/></defs><text><textPath href="#circ{extra}" textLength="486" lengthAdjust="spacing">TRUSTED BY BAY AREA SCHOOLS · 1,000+ KIDS EVERY WEEK ·</textPath></text></svg>
        <span class="badge-spin__center"><b>50+</b><small>Schools</small></span>
      </div>'''


def opt1():
    return f'''<div class="hx-wrap" id="h1">{label("1", "Collage (current)", "Arch photo with two tilted photo cards and the spinning badge. Playful, but the main photo is fairly small and the extra cards compete with it.")}</div>
{CURRENT.replace('id="hero-title"', '').replace('class="hero"', 'class="hero hx-current"')}'''


def opt2():
    return f'''<div class="hx-wrap" id="h2">{label("2", "Full-width photo", "One big photo behind everything with a dark red fade. The strongest first impression and the most “professional” look. Uses your best camera photo.")}</div>
<section class="hx hx--bleed on-dark">
  {big("5063", "Smiling students holding soccer balls with their Stanford Park Sports coach on a school field", cls="hx-bleed__img")}
  <div class="container hx-bleed__inner">
    <div class="hx-bleed__copy">
      <span class="eyebrow">School sports programs · Bay Area · Since 2021</span>
      {TITLE}
      <p class="lede">{LEDE}</p>
      {ctas(light=True)}
    </div>
  </div>
  <div class="container hx-bleed__stats">{STATS.replace('class="container hero-stats"', 'class="hero-stats"')}</div>
</section>'''


def opt3():
    return f'''<div class="hx-wrap" id="h3">{label("3", "Big split photo", "Text on the left, one large photo running off the right edge of the screen. Clean and modern, and keeps the cream look of the rest of the site.")}</div>
<section class="hx hx--split">
  <div class="hx-split__grid">
    <div class="hx-split__copy">
      <span class="eyebrow">School sports programs · Bay Area · Since 2021</span>
      {TITLE}
      <p class="lede">{LEDE}</p>
      {ctas()}
      <p class="hero__alt">Parent at a partner school?<a class="link-arrow" href="programs.html">Find your program {ARROW}</a></p>
    </div>
    <div class="hx-split__media">
      {big("5063", "Smiling students holding soccer balls with their Stanford Park Sports coach on a school field")}
      <span class="hx-chip">Coach-led · On your campus</span>
      {badge("b3")}
    </div>
  </div>
  {STATS}
</section>'''


def opt4():
    slides = [("5063", "Smiling students holding soccer balls with their coach"),
              ("i5196", "Students celebrating with their coach in the gym"),
              ("5220", "Stanford Park Sports coach with a whistle directing a session"),
              ("i1038", "Students holding a Stanford Park Youth Sports banner on a school court")]
    imgs = "".join(f'<figure class="hx-slide{" is-active" if i == 0 else ""}">{big(n, alt, w=2600 if n[0].isdigit() else 2400)}</figure>' for i, (n, alt) in enumerate(slides))
    dots = "".join(f'<button class="hx-dot{" is-active" if i == 0 else ""}" aria-label="Photo {i+1}"></button>' for i in range(len(slides)))
    return f'''<div class="hx-wrap" id="h4">{label("4", "Big arch slideshow", "Keeps the arch shape you have now, but much bigger, with no tilted cards. It fades between four photos: soccer, gym, coach and your banner.")}</div>
<section class="hx hx--arch">
  <div class="container hx-arch__grid">
    <div class="hx-arch__copy">
      <span class="eyebrow">School sports programs · Bay Area · Since 2021</span>
      {TITLE}
      <p class="lede">{LEDE}</p>
      {ctas()}
      <p class="hero__alt">Parent at a partner school?<a class="link-arrow" href="programs.html">Find your program {ARROW}</a></p>
    </div>
    <div class="hx-arch__media">
      <div class="hx-arch__frame">{imgs}</div>
      <div class="hx-dots">{dots}</div>
      {badge("b4")}
    </div>
  </div>
  {STATS}
</section>'''


CSS = '''
<style>
.opt-top { position: sticky; top: 0; z-index: 90; background: var(--ink); color: var(--cream); }
.opt-top .container { display: flex; align-items: center; justify-content: space-between; gap: 16px; min-height: 64px; flex-wrap: wrap; padding-block: 8px; }
.opt-top img { height: 40px; width: auto; background: var(--cream); border-radius: 6px; padding: 4px 8px; }
.opt-top nav { display: flex; gap: 6px; flex-wrap: wrap; }
.opt-top nav a { padding: 8px 14px; border-radius: 6px; font-weight: 800; font-size: 0.85rem; background: rgba(251,245,236,0.1); }
.opt-top nav a:hover { background: var(--maroon); }
.opt-intro { padding-block: 48px 24px; }
.opt-intro h1 { font-family: var(--font-display); text-transform: uppercase; font-size: clamp(2rem, 4vw, 3rem); }
.opt-intro p { color: var(--ink-2); max-width: 72ch; margin-top: 10px; }
.hx-wrap { background: var(--ink); color: var(--cream); padding-block: 18px; scroll-margin-top: 64px; }
.hx-wrap .opt-label { display: flex; align-items: center; gap: 14px; margin: 0 auto; }
.opt-label .opt-label__tag { background: var(--cream); color: var(--maroon); font-family: var(--font-display); text-transform: uppercase; letter-spacing: 0.06em; padding: 8px 14px; border-radius: 6px; font-size: 1.1rem; flex: none; }
.opt-label strong { display: block; font-size: 1.1rem; }
.opt-label span { color: #f2dcd7; font-size: 0.95rem; }
.hx-current { padding-top: clamp(60px, 7vw, 90px); }
.hx { position: relative; overflow: hidden; }
.hx .hero-stats { margin-top: clamp(36px, 4vw, 56px); }
.hx-badge { position: absolute; width: clamp(150px, 15vw, 210px); }

/* 2: full-bleed */
.hx--bleed { min-height: clamp(640px, 92vh, 880px); display: flex; flex-direction: column; justify-content: flex-end; color: var(--cream); padding-block: clamp(90px, 10vw, 140px) 40px; isolation: isolate; }
.hx-bleed__img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: 60% 40%; z-index: -2; animation: settle 2.2s var(--ease-out) both; transform: scale(1.08); }
.hx--bleed::after { content: ""; position: absolute; inset: 0; z-index: -1; background: linear-gradient(90deg, rgba(63,8,9,0.93) 0%, rgba(63,8,9,0.78) 38%, rgba(29,18,19,0.15) 72%), linear-gradient(0deg, rgba(29,18,19,0.75), transparent 45%); }
.hx-bleed__inner { position: relative; }
.hx-bleed__copy { max-width: 700px; display: grid; gap: 24px; }
.hx--bleed .hx-title { color: var(--cream); }
.hx--bleed .hx-title em { color: #f3a9a2; }
.hx--bleed .hx-badge { right: 0; top: -40px; }
.hx--bleed .hero-stats .stat { background: rgba(251,245,236,0.1); border-color: rgba(251,245,236,0.35); box-shadow: none; backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px); }
.hx--bleed .stat__num { color: var(--cream); }
.hx--bleed .stat__label { color: #f2dcd7; }
.hx--bleed .stat svg.corner { color: var(--cream); }

/* 3: split */
.hx--split { padding-block: clamp(60px, 7vw, 90px) clamp(40px, 5vw, 64px); }
.hx-split__grid { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1.05fr); gap: clamp(32px, 4vw, 64px); align-items: center;
  padding-left: max(var(--gutter), calc((100vw - var(--container)) / 2)); }
.hx-split__copy { display: grid; gap: 26px; }
.hx-split__media { position: relative; height: clamp(460px, 44vw, 640px); }
.hx-split__media > img { width: 100%; height: 100%; object-fit: cover; object-position: 55% 40%; border-radius: 16px 0 0 16px; animation: reveal-arch 1.2s var(--ease-out) both; }
.hx-split__media .hx-badge { left: -60px; bottom: -30px; }
.hx-chip { position: absolute; top: 22px; left: 22px; background: var(--cream); color: var(--maroon); font-weight: 800; font-size: 0.78rem; letter-spacing: 0.12em; text-transform: uppercase; padding: 10px 14px; border-radius: 6px; }
.hx--split .hero-stats { width: min(100% - var(--gutter) * 2, var(--container)); margin-inline: auto; }

/* 4: arch slideshow */
.hx--arch { padding-block: clamp(60px, 7vw, 90px) clamp(40px, 5vw, 64px); }
.hx-arch__grid { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: clamp(32px, 4vw, 64px); align-items: center; }
.hx-arch__copy { display: grid; gap: 26px; }
.hx-arch__media { position: relative; }
.hx-arch__frame { position: relative; aspect-ratio: 1 / 1.08; border-radius: 999px 999px 18px 18px; overflow: hidden; border: 3px solid var(--maroon); box-shadow: 12px 12px 0 var(--maroon); background: var(--cream-2); }
.hx-slide { position: absolute; inset: 0; margin: 0; opacity: 0; transition: opacity 1.1s var(--ease-out); }
.hx-slide.is-active { opacity: 1; }
.hx-slide img { width: 100%; height: 100%; object-fit: cover; transform: scale(1.1); transition: transform 6s linear; }
.hx-slide.is-active img { transform: scale(1); }
.hx-dots { display: flex; gap: 8px; justify-content: center; margin-top: 22px; }
.hx-dot { width: 34px; height: 6px; border-radius: 6px; border: 0; background: var(--line); padding: 0; transition: background-color 0.3s, width 0.3s; }
.hx-dot.is-active { background: var(--maroon); width: 54px; }
.hx-arch__media .hx-badge { right: -20px; bottom: 40px; }

@media (max-width: 960px) {
  .hx-split__grid, .hx-arch__grid { grid-template-columns: 1fr; padding-left: 0; }
  .hx-split__copy { padding-inline: var(--gutter); }
  .hx-split__media > img { border-radius: 0; }
  .hx-split__media .hx-badge { left: auto; right: 16px; bottom: -40px; }
  .hx--bleed .hx-badge { display: none; }
  .hx--bleed::after { background: linear-gradient(0deg, rgba(63,8,9,0.95) 30%, rgba(29,18,19,0.35)); }
}
</style>
'''

JS = '''
<script>
(function () {
  var slides = [].slice.call(document.querySelectorAll(".hx-slide"));
  var dots = [].slice.call(document.querySelectorAll(".hx-dot"));
  if (!slides.length) return;
  var i = 0, reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches, t;
  function show(n) { i = n; slides.forEach(function (s, k) { s.classList.toggle("is-active", k === n); }); dots.forEach(function (d, k) { d.classList.toggle("is-active", k === n); }); }
  function start() { if (reduce) return; clearInterval(t); t = setInterval(function () { show((i + 1) % slides.length); }, 4500); }
  dots.forEach(function (d, k) { d.addEventListener("click", function () { show(k); start(); }); });
  start();
})();
</script>
'''


def page():
    top = '''<div class="opt-top"><div class="container">
  <a href="index.html"><img src="assets/img/logo.png" alt="Stanford Park Youth Sports" width="640" height="184"></a>
  <nav aria-label="Options"><a href="#h1">1 · Current</a><a href="#h2">2 · Full photo</a><a href="#h3">3 · Split</a><a href="#h4">4 · Slideshow</a><a href="options.html">Section options →</a></nav>
</div></div>'''
    intro = '''<div class="container opt-intro">
  <span class="eyebrow">Prototype · pick one</span>
  <h1>Hero (first screen): 4 options</h1>
  <p>Same headline, buttons and numbers in each; only the photo treatment changes. Look at each one as if you were a principal landing on the site for the first time.</p>
</div>'''
    html = b.head("Hero options | Stanford Park Youth Sports", "Design options for the homepage hero.", "hero-options.html")
    html = html.replace("</head>", CSS + "</head>")
    html += top + '<main id="main">' + intro + opt1() + opt2() + opt3() + opt4() + "</main>"
    html += '<script src="assets/js/site.js?v=20261027" defer></script>' + JS + "</body></html>\n"
    b.write("hero-options.html", html)


if __name__ == "__main__":
    page()
