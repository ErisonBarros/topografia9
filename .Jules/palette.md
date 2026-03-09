## 2024-05-18 - GitBook FontAwesome Screen Reader Fallbacks
**Learning:** Decorative FontAwesome icons in Markdown files might include textual fallbacks inside the `<i>` tag. If screen readers read these, it creates noise and hurts accessibility.
**Action:** Always add `aria-hidden="true"` to pure decorative GitBook `<i>` icon tags to hide textual fallbacks from screen readers.
