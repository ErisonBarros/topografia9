## 2024-08-03 - Added aria-hidden to decorative FontAwesome icons in GitBook
**Learning:** GitBook markdown allowing raw HTML `<i>` tags for FontAwesome icons can lead to screen readers reading out the textual fallback (like `:map-marked-alt:`) if they aren't hidden using `aria-hidden="true"`.
**Action:** Always ensure raw HTML decorative icons embedded in markdown files have `aria-hidden="true"`.
