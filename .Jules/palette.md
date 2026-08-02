## 2024-08-02 - Decorative FontAwesome Icons in GitBook Markdown
**Learning:** Raw HTML decorative FontAwesome `<i>` tags embedded in GitBook Markdown are read by screen readers along with their text content (e.g. `:map-marked-alt:`). Since these are decorative icons, they shouldn't be read aloud as they don't provide extra semantic meaning to a visually impaired user and can cause noise.
**Action:** Always add the `aria-hidden="true"` attribute to embedded decorative `<i>` elements (e.g., `<i class="fa-icon" aria-hidden="true">:icon:</i>`) so screen readers will skip them.
