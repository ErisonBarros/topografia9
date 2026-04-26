## 2024-05-19 - Decorative FontAwesome Icons in GitBook Markdown

**Learning:** When using raw HTML to embed decorative FontAwesome icons in GitBook Markdown (e.g., `<i class="fa-envelope">:envelope:</i>`), screen readers may read the textual fallbacks (like ":envelope:") which disrupts the flow of the document when the icon is purely decorative.
**Action:** Always include the `aria-hidden="true"` attribute on purely decorative `<i>` tags in Markdown files to ensure screen readers ignore them.
