## 2026-04-14 - Accessibility on Decorative Icons
**Learning:** Raw HTML decorative FontAwesome tags in Markdown fallback as text for screen readers, meaning users would just hear text like ':envelope:'.
**Action:** Always add aria-hidden="true" to embedded <i> elements that are purely decorative in Markdown content.
