## 2025-04-04 - Screen Reader Fallbacks in Markdown Icons
**Learning:** When using FontAwesome icons embedded as raw HTML `<i>` tags in Markdown files, screen readers can sometimes attempt to read the textual fallback content (like `:map-marked-alt:` or the CSS class names) if the element is not properly hidden from assistive technologies. This creates noisy, unhelpful audio output for users relying on screen readers.
**Action:** Always add `aria-hidden="true"` to decorative `<i>` tags (like `<i class="fa-icon" aria-hidden="true">`) to ensure a cleaner, more accessible reading experience.
