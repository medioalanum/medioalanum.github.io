# Raymatic parity audit

Date: 2026-10-03

Reference: https://medioalanum.github.io/
Preview: https://medioalanum.github.io/ray/

## Page matrix

| Page | Behavior | Layout/design | Result |
|---|---|---|---|
| Home | Three articles, canonical article links, external menu links, closing illustration and footer are present | Wordmark, vertical menu, typography, separators, metadata hierarchy and closing illustration are aligned with the reference | Pass after removing preview-only visible tags |
| Spacey article | Article route, byline, avatar, category, date, body and back link work | Article header follows the reference: byline replaces the homepage menu; weekday date format is shared | Pass |
| Type hints article | Same route and article structure as reference | Same editorial structure; content remains Raymatic-native Markdown/TOML | Pass |
| Journey article | Same route and article structure as reference | Same editorial structure; content remains Raymatic-native Markdown/TOML | Pass |

## Item audit

- Menu: homepage keeps wordmark plus GitHub, LinkedIn and Mastodon links in the reference vertical arrangement. Article pages use the author byline header, matching the reference instead of repeating the homepage menu.
- Dates: Raymatic now renders the weekday-inclusive format, for example Tue 22 September 2026.
- Categories: preserved with the same values and editorial casing.
- Tags: retained as source metadata for Raymatic, but hidden from the parity presentation because the reference blog does not display tags on its homepage or article pages.
- Titles: links have no default underline; article body links retain underlining.
- Author: by, GitHub avatar and Alan Viana are present on article pages.
- Illustration: the closing cartoon is present on the preview homepage.
- Assets: stylesheet and local Allura font are served from the /ray/assets/ prefix.
- Root preservation: the Pelican publication remains at /; Raymatic is copied under /ray/.
- Responsive behavior: desktop and narrow viewport rules are present; a final mobile screenshot pass remains to be recorded.

## Remaining differences

Raymatic deliberately does not reproduce Pelican-only surfaces that are outside this preview slice, including reading-time metadata, RSS/archive/category index pages and Pelican's plugin architecture. These are product decisions to evaluate separately from visual parity.


Visual comparison pass: aligned horizontal home navigation, abbreviated weekdays, and uppercase accent-colored categories with the editorial separator.