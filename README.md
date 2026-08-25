# medioalanum

Personal notes on Python, APIs, and software engineering.

This site is built with [Pelican](https://getpelican.com/), managed with
[uv](https://docs.astral.sh/uv/), styled with the mnmlist theme, and deployed
to GitHub Pages.

## Local development

```bash
uv sync --locked
uv run pelican --autoreload --listen
```

Open <http://localhost:8000>.

## Production build

```bash
uv run pelican content -s publishconf.py
```
