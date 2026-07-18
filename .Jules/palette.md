## 2024-05-18 - Accessibility for Embedded Icons in Markdown
**Learning:** Raw HTML decorative FontAwesome `<i>` tags embedded in Markdown pages lack inherent accessibility, which may result in screen readers reading the textual fallbacks out loud incorrectly or unnecessarily.
**Action:** Always include `aria-hidden="true"` attribute to FontAwesome `<i>` tags when directly embedded as HTML in Markdown to prevent screen readers from announcing decorative text or fallback characters.
