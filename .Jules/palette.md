## 2026-02-10 - Decorative Icon Accessibility in GitBook

**Learning:** When using raw HTML embedded in GitBook Markdown (such as FontAwesome `<i>` tags like `<i class="fa-map-marked-alt">:map-marked-alt:</i>`), screen readers will read the textual fallback (e.g., ":map-marked-alt:") if they aren't explicitly hidden. Since these are purely decorative icons visually accompanying text, reading the raw fallback text is confusing and creates a poor auditory UX.

**Action:** Always add `aria-hidden="true"` to decorative `<i>` tags when embedding raw HTML icons in GitBook Markdown.
