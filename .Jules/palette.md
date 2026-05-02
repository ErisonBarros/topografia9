## 2024-11-20 - Adding aria-hidden to GitBook FontAwesome icons
**Learning:** In GitBook environments, decorative FontAwesome `<i>` tags embedding emojis or textual fallbacks (like `:map-marked-alt:`) can be announced inappropriately by screen readers.
**Action:** Always add `aria-hidden="true"` to these `<i>` tags embedded in Markdown to hide them from assistive technologies, since they are strictly visual/decorative.
