## 2026-05-06 - Prevent screen readers from incorrectly announcing text fallbacks in FontAwesome icons
**Learning:** Found an accessibility issue pattern in GitBook raw HTML where FontAwesome `<i>` tags include text fallbacks (e.g., `:map-marked-alt:`) that are read aloud by screen readers, creating a confusing and degraded auditory experience.
**Action:** Added `aria-hidden="true"` to the `<i>` tags to hide these decorative icons from assistive technologies. Going forward, apply this to all similar icon implementations in GitBook markdown.
