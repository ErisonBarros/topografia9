## 2023-10-27 - GitBook Decorative FontAwesome Tags Accessibility
**Learning:** GitBook sometimes uses raw HTML `<i>` tags for FontAwesome icons embedded in Markdown, which include textual fallbacks inside (e.g., `:envelope:`). Without `aria-hidden="true"`, screen readers will unnecessarily read these decorative fallback texts aloud, cluttering the experience.
**Action:** Always verify if embedded `<i>` icon tags in GitBook Markdown have the `aria-hidden="true"` attribute to prevent redundant screen reader announcements.
