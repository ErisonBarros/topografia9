## 2024-05-24 - Hiding decorative FontAwesome text from screen readers
**Learning:** Screen readers may read out the textual fallbacks embedded inside decorative FontAwesome icons (e.g., `:map-marked-alt:` inside `<i class="fa-map-marked-alt">:map-marked-alt:</i>`), resulting in a poor experience.
**Action:** Always add `aria-hidden="true"` to decorative `<i>` tags used for icons to explicitly hide them from assistive technologies.
