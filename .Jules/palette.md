## 2024-05-17 - Decorative FontAwesome Tags Accessibility
**Learning:** Raw HTML decorative FontAwesome `<i>` tags embedded in Markdown can be problematic for screen readers, as they might attempt to read the textual fallbacks (like `:map-marked-alt:` inside the tag).
**Action:** Always ensure that embedded decorative icon tags (like FontAwesome `<i>`) include the `aria-hidden="true"` attribute to prevent screen readers from reading meaningless textual fallbacks.
