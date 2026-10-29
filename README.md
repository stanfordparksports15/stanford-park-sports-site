# Stanford Park Youth Sports website

Working with Claude or Codex? See `AGENTS.md` for how the site is built, the common edits and the rules.

Plain static site: open `index.html`, or upload the whole folder to any static host
(Netlify drag-and-drop, Vercel, GitHub Pages, Cloudflare Pages). No build step.

## Pages
`index.html` Home · `about.html` · `programs.html` · `schools.html` · `donate.html` · `contact.html`

## Common edits
- **Programs each season:** edit the `PROGRAMS` list in `tools/build.py`, then run
  `python3 tools/build.py` (needs Pillow: `pip3 install pillow`). The script regenerates all
  six pages, so make copy changes in `tools/build.py` rather than in the HTML files.
- **Contact form:** by default it opens the visitor's email app, pre-filled to
  info@stanfordparksports.com. To receive messages directly, create a free form at
  formspree.io and put its URL in `data-endpoint=""` on the form (in `tools/build.py`).
- **Colors / fonts:** tokens at the top of `assets/css/styles.css`.
- **Photos:** `assets/img/pNNNN-800.webp` / `-1600.webp` (NNNN = last 4 digits of the original file name).
