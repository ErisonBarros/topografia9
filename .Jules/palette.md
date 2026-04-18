## 2024-11-20 - GitBook Markdown Decorative Icons
**Learning:** Raw HTML decorative FontAwesome `<i>` tags embedded in GitBook Markdown don't have built-in accessibility. Screen readers may read their textual fallbacks (like `:map-marked-alt:`).
**Action:** When working on GitBook raw HTML elements, ensure `aria-hidden="true"` is manually added to decorative icons so screen readers skip them and don't announce confusing fallback text.
