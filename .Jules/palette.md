## 2024-05-14 - Add aria-hidden to decorative FontAwesome icons in Markdown
**Learning:** Raw HTML icons like `<i class="fa-map-marked-alt">:map-marked-alt:</i>` in Markdown get announced weirdly by screen readers because of the fallback text.
**Action:** When using decorative HTML tags in Markdown files (like FontAwesome icons), explicitly add `aria-hidden="true"` to hide them from assistive technologies.
