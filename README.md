# Personal website

A lightweight, responsive personal website with a dedicated Teaching Portfolio. No build step or JavaScript dependencies.

## Preview

Run `python3 -m http.server 8000 --directory personal-site/dist` and visit http://localhost:8000.

## Edit content

- `personal-site/dist/index.html`: name, bio, projects, and publications.
- `personal-site/dist/teaching.html`: teaching philosophy, experience, materials, and reflections.
- `personal-site/dist/styles.css`: shared styles and mobile layout.

Unprovided biography and academic details are marked as coming soon. Add documents inside `personal-site/dist/` and link to them from the relevant section. Both pages can be hosted by any static web host. Google Fonts is optional; system fonts are used if unavailable.

## Hosting

GitHub Pages publishes `personal-site/dist` automatically when changes are pushed to `main`, using `.github/workflows/pages.yml`.

Public address: https://blakenewhouse.github.io/website/

A custom domain can be configured later in the repository's Pages settings after registration and DNS setup.
