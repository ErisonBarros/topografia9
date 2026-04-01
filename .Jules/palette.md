## 2024-05-24 - GitBook Raw HTML FontAwesome Accessibility
**Learning:** GitBook's raw HTML FontAwesome icons contain textual fallbacks (e.g., `:map-marked-alt:`) embedded directly inside the `<i>` tags. These fallbacks get read aloud by screen readers when scanning the decorative icons, which is confusing.
**Action:** When adding raw HTML FontAwesome `<i>` tags in GitBook markdown, always add `aria-hidden="true"` to prevent screen readers from reading the textual fallback.
