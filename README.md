# TweComments

Comment rules for Twe: where each manga site keeps its comments and how to read them.
Twe uses `https://raw.githubusercontent.com/SriKousik/TweComments/main/comment-rules.json` by default
(Settings → Browse → Comment rules).

## Layout

```
comment-rules.json          index: links everything below
rules/global.json           rules for every site (comment systems: wpDiscuz, Disqus, WordPress, …)
rules/<name>.json           rules for particular extensions or sites
```

`comment-rules.json`:

```json
{
  "version": 2,
  "global": "rules/global.json",
  "extensions": { "eu.kanade.tachiyomi.extension.en.mangareadorg": "rules/madara-wpdiscuz.json" },
  "sources": { "734865402529567092": "rules/mangageko.json" },
  "domains": { "mangaread.org": "rules/madara-wpdiscuz.json" }
}
```

- `extensions` links an extension (its package ID, as in keiyoushi's index), `sources` a source
  (its ID), `domains` a site.
  Several extensions or sites can link to the same file (sites on the same theme share one).
- Rules in a linked file apply to that extension or site directly (no `match` needed).
- Paths are relative to the index (or full addresses).
- Twe checks the index once a day and downloads every linked file.

## Checklist

[CHECKLIST.md](CHECKLIST.md) lists every keiyoushi extension (1,458) with its comment status:
complete, works, needs rule, unsupported, check in app, no comments, or site down, and for the
working ones whether reading, replies, liking, commenting and sign-in work. Regenerate it with:

```
python3 tools/survey.py index.json tools/survey.jsonl     # keiyoushi's index.json; resumes where it stopped
python3 tools/recheck.py tools/survey.jsonl checklist.json tools/recheck.jsonl   # after adding a new comment system
python3 tools/checklist.py tools/survey.jsonl CHECKLIST.md checklist.json
```

Rows tested by hand are kept in `MANUAL` in `tools/checklist.py`; add a site there when you confirm it.

## Blocked sites

Sites behind a Cloudflare check can't be surveyed by script. [BLOCKED-SITES.md](BLOCKED-SITES.md)
says what Twe needs for them and how to collect what a rule needs with
[`tools/collect.js`](tools/collect.js), pasted into the browser console on the site.

## Sites with rules

See [CHECKLIST.md](CHECKLIST.md) for every extension. Rules written so far:

| Rule | Sites | Read | Replies | Like / comment / reply |
|---|---|---|---|---|
| madara-wpdiscuz | MangaRead.org | ✅ | ✅ View replies | ⏳ (WordPress sign-in) |
| mangageko | MangaGeko | ✅ | ✅ | ⏳ (site sign-in) |
| asura | Asura Scans | ✅ (+ GIFs) | ✅ | — |
| mangadex | MangaDex | ✅ forum | quotes | — |
| weebcentral | Weeb Central | ✅ | — | — |
| mangakatana | MangaKatana | ✅ | ✅ | — |
| zmio | Asmodeus, Siren, Genz Toons, Grim, Mist, Nyanu Kafe, TimelessToons, Writer Scans | ✅ | ✅ | — |
| qq-comments | Mangabat, Mangakakalot, Kun Manga, Zinmanga, ZetTruyen | ✅ | ✅ | ⏳ like, reply |
| aethon | Aethon Webcomics | ✅ | — | — |
| otranslations | O Translations | ✅ | ✅ | — |
| toongod | ToonGod | ✅ first batch | ✅ first batch | — |
| comicfury | Comic Fury | ✅ | — | — |
| saymanhwa | SayManhwa | ✅ | — | — |
| global: wpdiscuz | any wpDiscuz site | ✅ | ✅ | ⏳ |
| global: disqus | any Disqus site | ✅ | ✅ | — |
| global: wordpress | any WordPress comments | ✅ | ✅ | — |
| global: mcs | Manga Comments System sites (Violet Scans…) | ✅ | ✅ | — |
| global: comment-body-articles | YaoiScan and its platform | ✅ | — | — |
| global: livewire-discussion | RitharScans, Art Lapsa, Kitsune Dawn | ✅ | — | — |
| global: manga-comments-pro | AquaManga and the plugin's sites | ✅ | ✅ | — |
| global: discourse | Swords Comic and any Discourse embed | ✅ | — | — |
| global: blogger | Blogger / ZeistManga sites | ✅ | — | — |

⏳ written from the site's own requests; needs a signed-in check to mark ✅.

ToonGod uses its TNGD JSON API, so reading avoids the widget's shadow root and does not
need a saved Cloudflare cookie. The rule covers title and chapter threads, author names,
avatars, timestamps, scores, spoiler flags and replies. Tested through the running
Turnstile-Slip service on 2026-11-04: 16 title comments, 6 chapter comments and a 3-reply
thread on Return of the Mount Hua Sect. The API needs a browser user agent; the tested
Android user agent is included in the rule. Only the first batch of comments and replies
is supported: TNGD returns `nextCursor`, while Twe's current rule format supports page
numbers and offsets. Posting, voting, media markup and cursor paging remain unsupported.

## Matching order

1. A rule whose `match.sources`, `match.extensions` or `match.domains` fits the source or site.
   These can work without opening the page (API rules).
2. Otherwise Twe opens the page in a hidden web view and uses the first rule whose
   `match.detect` selector is on the page. Use this for comment systems (wpDiscuz, Disqus) and
   site themes (Madara, MangaThemesia, …), so one rule covers every site built on them.
3. Otherwise a general search for a section headed or named "comments" / "discussion".

Rule files are tried before the built-in rules (later files first), and a rule with the same
`id` as a built-in one replaces it.

## File

```json
{
  "version": 1,
  "name": "My rules",
  "rules": [ { …rule… } ]
}
```

## Rule

| Key | Meaning |
|---|---|
| `id` | Unique name. Reusing a built-in id replaces that rule. |
| `name` | Shown in Twe ("Rule used: …"). |
| `match` | `sources` (Twe source IDs), `extensions` (extension package IDs), `domains` ("example.com" also matches subdomains), `detect` (CSS selector present on the page). |
| `entry`, `chapter` | `{ "url": "…" }`: where comments are for a title or a chapter, if not the page itself. Templates allowed. |
| `type` | `page`, `api`, `disqus` or `unsupported`. |
| `vars` | Values worked out first, used as `{name}` in templates (below). |
| `page` | For `page` rules. |
| `api` | For `api` rules. |
| `disqus` | For `disqus` rules. |
| `message` | For `unsupported` rules: what to tell the reader. |

### Templates and variables

Templates use `{pageUrl}` (the title or chapter page), `{entryUrl}` / `{chapterUrl}`, `{page}`
(1) and any `vars`:

```json
"vars": {
  "slug":  { "from": "url",  "regex": "/manga/([^/]+)" },
  "forum": { "from": "html", "regex": "//([a-z0-9-]+)\\.disqus\\.com/embed\\.js" },
  "objectId": { "from": "page", "selector": "section.comment-list", "attr": "data-objectid" }
}
```

- `url`: a regex on the page address (first group).
- `fetch`: a regex on the page's HTML, downloaded without opening it (quick).
- `json`: `url` and `path` (both templated): a value from a JSON API.
- `value`: a fixed `value`.
- `entry.vars` / `chapter.vars`: values only for titles or only for chapters.
- `fallback`: a list of alternatives tried in order when a variable finds nothing.
- `html`: a regex on the page's HTML (opens the page).
- `page`: an element's attribute (`attr`) or text, optionally narrowed with `regex`.

In API URLs, values are URL-encoded.

### `page` rules (read in the web view)

Selectors inside each comment item; only the item's own elements are read, so replies nested
in a comment are their own items (and shown indented).

```json
"page": {
  "wait": ".comment-item",
  "item": ".comment-item",
  "author": ".username",
  "text": ".comment-body",
  "time": "time, .date",
  "avatar": "img.avatar",
  "likes": ".like-count",
  "spoiler": ".spoiler",
  "more": "button.load-more"
}
```

Only `item` is required; missing ones are guessed.

### `api` rules (JSON, no web view)

Paths are dotted: `data.comments`, `user.name`, `items.0.text`.

```json
"api": {
  "url": "https://example.com/api/comments?id={objectId}&page={page}",
  "headers": { "X-Requested-With": "XMLHttpRequest" },
  "list": "data.comments",
  "id": "id",
  "author": "user.username",
  "text": "content",
  "html": true,
  "time": "created_at",
  "avatar": "user.avatar",
  "likes": "likes",
  "spoiler": "is_spoiler",
  "parent": "parent_id"
}
```

Use `parent` for flat lists with parent ids, or `children` for replies nested in each comment.
`method` and `body` (templated) are available for POST endpoints. The source's own headers and
the page as Referer are sent too.

### `disqus` rules

```json
"disqus": { "forum": "{forum}", "identifier": "{identifier}", "url": "{threadUrl}" }
```

### `unsupported`

For comment systems Twe can't read (Facebook's plugin): the reader sees `message` and an
"Open in WebView" button.

### Actions (like, comment, reply)

Sent from the site's own page in Twe's hidden web view, so your sign-in there (in WebView) and
its cookies go with them. Templates can use `{id}` (the comment), `{text}`, `{spoiler}`
(`true`/`false`), `{cookie:name}` (a cookie's value, e.g. a CSRF token), `{js:path}` (a page script value), `{meta:name}` (a meta tag's content) and the rule's values.

```json
"actions": {
  "login": "{origin}/login/",
  "loggedOut": "not_logged_in",
  "like":  { "url": "{origin}/comments/like/",  "method": "POST", "body": "comment_id={id}",
             "headers": { "Content-Type": "application/x-www-form-urlencoded", "X-CSRFToken": "{cookie:csrftoken}" } },
  "dislike": { … },
  "post":  { "url": "{origin}/comments/new/",   "method": "POST", "body": "comment={text}&location={slug}&spoiler={spoiler}", "headers": { … } },
  "reply": { "url": "{origin}/comments/reply/", "method": "POST", "body": "comment={text}&reply_id={id}&location={slug}", "headers": { … } }
}
```

`loggedOut` is text in the site's answer that means "not signed in" (401/403 answers count too);
Twe then offers the `login` page in WebView.

### Threads

API rules can give `replyCount` (a path) and `replies` (`url` with `{id}`, `list`, `lastPage`)
for sites that send replies separately; Twe shows "View N replies" and fetches them when opened.
