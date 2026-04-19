## 2024-06-25 - Prevent Redundant Screen Reader Output for Markdown Icons
**Learning:** Raw HTML icons (like FontAwesome `<i>`) embedded within Markdown (common in GitBook) can present accessibility issues because screen readers may needlessly read the textual fallback content (e.g. ":map-marked-alt:").
**Action:** Always append `aria-hidden="true"` to these decorative `<i>` tags in Markdown files to maintain a clean screen reading experience.
