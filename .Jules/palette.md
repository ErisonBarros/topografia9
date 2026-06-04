## 2024-11-20 - GitBook FontAwesome Icon Accessibility
**Learning:** GitBook markdown files sometimes embed raw HTML `<i class="fa-*">` tags as fallback representations for missing or unsupported FontAwesome icons. Screen readers may read the textual content inside these tags (e.g., `:map-marked-alt:`), confusing users when these elements are purely decorative.
**Action:** Always ensure embedded `<i class="fa-*">` tags in GitBook markdown have `aria-hidden="true"` applied to prevent screen readers from reading textual fallbacks.
