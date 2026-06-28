## 2024-05-16 - Decorative FontAwesome Icons in GitBook
**Learning:** GitBook markdown sometimes embeds raw HTML like `<i class="fa-icon">:icon-name:</i>`. Screen readers can incorrectly read the textual fallback (`:icon-name:`) if these decorative icons do not have the `aria-hidden="true"` attribute.
**Action:** Always verify raw HTML `<i>` tags used for decorative FontAwesome icons in GitBook markdown and add `aria-hidden="true"` to prevent them from confusing screen reader users.
