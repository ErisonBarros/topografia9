## 2026-04-09 - Accessibility: FontAwesome Icons in Markdown
**Learning:** When embedding raw HTML like FontAwesome `<i>` tags in Markdown for GitBook, these purely decorative icons can be read by screen readers as their textual fallbacks (e.g., ':map-marked-alt:'), creating a confusing auditory experience.
**Action:** Always add `aria-hidden="true"` to raw HTML `<i>` decorative icons in Markdown files to ensure screen readers ignore them and focus on the meaningful text content.
