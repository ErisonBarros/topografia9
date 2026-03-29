## 2024-05-18 - Missing aria-hidden in GitBook FA Icons
**Learning:** Found decorative FontAwesome icons in Markdown lacking `aria-hidden="true"`, causing screen readers to improperly read the textual fallback content within the `<i>` tag.
**Action:** Add `aria-hidden="true"` to raw HTML `<i>` tags used for FontAwesome in Markdown files.
