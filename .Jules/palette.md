## 2024-05-24 - Accessibility for Decorative FontAwesome Tags in GitBook

**Learning:** When using raw HTML to embed decorative FontAwesome tags (e.g., `<i class="fa-icon">:icon-name:</i>`) within GitBook Markdown files, screen readers might incorrectly announce the textual fallback (like ":icon-name:") which creates a confusing and repetitive auditory experience for users relying on assistive technologies.

**Action:** Consistently add the `aria-hidden="true"` attribute to all decorative FontAwesome `<i>` tags embedded via raw HTML in GitBook Markdown to ensure screen readers explicitly ignore these visual-only elements.
