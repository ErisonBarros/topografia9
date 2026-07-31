## 2024-03-24 - Screen Reader Fallback Fix for FontAwesome in Markdown
**Learning:** Raw HTML `<i>` tags embedding decorative icons in Markdown often display a textual fallback like `:map-marked-alt:` which screen readers can inadvertently announce. Since these are purely decorative, they break the reading flow.
**Action:** Always add `aria-hidden="true"` to decorative FontAwesome `<i>` tags to hide them from assistive technologies.
