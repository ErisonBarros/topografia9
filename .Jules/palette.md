## 2024-05-18 - FontAwesome fallback text accessibility
**Learning:** Raw HTML decorative FontAwesome `<i>` tags embedded in Markdown pages of this GitBook project often contain textual fallbacks that are read by screen readers, harming accessibility.
**Action:** When working on GitBook repositories or rendering raw HTML inside Markdown, ensure all decorative `<i>` icon tags include `aria-hidden="true"` to prevent screen readers from reading textual fallbacks.
