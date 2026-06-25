## 2024-06-25 - FontAwesome in Markdown accessibility
**Learning:** Found decorative FontAwesome `<i>` tags embedded within GitBook markdown content. These tags also contain text snippets inside (like `:map-marked-alt:`). If read by a screen reader, these embedded icons and their fallback text strings could cause confusing output and disrupt reading flow for visually impaired users.
**Action:** Always append `aria-hidden="true"` to raw HTML decorative FontAwesome `<i>` tags when embedded within Markdown to instruct screen readers to ignore them.
