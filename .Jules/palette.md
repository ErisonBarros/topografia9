## 2024-05-24 - Accessibility for Embedded HTML in Markdown
**Learning:** GitBook projects may rely on raw HTML tags embedded directly in Markdown for decorative elements like icons (e.g., FontAwesome `<i>` tags). These can be verbose or confusing for screen readers.
**Action:** When working in GitBook or Markdown environments, actively look for embedded HTML icons and add `aria-hidden="true"` to pure decorative ones.
