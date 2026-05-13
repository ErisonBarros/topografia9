
## 2024-05-13 - Raw HTML decorative FontAwesome tags in GitBook
**Learning:** GitBook markdown files often embed raw HTML tags like `<i>` for FontAwesome icons with textual fallbacks inside (e.g., `:envelope:`). Without explicit aria attributes, screen readers will read the textual fallbacks out loud to users, creating noise.
**Action:** Always check raw HTML `<i>` icon tags in GitBook markdown and add `aria-hidden="true"` to prevent screen readers from reading textual fallbacks if the icons are purely decorative.
