## 2024-05-18 - GitBook Markdown FontAwesome Accessibility
**Learning:** Raw HTML decorative FontAwesome `<i>` tags embedded in GitBook Markdown can be read out by screen readers using their textual fallbacks (e.g., `:map-marked-alt:`), creating a poor and confusing auditory experience for users.
**Action:** Always ensure embedded decorative icon tags (like `<i>` from FontAwesome) include the `aria-hidden="true"` attribute in GitBook projects to prevent screen readers from reading raw text representations of icons.
