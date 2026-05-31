## 2024-05-24 - Accessibility for GitBook FontAwesome tags
**Learning:** GitBook markdown files sometimes embed raw HTML tags like `<i>` for decorative FontAwesome icons. Screen readers might attempt to read the inner text fallback (like `:envelope:`), causing confusion.
**Action:** Always add `aria-hidden="true"` to embedded decorative `<i>` tags in GitBook markdown to ensure a cleaner screen reader experience.
