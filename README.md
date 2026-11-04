# TweComments

Comment rules for Twe: where each manga site keeps its comments and how to read them.
Add `https://raw.githubusercontent.com/SriKousik/TweComments/main/comment-rules.json` in Twe → Settings → Browse → Comment rules (it's the default).


Twe reads what readers say about a title or chapter from the source's own website. A **comment
rules file** tells it where each site keeps its comments and how to read them. Host the file
anywhere (a raw GitHub link works) and add its address in **Settings → Browse → Comment rules**.
Twe checks rule files once a day, so when a site changes its layout, fixing the rule in the file
fixes every copy of Twe, with no app update.

`docs/comment-rules.json` is the starter file (the same rules are built into Twe).

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
