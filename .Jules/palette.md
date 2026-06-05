## 2024-06-05 - Decorative FontAwesome Icons Fallback in GitBook
**Learning:** Raw HTML decorative FontAwesome `<i>` tags embedded in GitBook Markdown can contain textual fallbacks (e.g., `:map-marked-alt:`). Screen readers will read these textual fallbacks if the tags don't have `aria-hidden="true"`, causing a confusing auditory experience for users when the icon is purely decorative.
**Action:** Always ensure embedded FontAwesome `<i>` tags in GitBook Markdown include the `aria-hidden="true"` attribute to prevent screen readers from announcing the textual fallbacks.
