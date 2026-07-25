## 2024-07-25 - Accessibility for raw HTML FontAwesome icons in GitBook Markdown
**Learning:** Raw HTML decorative FontAwesome `<i>` tags embedded in GitBook Markdown can be read out incorrectly by screen readers, leading to confusing auditory experiences for visually impaired users.
**Action:** Consistently apply the `aria-hidden="true"` attribute to all such decorative FontAwesome `<i>` tags across the GitBook Markdown files in this project to prevent screen readers from reading textual fallbacks.
