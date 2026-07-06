
## 2026-07-06 - Hidden Decorative Icons in GitBook
**Learning:** In GitBook environments, when embedding FontAwesome decorative icons directly within Markdown using `<i>` tags alongside their textual emoji fallbacks (e.g., `:envelope:`), screen readers may read out the raw fallback text aloud if the tag lacks proper accessibility attributes.
**Action:** Always ensure that decorative `<i class="fa-*">` tags embedded in Markdown include the `aria-hidden="true"` attribute to prevent redundant or confusing audio output for screen reader users.
