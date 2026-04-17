## 2026-04-17 - Decorative Icons in GitBook Markdown
**Learning:** Raw HTML FontAwesome `<i>` tags embedded in GitBook Markdown can be read out by screen readers (often announcing the textual fallback/class names) if they are purely decorative.
**Action:** Always ensure embedded `<i>` icon tags include the `aria-hidden="true"` attribute to prevent screen readers from reading textual fallbacks in GitBook projects.
