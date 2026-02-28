# CLAUDE.md

This file provides guidance for AI assistants working on this repository.

## Project Overview

Personal blog and portfolio website for Max Khor, built with **Jekyll** and hosted on **GitHub Pages** at [https://maxkskhor.github.io](https://maxkskhor.github.io). The site focuses on technical writing covering Python, data science, LLMs, and AI topics.

## Technology Stack

| Layer | Technology |
|-------|-----------|
| Site generator | Jekyll (via `github-pages` gem ~232) |
| Theme | Minima ~2.5 |
| Dependency management | Bundler |
| Hosting | GitHub Pages |
| Content format | Markdown with YAML front matter |
| Icons | Font Awesome 6.5.1 (CDN) |
| Scripting | Python (utility/educational scripts) |

## Repository Structure

```
maxkskhor.github.io/
├── _config.yml          # Jekyll site-wide configuration
├── _includes/
│   └── footer.html      # Custom footer (logo, copyright, GitHub link)
├── _posts/              # Blog posts (filename: YYYY-MM-DD-slug.md)
├── assets/
│   ├── css/
│   │   └── footer.css   # Footer styles (flexbox layout)
│   └── images/          # Site images (logo, cat photos, chart PNGs)
├── scripts/
│   └── optimal_explore.py  # Standalone Python script for explore-exploit simulation
├── about.markdown       # About Me page
├── book.md              # Reading list page
├── cats.md              # Cat photo gallery page
├── index.markdown       # Home page (layout: home, auto-lists posts)
├── 404.html             # Custom 404 page
├── Gemfile              # Ruby gem dependencies
└── README.md            # Minimal project description
```

## Development Workflow

### Local Development

```bash
# Install Ruby dependencies (first time or after Gemfile changes)
bundle install

# Serve site locally with live reload at http://localhost:4000
bundle exec jekyll serve

# Build static site into _site/ directory
bundle exec jekyll build
```

The `_site/` directory is generated output — never edit files there directly.

### Deployment

Pushing to the `main` branch triggers GitHub Pages to automatically build and deploy the Jekyll site. There is no CI/CD pipeline or GitHub Actions workflow. Deployment is fully managed by GitHub Pages.

## Content Conventions

### Blog Posts

- Files live in `_posts/` and must be named `YYYY-MM-DD-slug.md`
- Required front matter:

```yaml
---
layout: post
title: "Human-readable title"
date: YYYY-MM-DD HH:MM:SS +0000
categories: <category> <subcategory>
permalink: /notes/<topic>/<slug>
---
```

- Existing category patterns: `python notes`, `llm notes`
- Existing permalink patterns: `/notes/python/slug`, `/notes/llm/slug`
- Use `{% highlight python %}...{% endhighlight %}` for syntax-highlighted code blocks
- Images are referenced via `{{ site.baseurl }}/assets/images/filename.ext`

### Static Pages

- Stored as `.markdown` or `.md` at the repo root
- Required front matter:

```yaml
---
layout: page
title: Page Title
permalink: /slug/
---
```

### Custom Includes

- `_includes/footer.html` is the only custom include; it loads `footer.css` and Font Awesome from CDN
- To add a new reusable component, create a file in `_includes/` and reference it with `{% include filename.html %}`

### Images

- Store images in `assets/images/`
- Prefer WebP format for photos (a `logo.webp` already exists alongside `logo.png`)
- Images used in posts should be sized reasonably; the repository already contains ~27 MB of images

## Configuration

Key values in `_config.yml`:

```yaml
title: Max Khor
email: maxkskhor@gmail.com
url: "https://maxkskhor.github.io"
baseurl: ""          # No subdirectory — leave empty
github_username: maxkskhor
theme: minima
plugins:
  - jekyll-feed      # Generates /feed.xml RSS feed
```

`_config.yml` is **not** hot-reloaded during `bundle exec jekyll serve`. Restart the server after any changes to it.

## Git Conventions

- **Primary branch**: `main` (triggers GitHub Pages deployment)
- **Commit style**: short, imperative messages (e.g., `Add Book section`, `Edit llm prompt`)
- The `Gemfile.lock` is intentionally excluded from version control via `.gitignore`
- Demo/draft posts are also gitignored: `_posts/2000-01-01-demo.markdown`, `_posts/2024-12-14-example.md`

## Key Constraints

- **No JavaScript frameworks** — the site is intentionally minimal; avoid introducing React, Vue, etc.
- **No Node.js toolchain** — there is no `package.json`; do not add npm build steps
- **GitHub Pages plugin compatibility** — only use Jekyll plugins supported by the `github-pages` gem; adding unsupported plugins will break the build
- **No CI/CD** — there are no GitHub Actions workflows; do not assume automated testing exists
- **`baseurl` is empty** — all internal links must work with an empty baseurl; use `{{ site.baseurl }}/path` or `relative_url` filter for asset paths

## Scripts

`scripts/optimal_explore.py` is a standalone educational Python script that:
- Runs a Monte Carlo simulation (N=50,000) of the explore-exploit stopping-point problem
- Generates matplotlib charts (exported to `assets/images/`)
- Is related to the blog post `_posts/2024-12-08-explore-exploit.md`
- Requires: `numpy`, `matplotlib`

To regenerate charts: `python scripts/optimal_explore.py`
