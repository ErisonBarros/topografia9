## 2026-05-15 - [GitBook Markdown A11y] Decorative Icons with Textual Fallbacks
**Learning:** GitBook markdown sometimes embeds raw HTML `<i class="fa-*">` tags for FontAwesome icons containing fallback text nodes (like `:map-marked-alt:`). Screen readers will attempt to read these textual fallbacks, creating a confusing audible experience for decorative graphics.
**Action:** Always ensure any decorative raw HTML `<i>` tags embedded within GitBook markdown use the `aria-hidden="true"` attribute so screen readers cleanly skip over both the icon and its textual fallback content.
