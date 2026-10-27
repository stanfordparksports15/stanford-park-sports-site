#!/usr/bin/env python3
"""Prototype page: design options for the 'Five ways to partner' section."""
import build as b

F = b.SCHOOL_FORMATS  # (icon, title, desc, when)
PH = b.FORMAT_PHOTOS

# Chronological order for the "day at your school" timeline
DAY = [("sunrise", "Morning"), ("clipboard", "During class time"), ("sun", "Midday"),
       ("backpack", "After the bell"), ("tent", "School breaks")]
BY_ICON = {f[0]: f for f in F}


def label(letter, name, note):
    return f'''<div class="opt-label container">
  <span class="opt-label__tag">Option {letter}</span>
  <div><strong>{name}</strong><span>{note}</span></div>
</div>'''


def head_block():
    return f'''<div class="section-head section-head--split reveal">
      <div style="display:grid;gap:18px">
        <span class="eyebrow">What we run for schools</span>
        <h2 class="display h-lg">Five ways <span class="outline">to partner</span></h2>
      </div>
      <p class="lede">Choose one format or combine them. Every program fits into your school day and runs on your campus.</p>
    </div>'''


# ---------------- Option A: current photo cards
def option_a():
    more = f'''<a class="format format--more reveal" href="contact.html">
        <span class="format__no">06</span>
        <div class="format__icon">{b.icon("plus", sw=2)}</div>
        <h3>And more</h3><p>Clinics, special events or something custom. Tell us what your school needs and we’ll build it.</p><span class="format__when">Let’s talk {b.ARROW}</span>
      </a>'''
    return f'''<section class="section opt" id="opt-a">
  {label("A", "Photo cards (current)", "Six equal cards in a grid. Simple and scannable, but every card has the same weight.")}
  <div class="container">{head_block()}<div class="formats" data-stagger="0.1">{b.format_cards(F)}{more}</div></div>
</section>'''


# ---------------- Option B: spotlight (list + big photo)
def option_b():
    tabs, panels = "", ""
    for i, (ic, t, d, w) in enumerate(F):
        n, alt = PH[ic]
        sel = "true" if i == 0 else "false"
        tabs += f'''<button class="spot__tab" role="tab" id="spot-tab-{i}" aria-selected="{sel}" aria-controls="spot-panel-{i}" data-i="{i}">
          <span class="spot__no">0{i+1}</span><span class="spot__name">{t}</span><span class="spot__when">{w}</span>
          <span class="spot__bar"><i></i></span>
        </button>'''
        panels += f'''<div class="spot__panel{' is-active' if i == 0 else ''}" role="tabpanel" id="spot-panel-{i}" aria-labelledby="spot-tab-{i}">
          {b.img(n, alt, sizes="(max-width: 960px) 100vw, 60vw")}
          <div class="spot__caption"><span class="spot__icon">{b.icon(ic, sw=1.8)}</span><div><h3>{t}</h3><p>{d}</p></div></div>
        </div>'''
    return f'''<section class="section opt opt--tint" id="opt-b">
  {label("B", "Spotlight", "One format at a time with a big photo. Rotates on its own every few seconds; hover or tap a format to jump to it.")}
  <div class="container">{head_block()}
    <div class="spot reveal">
      <div class="spot__list" role="tablist" aria-label="Program formats">{tabs}
        <a class="btn" href="contact.html" style="margin-top:8px">Build my school’s program {b.ARROW}</a>
      </div>
      <div class="spot__stage">{panels}</div>
    </div>
  </div>
</section>'''


# ---------------- Option C: expanding panels
def option_c():
    panels = ""
    for i, (ic, t, d, w) in enumerate(F):
        n, alt = PH[ic]
        panels += f'''<button class="acc__panel{' is-open' if i == 0 else ''}" type="button" aria-expanded="{'true' if i == 0 else 'false'}">
          {b.img(n, alt, sizes="(max-width: 960px) 100vw, 55vw", cls="acc__bg")}
          <span class="acc__no">0{i+1}</span>
          <span class="acc__vtitle">{t}</span>
          <span class="acc__content"><span class="acc__when">{w}</span><span class="acc__title">{t}</span><span class="acc__desc">{d}</span></span>
        </button>'''
    return f'''<section class="section opt" id="opt-c">
  {label("C", "Expanding panels", "Five tall photo strips side by side. The one you hover opens wide to show its details. Very visual and interactive.")}
  <div class="container">{head_block()}<div class="acc reveal">{panels}</div></div>
</section>'''


# ---------------- Option D: a day at your school (timeline)
def option_d():
    stops = ""
    for i, (ic, when) in enumerate(DAY):
        _, t, d, _w = BY_ICON[ic]
        n, alt = PH[ic]
        stops += f'''<div class="day__stop reveal">
          <span class="day__time">{when}</span>
          <span class="day__dot">{b.icon(ic, sw=1.8)}</span>
          <div class="day__card">
            <div class="day__photo">{b.img(n, alt, sizes="(max-width: 960px) 50vw, 20vw")}</div>
            <h3>{t}</h3><p>{d}</p>
          </div>
        </div>'''
    return f'''<section class="section opt steps-band on-dark" id="opt-d">
  {label("D", "A day at your school", "The formats laid out along a school day, from morning to school breaks. Tells the story that you cover the whole day.")}
  <div class="container">
    <div class="section-head section-head--split reveal">
      <div style="display:grid;gap:18px">
        <span class="eyebrow">What we run for schools</span>
        <h2 class="display h-lg">From first bell <span class="outline">to last.</span></h2>
      </div>
      <p class="lede">Five ways to partner, covering your whole school day and every break in between.</p>
    </div>
    <div class="day reveal-line" data-stagger="0.12">{stops}</div>
  </div>
</section>'''


CSS = '''
<style>
.opt-top { position: sticky; top: 0; z-index: 90; background: var(--ink); color: var(--cream); }
.opt-top .container { display: flex; align-items: center; justify-content: space-between; gap: 16px; min-height: 64px; flex-wrap: wrap; padding-block: 8px; }
.opt-top img { height: 40px; width: auto; background: var(--cream); border-radius: 6px; padding: 4px 8px; }
.opt-top nav { display: flex; gap: 6px; flex-wrap: wrap; }
.opt-top nav a { padding: 8px 14px; border-radius: 6px; font-weight: 800; font-size: 0.85rem; background: rgba(251,245,236,0.1); }
.opt-top nav a:hover { background: var(--maroon); }
.opt-intro { padding-block: 48px 8px; }
.opt-intro h1 { font-family: var(--font-display); text-transform: uppercase; font-size: clamp(2rem, 4vw, 3rem); }
.opt-intro p { color: var(--ink-2); max-width: 70ch; margin-top: 10px; }
.opt { border-top: 2px dashed var(--line); scroll-margin-top: 64px; }
.opt--tint { background: var(--paper); }
.opt-label { display: flex; align-items: center; gap: 14px; margin-bottom: 36px; }
.opt-label .opt-label__tag { background: var(--ink); color: var(--cream); font-family: var(--font-display); text-transform: uppercase; letter-spacing: 0.06em; padding: 8px 14px; border-radius: 6px; font-size: 1.1rem; flex: none; }
.opt-label strong { display: block; font-size: 1.1rem; }
.opt-label span { color: var(--muted); font-size: 0.95rem; }
.on-dark .opt-label .opt-label__tag { background: var(--cream); color: var(--maroon); }
.on-dark .opt-label strong { color: var(--cream); }
.on-dark .opt-label span { color: #f2dcd7; }

/* B: spotlight */
.spot { display: grid; grid-template-columns: minmax(280px, 0.8fr) 1.6fr; gap: 28px; align-items: stretch; }
.spot__list { display: grid; gap: 10px; align-content: start; }
.spot__tab { position: relative; display: grid; grid-template-columns: auto 1fr; grid-template-areas: "no name" "no when"; column-gap: 16px; text-align: left;
  padding: 18px 20px; border-radius: 10px; border: 1.5px solid var(--line); background: var(--cream); overflow: hidden;
  transition: background-color 0.3s, border-color 0.3s, color 0.3s, transform 0.3s var(--ease-out); }
.spot__tab:hover { transform: translateX(4px); border-color: var(--maroon); }
.spot__no { grid-area: no; font-family: var(--font-display); font-size: 2rem; line-height: 1; color: var(--maroon); align-self: center; }
.spot__name { grid-area: name; font-family: var(--font-display); text-transform: uppercase; font-size: 1.45rem; line-height: 1.05; }
.spot__when { grid-area: when; font-size: 0.78rem; font-weight: 800; letter-spacing: 0.12em; text-transform: uppercase; color: var(--muted); }
.spot__bar { position: absolute; left: 0; right: 0; bottom: 0; height: 3px; background: transparent; }
.spot__bar i { display: block; height: 100%; background: var(--cream); transform-origin: left; transform: scaleX(0); }
.spot__tab[aria-selected="true"] { background: var(--maroon); border-color: var(--maroon); color: var(--cream); }
.spot__tab[aria-selected="true"] .spot__no { color: #f3c9c4; }
.spot__tab[aria-selected="true"] .spot__when { color: #f3c9c4; }
.spot__tab[aria-selected="true"] .spot__bar i { animation: spotbar var(--spot-dur, 5s) linear forwards; }
.spot.is-paused .spot__bar i { animation-play-state: paused; }
@keyframes spotbar { to { transform: scaleX(1); } }
.spot__stage { position: relative; min-height: 520px; border-radius: 12px; overflow: hidden; background: var(--maroon-900); }
.spot__panel { position: absolute; inset: 0; opacity: 0; transition: opacity 0.6s var(--ease-out); }
.spot__panel.is-active { opacity: 1; }
.spot__panel img { width: 100%; height: 100%; object-fit: cover; transform: scale(1.08); transition: transform 6s linear; }
.spot__panel.is-active img { transform: scale(1); }
.spot__caption { position: absolute; left: 20px; right: 20px; bottom: 20px; display: flex; gap: 16px; align-items: flex-start;
  background: rgba(251,245,236,0.96); border-radius: 10px; padding: 20px 22px; transform: translateY(20px); opacity: 0; transition: all 0.6s var(--ease-out) 0.15s; }
.spot__panel.is-active .spot__caption { transform: none; opacity: 1; }
.spot__caption h3 { font-family: var(--font-display); text-transform: uppercase; font-size: 1.8rem; line-height: 1; margin-bottom: 6px; }
.spot__caption p { color: var(--ink-2); }
.spot__icon { width: 52px; height: 52px; flex: none; border-radius: 10px; background: var(--maroon); color: var(--cream); display: grid; place-items: center; }
.spot__icon svg { width: 28px; height: 28px; }

/* C: expanding panels */
.acc { display: flex; gap: 12px; height: clamp(440px, 42vw, 560px); }
.acc__panel { position: relative; flex: 1; min-width: 0; border: 0; padding: 0; border-radius: 12px; overflow: hidden; isolation: isolate; color: var(--cream); text-align: left;
  transition: flex 0.7s var(--ease-out); background: var(--maroon-900); }
.acc__panel.is-open { flex: 4.2; }
.acc__bg { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; z-index: -2; transition: transform 1s var(--ease-out), filter 0.5s; filter: saturate(0.85); }
.acc__panel.is-open .acc__bg { filter: none; }
.acc__panel::after { content: ""; position: absolute; inset: 0; z-index: -1; background: linear-gradient(180deg, rgba(63,8,9,0.25), rgba(63,8,9,0.85)); transition: background 0.5s; }
.acc__panel.is-open::after { background: linear-gradient(180deg, rgba(29,18,19,0.05) 30%, rgba(63,8,9,0.92)); }
.acc__no { position: absolute; top: 18px; left: 18px; font-family: var(--font-display); background: var(--maroon); padding: 6px 10px; border-radius: 6px; font-size: 1.05rem; }
.acc__vtitle { position: absolute; left: 50%; bottom: 24px; transform: translateX(-50%) rotate(180deg); writing-mode: vertical-rl; white-space: nowrap;
  font-family: var(--font-display); text-transform: uppercase; font-size: clamp(1.4rem, 2vw, 1.9rem); transition: opacity 0.3s; }
.acc__panel.is-open .acc__vtitle { opacity: 0; }
.acc__content { position: absolute; left: 28px; right: 28px; bottom: 28px; display: grid; gap: 10px; max-width: 520px; opacity: 0; transform: translateY(16px); transition: opacity 0.4s, transform 0.5s var(--ease-out); pointer-events: none; }
.acc__panel.is-open .acc__content { opacity: 1; transform: none; transition-delay: 0.25s; }
.acc__when { justify-self: start; background: var(--cream); color: var(--maroon); font-weight: 800; font-size: 0.74rem; letter-spacing: 0.12em; text-transform: uppercase; padding: 6px 10px; border-radius: 6px; }
.acc__title { font-family: var(--font-display); text-transform: uppercase; font-size: clamp(2rem, 3.4vw, 3rem); line-height: 1; }
.acc__desc { color: #f2dcd7; font-size: 1.02rem; }

/* D: day timeline */
.day { display: grid; grid-template-columns: repeat(5, 1fr); gap: 18px; position: relative; }
.day.reveal-line::before, .day.reveal-line::after { content: ""; position: absolute; left: 28px; right: 28px; top: 58px; height: 3px; border-radius: 3px; }
.day.reveal-line::before { background: rgba(251,245,236,0.22); }
.day.reveal-line::after { background: var(--cream); transform-origin: left; transform: scaleX(0); transition: transform 2s var(--ease-out) 0.2s; }
.day.reveal-line.is-in::after { transform: scaleX(1); }
.day__stop { display: flex; flex-direction: column; gap: 14px; }
.day__stop .day__card { flex: 1; }
.day__time { font-weight: 800; font-size: 0.78rem; letter-spacing: 0.14em; text-transform: uppercase; color: #f3c9c4; height: 18px; }
.day__dot { position: relative; z-index: 1; width: 56px; height: 56px; border-radius: 50%; background: var(--cream); color: var(--maroon); display: grid; place-items: center; box-shadow: 0 0 0 6px var(--maroon); }
.day__dot svg { width: 26px; height: 26px; }
.day__card { background: var(--paper); color: var(--ink); border-radius: 12px; overflow: hidden; display: grid; align-content: start; height: 100%;
  transition: transform 0.35s var(--ease-out), box-shadow 0.35s; }
.day__card:hover { transform: translateY(-6px); box-shadow: 0 22px 36px -22px rgba(0,0,0,0.6); }
.day__photo { aspect-ratio: 4 / 3; overflow: hidden; }
.day__photo img { width: 100%; height: 100%; object-fit: cover; transition: transform 0.9s var(--ease-out); }
.day__card:hover .day__photo img { transform: scale(1.06); }
.day__card h3 { font-family: var(--font-display); text-transform: uppercase; font-size: 1.45rem; line-height: 1.05; padding: 16px 18px 6px; }
.day__card p { color: var(--ink-2); font-size: 0.92rem; padding: 0 18px 20px; }

@media (max-width: 960px) {
  .spot { grid-template-columns: 1fr; }
  .spot__stage { min-height: 440px; order: -1; }
  .acc { flex-direction: column; height: auto; }
  .acc__panel, .acc__panel.is-open { flex: none; height: 320px; }
  .acc__vtitle { display: none; }
  .acc__content { opacity: 1; transform: none; }
  .day { grid-template-columns: 1fr 1fr; }
  .day.reveal-line::before, .day.reveal-line::after { display: none; }
}
@media (max-width: 640px) { .day { grid-template-columns: 1fr; } }
</style>
'''

JS = '''
<script>
(function () {
  // Option B: spotlight tabs with auto-rotate
  var spot = document.querySelector(".spot");
  if (spot) {
    var tabs = [].slice.call(spot.querySelectorAll(".spot__tab"));
    var panels = [].slice.call(spot.querySelectorAll(".spot__panel"));
    var cur = 0, timer = null, DUR = 5000;
    var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    function show(i) {
      cur = i;
      tabs.forEach(function (t, k) { t.setAttribute("aria-selected", String(k === i)); });
      panels.forEach(function (p, k) { p.classList.toggle("is-active", k === i); });
    }
    function start() { if (reduce) return; stop(); timer = setInterval(function () { show((cur + 1) % tabs.length); }, DUR); spot.classList.remove("is-paused"); }
    function stop() { if (timer) clearInterval(timer); timer = null; spot.classList.add("is-paused"); }
    tabs.forEach(function (t, i) {
      t.addEventListener("mouseenter", function () { show(i); stop(); });
      t.addEventListener("click", function () { show(i); stop(); });
      t.addEventListener("focus", function () { show(i); stop(); });
    });
    spot.addEventListener("mouseleave", start);
    start();
  }
  // Option C: expanding panels
  var acc = [].slice.call(document.querySelectorAll(".acc__panel"));
  function open(p) { acc.forEach(function (x) { var on = x === p; x.classList.toggle("is-open", on); x.setAttribute("aria-expanded", String(on)); }); }
  acc.forEach(function (p) {
    p.addEventListener("mouseenter", function () { open(p); });
    p.addEventListener("focus", function () { open(p); });
    p.addEventListener("click", function () { open(p); });
  });
})();
</script>
'''


def page():
    top = f'''<div class="opt-top"><div class="container">
  <a href="index.html"><img src="assets/img/logo.png" alt="Stanford Park Youth Sports" width="640" height="184"></a>
  <nav aria-label="Options"><a href="#opt-a">A · Current</a><a href="#opt-b">B · Spotlight</a><a href="#opt-c">C · Panels</a><a href="#opt-d">D · School day</a></nav>
</div></div>'''
    intro = '''<div class="container opt-intro">
  <span class="eyebrow">Prototype · pick one</span>
  <h1>"Five ways to partner": 4 design options</h1>
  <p>Same content, photos and brand in each. Scroll through, try hovering and clicking, then tell us which letter to use on the homepage.</p>
</div>'''
    html = b.head("Section options | Stanford Park Youth Sports", "Design options for the Five ways to partner section.", "options.html")
    html = html.replace("</head>", CSS + "</head>")
    html += top + '<main id="main">' + intro + option_a() + option_b() + option_c() + option_d() + "</main>"
    html += '<script src="assets/js/site.js?v=20261027" defer></script>' + JS + "</body></html>\n"
    b.write("options.html", html)


if __name__ == "__main__":
    page()
