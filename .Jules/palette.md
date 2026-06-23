
## 2026-06-23 - Accessibility on Decorative FontAwesome Icons
**Learning:** In Gitbook Markdown, raw HTML `<i>` tags used for FontAwesome icons can inadvertently expose textual fallbacks (like `:map-marked-alt:`) to screen readers, creating noise.
**Action:** Always add `aria-hidden="true"` to these `<i>` tags so that screen readers correctly skip them and provide a better UX.
