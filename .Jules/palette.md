## 2024-03-24 - Decorative FontAwesome Icons
**Learning:** GitBook markdown sometimes includes raw HTML `<i>` tags for FontAwesome icons. If these are decorative and include textual fallbacks (like `:envelope:`), screen readers might unnecessarily read them.
**Action:** Always add `aria-hidden="true"` to raw `<i>` tags used for decorative FontAwesome icons in Markdown files to hide them from screen readers and improve accessibility.
