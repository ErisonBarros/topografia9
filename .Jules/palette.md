## 2026-05-08 - GitBook Markdown Embedded HTML FontAwesome Accessibility
**Learning:** Raw HTML decorative FontAwesome `<i>` tags embedded directly within Markdown files in GitBook are read by screen readers if their textual fallbacks (like `:map-marked-alt:`) are inside or if they are generally processed as text. This creates confusing noise for screen reader users.
**Action:** Always ensure any raw HTML FontAwesome `<i>` tag used for decorative purposes within Markdown includes the `aria-hidden="true"` attribute so screen readers skip over the textual fallbacks.
