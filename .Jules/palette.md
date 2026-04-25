## 2026-04-25 - Adding ARIA hidden to GitBook Markdown Icons
**Learning:** In GitBook Markdown environments where raw HTML icons with fallback text are used (e.g. `<i class="fa-icon">:icon-text:</i>`), screen readers will read the textual fallbacks out loud, causing unnecessary redundancy for decorative icons.
**Action:** Ensure all decorative `<i>` tags have `aria-hidden="true"` added by default when encountering GitBook repos using this pattern.
