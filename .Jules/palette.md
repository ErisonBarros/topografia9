## 2026-03-26 - Decorative Icon Accessibility in Markdown
**Learning:** Raw HTML decorative icons (like FontAwesome `<i>` tags) embedded in Markdown can be problematic for screen readers, often resulting in unhelpful textual fallbacks being announced. They are missing built-in context hiding.
**Action:** Always add `aria-hidden="true"` to these raw HTML decorative `<i>` tags within GitBook Markdown files to explicitly hide them from assistive technologies, ensuring a cleaner reading experience.
