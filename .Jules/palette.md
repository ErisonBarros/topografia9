## 2024-05-24 - Accessibility for Markdown Icons
**Learning:** In GitBook Markdown containing inline HTML like FontAwesome `<i>` tags (e.g., `<i class="fa-envelope">:envelope:</i>`), screen readers may attempt to read the textual fallback `:envelope:` or the tag structure if not properly hidden. Since these icons are typically decorative, this creates a confusing audio experience.
**Action:** Always append `aria-hidden="true"` to pure decorative `<i>` tags embedded within GitBook Markdown.
