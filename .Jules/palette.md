## 2024-05-18 - GitBook FontAwesome Emoji Fallbacks
**Learning:** GitBook users sometimes embed standard FontAwesome icons (e.g. `<i class="fa-envelope">`) but add textual emoji fallbacks (e.g. `:envelope:`) inside them. Screen readers may announce these raw textual emojis, creating redundant or confusing audio output for decorative icons.
**Action:** When auditing GitBook raw HTML or markdown embedded tags, ensure any purely decorative `<i class="...">` that wraps emoji syntax has an `aria-hidden="true"` attribute attached to prevent screen readers from reading the textual fallback.
