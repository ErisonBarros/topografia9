## 2024-05-18 - GitBook Decorative FontAwesome Icons Fallback Issue
**Learning:** GitBook markdown sometimes renders FontAwesome decorative icons using textual fallbacks inside `<i>` tags (e.g., `<i class="fa-map-marked-alt">:map-marked-alt:</i>`). Screen readers will read these raw text strings like ":map-marked-alt:", which degrades the accessibility experience.
**Action:** Always add `aria-hidden="true"` to pure decorative FontAwesome `<i>` tags containing textual fallbacks in GitBook markdown.
