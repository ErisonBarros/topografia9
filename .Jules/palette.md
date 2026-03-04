## 2024-05-14 - FontAwesome Icons in GitBook Markdown
**Learning:** Raw HTML `<i>` tags used for decorative FontAwesome icons in GitBook Markdown files are read out as gibberish (e.g. ":map-marked-alt:") by screen readers unless hidden properly.
**Action:** Always add `aria-hidden="true"` to decorative `<i>` tags in Markdown files to ensure screen readers skip them and provide a clean reading experience.
