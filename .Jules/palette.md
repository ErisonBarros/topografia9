## 2024-05-16 - Prevent Screen Readers from reading FontAwesome textual fallbacks
**Learning:** Decorative FontAwesome tags in GitBook Markdown can be read as text by screen readers if their text fallback (like `:map-marked-alt:`) is included.
**Action:** Always add `aria-hidden="true"` to these decorative `<i>` tags so that they are ignored by assistive technologies.
