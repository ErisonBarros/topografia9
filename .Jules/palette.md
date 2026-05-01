## 2024-05-18 - Hiding Embedded Decorative HTML Icons from Screen Readers in Markdown Text
**Learning:** When using raw HTML inside Markdown for decorative icons (like FontAwesome `<i>` tags with textual fallbacks), screen readers will announce the textual fallback (e.g., ":map-marked-alt:"), which creates noise and degrades the screen reader UX.
**Action:** Always add `aria-hidden="true"` to decorative `<i>` elements embedded within Markdown content to prevent screen readers from reading these unnecessary textual fallbacks.
