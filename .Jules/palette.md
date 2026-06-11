## 2024-05-18 - GitBook FontAwesome Fallback Accessibility
**Learning:** GitBook automatically renders fallback text inside raw HTML `<i>` tags for FontAwesome icons (e.g., `<i class="fa-envelope">:envelope:</i>`). This causes screen readers to read the raw fallback text aloud, disrupting the reading experience for decorative icons.
**Action:** When working with raw HTML decorative icons in Markdown, explicitly add `aria-hidden="true"` to the `<i>` tags to hide both the icon and the textual fallback from screen readers.
