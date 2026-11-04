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

## All blocked sites

Every extension whose site the survey couldn't read (814): behind a Cloudflare check, refusing scripts (403), or with no title page the survey could find from the home page. Check them in Twe, or collect a report for them (section 2). The English table below records verified reads separately from unverified rules.

| Reason | Count |
|---|---|
| No title page found | 299 |
| Cloudflare | 284 |
| 403 Forbidden | 231 |

### English (189)

**English audit:** 189 checked · 37 verified reads · 38 configured/unverified · 23 access/API failures · 2 loader limitations · 89 with no initialized widget in samples or unresolved discovery.

This pass checks English entries only. ✅ means a live API or downloaded/rendered comment
sample was read and the rule's fields were checked. It does not claim an iOS device or
signed-in action test. 🟡 marks an unverified rule or discussion system; the sampled thread is empty or still
needs a usable mapping/read check. ⚠️ marks a loader limitation with a WebView fallback. ⛔ means access or the upstream comment service failed. 🔎 entries
still need title discovery or a custom rule; they are not marked working.

Progress is saved in [`tools/blocked-english-status.json`](tools/blocked-english-status.json)
and the request/selector audit in [`tools/blocked-english.jsonl`](tools/blocked-english.jsonl).
Raw pages and response bodies stay in `/tmp/twe-blocked-english`; cookies are not committed.

| Extension | Site | Original reason | Rule | Latest check |
|---|---|---|---|---|
| 1Manga.co | https://1manga.co | Cloudflare | [mangahub-remark42](rules/mangahub-remark42.json) | 🟡 Remark42 rule linked; own-domain read verification pending; original thread URL preserved · [sample](https://1manga.co/manga/mao) |
| 8Muses 🔞 | https://comics.8muses.com | No title page found |  | 🔎 7 saved page samples checked, including browser rendering; no initialized comment widget found; no rule inferred · [sample](https://comics.8muses.com/porn) |
| AllManga | https://mkissa.to | No title page found |  | ⛔ Browser could not stabilize after retries; no comment read verified · [sample](https://mkissa.to/manga) |
| AllPornComic 🔞 | https://allporncomic.com | Cloudflare |  | 🔎 7 saved page samples checked, including browser rendering; no initialized comment widget found; no rule inferred · [sample](https://allporncomic.com/series/ben-10e/) |
| Alpha Manga | https://www.alpha-manga.com | No title page found |  | 🔎 2 saved page samples checked, including browser rendering; no initialized comment widget found; no rule inferred · [sample](https://www.alpha-manga.com/manga/44000215) |
| Arc-Relight | https://arc-relight.com | No title page found |  | 🔎 8 saved page samples checked, including browser rendering; no initialized comment widget found; no rule inferred · [sample](https://arc-relight.com/reader/babel/) |
| Arknights Comics | https://arknights.global | No title page found |  | 🔎 Home rendered; a public title/chapter could not be resolved for comment verification · [sample](https://arknights.global/) |
| Athrea Scans | https://athreascans.com | Cloudflare | [wordpress](rules/wordpress.json) | 🟡 Standard WordPress discussion/form found; sampled thread empty; comment extraction remains unverified · [sample](https://athreascans.com/manga/burn/) |
| Atsumaru | https://atsu.moe | No title page found | [atsu](rules/atsu.json) | ✅ Working: 7 comments via v2 API; nested replies mapped; first batch only; custom media/avatars not mapped · [sample](https://atsu.moe/manga/-tya) |
| Bakkin | https://bakkin.moe/reader/ | No title page found |  | 🔎 2 saved page samples checked, including browser rendering; no initialized comment widget found; no rule inferred · [sample](https://bakkin.moe/reader/) |
| BatCave | https://batcave.biz | 403 Forbidden |  | ⛔ Access failed after direct and running-service attempts; no readable discussion verified · [sample](https://batcave.biz) |
| Bbato | https://bato1.com | No title page found |  | 🔎 4 saved page samples checked, including browser rendering; no initialized comment widget found; no rule inferred · [sample](https://bato1.com/home) |
| BookWalker | https://bookwalker.com | Cloudflare |  | 🔎 8 saved page samples checked, including browser rendering; no initialized comment widget found; no rule inferred · [sample](https://bookwalker.com/series/21A94B5XYR80/one-piece) |
| Borat Scans | https://boratscans.com | 403 Forbidden | [wordpress](rules/wordpress.json) | 🟡 Standard WordPress discussion/form found; sampled thread empty; comment extraction remains unverified · [sample](https://boratscans.com/manga/axe-god-the-road-to-invincibility/) |
| BrainRotComics | https://brainrotcomics.com | 403 Forbidden |  | ⛔ Access failed after direct and running-service attempts; no readable discussion verified · [sample](https://brainrotcomics.com) |
| CartoonPorn 🔞 | https://cartoonporn.to | Cloudflare |  | 🔎 8 saved page samples checked, including browser rendering; no initialized comment widget found; no rule inferred · [sample](https://cartoonporn.to/porncomic/the-improbables-the-incredibles-jabcomix-animated/chapter-1/#1) |
| Clone Manga | https://manga.clone-army.org | No title page found | [clonemanga-disqus](rules/clonemanga-disqus.json) | 🟡 Disqus forum/identifier confirmed in browser; sampled thread is empty · [sample](https://manga.clone-army.org/world_tour.php) |
| CManhua | https://cmanhua.com | Cloudflare | [cmanhua](rules/cmanhua.json) | 🟡 Comment selectors confirmed in site stylesheet; sampled server-rendered discussion has no comments · [sample](https://cmanhua.com/comic/fangsi) |
| Cocomic | https://cocomic.co | Cloudflare | [wordpress](rules/wordpress.json) | ✅ Working: 1 comments; author/text selectors verified · [sample](https://cocomic.co/manga/open-the-door/) |
| Collected Curios | https://www.collectedcurios.com | No title page found |  | 🔎 7 saved page samples checked, including browser rendering; no initialized comment widget found; no rule inferred · [sample](https://www.collectedcurios.com/links.html) |
| Comic Asura | https://comicasura.net | No title page found | [comicasura](rules/comicasura.json) | 🟡 QQ API rule linked with string chapter IDs and page count; sampled chapter thread empty · [sample](https://comicasura.net/manga/but-youre-2d/chapter-15) |
| ComicHubFree | https://comichubfree.com | Cloudflare |  | 🔎 7 saved page samples checked, including browser rendering; no initialized comment widget found; no rule inferred · [sample](https://cdn.bollywoodmenswear.com/tml/wheelPink_IOS_IDN.html?v=2608271415-3#/?pid=20380&d.algId=43&dtype=1&uid=cc336d42-23f6-4837-a3ce-77dd465da562&os=1&lang=en-US&d.pext=29868975&reqId=9c2e037ae0194cd4832b89189b2e4512&d.pst=1&d.adPlat=1&appk=dAGjIcTOAsmLGIVmtxe2cj6QbpdIjp15&d.pubCatId=56&d.mltype=0&jsv=2610261646&brd=1_2611031733&d.rankab=3&did=cc336d42-23f6-4837-a3ce-77dd465da562&d.ptkid=72b97e9db85c9ef3a881c47e16054195&tid=10508) |
| ComicLand | https://comicland.org | No title page found |  | 🔎 Home rendered; a public title/chapter could not be resolved for comment verification · [sample](https://comicland.org/) |
| Comix | https://comix.to | Cloudflare | [comix](rules/comix.json) | ✅ Working: 28 rendered comments/replies; 14 contain images; Load more selector verified; only rendered reply batches · [sample](https://comix.to/title/zgk6j-unbeknownst-to-me-i-am-secretly-dating-the-emperor) |
| Coolmic | https://coolmic.me | No title page found |  | 🔎 Home rendered; a public title/chapter could not be resolved for comment verification · [sample](https://coolmic.me/) |
| Cutie Comics 🔞 | https://cutiecomics.com | Cloudflare |  | ⛔ Browser could not stabilize after retries; no comment read verified · [sample](https://cutiecomics.com/22954-secret-fan-meeting.html) |
| Cyanide & Happiness | https://explosm.net | No title page found |  | 🔎 6 saved page samples checked, including browser rendering; no initialized comment widget found; no rule inferred · [sample](https://explosm.net/comics/dancer) |
| Dark Legacy Comics | https://www.darklegacycomics.com | No title page found | [darklegacy-vuukle](rules/darklegacy-vuukle.json) | ✅ Working: 9 comments via Vuukle; HTML images and nested replies mapped; first batch only · [sample](https://www.darklegacycomics.com/1) |
| Darths & Droids | https://www.darthsanddroids.net | No title page found |  | 🔎 3 saved page samples checked, including browser rendering; no initialized comment widget found; no rule inferred · [sample](https://www.darthsanddroids.net/rss.html) |
| Digital Comic Museum | https://digitalcomicmuseum.com | 403 Forbidden | [digitalcomicmuseum](rules/digitalcomicmuseum.json) | ⛔ WebView required: 2 public comments found, but each spans three sibling table rows; current rule format cannot preserve author/date grouping · [sample](https://digitalcomicmuseum.com/index.php?dlid=4) |
| Diva Scans | https://divascans.org | Cloudflare | [diva-valir](rules/diva-valir.json) | ✅ Working: 2 title / 13 chapter comments; HTML, spoilers, paging and reply API mapped · [sample](https://divascans.org/series/comic/slave-diary) |
| Doujin.io - J18 🔞 | https://doujin.io | No title page found |  | 🔎 Home rendered; a public title/chapter could not be resolved for comment verification · [sample](https://doujin.io/) |
| DragonTea | https://dragontea.ink | 403 Forbidden |  | 🟡 Load Comments link found; no initialized discussion or successful comment read observed · [sample](https://dragontea.ink/novel/wheel-world/) |
| Eggporncomics 🔞 | https://eggporncomics.com | Cloudflare |  | 🔎 Home rendered; a public title/chapter could not be resolved for comment verification · [sample](https://eggporncomics.com/) |
| Elan School | https://elan.school | No title page found | [wordpress](rules/wordpress.json) | 🟡 Standard WordPress discussion/form found; sampled thread empty; comment extraction remains unverified · [sample](https://elan.school/fr/) |
| emaqi | https://emaqi.com | No title page found |  | 🔎 2 saved page samples checked, including browser rendering; no initialized comment widget found; no rule inferred · [sample](https://emaqi.com/forbidden) |
| Eris Scans | https://erisscans.com | Cloudflare | [zmio-raw-path](rules/zmio-raw-path.json) | 🟡 Raw-path zmio variant linked; post resolved; sampled thread has no comments · [sample](https://erisscans.com/series/65f60a50e76/) |
| Ero18x 🔞 | https://ero18x.com | 403 Forbidden |  | 🔎 4 saved page samples checked, including browser rendering; no initialized comment widget found; no rule inferred · [sample](https://ero18x.com/manga/subzero/) |
| Erofus 🔞 | https://www.erofus.com | Cloudflare |  | 🔎 7 saved page samples checked, including browser rendering; no initialized comment widget found; no rule inferred · [sample](https://www.erofus.com/comics/zzz-comics) |
| Flame Comics | https://flamecomics.xyz | Cloudflare | [flamecomics](rules/flamecomics.json) | ✅ Working: 11 comments and 1 reply via API; HTML images mapped; first batch only · [sample](https://flamecomics.xyz/series/24) |
| GEDE Comix 🔞 | https://gedecomix.com | Cloudflare |  | 🔎 6 saved page samples checked, including browser rendering; no initialized comment widget found; no rule inferred · [sample](https://gedecomix.com/porn-comics/) |
| GingeRTooN 🔞 | https://gingertoon.com | No title page found |  | 🔎 Home rendered; a public title/chapter could not be resolved for comment verification · [sample](https://gingertoon.com/) |
| GirlsTop 🔞 | https://en.girlstop.info | No title page found | [girlstop](rules/girlstop.json) | ✅ Working: 10 comments read by Twe's actual extractor; 1 with images · [sample](https://me.girlstop.info/psto.php?id=256520) |
| Goda | https://manhuascans.org | Cloudflare |  | 🔎 7 saved page samples checked, including browser rendering; no initialized comment widget found; no rule inferred · [sample](https://manhuascans.org/manga/1-second) |
| Gourmet Scans | https://gourmetsupremacy.com | Cloudflare | [madara-wpdiscuz](rules/madara-wpdiscuz.json) | ✅ Working: 15 comments; author/text selectors verified · [sample](https://gourmetsupremacy.com/project/lb/) |
| Gunnerkrigg Court | https://www.gunnerkrigg.com | No title page found |  | 🟡 Latest ?comments=1 page says comments not approved yet; older page samples had no discussion markup · [sample](https://www.gunnerkrigg.com/cast/) |
| Hades Scans | https://hadesscans.com | No title page found |  | 🔎 Home rendered; a public title/chapter could not be resolved for comment verification · [sample](https://hadesscans.com/) |
| Hentai4Free 🔞 | https://hentai4free.net | Cloudflare |  | ⛔ Browser could not stabilize after retries; no comment read verified · [sample](https://hentai4free.net/bondage-manga/) |
| HentaiFC 🔞 | https://hentaifc.com | No title page found |  | 🟡 Disqus placeholder found, but no forum/thread initialization observed; rule needs a usable embed configuration · [sample](https://hentaifc.com/e/90580) |
| HentaiHere 🔞 | https://hentaihere.com | No title page found | [hentaihere](rules/hentaihere.json) | 🟡 HTML comment-feed URL mapped from source; sampled feed empty; first batch and field guesses need a nonempty fixture · [sample](https://hentaihere.com/reader/71744-3-gal-choukyokon-otaku-kun-no-nakadashi-sex-de-meromero-ni-sarechau-gal-3-nin-gu/115049/page-1) |
| HentaiKun 🔞 | https://hentaikun.com | No title page found |  | 🔎 Home rendered; a public title/chapter could not be resolved for comment verification · [sample](https://hentaikun.com/) |
| HentaiNexus 🔞 | https://hentainexus.com | No title page found |  | 🔎 8 saved page samples checked, including browser rendering; no initialized comment widget found; no rule inferred · [sample](https://hentainexus.com/view/22364) |
| HentaiRead 🔞 | https://hentairead.com | 403 Forbidden |  | 🟡 React MangaComments widget found; sampled title has 0 comments; endpoint mapping remains unresolved · [sample](https://hentairead.com/hentai/ntreport/) |
| HentaiSco 🔞 | https://hentaisco.cc | No title page found |  | 🔎 Home rendered; a public title/chapter could not be resolved for comment verification · [sample](https://hentaisco.cc/) |
| HentaiTnT 🔞 | https://hentaitnt.net | No title page found | [hentaitnt](rules/hentaitnt.json) | 🟡 Review-page redirect linked; sampled book and community page empty; reading still unverified · [sample](https://hentaitnt.net/love-quest.html) |
| Hiperdex | https://hiperdex.tv | No title page found | [hiperdex](rules/hiperdex.json) | ✅ Working: native extractor reads 1 image-only comment; rendered batch only · [sample](https://hiperdex.tv/manga/naked-life) |
| Hive Scans | https://hivetoons.org | Cloudflare |  | ⛔ Disqus forum hiiv returned load error (code 15); not working · [sample](https://hivetoons.org/series/lookism) |
| HotComics 🔞 | https://hotcomics.io | 403 Forbidden |  | ⛔ Cusdis comment service returned HTTP 502; rule cannot be verified · [sample](https://hotcomics.io/en/bad-guy/cIHiI5CC.html) |
| ILikeComix 🔞 | https://ilikecomix.com | Cloudflare |  | 🔎 4 saved page samples checked, including browser rendering; no initialized comment widget found; no rule inferred · [sample](https://ilikecomix.com/manga/c/au-naturel-pegasus-smith/29-au-naturel-chapter-29/) |
| InfinityScans | https://infinityscans.org | Cloudflare |  | 🔎 Home rendered; a public title/chapter could not be resolved for comment verification · [sample](https://infinityscans.org/) |
| J-Novel | https://j-novel.club | Cloudflare | [jnovel-forum](rules/jnovel-forum.json) | ✅ Working: 20 posts per page; pages 1 and 2 verified (86 total); linked series forum only, chapter links not found · [sample](https://j-novel.club/series/slayers) |
| Kaizen Scan 🔞 | https://kaizenscan.com | 403 Forbidden | [zmio](rules/zmio.json) | ✅ Working: 1 comment via existing zmio API rule · [sample](https://kaizenscan.com/hwan) |
| Kappa Beast | https://kappabeast.com | No title page found |  | 🟡 Client defines series/chapter comment APIs; public catalogue did not provide a verifiable thread ID · [sample](https://kappabeast.com/series/taimashi-tensei) |
| KingComiX 🔞 | https://kingcomix.com | Cloudflare | [madara-wpdiscuz](rules/madara-wpdiscuz.json) | 🟡 Rule linked: wpDiscuz widget confirmed; sampled thread has no rendered comments · [sample](https://kingcomix.com/redacted-yazen/) |
| Kissmanga.in | https://kissmanga.in | 403 Forbidden | [madara-wpdiscuz](rules/madara-wpdiscuz.json) | ✅ Working: 3 comments read with wpDiscuz selectors · [sample](https://kissmanga.in/kissmanga/fog-land/) |
| Komix | https://komix.to | Cloudflare |  | ⛔ Browser could not stabilize after retries; no comment read verified · [sample](https://komix.to) |
| Lagoon Scans | https://lagoonscans.com | Cloudflare | [madara-wpdiscuz](rules/madara-wpdiscuz.json) | 🟡 Rule linked: wpDiscuz widget confirmed; sampled thread has no rendered comments · [sample](https://lagoonscans.com/manga/eleceed/) |
| Leslie&Victims | https://leslie-victims.pages.dev | No title page found |  | 🟡 Firebase discussion UI found; title/thread identifiers were not resolved from the sampled page · [sample](https://leslie-victims.pages.dev/) |
| Lgbtics 🔞 | https://lgbtics.com | 403 Forbidden |  | ⛔ Access failed after direct and running-service attempts; no readable discussion verified · [sample](https://lgbtics.com) |
| LHTranslation | https://lhtranslation.net | Cloudflare | [wordpress](rules/wordpress.json) | ✅ Working: 38 comments read by Twe's actual extractor · [sample](https://lhtranslation.net/manga/the-new-gate/) |
| Lily Manga | https://lilymanga.net | No title page found |  | 🔎 Home rendered; a public title/chapter could not be resolved for comment verification · [sample](https://lilymanga.net/) |
| LinkManga | https://linkmanga.com | Cloudflare | [wordpress](rules/wordpress.json) | 🟡 Standard WordPress discussion/form found; sampled thread empty; comment extraction remains unverified · [sample](https://linkmanga.com/manga/hyouka/) |
| Loading Artist | https://loadingartist.com | No title page found |  | ⛔ Public Reddit JSON returned HTTP 403; native discussion read unavailable at this check · [sample](https://loadingartist.com/comic/downtime/) |
| LoLoBun | https://www.lolobun.com | No title page found | [lolobun](rules/lolobun.json) | ✅ Working: 2 comic comments via zero-based API; first 20 roots; replies/avatars need loader support · [sample](https://www.lolobun.com/c/20106) |
| Lua Scans | https://luacomic.org | Cloudflare |  | 🟡 Series comments accordion found; no comment read response or nonempty comment markup observed · [sample](https://luacomic.org/series/frost) |
| Luminare Translations | https://luminaretranslations.com | Cloudflare | [luminare](rules/luminare.json) | 🟡 API rule linked; two sampled series returned empty threads; first batch only · [sample](https://luminaretranslations.com/series/sherlock-academy/) |
| Luna Toons | https://lunatoons.net | 403 Forbidden | [zmio](rules/zmio.json) | 🟡 zmio rule linked; post resolved, sampled API thread has no comments · [sample](https://lunatoons.net/lust) |
| MadaraDex | https://madaradex.org | Cloudflare |  | 🔎 8 saved page samples checked, including browser rendering; no initialized comment widget found; no rule inferred · [sample](https://madaradex.org/title/love-cheer/) |
| Magus Manga | https://magustoon.org | 403 Forbidden |  | ⛔ Disqus forum magusmanga-3 returned load error (code 15); not working · [sample](https://magustoon.org/series/peach-heart) |
| Manga 18x 🔞 | https://manga18x.net | Cloudflare | [manga18x-disqus](rules/manga18x-disqus.json) | 🟡 Disqus rule linked; API confirms empty sampled thread · [sample](https://manga18x.net/manga/set-it/) |
| Manga Demon | https://demonicscans.org | Cloudflare | [demonicscans](rules/demonicscans.json) | ✅ Working: 7 title / 2 chapter comments; 62 Eleceed roots and a 4-reply thread; first batch only; media markup not parsed · [sample](https://demonicscans.org/manga/Talker) |
| Manga Drama 🔞 | https://mangadrama.com | Cloudflare | [mangadrama](rules/mangadrama.json) | ✅ Working: 3 comments; author/text selectors verified · [sample](https://mangadrama.com/manga/shark/) |
| Manga-Bay | https://manga-bay.biz | 403 Forbidden |  | ⛔ Access failed after direct and running-service attempts; no readable discussion verified · [sample](https://manga-bay.biz) |
| Manga.uno | https://manga.uno | Cloudflare |  | 🔎 Home rendered; a public title/chapter could not be resolved for comment verification · [sample](https://manga.uno/) |
| MangaCloud | https://mangacloud.org | Cloudflare |  | 🔎 Home rendered; a public title/chapter could not be resolved for comment verification · [sample](https://mangacloud.org/) |
| MangaDE | https://mangade.io | No title page found |  | 🔎 3 saved page samples checked, including browser rendering; no initialized comment widget found; no rule inferred · [sample](https://mangade.io/home) |
| MangaDot | https://mangadot.net | 403 Forbidden | [mangadot](rules/mangadot.json) | ✅ Working: 8 comments read by Twe's actual extractor · [sample](https://mangadot.net/manga/41) |
| MangaFox.fun | https://mangafox.fun | Cloudflare | [mangahub-remark42](rules/mangahub-remark42.json) | 🟡 Rule linked: browser confirms own-domain Remark42 URL; sampled API thread empty · [sample](https://mangafox.fun/manga/zipang) |
| MangaHere.onl | https://mangahere.onl | Cloudflare | [mangahub-remark42-canonical](rules/mangahub-remark42-canonical.json) | 🟡 Rule linked: browser confirms shared mangahub.io thread URL; sampled thread empty · [sample](https://mangahere.onl/manga/zipang) |
| MangaHub | https://mangahub.io | Cloudflare | [mangahub-remark42](rules/mangahub-remark42.json) | ✅ Working: 34 nondeleted One Piece comments via Remark42; flat reply parents and HTML images mapped · [sample](https://mangahub.io/manga/one-piece) |
| MangaK | https://mangak.io | No title page found |  | 🔎 Home rendered; a public title/chapter could not be resolved for comment verification · [sample](https://mangak.io/) |
| Mangakakalot.fun | https://mangakakalot.fun | Cloudflare | [mangahub-remark42](rules/mangahub-remark42.json) | 🟡 Rule linked: browser confirms own-domain Remark42 URL; sampled API thread empty · [sample](https://mangakakalot.fun/manga/mao) |
| MangaLix | https://mangalix.com | No title page found |  | 🔎 2 saved page samples checked, including browser rendering; no initialized comment widget found; no rule inferred · [sample](https://mangalix.com/manga/dandadan) |
| MangaMelon | https://mangamelon.com | Cloudflare |  | 🔎 Home rendered; a public title/chapter could not be resolved for comment verification · [sample](https://mangamelon.com/) |
| MangaNel | https://manganel.me | Cloudflare | [mangahub-remark42-canonical](rules/mangahub-remark42-canonical.json) | 🟡 Rule linked: browser confirms shared mangahub.io thread URL; sampled thread empty · [sample](https://manganel.me/manga/wee) |
| MangaNow | https://manganow.to | No title page found |  | 🔎 Home rendered; a public title/chapter could not be resolved for comment verification · [sample](https://manganow.to/) |
| MangaOnline.fun | https://mangaonline.fun | Cloudflare | [mangahub-remark42](rules/mangahub-remark42.json) | 🟡 Rule linked: browser confirms own-domain Remark42 URL; sampled API thread empty · [sample](https://mangaonline.fun/manga/wee) |
| MangaOwl.io (unoriginal) | https://mangaowl.io | Cloudflare |  | 🟡 WordPress-style discussion found; sampled page has no comment items; mapping unverified · [sample](https://mangaowl.io/read-1/black-haze-2025/) |
| MangaPanda.onl | https://mangapanda.onl | Cloudflare | [mangahub-remark42](rules/mangahub-remark42.json) | 🟡 Rule linked: browser confirms own-domain Remark42 URL; sampled API thread empty · [sample](https://mangapanda.onl/manga/zipang) |
| MangaPark.tv (unoriginal) 🔞 | https://mangapark.tv | Cloudflare |  | 🔎 8 saved page samples checked, including browser rendering; no initialized comment widget found; no rule inferred · [sample](https://mangapark.tv/manhwa/desharow-mermaid/desharow-mermaid-chap-162/) |
| MangaReader.site | https://mangareader.site | Cloudflare | [mangahub-remark42-canonical](rules/mangahub-remark42-canonical.json) | 🟡 Rule linked: browser confirms shared mangahub.io thread URL; sampled thread empty · [sample](https://mangareader.site/manga/zipang) |
| MangaToday | https://mangatoday.fun | Cloudflare | [mangahub-remark42-canonical](rules/mangahub-remark42-canonical.json) | 🟡 Rule linked: browser confirms shared mangahub.io thread URL; sampled thread empty · [sample](https://mangatoday.fun/manga/wee) |
| Manhua Plus | https://manhuaplus.com | Cloudflare |  | 🔎 8 saved page samples checked, including browser rendering; no initialized comment widget found; no rule inferred · [sample](https://manhuaplus.com/manga/apotheosis/) |
| ManhuaHot | https://manhuahot.com | Cloudflare | [madara-wpdiscuz](rules/madara-wpdiscuz.json) | 🟡 Rule linked: wpDiscuz widget confirmed; sampled thread has no rendered comments · [sample](https://manhuahot.com/manga/whisper/) |
| ManhuaTop | https://manhuatop.org | Cloudflare | [manhuatop](rules/manhuatop.json) | ✅ Working: 20 rendered comments; images use page extraction; flat reply layout not nested · [sample](https://manhuatop.org/manhua/pick-me-up/) |
| ManhuaUS | https://manhuaus.com | 403 Forbidden | [wordpress](rules/wordpress.json) | ✅ Working: 851 comments read by Twe's actual extractor · [sample](https://manhuaus.com/manga/magic-emperor-0/) |
| Manhwa Comics 🔞 | https://manhwacomics.com | No title page found |  | 🔎 Home rendered; a public title/chapter could not be resolved for comment verification · [sample](https://manhwacomics.com/) |
| Manhwa Reads | https://manhwareads.com | Cloudflare |  | 🟡 Discussion count is 0; sampled title has no comment items; mapping unverified · [sample](https://manhwareads.com/manga/bleach/) |
| Manhwa18.today 🔞 | https://www.manhwa18.today | 403 Forbidden | [wordpress](rules/wordpress.json) | 🟡 Standard WordPress discussion/form found; sampled thread empty; comment extraction remains unverified · [sample](https://www.manhwa18.today/manga/slave-code/) |
| Manhwa68 🔞 | https://manhwa68.com | Cloudflare | [manhwa68-disqus](rules/manhwa68-disqus.json) | 🟡 Disqus rule linked; API confirms empty sampled thread · [sample](https://manhwa68.com/manga/set-it/) |
| Manhwalike 🔞 | https://manhwalike.com | No title page found | [manhwalike-disqus](rules/manhwalike-disqus.json) | ✅ Working: 2 Disqus posts read · [sample](https://manhwalike.com/manga-queen-bee) |
| ManhwaRead | https://manhwaread.com | 403 Forbidden | [madara-wpdiscuz](rules/madara-wpdiscuz.json) | ✅ Working: 67 comments read with wpDiscuz selectors · [sample](https://manhwaread.com/manhwa/queen-bee/) |
| Manhwatop | https://manhwatop.com | Cloudflare | [wordpress](rules/wordpress.json) | ✅ Working: 1 comments read; author/text selectors verified · [sample](https://manhwatop.com/manga/pick-me-up/) |
| ManhwaZone | https://manhwazone.com | No title page found |  | 🔎 3 saved page samples checked, including browser rendering; no initialized comment widget found; no rule inferred · [sample](https://manhwazone.com/explore) |
| Megatokyo | https://megatokyo.com | No title page found |  | 🔎 Home rendered; a public title/chapter could not be resolved for comment verification · [sample](https://megatokyo.com/) |
| MeiToon | https://meitoon.org | 403 Forbidden |  | ⛔ Access failed after direct and running-service attempts; no readable discussion verified · [sample](https://meitoon.org) |
| Milftoon 🔞 | https://milftoon.xxx | Cloudflare |  | 🔎 7 saved page samples checked, including browser rendering; no initialized comment widget found; no rule inferred · [sample](https://milftoon.xxx/comics/workout) |
| MLBB Lore | https://play.mobilelegends.com | No title page found |  | 🔎 Home rendered; a public title/chapter could not be resolved for comment verification · [sample](https://play.mobilelegends.com/) |
| Monochrome Custom | https://monochromecms.netlify.app | No title page found |  | 🔎 Home rendered; a public title/chapter could not be resolved for comment verification · [sample](https://monochromecms.netlify.app/) |
| Monochrome Scans | https://manga.d34d.one | No title page found |  | 🔎 2 saved page samples checked, including browser rendering; no initialized comment widget found; no rule inferred · [sample](https://manga.d34d.one/manga/79141782-bc73-44fe-a1b2-eff842ca6123) |
| MyAdultComics 🔞 | https://myadultcomics.com | No title page found |  | 🔎 7 saved page samples checked, including browser rendering; no initialized comment widget found; no rule inferred · [sample](https://myadultcomics.com/read.php?i=1637) |
| MyHentaiComics 🔞 | https://myhentaicomics.com | Cloudflare | [myhentai-comments](rules/myhentai-comments.json) | 🟡 API rule linked; Gallery/Page IDs parsed from source; sampled public thread empty; avatar URL needs loader support · [sample](https://myhentaicomics.com/gallery/thumbnails/64182) |
| MyHentaiGallery 🔞 | https://myhentaigallery.com | Cloudflare | [myhentai-comments](rules/myhentai-comments.json) | 🟡 API rule linked; Gallery/Page IDs parsed from source; sampled public thread empty; avatar URL needs loader support · [sample](https://myhentaigallery.com/a/60602) |
| NineHentai 🔞 | https://9hentai.so | No title page found |  | 🔎 Home rendered; a public title/chapter could not be resolved for comment verification · [sample](https://9hentai.so/) |
| Nortverse 🔞 | https://nortverse.com | 403 Forbidden | [nortverse](rules/nortverse.json) | ✅ Working: 16 rendered comments; images use page extraction · [sample](https://nortverse.com/comic/mansion-mystery-9/) |
| NovelCrow 🔞 | https://novelcrow.com | 403 Forbidden |  | ⛔ Access failed after direct and running-service attempts; no readable discussion verified · [sample](https://novelcrow.com) |
| Oglaf 🔞 | https://www.oglaf.com | No title page found |  | 🔎 3 saved page samples checked, including browser rendering; no initialized comment widget found; no rule inferred · [sample](https://www.oglaf.com/feeds/rss/) |
| OneManga.info | https://onemanga.info | Cloudflare | [mangahub-remark42-canonical](rules/mangahub-remark42-canonical.json) | 🟡 Rule linked: browser confirms shared mangahub.io thread URL; sampled thread empty · [sample](https://onemanga.info/manga/wee) |
| Only The Best Hentai 🔞 | https://onlythebesthentai.com | Cloudflare |  | 🔎 7 saved page samples checked, including browser rendering; no initialized comment widget found; no rule inferred · [sample](https://onlythebesthentai.com/anywhere-door/) |
| oots | https://www.giantitp.com | 403 Forbidden |  | 🔎 4 saved page samples checked, including browser rendering; no initialized comment widget found; no rule inferred · [sample](https://www.giantitp.com/comics/oots.html) |
| Patch Friday | https://patchfriday.com | No title page found |  | 🔎 Home rendered; a public title/chapter could not be resolved for comment verification · [sample](https://patchfriday.com/) |
| Philia Scans | https://philiascans.org | Cloudflare |  | 🟡 Reader review section found; sampled reviews empty; no verified comment mapping · [sample](https://philiascans.org/series/in-for-poison-in-for-love) |
| PornComix 🔞 | https://bestporncomix.com | Cloudflare |  | 🔎 Home rendered; a public title/chapter could not be resolved for comment verification · [sample](https://bestporncomix.com/) |
| PornhwaDB Reader 🔞 | https://pornhwareader.com | Cloudflare | [pornhwadb-reader](rules/pornhwadb-reader.json) | ✅ Working: 1 public series review; native extractor check recorded separately · [sample](https://pornhwareader.com/series/13/moby-dick) |
| Pornhwaz 🔞 | https://www.pornhwaz.com | Cloudflare | [pornhwaz](rules/pornhwaz.json) | 🟡 Plugin selectors and reply toggle confirmed in assets; sampled thread has no comments; read still unverified · [sample](https://www.pornhwaz.com/webtoon/scumbag/) |
| Questionable Content | https://www.questionablecontent.net | No title page found |  | 🔎 Home rendered; a public title/chapter could not be resolved for comment verification · [sample](https://www.questionablecontent.net/) |
| Rage Scans | https://ragescans.com | 403 Forbidden | [madara-wpdiscuz](rules/madara-wpdiscuz.json) | 🟡 Rule linked: wpDiscuz widget confirmed; sampled thread has no rendered comments · [sample](https://ragescans.com/manga/devil-ice/) |
| Raven Scans | https://ravenscans.org | 403 Forbidden |  | ⛔ Disqus forum ravenscans returned load error (code 15); not working · [sample](https://ravenscans.org/manga/lookism/) |
| Read Berserk Manga | https://readberserk.com | Cloudflare | [comentario-webview](rules/comentario-webview.json) | ⚠️ Public API returns 12 comments, but author IDs require a dictionary join; native rules cannot map authors. WebView fallback provided · [sample](https://readberserk.com/chapter/berserk-the-motion-comic-episode-1-the-black-swordsman-part-1/) |
| Read Chainsaw Man Manga Online 🔞 | https://ww6.readchainsawman.com | Cloudflare |  | ⛔ Comentario rejects the site origin (HTTP 403 domain verification); upstream configuration error · [sample](https://ww6.readchainsawman.com/chapter/look-back-chapter-1/) |
| Read Comics Online | https://readcomicsonline.ru | 403 Forbidden |  | 🔎 4 saved page samples checked, including browser rendering; no initialized comment widget found; no rule inferred · [sample](https://readcomicsonline.ru/comic/2000-ad) |
| Read Fairy Tail & Edens Zero Manga Online | https://ww9.readfairytail.com | Cloudflare |  | ⛔ Comentario rejects the site origin (HTTP 403 domain verification); upstream configuration error · [sample](https://ww9.readfairytail.com/chapter/heros-chapter-10.5/) |
| Read Kingdom Manga Online | https://ww6.readkingdom.com | Cloudflare |  | ⛔ Comentario rejects the site origin (HTTP 403 domain verification); upstream configuration error · [sample](https://ww6.readkingdom.com/chapter/kingdom-history-spoilers-chapter-0/) |
| Real Life Comics | https://reallifecomics.com | No title page found |  | 🔎 7 saved page samples checked, including browser rendering; no initialized comment widget found; no rule inferred · [sample](https://reallifecomics.com/comic-mobile.php/?comic=title-1) |
| Renascans | https://renascans.net | Cloudflare | [renascans](rules/renascans.json) | 🟡 Series API schema mapped from client; public sample empty; Markdown/spoiler formatting not parsed · [sample](https://renascans.net/manga/widower-osot9qro) |
| Revival Scans 🔞 | https://www.revivalscans.com | Cloudflare | [revivalscans](rules/revivalscans.json) | 🟡 Series API rule linked; sampled thread is empty; chapter comments not verified · [sample](https://www.revivalscans.com/series/cctv) |
| Rolia Scan | https://roliascan.com | No title page found |  | 🔎 4 saved page samples checked, including browser rendering; no initialized comment widget found; no rule inferred · [sample](https://roliascan.com/home/) |
| Rose Squad Scans 🔞 | https://rosesquadscans.aishiteru.org | No title page found |  | 🔎 2 saved page samples checked, including browser rendering; no initialized comment widget found; no rule inferred · [sample](https://rosesquadscans.aishiteru.org/wp-login.php?redirect_to=https%3A%2F%2Frosesquadscans.aishiteru.org%2F) |
| S2Manga | https://s2read.com | Cloudflare | [wordpress](rules/wordpress.json) | ✅ Working: 1 chapter comment; native extractor check recorded separately · [sample](https://s2read.com/manga/ill-be-the-warriors-mother/chapter-95/) |
| Sabrina Online | https://www.sabrina-online.com | No title page found |  | 🔎 7 saved page samples checked, including browser rendering; no initialized comment widget found; no rule inferred · [sample](https://www.sabrina-online.com/links.html) |
| SACACHISPA | https://sacachispa.site | No title page found |  | 🟡 Reader and dedicated discussion page checked; sampled chapter has 0 comments; item layout unverified · [sample](https://sacachispa.site/read/7adb4956-0be1-5c0c-bbac-2040fa91394e) |
| ScansGG | https://scans.gg | Cloudflare |  | 🔎 Home rendered; a public title/chapter could not be resolved for comment verification · [sample](https://scans.gg/) |
| Scythe Scans | https://scythescans.com | Cloudflare | [madara-wpdiscuz](rules/madara-wpdiscuz.json) | ✅ Working: 3 comments read with wpDiscuz selectors · [sample](https://scythescans.com/manga/the-shepherd-wizard/) |
| Setsu Scans | https://setsuscans.com | 403 Forbidden |  | ⛔ Access failed after direct and running-service attempts; no readable discussion verified · [sample](https://setsuscans.com) |
| SilentQuill | https://silentquill.net | Cloudflare |  | 🟡 Comment component found; sampled series has no comments; item layout remains unverified · [sample](https://silentquill.net/series/the-monstrous-new-life-of-the-fallen-empires-recruit/) |
| Snafu Comics | https://www.snafu-comics.com | No title page found | [snafucomic-disqus](rules/snafucomic-disqus.json) | ✅ Working: 50 Disqus posts read · [sample](https://www.snafu-comics.com/grimtales) |
| Solar and Sundry | https://sas-api.fly.dev | No title page found |  | 🔎 Home rendered; a public title/chapter could not be resolved for comment verification · [sample](https://sas-api.fly.dev/) |
| SpyFakku 🔞 | https://hentalk.pw | Cloudflare |  | 🔎 8 saved page samples checked, including browser rendering; no initialized comment widget found; no rule inferred · [sample](https://hentalk.pw/g/18948) |
| Sunshine Butterfly Scans 🔞 | https://wings.sbs | No title page found |  | 🔎 Home rendered; a public title/chapter could not be resolved for comment verification · [sample](https://wings.sbs/) |
| SUPER MEGA | https://www.supermegacomics.com | No title page found |  | 🔎 7 saved page samples checked, including browser rendering; no initialized comment widget found; no rule inferred · [sample](https://www.supermegacomics.com/index.php) |
| Team Shadowi | https://www.team-shadowi.com | 403 Forbidden | [teamshadowi](rules/teamshadowi.json) | ✅ Working: 3 root comments and 7 nested replies expanded; rendered images mapped · [sample](https://www.team-shadowi.com/read/first-love-trap/7) |
| Temple Scan 🔞 | https://templetoons.com | Cloudflare |  | ⛔ Browser still shows an access challenge; no comment read verified · [sample](https://templetoons.com/challenge?redirect=%2F) |
| The Blank 🔞 | https://theblank.net | 403 Forbidden |  | 🔎 Home rendered; a public title/chapter could not be resolved for comment verification · [sample](https://theblank.net/) |
| The Property of Hate | https://jolleycomics.com | No title page found |  | 🔎 7 saved page samples checked, including browser rendering; no initialized comment widget found; no rule inferred · [sample](https://jolleycomics.com/Art/) |
| ToonHey 🔞 | https://toonhey.com | 403 Forbidden |  | 🔎 4 saved page samples checked, including browser rendering; no initialized comment widget found; no rule inferred · [sample](https://toonhey.com/en/) |
| Toonily | https://toonily.com | Cloudflare | [toonily](rules/toonily.json) | ✅ Working: title and chapter API each returned 1 comment; offset paging mapped; rich media markup not parsed · [sample](https://toonily.com/serie/overgeared-86ba23b3/) |
| Toonily.me 🔞 | https://toontop.io | No title page found |  | 🔎 Home rendered; a public title/chapter could not be resolved for comment verification · [sample](https://toontop.io/) |
| Toonkotsu | https://toonkotsu.com | Cloudflare | [toonkotsu](rules/toonkotsu.json) | ✅ Working: 1 series comment + 1 reply and 1 chapter comment via service browser; first 20 per feed; Markdown media not parsed · [sample](https://toonkotsu.com/title/qy17we-the-trashy-pd-has-to-survive-as-an-idol/4924511-chapter-66) |
| TopManhua.net | https://topmanhua.net | Cloudflare | [topmanhuanet-disqus](rules/topmanhuanet-disqus.json) | ✅ Working: 1 Disqus posts read · [sample](https://topmanhua.net/manga/overgeared/) |
| Tower Of God Manga Online | https://w82.thetowerofgod.com | Cloudflare |  | ⛔ Disqus forum towerofgod returned load error (code 15); not working · [sample](https://w85.thetowerofgod.com/manga/tower-of-god-chapter-9/) |
| Valir Scans | https://valirscans.org | Cloudflare | [diva-valir](rules/diva-valir.json) | ✅ Working: 1 title / 14 chapter comments; HTML, spoilers, paging and reply API mapped · [sample](https://valirscans.org/series/comic/roxana) |
| vgperson | https://vgperson.com | No title page found |  | 🔎 Home rendered; a public title/chapter could not be resolved for comment verification · [sample](https://vgperson.com/) |
| Vision Haze | https://www.visionhaze.com | 403 Forbidden |  | 🔎 4 saved page samples checked, including browser rendering; no initialized comment widget found; no rule inferred · [sample](https://www.visionhaze.com/about/) |
| VIZ | https://www.viz.com | No title page found | [viz](rules/viz.json) | ✅ Working: 2 public product comments; spoiler attribute mapped · [sample](https://www.viz.com/manga-books/manga/jujutsu-kaisen-complete-box-set/product/9017) |
| Voyce.Me | https://www.voyce.me | No title page found |  | 🔎 Home rendered; a public title/chapter could not be resolved for comment verification · [sample](https://www.voyce.me/) |
| VyvyManga | https://mangavyvy.net | 403 Forbidden |  | ⛔ Access failed after direct and running-service attempts; no readable discussion verified · [sample](https://mangavyvy.net) |
| War For Rayuba | https://xrabohrok.github.io/WarMap/#/ | No title page found |  | 🔎 2 saved page samples checked, including browser rendering; no initialized comment widget found; no rule inferred · [sample](https://xrabohrok.github.io/WarMap/#/) |
| Webdex Scans | https://webdexscans.com | Cloudflare |  | 🔎 2 saved page samples checked, including browser rendering; no initialized comment widget found; no rule inferred · [sample](https://webdexscans.com/) |
| WebNovel | https://www.webnovel.com | Cloudflare |  | 🔎 7 saved page samples checked, including browser rendering; no initialized comment widget found; no rule inferred · [sample](https://m.webnovel.com/book/mr.-sunshine_16873587705577105) |
| WebtoonLib | https://webtoonlib.to | Cloudflare | [webtoonlib](rules/webtoonlib.json) | ✅ Working: 50 series roots + nested replies and 4 chapter roots via public API in service browser; first batch only · [sample](https://webtoonlib.to/series/the-boxer-b6cb3a) |
| WebtoonXYZ | https://www.webtoon.xyz | 403 Forbidden |  | ⛔ Disqus forum webtoonxyz returned load error (code 15); not working · [sample](https://www.webtoon.xyz/read/get-out/) |
| Wildtoon 🔞 | https://wildtoon.com | 403 Forbidden | [wordpress](rules/wordpress.json) | 🟡 Standard WordPress discussion/form found; sampled thread empty; comment extraction remains unverified · [sample](https://wildtoon.com/webtoon/bunk-bed-official/) |
| WuxiaWorld | https://wuxiaworld.site | Cloudflare | [madara-wpdiscuz](rules/madara-wpdiscuz.json) | 🟡 Rule linked: wpDiscuz widget confirmed; sampled thread has no rendered comments · [sample](https://wuxiaworld.site/novel/pick-me-up/) |
| XlecX 🔞 | https://xlecx.one | No title page found | [xlecx](rules/xlecx.json) | ✅ Working: 2 comments; author/text selectors verified · [sample](https://xlecx.one/64666-lickin-it.html) |
| XoManga | https://www.xomanga.site | 403 Forbidden |  | 🔎 Home rendered; a public title/chapter could not be resolved for comment verification · [sample](https://www.xomanga.site/) |
| XOXO Comics | https://xoxocomic.com | Cloudflare |  | 🔎 7 saved page samples checked, including browser rendering; no initialized comment widget found; no rule inferred · [sample](https://istod.com/wvrv?ofv_id=1662&aff_pub_id=120796&click_id=cr287164819161219142&subid1=120796&subid2=3274293) |
| YakshaComics | https://yakshacomics.com | Cloudflare | [wordpress](rules/wordpress.json) | 🟡 Standard WordPress discussion/form found; sampled thread empty; comment extraction remains unverified · [sample](https://yakshacomics.com/manga/the-mech-mechanic/) |
| YaoiScan | https://yaoiscan.com | 403 Forbidden | [wordpress](rules/wordpress.json) | ✅ Working: 2 comments; author/text selectors verified · [sample](https://yaoiscan.com/read/hwan/) |
| Zinmanga | https://mangazin.org | Cloudflare | [madara-wpdiscuz](rules/madara-wpdiscuz.json) | 🟡 Rule linked: wpDiscuz widget confirmed; sampled thread has no rendered comments · [sample](https://mangazin.org/manga/breakers/) |
### Multi (87)

| Extension | Site | Reason | Rule |
|---|---|---|---|
| 3Hentai 🔞 | https://3hentai.net | No title page found |  |
| 4KHD 🔞 | https://www.4khd.com | Cloudflare |  |
| AHottie 🔞 | https://ahottie.top | No title page found |  |
| Akuma 🔞 | https://akuma.moe | 403 Forbidden |  |
| AsmHentai 🔞 | https://asmhentai.com | Cloudflare |  |
| BaoBua 🔞 | https://baobua.net | No title page found |  |
| Buon Dua 🔞 | https://buondua.com | Cloudflare |  |
| Comic Growl | https://comic-growl.com | 403 Forbidden |  |
| Comikey | https://comikey.com | Cloudflare |  |
| Coomer 🔞 | https://coomer.st | No title page found |  |
| Cubari | https://cubari.moe | No title page found |  |
| Danbooru 🔞 | https://danbooru.donmai.us | 403 Forbidden |  |
| DB New Hope | https://dbnewhope.com | No title page found |  |
| Doujiva 🔞 | https://doujiva.com | 403 Forbidden |  |
| Dragon Ball Multiverse | https://www.dragonball-multiverse.com | No title page found |  |
| Elite Babes 🔞 | https://www.elitebabes.com | Cloudflare |  |
| EveriaClub (unoriginal) 🔞 | https://www.everiaclub.com | No title page found |  |
| Femjoy Hunter 🔞 | https://www.femjoyhunter.com | Cloudflare |  |
| FoamGirl 🔞 | https://foamgirl.net | Cloudflare |  |
| FSI Comics 🔞 | https://fsicomics.com | Cloudflare |  |
| FTV Hunter 🔞 | https://www.ftvhunter.com | Cloudflare |  |
| GlobalComix | https://globalcomix.com | No title page found |  |
| Grabber Zone | https://grabber.zone | Cloudflare |  |
| HDoujin 🔞 | https://hdoujin.org | No title page found |  |
| Hentai Cosplay 🔞 | https://hentai-cosplay-xxx.com | Cloudflare |  |
| HentaiEnvy 🔞 | https://hentaienvy.com | No title page found |  |
| HentaiEra 🔞 | https://hentaiera.com | Cloudflare |  |
| HentaiFox 🔞 | https://hentaifox.com | No title page found |  |
| HentaiRox 🔞 | https://hentairox.com | No title page found |  |
| HentaiZap 🔞 | https://hentaizap.com | Cloudflare |  |
| HNI-Scantrad | https://hni-scantrad.net | No title page found |  |
| HOLONOMETRIA | https://holoearth.com | No title page found |  |
| IMHentai 🔞 | https://imhentai.xxx | Cloudflare |  |
| INKRUSH | https://inkrush.site | No title page found |  |
| JJCOS 🔞 | https://jjcos.com | No title page found |  |
| Joymii Hub 🔞 | https://www.joymiihub.com | Cloudflare |  |
| Junmeitu 🔞 | https://meijuntu.com | No title page found |  |
| Kagane | https://kagane.moe | No title page found |  |
| Kemono 🔞 | https://kemono.cr | No title page found |  |
| Kiutaku 🔞 | https://kiutaku.com | No title page found |  |
| Kodoku Studio | https://kodokueasyaccess.com | No title page found |  |
| Lunar Manga | https://lunarx.to | Cloudflare |  |
| Manga Ball | https://mangaball.com | Cloudflare |  |
| Manga Million | https://mangamillion.shueisha.co.jp | No title page found |  |
| MANGA Plus by SHUEISHA | https://mangaplus.shueisha.co.jp | No title page found |  |
| MANGA Plus Creators by SHUEISHA | https://mangaplus-creators.jp | No title page found |  |
| MangaCrazy 🔞 | https://mangacrazy.net | Cloudflare |  |
| MangaFire | https://mangafire.to | Cloudflare |  |
| MangaTaro | https://mangataro.org | No title page found |  |
| MangaToon (Limited) | https://mangatoon.mobi | No title page found |  |
| Manhuarm | https://manhuarmtl.com | 403 Forbidden |  |
| Manhwa-raw 🔞 | https://manhwa-raw.com | 403 Forbidden |  |
| Manhwa18.net 🔞 | https://manhwa18.net | No title page found |  |
| Manta Comics | https://manta.net/en | No title page found |  |
| MayoTune | https://mayochuu.xyz | Cloudflare |  |
| Metart Hunter 🔞 | https://www.metarthunter.com | Cloudflare |  |
| Mitaku 🔞 | https://mitaku.net | Cloudflare |  |
| MyReadingManga 🔞 | https://myreadingmanga.info | 403 Forbidden |  |
| NHentai.to 🔞 | https://nhentai.to | No title page found |  |
| NHentai.xxx 🔞 | https://nhentai.xxx | Cloudflare |  |
| NovelCool | https://www.novelcool.com | No title page found |  |
| One Piece Fans | https://one-piece-fans2.com | No title page found |  |
| OniSaga | https://onisaga.com | 403 Forbidden |  |
| OSOSEDKI 🔞 | https://ososedki.com | Cloudflare |  |
| PandaChaika 🔞 | https://panda.chaika.moe | No title page found |  |
| Pawchive 🔞 | https://pawchive.pw | No title page found |  |
| Pepper&Carrot | https://www.peppercarrot.com | No title page found |  |
| Photos18 🔞 | https://www.photos18.com | Cloudflare |  |
| Pixiv | https://www.pixiv.net | Cloudflare |  |
| Playmate Hunter 🔞 | https://pmatehunter.com | Cloudflare |  |
| Project Suki | https://projectsuki.com | Cloudflare |  |
| RokuHentai 🔞 | https://rokuhentai.com | Cloudflare |  |
| SchaleNetwork 🔞 | https://shupogaki.moe | No title page found |  |
| Swarm | https://swarm.ws | No title page found |  |
| Taddy INK (Webtoons) | https://taddy.org | No title page found |  |
| The Library of Ohara | https://thelibraryofohara.com | No title page found |  |
| ToonLook 🔞 | https://toonlook.com | Cloudflare |  |
| Twicomi | https://twicomi.com | No title page found |  |
| V2PH 🔞 | https://www.v2ph.com | 403 Forbidden |  |
| Webcomics | https://webcomicsapp.com | No title page found |  |
| Webtoons.com | https://www.webtoons.com | No title page found |  |
| XArt Hunter 🔞 | https://www.xarthunter.com | Cloudflare |  |
| Xiutaku 🔞 | https://xiutaku.com | Cloudflare |  |
| Yabai 🔞 | https://yabai.si | 403 Forbidden |  |
| Yaoi Manga Online 🔞 | https://yaoimangaonline.com | Cloudflare |  |
| Yaoi.me 🔞 | https://yaoi.me | Cloudflare |  |
| YellowNote 🔞 | https://xchina.co | Cloudflare |  |

### Arabic (33)

| Extension | Site | Reason | Rule |
|---|---|---|---|
| Anyone Manga | https://anyonemanga.com | Cloudflare |  |
| Arab Toons 🔞 | https://arabtoons.net | Cloudflare |  |
| ArabManhwa 🔞 | https://arabmanhwa.com | Cloudflare |  |
| Arabs Hentai 🔞 | https://arabshentai.com | 403 Forbidden |  |
| Area Manga | https://ar.kenmanga.com | 403 Forbidden |  |
| AriaToon | https://ariatoon.com | Cloudflare |  |
| Despair Manga | https://despair-world.com | 403 Forbidden |  |
| Detective Conan Ar | https://manga.detectiveconanar.com | 403 Forbidden |  |
| Dilar | https://dilar.tube | Cloudflare |  |
| Duskoryvile | https://duskoryvile.com | No title page found |  |
| Empire Webtoon 🔞 | https://webtoonempire-bl.com | Cloudflare |  |
| EShadow | https://eshadow.net | No title page found |  |
| Hentai Slayer 🔞 | https://hentaislayer.net | Cloudflare |  |
| Hijala | https://hijala.com | 403 Forbidden |  |
| HizoManga | https://hizomanga.net | Cloudflare |  |
| Kawii Manga | https://kawaiimanga.org | Cloudflare |  |
| Lava Scans | https://lavascans.com | Cloudflare |  |
| Manga Bab 🔞 | https://mangabab.com | Cloudflare |  |
| Manga Starz | https://starzmanga.com | Cloudflare |  |
| MangaDar | https://mangadar.com | 403 Forbidden |  |
| Mangalink | https://link-manga.net | Cloudflare |  |
| MangaLionz | https://manga-lionz.org | Cloudflare |  |
| MangaSpark | https://sparkmanga.net | Cloudflare |  |
| MangaSwat | https://meshmanga.com | No title page found |  |
| MangaTek | https://mangatek.com | 403 Forbidden |  |
| MangaTik | https://mangatik.com | Cloudflare |  |
| Murim | https://www.murim.site | No title page found |  |
| NeverScans | https://neverscans.com | No title page found |  |
| Oduto | https://nb19u.blogspot.com | No title page found |  |
| Paradise BL 🔞 | https://paradise-bl.com | 403 Forbidden |  |
| StellarSaber | https://stellarsaber.pro | 403 Forbidden |  |
| Team X | https://olympustaff.com | Cloudflare |  |
| XSano Manga | https://www.xsano-manga.com | No title page found |  |

### Catalan (2)

| Extension | Site | Reason | Rule |
|---|---|---|---|
| Fansubs.cat | https://manga.fansubs.cat | No title page found |  |
| Hentai.cat 🔞 | https://manga.hentai.cat | No title page found |  |

### Chinese (37)

| Extension | Site | Reason | Rule |
|---|---|---|---|
| 18Manhua | https://18mh.org | 403 Forbidden |  |
| Baka Manhua 🔞 | https://bakamh.com | 403 Forbidden |  |
| Baozi Manhua | https://cn.baozimh.com | 403 Forbidden |  |
| BiliManga | https://www.bilimanga.net | No title page found |  |
| Cartoon18 🔞 | https://www.cartoon18.com | Cloudflare |  |
| Creative Comic Collection | https://www.creative-comic.tw | No title page found |  |
| Dm5 | https://www.dm5.com | No title page found |  |
| GoDa | https://baozimh.org | Cloudflare |  |
| Guazimanhua | https://www.guazimanhua.com | No title page found |  |
| H-Comic 🔞 | https://h-comic.com | No title page found |  |
| Hanime1 🔞 | https://hanimeone.me | Cloudflare |  |
| Hikarinagi | https://www.hikarinagi.org | Cloudflare |  |
| Iqiyi | https://bud.m.iqiyi.com | No title page found |  |
| JComic 🔞 | https://jcomic.net | No title page found |  |
| Jinman Tiantang 🔞 | https://18comic.vip | 403 Forbidden |  |
| Komiic | https://komiic.com | Cloudflare |  |
| Kuaikanmanhua | https://www.kuaikanmanhua.com | No title page found |  |
| Mangabz | https://mangabz.com | No title page found |  |
| Manhua160 | https://www.mh160mh.com | No title page found |  |
| Manhuaren | https://mangaapi.manhuaren.com | No title page found |  |
| Manhuashe | https://www.311s.com | No title page found |  |
| Miaoqu Manhua | https://www.miaoqumh.org | Cloudflare |  |
| MyComic | https://mycomic.com | 403 Forbidden |  |
| Picacomic 🔞 | https://manhuabika.com | No title page found |  |
| Roumanwu 🔞 | https://rouman5.com | No title page found |  |
| Shenshi Huisuo | https://www.hentaiclub.net | Cloudflare |  |
| Tencent Comics (ac.qq.com) | https://m.ac.qq.com | No title page found |  |
| Terra Historicus | https://comic.hypergryph.com | No title page found |  |
| Tongli | https://ebook.tongli.com.tw | Cloudflare |  |
| Utifa | https://bx.yaimer.com | Cloudflare |  |
| vomic | https://vomicmh.com | No title page found |  |
| WNACG 🔞 | https://www.wnacg.buzz | No title page found |  |
| Xipi Manhua | https://m.hipmh.com | Cloudflare |  |
| YKMH | https://www.ykmh.net | 403 Forbidden |  |
| Zaimanhua | https://manhua.zaimanhua.com | No title page found |  |
| Zazhimi | https://www.zazhimi.net | No title page found |  |
| Zerobyw | http://www.zerobyw33.com | No title page found |  |

### Czech (1)

| Extension | Site | Reason | Rule |
|---|---|---|---|
| Evil production 🔞 | https://evil-manga.eu | 403 Forbidden |  |

### French (42)

| Extension | Site | Reason | Rule |
|---|---|---|---|
| AnimeSama | https://anime-sama.to | 403 Forbidden |  |
| Aniverse | https://aniverse.fr | 403 Forbidden |  |
| AralosBD | https://aralosbd.fr | No title page found |  |
| Astral-Manga | https://astral-manga.fr | 403 Forbidden |  |
| Banchan Scan | https://banchanscan.fr | 403 Forbidden |  |
| BDplus | https://bdplus.cc | Cloudflare |  |
| BigSolo | https://bigsolo.org | 403 Forbidden |  |
| Blossom Scans | https://blossom-scans.com | 403 Forbidden |  |
| Blue Solo | https://bluesolo.org | No title page found |  |
| ChaosTrad | https://chaostrad.fr | Cloudflare |  |
| CrunchyScan | https://crunchyscan.st | 403 Forbidden |  |
| Epsilon Scan 🔞 | https://epsilonscan.to | 403 Forbidden |  |
| Hana Book 🔞 | https://www.hana-book.fr | No title page found |  |
| Harmony-Scan | https://harmony-scan.fr | Cloudflare |  |
| Hentai Scan Reader 🔞 | https://hentai.scanreader.net | Cloudflare |  |
| HentaiZone 🔞 | https://hentaizone.xyz | 403 Forbidden |  |
| HentaiZone (Beta) 🔞 | https://beta.hentaizone.xyz | 403 Forbidden |  |
| HistoireDHentai 🔞 | https://hhentai.fr | Cloudflare |  |
| Japscan | https://www.japscan.foo | Cloudflare |  |
| LanorTrad | https://lanortrad.com | No title page found |  |
| Lelmanga | https://www.lelmanga.com | Cloudflare |  |
| Lelscan-VF | https://www.lelscanfr.com | Cloudflare |  |
| Les Poroiniens | https://lesporoiniens.org | No title page found |  |
| Ma Brute 🔞 | https://mabrute.com | 403 Forbidden |  |
| Manga-Corporation | https://manga-corporation.com | Cloudflare |  |
| Manga-Scantrad | https://manga-scantrad.io | 403 Forbidden |  |
| MangaHub.fr | https://mangahub.fr | 403 Forbidden |  |
| Mangakawaii | https://www.mangakawaii.fr | Cloudflare |  |
| MangaMoins | https://mangamoins.com | 403 Forbidden |  |
| Mangas-Origines.fr | https://mangas-origines.fr | 403 Forbidden |  |
| Ono | https://www.ono.live | No title page found |  |
| Ortega Scans 🔞 | https://ortegascans.fr | Cloudflare |  |
| Pantheon Scan | https://pantheon-scan.com | No title page found |  |
| Rimu Scans | https://rimuscan.fr | Cloudflare |  |
| Scan Reader | https://scanreader.net | Cloudflare |  |
| Scan VF | https://www.scan-vf.net | 403 Forbidden |  |
| ScanR | https://teamscanr.fr | No title page found |  |
| Soft Epsilon Scan | https://epsilonsoft.to | 403 Forbidden |  |
| Sushi-Scan | https://sushiscan.net | 403 Forbidden |  |
| Toon FR 🔞 | https://toonfr.com | 403 Forbidden |  |
| Twatt | https://twatt.fr | No title page found |  |
| X-Manga 🔞 | https://x-manga.org | 403 Forbidden |  |

### German (1)

| Extension | Site | Reason | Rule |
|---|---|---|---|
| Manga Tube | https://manga-tube.me | No title page found |  |

### Indonesian (52)

| Extension | Site | Reason | Rule |
|---|---|---|---|
| Ainz Scans ID | https://v3.ainzscans01.com | Cloudflare |  |
| APKOMIK | https://01.apkomik.com | 403 Forbidden |  |
| Area Komik 🔞 | https://areakomik.com | Cloudflare |  |
| BacaKomik | https://bacakomik.my | Cloudflare |  |
| Bacami | https://v1.bacami.site | 403 Forbidden |  |
| CGBUM | https://cgbum.com | Cloudflare |  |
| Comicaso | https://v3.comicaso.pro | No title page found |  |
| CosmicScans | https://04.cosmicscans.to | Cloudflare |  |
| CrotPedia 🔞 | https://crotpedia.net | Cloudflare |  |
| Doujindesu 🔞 | https://doujin.desu.xxx | Cloudflare |  |
| Doujinku 🔞 | https://doujinku.org | 403 Forbidden |  |
| Hentai Crot 🔞 | https://hentaicrot.com | Cloudflare |  |
| Holotoon | https://holodek.run | Cloudflare |  |
| Ikiru | https://09.ikiru.wtf | Cloudflare |  |
| Kaguya 🔞 | https://02.kaguya.pro | 403 Forbidden |  |
| Kiryuu | https://v7.kiryuu.to | Cloudflare |  |
| KlikManga | https://klikmanga.org | Cloudflare |  |
| Komik Dewasa 🔞 | https://komikdewasa.mom | Cloudflare |  |
| Komik Dewasa Art 🔞 | https://komikdewasa.art | 403 Forbidden |  |
| Komik Station | https://komikstation.org | Cloudflare |  |
| Komikindo 🔞 | https://2.komikindo.shop | Cloudflare |  |
| KomikIndoID | https://komikindo.ch | Cloudflare |  |
| Komikmu 🔞 | https://komikmu.top | Cloudflare |  |
| KomikNesia | https://v2.komiknesiaku.com | Cloudflare |  |
| Komiku.com | https://01.komiku.asia | Cloudflare |  |
| Komikzoid | https://01.komikzoid.id | 403 Forbidden |  |
| KoronaxScan | https://project.koronaxscan.my.id | No title page found |  |
| KumoPoi 🔞 | https://beta.kumopoi.com | No title page found |  |
| Kuro Manga | https://kuromanga.id | Cloudflare |  |
| LepoyTL | https://www.lepoytl.my.id | No title page found |  |
| LianScans 🔞 | https://www.lianscans.com | No title page found |  |
| LumosKomik | https://03.lumosgg.com | Cloudflare |  |
| Luvyaa | https://v5.luvyaa.co | 403 Forbidden |  |
| Manga Can | https://mangacanblog.com | Cloudflare |  |
| Mangakuri 🔞 | https://lc2.mangakuri.online | 403 Forbidden |  |
| Mangalay | http://mangalay.blogspot.com | No title page found |  |
| Manhwa Indo | https://www.manhwaindo.my | Cloudflare |  |
| MG Komik | https://web1.mgkomik.cc | 403 Forbidden |  |
| MikoRoku | https://mikoroku.com | No title page found |  |
| Narasi Ninja | https://narasininja.net | Cloudflare |  |
| Ngomik (unoriginal) | https://02.ngomik.cc | Cloudflare |  |
| Omicaso | https://omicaso.org | No title page found |  |
| Pix Hentai 🔞 | https://pixhentai.com | Cloudflare |  |
| Riztranslation | https://riztranslation.pages.dev | No title page found |  |
| Ryukomik 🔞 | https://ryukomik.my.id | Cloudflare |  |
| Sasangeyou 🔞 | https://sasangeyou.net | Cloudflare |  |
| Shinigami | https://11.shinigami.asia | 403 Forbidden |  |
| Shiro Doujin 🔞 | https://shirodoujin.com | 403 Forbidden |  |
| Siikomik | https://siikomik.id | Cloudflare |  |
| Softkomik | https://softkomik.app | No title page found |  |
| TheManga | https://themanga.site | 403 Forbidden |  |
| Ulas Comic | https://www.ulascomic01.xyz | No title page found |  |

### Italian (13)

| Extension | Site | Reason | Rule |
|---|---|---|---|
| Anime GDR Club | http://www.agcscanlation.it | No title page found |  |
| DDT Team | https://ddt.hastateam.com | 403 Forbidden |  |
| GTO The Great Site | https://reader.gtothegreatsite.net | No title page found |  |
| Hasta Team | https://reader.hastateam.com | 403 Forbidden |  |
| Hentai ITA 🔞 | https://hentai-ita.net | No title page found |  |
| Hentai Zone 🔞 | https://hentaizone.me | 403 Forbidden |  |
| LupiTeam | https://lupiteam.net | No title page found |  |
| Mangaworld | https://www.mangaworld.mx | No title page found |  |
| MangaworldAdult 🔞 | https://www.mangaworldadult.net | No title page found |  |
| NIFTeam | https://read-nifteam.info | No title page found |  |
| Phoenix Scans | https://www.phoenixscans.com | No title page found |  |
| TuttoAnimeManga | https://tuttoanimemanga.net | No title page found |  |
| Walpurgi Scan | https://www.walpurgiscan.it | 403 Forbidden |  |

### Japanese (100)

| Extension | Site | Reason | Rule |
|---|---|---|---|
| Alphapolis | https://www.alphapolis.co.jp | No title page found |  |
| Asacomi | https://asacomi.jp | 403 Forbidden |  |
| Bibibi Comic | https://bibibi-comic.com | 403 Forbidden |  |
| Big Comics | https://bigcomics.jp | 403 Forbidden |  |
| Booklista Studio | https://studio.booklista.co.jp | 403 Forbidden |  |
| BookLive | https://booklive.jp | No title page found |  |
| Champion Cross | https://championcross.jp | 403 Forbidden |  |
| Comic Action | https://comic-action.com | No title page found |  |
| Comic Boost | https://comic-boost.com | No title page found |  |
| Comic Border | https://comicborder.com | No title page found |  |
| Comic Days | https://comic-days.com | No title page found |  |
| Comic Earth Star | https://comic-earthstar.com | No title page found |  |
| Comic Festa | https://comic.iowl.jp | No title page found |  |
| COMIC FUZ | https://comic-fuz.com | No title page found |  |
| Comic Gardo | https://comic-gardo.com | No title page found |  |
| Comic Grast | https://novema.jp | 403 Forbidden |  |
| Comic Ogyaaa | https://comic-ogyaaa.com | No title page found |  |
| Comic Pash | https://comicpash.jp | 403 Forbidden |  |
| Comic Ride | https://comicride.jp | 403 Forbidden |  |
| Comic Room Base | https://comic-room-base.com | 403 Forbidden |  |
| Comic Ryu | https://comic-ryu.jp | 403 Forbidden |  |
| Comic Seasons | https://comic-seasons.com | No title page found |  |
| Comic Trail | https://comic-trail.com | No title page found |  |
| Comic Y-OURs | https://comic-y-ours.com | No title page found |  |
| Comirela | https://comirela.com | 403 Forbidden |  |
| Corocoro Online | https://www.corocoro.jp | No title page found |  |
| DMM/FANZA | https://book.dmm.com | No title page found |  |
| Docomo | https://dbook.docomo.ne.jp | No title page found |  |
| Dokiraw | https://dokiraw.city | No title page found |  |
| DreComi+ | https://drecomi-plus.jp | 403 Forbidden |  |
| eBookJapan | https://ebookjapan.yahoo.co.jp | No title page found |  |
| Feel Web | https://feelweb.jp | No title page found |  |
| FireCross | https://firecross.jp | No title page found |  |
| FOD | https://manga.fod.fujitv.co.jp | 403 Forbidden |  |
| G-Comi | https://g-comi.jp | 403 Forbidden |  |
| GANMA! | https://ganma.jp | No title page found |  |
| Gaugau Monster Plus | https://gaugau.futabanet.jp | No title page found |  |
| Goraku Web | https://gorakuweb.com | No title page found |  |
| Hachiraw | https://hachiraw.net | 403 Forbidden |  |
| Hakusensha e-net | https://www.hakusensha-e.net | No title page found |  |
| Hana To Yume+ | https://hanayume.com | 403 Forbidden |  |
| HAYA Comic | https://hayacomic.jp | 403 Forbidden |  |
| HERO'S Web | https://heros-web.com | 403 Forbidden |  |
| Honto | https://honto.jp | 403 Forbidden |  |
| Idol. gravureprincess .date 🔞 | https://idol.gravureprincess.date | No title page found |  |
| J-N Books | https://comic.j-nbooks.jp | 403 Forbidden |  |
| Jestful | https://jestful.net | No title page found |  |
| Jmanga | https://jmanga.cool | No title page found |  |
| KimiComi | https://kimicomi.com | 403 Forbidden |  |
| KissLove | https://klz9.com | Cloudflare |  |
| Klto9 | https://klto9.com | No title page found |  |
| Kmansin09 | https://kmansin09.top | Cloudflare |  |
| Kumaraw | https://kumaraw.com | 403 Forbidden |  |
| MAGCOMI | https://magcomi.com | No title page found |  |
| MagKan | https://kansai.mag-garden.co.jp | 403 Forbidden |  |
| Manga One | https://manga-one.com | No title page found |  |
| Manga Rw | https://mangarw.com | No title page found |  |
| Manga Saison | https://mechacomi.jp | No title page found |  |
| Manga SPA | https://mangaspa.nikkan-spa.jp | 403 Forbidden |  |
| Manga Time Square | https://mangatime-square.com | No title page found |  |
| Manga UP! (Japan) | https://www.manga-up.com | No title page found |  |
| Manga Zegra | https://manga-zegra.com | 403 Forbidden |  |
| Manga-5 | https://manga-5.com | No title page found |  |
| Manga1000 | https://hachiraw.win | No title page found |  |
| MangaBang Comics | https://comics.manga-bang.com | 403 Forbidden |  |
| MangaBox | https://www.mangabox.me | No title page found |  |
| MangaBu | https://mangabu.jp | 403 Forbidden |  |
| Mangalt | https://mangalt.jp | 403 Forbidden |  |
| MangaMee | https://manga-mee.jp | No title page found |  |
| MangaNo | https://manga-no.com | No title page found |  |
| MangaRaw | https://mangaraw.co.uk | No title page found |  |
| Mecha Comic | https://mechacomic.jp | No title page found |  |
| MiuRaw | https://miuraw.net | Cloudflare |  |
| Mokuro | https://mokuro.moe | No title page found |  |
| Music Book Japan | https://music-book.jp | No title page found |  |
| Nami Comic | https://namicomic.jp | 403 Forbidden |  |
| Nicovideo Seiga | https://sp.manga.nicovideo.jp | No title page found |  |
| Ohta Web Comic | https://webcomic.ohtabooks.com | No title page found |  |
| Our Feel | https://ourfeel.jp | No title page found |  |
| Pash Up! | https://pash-up.jp | No title page found |  |
| PiaComic | https://piacomic.jp | 403 Forbidden |  |
| Piccoma | https://piccoma.com | No title page found |  |
| Pixiv Comic | https://comic.pixiv.net | Cloudflare |  |
| Raw18 🔞 | https://raw18.guru | No title page found |  |
| RawBaka | https://rawbaka.site | Cloudflare |  |
| RawINU | https://rawinu.com | Cloudflare |  |
| Rawkuma | https://rawkuma.net | Cloudflare |  |
| RimacomiPlus | https://rimacomiplus.jp | 403 Forbidden |  |
| Sen Manga | https://raw.senmanga.com | No title page found |  |
| SoraRaw | https://soraraw.com | 403 Forbidden |  |
| Sugo Comics | https://nadeshiko-shoten.jp | No title page found |  |
| Sunday Web Every | https://www.sunday-webry.com | No title page found |  |
| TakeComic | https://takecomic.jp | 403 Forbidden |  |
| U-NEXT | https://video.unext.jp | No title page found |  |
| WeLoveManga | https://weloma.net | No title page found |  |
| Yomonga | https://www.yomonga.com | No title page found |  |
| Young Animal | https://younganimal.com | 403 Forbidden |  |
| Young Champion | https://youngchampion.jp | 403 Forbidden |  |
| Zebrack | https://zebrack-comic.shueisha.co.jp | No title page found |  |
| Zerosum Online | https://zerosumonline.com | No title page found |  |

### Korean (5)

| Extension | Site | Reason | Rule |
|---|---|---|---|
| 11toon | https://www.11toon.com | No title page found |  |
| BlackToon | https://blacktoon426.com | No title page found |  |
| Newtoki (SBXH) | https://sbxh9.com | 403 Forbidden |  |
| Toonkor | https://toonkor0.org | No title page found |  |
| Wolf.com | https://wfwf507.com | No title page found |  |

### Portuguese (67)

| Extension | Site | Reason | Rule |
|---|---|---|---|
| Acervo Hentai 🔞 | https://acervohentai.com | 403 Forbidden |  |
| Amuy | https://apenasmaisumyaoi.com | 403 Forbidden |  |
| Animy | https://animy.net | No title page found |  |
| Apenas Uma Fã | https://apenasuma-fa.blogspot.com | No title page found |  |
| Argos Scan | https://argoscomics.online | No title page found |  |
| Arthur Scan | https://arthurscan.xyz | Cloudflare |  |
| Astratoons | https://new.astratoons.com | Cloudflare |  |
| BenDezOmniHero | https://bendezomnihero.blogspot.com | No title page found |  |
| Blackout Comics 🔞 | https://blackoutcomics.com | Cloudflare |  |
| BR Yaoi 🔞 | https://bryaoi.com | No title page found |  |
| Ego Toons | https://egotoons.com | Cloudflare |  |
| Fliptru 🔞 | https://fliptru.com.br | Cloudflare |  |
| FlowerManga.net | https://flowermangas.net | Cloudflare |  |
| Geass Comics | https://geasscomics.xyz | Cloudflare |  |
| Hentai Season 🔞 | https://hentaiseason.com | 403 Forbidden |  |
| Hentai Teca.net 🔞 | https://hentaiteca.net | 403 Forbidden |  |
| HipercooL 🔞 | https://lerhentais.com | No title page found |  |
| Hipertoon | https://hipertoon.com | 403 Forbidden |  |
| HQ Now! | https://www.hq-now.com | No title page found |  |
| Inkapk 🔞 | https://inkapk.net | Cloudflare |  |
| KuroMangas | https://kuromangas.com | 403 Forbidden |  |
| Leitor de Mangas | https://leitordemangas.com | 403 Forbidden |  |
| Leitura Manga | https://leituramanga.net | Cloudflare |  |
| Little Tyrant | https://tiraninha.world | 403 Forbidden |  |
| Lura Toon | https://luratoons.net | 403 Forbidden |  |
| Lycan Toons | https://lycantoons.com | 403 Forbidden |  |
| Maid Scan | https://empreguetes.wtf | 403 Forbidden |  |
| Manga Flix | https://mangaflix.net | 403 Forbidden |  |
| Manga Livre Blog | https://mangalivre.blog | Cloudflare |  |
| Manga NXY | https://manganyx.com | 403 Forbidden |  |
| Manga Online | https://mangaonline.green | Cloudflare |  |
| Manga Stop | https://mangastop.net | 403 Forbidden |  |
| MangaDash | https://mangadash.net | 403 Forbidden |  |
| ManGeek | https://mangeek.app | No title page found |  |
| Mango Toons | https://mangotoons.com | No title page found |  |
| Manhastro 🔞 | https://manhastro.net | Cloudflare |  |
| Mediocre Toons | https://mediocrescan.com | No title page found |  |
| MiniTwo Scan | https://minitwoscan.com | 403 Forbidden |  |
| Nexus Mangás | https://www.nexusmangas.com | Cloudflare |  |
| Nexus Toons | https://nexustoons.com | 403 Forbidden |  |
| NoxManga | https://noxmangas.org | 403 Forbidden |  |
| OneReader | https://onereader.net | No title page found |  |
| Pink Rosa | https://scanpinkrosa.blogspot.com | No title page found |  |
| Pink Sea Unicorn 🔞 | https://psunicorn.com | No title page found |  |
| Pluma Comics | https://plumacomics.cloud | No title page found |  |
| Point Zero Toons | https://kitsuneyako.com | Cloudflare |  |
| Revistas e Quadrinhos 🔞 | https://revistasequadrinhos.com | Cloudflare |  |
| RF Dragon Scan | https://rfdragonscan.net | No title page found |  |
| Risentoons | https://risentoons.xyz | No title page found |  |
| Roxinha | https://roxinha.online | Cloudflare |  |
| Sagrado Império da Britannia | https://imperiodabritannia.net | No title page found |  |
| Saikai Scan | https://housesaikai.net | 403 Forbidden |  |
| Shirai Scans | https://shiraixis.space | Cloudflare |  |
| Super Ecchi 🔞 | https://superecchi.com | No title page found |  |
| TaimuMangas | https://beta.taimumangas.com | 403 Forbidden |  |
| Taiyō | https://taiyo.moe | No title page found |  |
| Tao Sect | https://taosect.com | Cloudflare |  |
| Temaki mangás 🔞 | https://temakimangas.blogspot.com | No title page found |  |
| Tia Manhwa 🔞 | https://tiamanhwa.com | 403 Forbidden |  |
| ToonBr | https://beta.toonbr.com | No title page found |  |
| Vegitoons | https://vegitoons.black | No title page found |  |
| Verdinha | https://verdinha.wtf | No title page found |  |
| XXX Yaoi 🔞 | https://3xyaoi.com | 403 Forbidden |  |
| Yaoi Fan Club | https://yaoifanclub.com | 403 Forbidden |  |
| Yomu Comics | https://yomu.com.br | 403 Forbidden |  |
| Yomu Mangás | https://yomumangas.com | No title page found |  |
| Yuri on Air | https://yurionair.top | Cloudflare |  |

### Russian (15)

| Extension | Site | Reason | Rule |
|---|---|---|---|
| AComics | https://acomics.ru | Cloudflare |  |
| AllHentai 🔞 | https://20.allhen.online | No title page found |  |
| Com-X | https://ru.com-x.life | 403 Forbidden |  |
| HentaiLib 🔞 | https://hentailib.me | Cloudflare |  |
| MangaBuff | https://mangabuff.ru | 403 Forbidden |  |
| MangaLib | https://mangalib.me | 403 Forbidden |  |
| MangaMen | https://mangamen.com | 403 Forbidden |  |
| Nude-Moon 🔞 | https://nude-moon.org | 403 Forbidden |  |
| ReadManga | https://a.zazaza.me | No title page found |  |
| SeiManga | https://1.seimanga.me | No title page found |  |
| SelfManga | https://1.selfmanga.live | No title page found |  |
| Senkognito 🔞 | https://senkuro.me | 403 Forbidden |  |
| Senkuro | https://senkuro.me | 403 Forbidden |  |
| SlashLib | https://v2.shlib.life | No title page found |  |
| Tomilo-lib | https://tomilo-lib.ru | No title page found |  |

### Spanish (58)

| Extension | Site | Reason | Rule |
|---|---|---|---|
| BarManga | https://archiviumbar.com | 403 Forbidden |  |
| Bega Translation | https://begatranslation.com | 403 Forbidden |  |
| Bloom Scans | https://bloomscans.com | 403 Forbidden |  |
| BokugenTranslation | https://bokugents.com | 403 Forbidden |  |
| CapibaraTraductor | https://capibaratraductor.com | 403 Forbidden |  |
| Catharsis World | https://newcatharsis.dig-it.info | No title page found |  |
| Catoons 🔞 | https://cattoons.org | No title page found |  |
| ChoChoX 🔞 | https://chochox.com | 403 Forbidden |  |
| Code Arc Mangas 🔞 | https://mangas.codearctraducciones.com | No title page found |  |
| Dark Room Fansub 🔞 | https://lector-darkroomfansub.blogspot.com | No title page found |  |
| DragonTranslation.org | https://dragontranslation.org | 403 Forbidden |  |
| Emperor Scan | https://imperiomanhwa.com | 403 Forbidden |  |
| EnchiladaScan | https://enchiladascan.github.io/enchiladaweb | No title page found |  |
| EternalMangas | https://eternalmangas.org | Cloudflare |  |
| Falco Scan 🔞 | https://falcoscan.net | Cloudflare |  |
| Ikigai Mangas | https://visorikigai.gettocaboca.com | Cloudflare |  |
| InfraFandub | https://infrafandub.com | Cloudflare |  |
| InManga | https://inmanga.com | Cloudflare |  |
| Jeaz Scans | https://lectorhub.j5z.xyz | Cloudflare |  |
| Kumanga | https://www.kumanga.com | 403 Forbidden |  |
| LectorTMO (unoriginal) | https://lectortmo.vip | Cloudflare |  |
| LectorXD | https://lectorxd.com | 403 Forbidden |  |
| LeerCapitulo | https://www.leercapitulo.co | No title page found |  |
| LeerMangaEsp | https://mangalect.org | No title page found |  |
| Lmtos | https://lmtos.net | 403 Forbidden |  |
| Manga Crab | https://es.mangacrab.org | 403 Forbidden |  |
| Manga Romance | https://mangaromance19.com | 403 Forbidden |  |
| Manga TV | https://mangatv.net | Cloudflare |  |
| MangaOni | https://manga-oni.com | 403 Forbidden |  |
| Mangas No Sekai | https://mangasnosekai.com | 403 Forbidden |  |
| Mangas.in | https://m440.in | Cloudflare |  |
| MangoLibreria | https://lectorfenix.com | Cloudflare |  |
| Manhwa-Latino | https://manhwa-latino.com | 403 Forbidden |  |
| ManhwaOnline 🔞 | https://manhwa-online.com | 403 Forbidden |  |
| ManhwaWeb | https://manhwaweb.com | No title page found |  |
| Menudo-Fansub | https://www.menudo-fansub.com | No title page found |  |
| NexusScanlation 🔞 | https://nexusscanlation.com | Cloudflare |  |
| Olympus Scanlation | https://olympusxyz.com | Cloudflare |  |
| ONF MANGAS | https://onfmangas.com | Cloudflare |  |
| OrckuMangas 🔞 | https://orckumangas.com | 403 Forbidden |  |
| Plot Twist No Fansub | https://plotnofansub.com | 403 Forbidden |  |
| Ragna Scans | https://lector.ragnascan.xyz | No title page found |  |
| Ragnarok Scanlation | https://ragnarokscanlation.org | Cloudflare |  |
| Reizu Comics 🔞 | https://reizucomics.com | No title page found |  |
| Rncalation | https://rncalation.online | Cloudflare |  |
| Shadow Manga | https://shademanga.com | Cloudflare |  |
| Submanhwa 🔞 | https://submanhwa.com | Cloudflare |  |
| Taurus Fansub | https://lectortaurus.com | 403 Forbidden |  |
| TMOHentai (unoriginal) 🔞 | https://tmohentai.app | 403 Forbidden |  |
| Toon-es 🔞 | https://toon-es.com | 403 Forbidden |  |
| TopComicPorno 🔞 | https://topcomicporno.com | Cloudflare |  |
| TopComicPorno.net 🔞 | https://topcomicporno.net | 403 Forbidden |  |
| VCPVMP 🔞 | https://vercomicsporno.com | 403 Forbidden |  |
| Ver Manhwas 🔞 | https://vermanhwa.com | 403 Forbidden |  |
| Yupmanga | https://www.yupmanga.com | Cloudflare |  |
| Yuri-Online | https://yuri-online.com | Cloudflare |  |
| ZonaTMO.org (unoriginal) | https://zonatmo.org | Cloudflare |  |
| Zonatmo.to (unoriginal) | https://zonatmo.to | No title page found |  |

### Thai (19)

| Extension | Site | Reason | Rule |
|---|---|---|---|
| 1668Manga | https://1668manga.com | Cloudflare |  |
| Bully Manga | https://bully-manga.com | No title page found |  |
| Doodmanga | https://www.doodmanga.com | Cloudflare |  |
| Doujin-Lc 🔞 | https://doujin-lc.net | Cloudflare |  |
| Doujin69 🔞 | https://doujin69.com | Cloudflare |  |
| GodhMan 🔞 | https://www.godhman.net | Cloudflare |  |
| HentaiThai 🔞 | https://hentaithai.com | No title page found |  |
| HentaiThai.net 🔞 | https://hentaithai.net | Cloudflare |  |
| Manga-Lc | https://manga-lc.net | Cloudflare |  |
| MangaKimi | https://www.mangakimi.com | Cloudflare |  |
| ManhuaBug | https://www.manhuabug.com | Cloudflare |  |
| ManhuaThai | https://www.manhuathai.com | Cloudflare |  |
| ManhwaBreakup | https://www.manhwabreakup.com | Cloudflare |  |
| MikuDoujin 🔞 | https://miku-doujin.com | Cloudflare |  |
| Nekopost | https://www.nekopost.net | No title page found |  |
| Niceoppai | https://www.niceoppai.net | Cloudflare |  |
| Singmanga | https://www.sing-manga.com | Cloudflare |  |
| Sodsaime | https://www.xn--l3c0azab5a2gta.com | Cloudflare |  |
| ThaiManga | https://www.thaimanga.net | Cloudflare |  |

### Turkish (37)

| Extension | Site | Reason | Rule |
|---|---|---|---|
| ArazNovel | https://manga.araznovel.com | Cloudflare |  |
| Arcura Fansub | https://arcurafansub.com | 403 Forbidden |  |
| gafeland | https://gafeland.com | 403 Forbidden |  |
| Gaiatoon | https://gaiatoon.com | 403 Forbidden |  |
| Gölge Bahçesi | https://golgebahcesi.com | 403 Forbidden |  |
| Hattori Manga 🔞 | https://hattorimanga.net | 403 Forbidden |  |
| Hattori Scans | https://hattoriscans.com | 403 Forbidden |  |
| Hayalistic | https://hayalistic.online | 403 Forbidden |  |
| Holy Scans 🔞 | https://holyscans.com.tr | Cloudflare |  |
| Koreli Scans | https://www.nabicix.com | 403 Forbidden |  |
| Manga Bahçesi | https://mangabahcesi.com | Cloudflare |  |
| Manga Diyarı | https://mangadiyari.com | No title page found |  |
| Manga Kusu | https://mangakusu.com | 403 Forbidden |  |
| Manga Portalı | https://www.mangaportali.com | 403 Forbidden |  |
| Manga Ruhu | https://mangaruhu.com | Cloudflare |  |
| Manga-TR | https://manga-tr.com | 403 Forbidden |  |
| MangaciX | https://mangacix.net | No title page found |  |
| MangaWT | https://mangawt.com | 403 Forbidden |  |
| Mangitto 🔞 | https://mangtto.com | 403 Forbidden |  |
| Merlin Scans | https://merlintoon.com | 403 Forbidden |  |
| Mikrokosmos Fansub 🔞 | https://mikrokosmos.fans | No title page found |  |
| MilaSub | https://millascan.com | 403 Forbidden |  |
| Mono Manga | https://monomanga.com.tr | Cloudflare |  |
| Nemesis scans | https://nemesisscans.com | No title page found |  |
| Nivera Fansub | https://niverafansub.dev | 403 Forbidden |  |
| OkuToon | https://okutoon.com | 403 Forbidden |  |
| Paradox Scans | https://paradoxscans.com | 403 Forbidden |  |
| Pati Manga | https://www.patimanga.com | 403 Forbidden |  |
| Raindrop Fansub | https://www.raindropteamfan.com | No title page found |  |
| Serein Scan | https://sereinscan.com | 403 Forbidden |  |
| Siyah Melek 🔞 | https://siyahmelek.my | 403 Forbidden |  |
| Slept Manga | https://sleptmanga.com.tr | Cloudflare |  |
| Stray Fansub 🔞 | https://strayfansub.buzz | 403 Forbidden |  |
| Tarot Scans | https://www.tarotscans.com | Cloudflare |  |
| Toontaku | https://toontaku.com | No title page found |  |
| Webtoon Hatti | https://webtoonhatti.club | 403 Forbidden |  |
| Yaoi Manga Oku 🔞 | https://yaoimangaoku.net | 403 Forbidden |  |

### Ukrainian (5)

| Extension | Site | Reason | Rule |
|---|---|---|---|
| DGManga | https://dgmanga.app | Cloudflare |  |
| Faust | https://faust-web.com | Cloudflare |  |
| HoneyManga | https://honey-manga.com.ua | No title page found |  |
| MangaInUa | https://manga.in.ua | Cloudflare |  |
| Zenko | https://zenko.online | Cloudflare |  |

### Vietnamese (51)

| Extension | Site | Reason | Rule |
|---|---|---|---|
| CBHentai 🔞 | https://2tencb.pro | 403 Forbidden |  |
| CuuTruyen | https://cuutruyen.net | Cloudflare |  |
| CuuTruyen (unoriginal) | https://cuutruyen.moe | Cloudflare |  |
| DocTruyen3Q | https://doctruyen3qhub.fit | 403 Forbidden |  |
| FastScan | https://fastscan.org | 403 Forbidden |  |
| FoxTruyen | https://foxtruyen2.com | 403 Forbidden |  |
| Goc Truyen Tranh Vui | https://goctruyentranhvui41.com | 403 Forbidden |  |
| HentaiVNx 🔞 | https://www.hentaivnx.com | 403 Forbidden |  |
| HongTraTeam | https://hongtrateam.com | No title page found |  |
| Học Viện 2Ten 🔞 | https://hv2tcomics.net | No title page found |  |
| KiraKira | https://truyenkira.net | No title page found |  |
| LavibitWindroom | https://lavibitwindroomgl.fun | No title page found |  |
| LeesinComic | https://leesincomic.com | Cloudflare |  |
| LuotTruyen | https://luottruyen999.com | Cloudflare |  |
| Luvaholic | https://luvaholic.website | No title page found |  |
| LuvEvaLand | https://luvevalands2.co | 403 Forbidden |  |
| LxManga.org (unoriginal) 🔞 | https://lxmanga.org | No title page found |  |
| MangaMori | https://mangamori.dev | Cloudflare |  |
| MeDamTruyen | https://saytongtaii.site | No title page found |  |
| MeoSSS | https://meosss.com | Cloudflare |  |
| MiMi 🔞 | https://mimihentai.moe | Cloudflare |  |
| MiMiHentai 🔞 | https://mimihentai.net | 403 Forbidden |  |
| MinoTruyen | https://minotruyenv5.xyz | No title page found |  |
| MoeTruyen | https://moetruyen.net | 403 Forbidden |  |
| NetTruyenCO (unoriginal) | https://nettruyenar.com | 403 Forbidden |  |
| NetTruyenViet (unoriginal) | https://nettruyenviet10.com | 403 Forbidden |  |
| NetTruyenX (unoriginal) | https://nettruyenx.net | 403 Forbidden |  |
| NhatTruyen | https://nhattruyenqq.com | 403 Forbidden |  |
| Otakusic | https://otakusic.com | Cloudflare |  |
| OTruyen | https://otruyen.cc | No title page found |  |
| Panomic | https://panomic.online | 403 Forbidden |  |
| QuaDaoCute | https://qadcuteo.cc | Cloudflare |  |
| Roads Team 🔞 | https://nhaduong.com | Cloudflare |  |
| SayHentai 🔞 | https://sayhentai.cx | Cloudflare |  |
| Seikowo | https://seikowo-app.blogspot.com | No title page found |  |
| SinhSieuSao 🔞 | https://sinhsieusao.com | No title page found |  |
| SoaiCaComic | https://soaicacomic2.top | No title page found |  |
| SuicaoDex | https://suicaodex.com | Cloudflare |  |
| Team Lanh Lung | https://lanhlungteam3.top | No title page found |  |
| Thỏ Ham Ngủ | https://thohamngu.xyz | No title page found |  |
| Top Truyen | https://www.toptruyenzone13.com | 403 Forbidden |  |
| Truyen tranh dam my 🔞 | https://truyentranhdammyy.site | Cloudflare |  |
| TruyenGGVN | https://truyenggvn.com | 403 Forbidden |  |
| TruyenHentaivn 🔞 | https://truyenhentaivn.store | No title page found |  |
| TruyenHentaiz 🔞 | https://truyenhentaiz.net | Cloudflare |  |
| TruyenQQ | https://truyenqqko.com | 403 Forbidden |  |
| TruyenQQ VN | https://truyenqq.com.vn | 403 Forbidden |  |
| ViHentai 🔞 | https://vi-hentai.moe | Cloudflare |  |
| ViTruyen | https://vitruyen1.com | No title page found |  |
| YuriGarden | https://yurigarden.moe | Cloudflare |  |
| YuriNeko | https://yurinekoz.com | Cloudflare |  |
