## 2024-05-18 - GitBook FontAwesome Textual Fallbacks
**Learning:** Raw HTML `<i>` elements used for FontAwesome icons in GitBook Markdown contain textual fallbacks (e.g., `:envelope:`) inside them. Screen readers will read these raw texts out loud if not hidden, creating a confusing experience where random icon names are spoken mid-content.
**Action:** Always add `aria-hidden="true"` to decorative `<i>` tags embedded in GitBook Markdown to suppress these textual fallbacks for screen reader users.
