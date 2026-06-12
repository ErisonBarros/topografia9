## 2026-06-12 - FontAwesome Accessibility in GitBook Markdown

**Learning:** GitBook markdown might contain embedded raw HTML `<i>` tags for FontAwesome icons with textual fallbacks inside (e.g. `:map-marked-alt:`). If these decorative elements are not properly hidden from assistive technologies, screen readers may try to read the textual fallbacks out of context, leading to a confusing experience.

**Action:** Ensure all raw HTML decorative FontAwesome `<i>` tags embedded in the Markdown include the `aria-hidden="true"` attribute to prevent screen readers from reading the internal textual fallbacks.
