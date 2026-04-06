## 2026-04-06 - Hidden Textual Fallbacks in Decorative Icons
**Learning:** In GitBook, raw HTML FontAwesome `<i>` tags often contain textual fallbacks (like `:map-marked-alt:`) within the element content, which screen readers would read aloud unnecessarily.
**Action:** Always include `aria-hidden="true"` on decorative `<i>` tags embedded in Markdown files to prevent screen readers from reading textual fallbacks that are visually hidden but still present in the DOM.
