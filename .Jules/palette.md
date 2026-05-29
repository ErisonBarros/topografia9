## 2024-05-24 - Accessibility for Decorative Icons with Text Fallbacks
**Learning:** Raw HTML decorative FontAwesome tags embedding text fallbacks (like `:envelope:`) within Markdown will be read aloud by screen readers confusingly if they lack `aria-hidden="true"`.
**Action:** Always add `aria-hidden="true"` to `<i class="fa-...">` tags in Markdown files when they only serve a visual decorative purpose and contain text intended to be replaced visually or act as a fallback.
