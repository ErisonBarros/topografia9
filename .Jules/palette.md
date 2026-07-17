## 2024-07-17 - Accessible FontAwesome Icons in GitBook
**Learning:** In GitBook environments, decorative FontAwesome `<i>` tags embedded in Markdown can be read out by screen readers (reading textual fallbacks like `:map-marked-alt:`). They require `aria-hidden="true"` to prevent screen readers from announcing these decorative visual elements.
**Action:** Always verify that raw HTML `<i>` tags used for icons include `aria-hidden="true"` when adding or modifying GitBook Markdown content.
