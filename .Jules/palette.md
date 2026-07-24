## 2024-07-24 - Accessibility for Decorative Icons in GitBook
**Learning:** Raw HTML decorative FontAwesome `<i>` tags embedded in GitBook Markdown can cause screen readers to read fallback text inappropriately (e.g. reading `:envelope:`).
**Action:** Ensure all raw HTML decorative FontAwesome `<i>` tags include the `aria-hidden="true"` attribute to prevent screen readers from reading textual fallbacks in GitBook projects.
