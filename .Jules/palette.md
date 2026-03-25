## 2024-05-16 - Prevent screen readers from reading decorative FontAwesome fallbacks
**Learning:** Raw HTML decorative FontAwesome `<i>` tags embedded in Markdown often include textual fallbacks (like `:map-marked-alt:`). If not hidden, screen readers will redundantly and confusingly read these textual fallbacks to users.
**Action:** Always add the `aria-hidden="true"` attribute to embedded decorative HTML `<i>` tags in Markdown files.
