## 2024-05-24 - Accessibility for GitBook embedded FontAwesome

**Learning:** GitBook markdown files often embed raw HTML FontAwesome `<i>` tags as visual decorators with textual fallbacks inside (e.g., `<i class="fa-envelope">:envelope:</i>`). This causes screen readers to read out the fallback text like "colon envelope colon", which is confusing and redundant when the surrounding text provides the context.

**Action:** Always add `aria-hidden="true"` to these decorative `<i>` tags in GitBook markdown to ensure screen readers ignore the fallback text and focus on the substantive content.
