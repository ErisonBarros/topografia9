## 2024-05-18 - Adding `aria-hidden` to Embedded Icons in Markdown
**Learning:** Decorative icons embedded as HTML inside Markdown files (e.g., `<i class="fa-icon">:icon-name:</i>`) can create a confusing experience for screen reader users if left unhidden, as screen readers might attempt to interpret the textual fallback (`:icon-name:`).
**Action:** Always add `aria-hidden="true"` to such decorative HTML icons directly within Markdown content to preserve clean accessibility.
