## 2026-06-24 - Prevent screen readers from reading decorative FontAwesome fallbacks
**Learning:** Raw HTML `<i>` tags in GitBook Markdown can have textual fallbacks that are incorrectly read by screen readers if not hidden.
**Action:** Always add `aria-hidden="true"` to decorative `<i>` icon tags in Markdown to ensure a clean auditory experience.
