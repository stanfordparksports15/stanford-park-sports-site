/* Stanford Park Youth Sports — interactions (no dependencies) */
(function () {
  "use strict";

  var root = document.documentElement;
  root.classList.remove("no-js");
  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- Header: solid on scroll, hide on scroll down ---------- */
  var header = document.querySelector(".site-header");
  var lastY = window.scrollY;
  function onScrollHeader() {
    var y = window.scrollY;
    if (!header) return;
    header.classList.toggle("is-scrolled", y > 24);
    var goingDown = y > lastY && y > 400;
    if (!document.body.classList.contains("menu-open")) header.classList.toggle("is-hidden", goingDown);
    lastY = y;
  }

  /* ---------- Mobile menu ---------- */
  var toggle = document.querySelector(".menu-toggle");
  var menu = document.getElementById("mobile-menu");
  function setMenu(open) {
    document.body.classList.toggle("menu-open", open);
    toggle.setAttribute("aria-expanded", String(open));
    toggle.setAttribute("aria-label", open ? "Close menu" : "Open menu");
    menu.setAttribute("aria-hidden", String(!open));
    if (open) {
      header.classList.remove("is-hidden");
      var first = menu.querySelector("a");
      if (first) setTimeout(function () { first.focus(); }, 250);
    }
  }
  if (toggle && menu) {
    toggle.addEventListener("click", function () {
      setMenu(!document.body.classList.contains("menu-open"));
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && document.body.classList.contains("menu-open")) { setMenu(false); toggle.focus(); }
    });
    menu.querySelectorAll("a").forEach(function (a) { a.addEventListener("click", function () { setMenu(false); }); });
  }

  /* ---------- Scroll reveal ---------- */
  var revealEls = document.querySelectorAll(".reveal, .reveal-scale, .reveal-clip, .reveal-line");
  if ("IntersectionObserver" in window && !reduceMotion) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) { entry.target.classList.add("is-in"); io.unobserve(entry.target); }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.12 });
    revealEls.forEach(function (el) { io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add("is-in"); });
  }

  /* Stagger children: [data-stagger] sets --d on each .reveal child */
  document.querySelectorAll("[data-stagger]").forEach(function (group) {
    var step = parseFloat(group.getAttribute("data-stagger")) || 0.08;
    group.querySelectorAll(":scope > .reveal, :scope > .reveal-scale").forEach(function (el, i) {
      el.style.setProperty("--d", (i * step).toFixed(2) + "s");
    });
  });

  /* ---------- Count-up numbers ---------- */
  function countUp(el) {
    var target = parseFloat(el.getAttribute("data-count"));
    var suffix = el.getAttribute("data-suffix") || "";
    var fmt = function (n) { return Math.round(n).toLocaleString("en-US") + suffix; };
    if (reduceMotion) { el.textContent = fmt(target); return; }
    var start = null, dur = 1600;
    function frame(t) {
      if (!start) start = t;
      var p = Math.min((t - start) / dur, 1);
      var eased = 1 - Math.pow(1 - p, 4);
      el.textContent = fmt(target * eased);
      if (p < 1) requestAnimationFrame(frame);
    }
    requestAnimationFrame(frame);
  }
  var counters = document.querySelectorAll("[data-count]");
  if ("IntersectionObserver" in window) {
    var cio = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { countUp(e.target); cio.unobserve(e.target); } });
    }, { threshold: 0.6 });
    counters.forEach(function (el) { cio.observe(el); });
  } else {
    counters.forEach(countUp);
  }

  /* ---------- Parallax: hero collage (pointer) + [data-parallax] (scroll) ---------- */
  var collage = document.querySelector(".collage");
  var pointer = { x: 0, y: 0 }, eased = { x: 0, y: 0 };
  var finePointer = window.matchMedia("(pointer: fine)").matches;
  if (collage && finePointer && !reduceMotion) {
    window.addEventListener("pointermove", function (e) {
      pointer.x = e.clientX / window.innerWidth - 0.5;
      pointer.y = e.clientY / window.innerHeight - 0.5;
    }, { passive: true });
  }
  var parallaxEls = Array.prototype.slice.call(document.querySelectorAll("[data-parallax]"));
  var collageLayers = collage ? Array.prototype.slice.call(collage.querySelectorAll("[data-depth]")) : [];

  /* ---------- Horizontal gallery driven by vertical scroll ---------- */
  var gallery = document.querySelector(".gallery");
  var track = gallery && gallery.querySelector(".gallery__track");
  var bar = gallery && gallery.querySelector(".gallery__progress i");
  var galleryActive = false, galleryDistance = 0;
  var wideMQ = window.matchMedia("(min-width: 961px)");
  function sizeGallery() {
    if (!gallery || !track) return;
    galleryActive = wideMQ.matches && !reduceMotion;
    if (!galleryActive) { gallery.style.height = ""; track.style.transform = ""; return; }
    galleryDistance = Math.max(0, track.scrollWidth - window.innerWidth);
    gallery.style.height = (window.innerHeight + galleryDistance) + "px";
  }

  /* Runs only when something actually changed (scroll, pointer move, resize),
     never as a permanent per-frame loop. */
  var collageOn = collageLayers.length && !reduceMotion && getComputedStyle(collage).display !== "none";
  var depths = collageLayers.map(function (el) { return parseFloat(el.getAttribute("data-depth")); });
  var speeds = parallaxEls.map(function (el) { return parseFloat(el.getAttribute("data-parallax")) || 0.1; });
  var visible = parallaxEls.map(function () { return false; });
  if ("IntersectionObserver" in window && parallaxEls.length) {
    var pio = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        var i = parallaxEls.findIndex(function (el) { return el.parentElement === e.target; });
        if (i > -1) visible[i] = e.isIntersecting;
      });
      schedule();
    });
    parallaxEls.forEach(function (el) { pio.observe(el.parentElement); });
  }

  var queued = false;
  function schedule() { if (!queued) { queued = true; requestAnimationFrame(tick); } }

  function tick() {
    queued = false;
    var vh = window.innerHeight, sy = window.scrollY, again = false;

    if (collageOn && sy < vh * 1.2) {
      eased.x += (pointer.x - eased.x) * 0.08;
      eased.y += (pointer.y - eased.y) * 0.08;
      var heroScroll = Math.min(sy, vh);
      for (var i = 0; i < collageLayers.length; i++) {
        var d = depths[i];
        collageLayers[i].style.transform = "translate3d(" + (eased.x * d * 40).toFixed(1) + "px," + (eased.y * d * 40 - heroScroll * d * 0.12).toFixed(1) + "px,0)";
      }
      // keep easing toward the pointer until it settles, then stop
      again = Math.abs(pointer.x - eased.x) > 0.001 || Math.abs(pointer.y - eased.y) > 0.001;
    }

    if (!reduceMotion) {
      for (var j = 0; j < parallaxEls.length; j++) {
        if (!visible[j]) continue;
        var r = parallaxEls[j].parentElement.getBoundingClientRect();
        var progress = (r.top + r.height / 2 - vh / 2) / vh;
        parallaxEls[j].style.transform = "translate3d(0," + (progress * speeds[j] * -100).toFixed(1) + "px,0)";
      }
    }

    updateGallery();
    if (again) schedule();
  }

  if (collageOn && finePointer) window.addEventListener("pointermove", schedule, { passive: true });
  window.addEventListener("scroll", schedule, { passive: true });
  window.addEventListener("resize", schedule);

  /* Pause the scrolling strips (sports band, school logos, photo strip) while off-screen */
  if ("IntersectionObserver" in window) {
    var mio = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { e.target.classList.toggle("is-paused", !e.isIntersecting); });
    }, { rootMargin: "100px 0px" });
    document.querySelectorAll(".marquee").forEach(function (m) { mio.observe(m); });
  }

  function updateGallery() {
    if (!galleryActive) return;
    var gr = gallery.getBoundingClientRect();
    var p = Math.min(Math.max(-gr.top / (gr.height - window.innerHeight), 0), 1);
    track.style.transform = "translate3d(" + (-p * galleryDistance).toFixed(1) + "px,0,0)";
    if (bar) bar.style.transform = "scaleX(" + p.toFixed(3) + ")";
  }

  window.addEventListener("scroll", onScrollHeader, { passive: true });
  window.addEventListener("resize", sizeGallery);
  window.addEventListener("load", sizeGallery);
  onScrollHeader();
  sizeGallery();
  schedule();

  /* ---------- Programs filter ---------- */
  var filters = document.querySelectorAll(".filter[data-filter]");
  var programs = document.querySelectorAll(".program[data-sport]");
  var status = document.getElementById("filter-status");
  filters.forEach(function (btn) {
    btn.addEventListener("click", function () {
      var f = btn.getAttribute("data-filter");
      filters.forEach(function (b) { b.setAttribute("aria-pressed", String(b === btn)); });
      var shown = 0, i = 0;
      programs.forEach(function (card) {
        var match = f === "all" || card.getAttribute("data-sport") === f;
        card.classList.toggle("is-hidden", !match);
        if (match) {
          shown++;
          card.classList.remove("is-in");
          card.style.setProperty("--d", (i++ * 0.05).toFixed(2) + "s");
          requestAnimationFrame(function () { requestAnimationFrame(function () { card.classList.add("is-in"); }); });
        }
      });
      if (status) status.textContent = shown + " program" + (shown === 1 ? "" : "s") + " shown";
    });
  });

  /* ---------- Contact form ----------
     If the form has a data-endpoint (e.g. a Formspree URL) it posts there.
     Otherwise it opens the visitor's email app with the message pre-filled. */
  var form = document.querySelector("form[data-contact]");
  if (form) {
    // Preselect "I am a..." from ?role= links (e.g. Get Involved page)
    var wantRole = new URLSearchParams(location.search).get("role");
    if (wantRole) {
      var radio = form.querySelector('input[name="role"][value="' + wantRole.replace(/"/g, "") + '"]');
      if (radio) radio.checked = true;
    }
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var ok = true, firstBad = null;
      form.querySelectorAll("[required]").forEach(function (input) {
        var field = input.closest(".field");
        var valid = input.value.trim() !== "" && (input.type !== "email" || /^\S+@\S+\.\S+$/.test(input.value));
        if (field) field.classList.toggle("has-error", !valid);
        input.setAttribute("aria-invalid", String(!valid));
        if (!valid && !firstBad) firstBad = input;
        ok = ok && valid;
      });
      if (!ok) { firstBad.focus(); return; }

      var data = new FormData(form);
      var card = form.closest(".form-card");
      var endpoint = form.getAttribute("data-endpoint");
      var btn = form.querySelector("button[type=submit]");

      function done() { card.classList.add("is-sent"); card.querySelector(".form-success").focus(); }

      if (endpoint) {
        btn.disabled = true; btn.querySelector("span").textContent = "Sending…";
        fetch(endpoint, { method: "POST", body: new URLSearchParams(data).toString(), headers: { "Content-Type": "application/x-www-form-urlencoded" } })
          .then(function (r) { if (!r.ok) throw new Error(); done(); })
          .catch(function () {
            btn.disabled = false; btn.querySelector("span").textContent = "Send message";
            alert("Sorry, something went wrong. Please email info@stanfordparksports.com.");
          });
      } else {
        var who = data.get("role") || "Visitor";
        var subject = "Website inquiry (" + who + ")" + (data.get("school") ? " — " + data.get("school") : "");
        var body = "Name: " + data.get("name") + "\nEmail: " + data.get("email") +
          (data.get("phone") ? "\nPhone: " + data.get("phone") : "") +
          (data.get("school") ? "\nSchool: " + data.get("school") : "") +
          "\nI am a: " + who + "\n\n" + data.get("message");
        window.location.href = "mailto:info@stanfordparksports.com?subject=" + encodeURIComponent(subject) + "&body=" + encodeURIComponent(body);
        done();
      }
    });
    form.querySelectorAll("input, textarea").forEach(function (input) {
      input.addEventListener("input", function () {
        var field = input.closest(".field");
        if (field && field.classList.contains("has-error") && input.value.trim()) field.classList.remove("has-error");
      });
    });
  }

  /* ---------- Footer year ---------- */
  document.querySelectorAll("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
