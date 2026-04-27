## 2024-05-14 - Added aria-hidden to decorative icons
**Learning:** Raw HTML icons (e.g., `<i class="fa-icon">`) embedded in Markdown can be problematic for screen readers, as they might read out the text fallback.
**Action:** Always ensure decorative icons have `aria-hidden="true"` to hide them from assistive technology, even when embedded inside Markdown files.