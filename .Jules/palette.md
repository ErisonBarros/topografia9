## 2024-05-18 - FontAwesome textual fallbacks in GitBook

**Learning:** When embedding FontAwesome icons in GitBook Markdown using raw HTML `<i>` tags, screen readers may read out the textual fallbacks (e.g., `:map-marked-alt:`). This is a GitBook specific pattern.

**Action:** Always ensure that decorative `<i>` tags containing FontAwesome fallbacks have the `aria-hidden="true"` attribute to prevent screen readers from reading them out loud.
