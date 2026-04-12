## 2026-04-12 - Hide purely decorative icons from Screen Readers
**Learning:** Found raw HTML FontAwesome icons (`<i>`) embedded in GitBook Markdown docs without accessible text handling. They had text fallbacks like `:envelope:` that a screen reader might awkwardly announce to users, disrupting the content flow.
**Action:** When working on raw HTML icons in this project's Markdown, always apply `aria-hidden="true"` to pure decorative elements, so screen readers can skip the unnecessary textual fallback.
