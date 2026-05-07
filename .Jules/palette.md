## 2024-03-24 - Accessibility issue with GitBook FontAwesome icons
**Learning:** GitBook markdown might have custom FontAwesome icons represented by `<i>` tags containing a text fallback like `:map-marked-alt:`. This text fallback gets announced by screen readers as plain text because it's inside the DOM visually masquerading as an icon.
**Action:** Always add `aria-hidden="true"` to these decorative `<i>` tags with text fallbacks so that screen readers ignore the fallback text when it's just visually presenting an icon.
