## 2024-05-14 - Decorative Icons in Markdown Need Aria Hidden

**Learning:** When using raw HTML to embed decorative icons (like FontAwesome `<i>` tags) inside Markdown content (especially in GitBook documentation), screen readers may attempt to read their textual fallbacks (e.g., `:map-marked-alt:` or the class name itself) if they aren't explicitly hidden, confusing the user and providing non-semantic information.
**Action:** Always add `aria-hidden="true"` to decorative raw HTML tags embedded within Markdown files.