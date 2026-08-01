## 2024-05-18 - GitBook FontAwesome Icon Fallback A11y
**Learning:** GitBook markdown files often contain raw HTML `<i>` tags for FontAwesome icons with textual fallbacks inside (e.g., `<i class="fa-envelope">:envelope:</i>`). This can cause screen readers to announce the decorative fallback text, degrading the accessibility experience.
**Action:** When working with GitBook repositories, ensure all decorative HTML `<i>` icon tags include `aria-hidden="true"` to prevent screen readers from announcing unnecessary textual fallbacks.
