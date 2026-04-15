## 2024-04-15 - Decorative Icons in Markdown Need ARIA Hidden
**Learning:** Raw HTML decorative FontAwesome `<i>` tags embedded in Markdown will have their textual fallbacks read by screen readers unless explicitly hidden.
**Action:** Always include the `aria-hidden="true"` attribute on purely decorative `<i>` tags embedded in Markdown files.