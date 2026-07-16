## 2024-07-16 - Decorative FontAwesome Icons in GitBook Need Aria-Hidden
**Learning:** Embedded raw HTML FontAwesome `<i>` tags in GitBook markdown (e.g. `<i class="fa-envelope">:envelope:</i>`) often include textual fallbacks that get incorrectly read by screen readers since they are purely decorative.
**Action:** When working in GitBook repositories with FontAwesome, ensure `aria-hidden="true"` is added to all decorative `<i>` tags to improve screen reader accessibility and prevent redundant readouts.
