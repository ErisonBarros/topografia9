## 2024-05-18 - Hiding decorative FontAwesome elements from screen readers
**Learning:** In Markdown/HTML documentation content, decorative icons (like FontAwesome `<i>` tags) that have visual representation but no semantic meaning need to be hidden from screen readers. Otherwise, the screen reader may try to read out the icon's CSS class name or textual fallbacks (like `:envelope:`), causing a confusing experience for users.
**Action:** Always add `aria-hidden="true"` to decorative `<i>` icon tags embedded in Markdown files to ensure a cleaner and more professional screen reader experience.
