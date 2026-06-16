## 2024-05-18 - GitBook Icon Accessibility

**Learning:** GitBook often embeds raw HTML FontAwesome `<i>` tags inside Markdown with fallback text (e.g., `<i class="fa-envelope">:envelope:</i>`). Screen readers may read these textual fallbacks out loud to users, causing confusion or redundancy for visually impaired users.
**Action:** When manually writing or editing Markdown files with decorative icon tags, ensure `aria-hidden="true"` is added to the HTML `<i>` tag to hide it from screen readers, since the context usually makes the icon purely decorative.
