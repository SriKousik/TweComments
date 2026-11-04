# Comments on blocked sites

Some sites (ToonGod, and most of the 🛡️ "Check in app" rows in [CHECKLIST.md](CHECKLIST.md)) put
a Cloudflare check in front of every page. Scripts can't get past it, so the survey never saw their
comments. A person in a real browser can. This page says what Twe needs to show comments for such a
site, and what to send so a rule can be written.

## 1. What Twe needs on your device

Nothing to set up. When a site asks for a Cloudflare check:

1. Open the title in Twe and tap **Comments** (or **WebView**).
2. If Twe shows the check sheet, let it finish, or tap the box yourself.
3. Twe keeps that clearance and its WebView cookies, and reads comments with the same user agent.

If the site has a rule (or uses a system Twe reads everywhere: wpDiscuz, Disqus, Blogger,
Discourse, WordPress comments…), comments then load. If Twe says **"No comment rule matched"**,
the site needs a rule: go to step 2.

To like or post: sign in to the site once in Twe's WebView (⋯ → Sign in in the Comments sheet).

## 2. What to send for a new rule

A rule needs to know where the comments are and how one comment looks. Collect it like this, on a
computer (Chrome, Edge, Firefox or Safari with its developer menu):

1. Open a **title page** that has a few comments. Pass the Cloudflare check yourself.
2. Scroll to the comments. If there's a **Load more** or **View replies** button, press it once.
3. Open the developer console: **F12** (or **⌥⌘I** on a Mac) → **Console**.
4. Paste the whole of [`tools/collect.js`](tools/collect.js) and press **Enter**.
   (Chrome may ask you to type `allow pasting` first.)
5. It prints a report and copies it to the clipboard. Send the report.
6. Do the same on a **chapter page** if chapters have their own comments.

The report has the page address, the comment system it recognised, the site template, the
repeating element that holds each comment (with two samples of its HTML), comment-related
requests the page made, comment form field names, IDs on the comment section, and the names
(not values) of cookies and CSRF tags. It never includes cookie values, passwords, tokens or what
you typed.

### For liking, replying and posting (optional)

Sign in on the site, then in the developer tools open **Network**, filter by **Fetch/XHR**, and
like a comment (or post a test reply). Click the request that appears and send:

- the request **URL** and **method** (GET, POST, PUT…),
- the **Payload** field names (for example `comment_id`, `content`, `_token`); values only if
  they're plain numbers like a comment ID,
- the name of any header that looks like a token (for example `X-CSRF-TOKEN`), **not** its value,
- what the site answers when you're signed out, if you can see it (for example `not_logged_in`).

Never send cookie values, `cf_clearance`, session tokens or passwords: a rule doesn't need them,
and Twe uses your own sign-in on your device.

## 3. What happens next

The report is turned into a rule in [`rules/`](rules) and linked from
[`comment-rules.json`](comment-rules.json) by the extension's ID and the site's domain. Twe checks
rule files every few hours (and right away when a site has no rule), so the comments start
working without updating the app, unless the site needs something Twe can't do yet.

## Example: ToonGod

ToonGod (`toongod.org`, extension `en.toongod`) blocks page downloads with a Cloudflare check,
so the original survey marked it "down" (403). It now has a rule:
[`rules/toongod.json`](rules/toongod.json), checked on 2026-11-04 using the running
Turnstile-Slip service. Its custom widget lives in `#tngd-comments.shadowRoot`, but its
TNGD JSON API can read title and chapter threads directly with the rule's browser user
agent, without saved clearance cookies. Reading and replies are checked; only the first
batch is supported because cursor paging is not yet available in Twe's rule format.
