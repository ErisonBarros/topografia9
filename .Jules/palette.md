## 2024-05-15 - Decorative Markdown Icons Require aria-hidden
**Learning:** When using raw HTML decorative FontAwesome `<i>` tags embedded in Markdown files (like in GitBook environments), screen readers may attempt to read their text-based fallbacks (e.g. ":map-marked-alt:"), confusing visually impaired users.
**Action:** Always add the `aria-hidden="true"` attribute to raw HTML decorative `<i>` tags embedded in Markdown content to ensure they are properly ignored by assistive technologies.
