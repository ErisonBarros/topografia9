
## 2026-06-22 - Decorative Icons in Markdown
**Learning:** In GitBook Markdown projects, raw HTML decorative FontAwesome tags (like `<i class="fa-map-marked-alt">:map-marked-alt:</i>`) with textual fallbacks can be read by screen readers, harming accessibility.
**Action:** Always add `aria-hidden="true"` to decorative `<i>` tags embedded in Markdown to prevent screen readers from reading these fallbacks.
