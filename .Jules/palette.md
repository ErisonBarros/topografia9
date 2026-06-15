## 2024-06-15 - Decorative FontAwesome Icons in GitBook
**Learning:** GitBook markdown sometimes contains decorative HTML `<i>` tags for FontAwesome icons along with textual fallbacks inside them, which can result in screen readers reading the fallback text unnecessarily if `aria-hidden` is not applied.
**Action:** Always ensure embedded `<i>` tags used for purely decorative FontAwesome icons include the `aria-hidden="true"` attribute to prevent screen readers from announcing their textual fallbacks.
