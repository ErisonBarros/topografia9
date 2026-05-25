
## 2024-05-25 - Prevent Screen Reader Redundancy on Markdown Fallback Icons
**Learning:** Raw HTML decorative FontAwesome `<i>` tags embedded in Markdown often rely on text fallback (like `:map-marked-alt:`) which screen readers might announce awkwardly if the tag isn't explicitly hidden from assistive tech.
**Action:** Always add `aria-hidden="true"` to embedded decorative HTML icon tags in Markdown to ensure a seamless experience for screen reader users by preventing them from reading textual fallbacks that clutter the narrative.
