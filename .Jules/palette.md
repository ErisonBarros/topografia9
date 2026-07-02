## 2024-05-19 - Decorative FontAwesome Icons in GitBook Markdown
**Learning:** Raw HTML `<i>` tags embedded in GitBook Markdown for decorative icons (like FontAwesome) are read out by screen readers using their textual fallbacks (e.g. ":envelope:").
**Action:** Always add `aria-hidden="true"` to these decorative `<i>` tags in Markdown files to prevent screen readers from reading meaningless textual fallbacks.
