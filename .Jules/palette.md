## 2024-05-28 - GitBook FontAwesome Accessibility Pattern
**Learning:** Decorative icons embedded as raw HTML `<i>` tags in GitBook Markdown pages are read literally by screen readers (e.g., `:chalkboard-teacher:`), causing significant noise.
**Action:** Always add `aria-hidden="true"` to pure decorative FontAwesome tags embedded in markdown to prevent textual fallback from being read by assistive technologies.
