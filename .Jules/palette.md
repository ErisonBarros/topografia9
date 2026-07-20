## 2024-05-18 - Adding `aria-hidden` to decorative icons in Markdown
**Learning:** Screen readers may misinterpret text fallbacks (like `:map-marked-alt:`) embedded inside `<i>` tags for FontAwesome icons within Markdown content if the tags lack accessibility attributes.
**Action:** Consistently apply `aria-hidden="true"` to pure decorative embedded `<i>` elements that contain textual fallbacks across all Markdown docs.
