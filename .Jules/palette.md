## 2025-01-20 - Decorative Icons in GitBook Markdown
**Learning:** GitBook Markdown sometimes allows raw HTML embedding for icons (like `<i class="fa-envelope">:envelope:</i>`). When an icon is purely decorative or has a textual fallback next to it, screen readers might read the fallback text redundantly or awkwardly.
**Action:** Always ensure that raw HTML decorative FontAwesome `<i>` tags embedded in Markdown include the `aria-hidden="true"` attribute to prevent screen readers from reading textual fallbacks.
