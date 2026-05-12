## 2024-05-18 - GitBook Markdown Raw HTML Fallbacks
**Learning:** In this GitBook project, FontAwesome icons are embedded using raw HTML `<i>` tags containing text fallbacks (e.g., `:envelope:`). Without `aria-hidden="true"`, screen readers attempt to read these textual fallbacks alongside the icon's visual context, leading to redundant or confusing auditory feedback for visually impaired users.
**Action:** When working with raw HTML icons in GitBook markdown, always add `aria-hidden="true"` to prevent screen readers from reading textual fallbacks meant for markdown parsers.
