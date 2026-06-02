## 2024-03-24 - Accessibility Fix for FontAwesome Icons in Markdown
**Learning:** Screen readers might attempt to read text fallbacks or meaningless content for decorative FontAwesome `<i>` tags embedded directly within Markdown.
**Action:** Always ensure that decorative `<i class="fa-*">` tags embedded in Markdown include the `aria-hidden="true"` attribute to prevent them from being read aloud to screen reader users.
