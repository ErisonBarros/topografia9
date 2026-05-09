
## 2026-05-09 - Adding aria-hidden to decorative Markdown HTML elements
**Learning:** When using raw HTML to embed decorative icons (like FontAwesome `<i>` tags) directly in GitBook Markdown, screen readers might unnecessarily read out any textual fallbacks or internal content within the tag.
**Action:** Always include `aria-hidden="true"` on decorative embedded HTML tags in Markdown files to ensure screen readers ignore them and provide a cleaner reading experience.
