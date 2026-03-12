## 2024-05-24 - Accessibility for FontAwesome Icons in GitBook Markdown
**Learning:** Raw HTML decorative FontAwesome `<i>` tags embedded in GitBook Markdown can be read out by screen readers (often interpreting the textual fallbacks like `:map-marked-alt:`). Since these icons are purely decorative, they should be explicitly hidden from assistive technologies.
**Action:** Always add `aria-hidden="true"` to raw HTML decorative `<i>` tags embedded in Markdown files to ensure screen readers ignore them and do not read the textual fallbacks to users.
