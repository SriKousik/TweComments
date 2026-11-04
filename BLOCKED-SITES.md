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

Every extension whose site the survey couldn't read (814): behind a Cloudflare check, refusing scripts (403), or with no title page the survey could find from the home page. Check them in Twe, or collect a report for them (section 2). ✅ marks the ones that have a rule since.

| Reason | Count |
|---|---|
| No title page found | 299 |
| Cloudflare | 284 |
| 403 Forbidden | 231 |

### English (189)

| Extension | Site | Reason | Rule |
|---|---|---|---|
| 1Manga.co | https://1manga.co | Cloudflare |  |
| 8Muses 🔞 | https://comics.8muses.com | No title page found |  |
| AllManga | https://mkissa.to | No title page found |  |
| AllPornComic 🔞 | https://allporncomic.com | Cloudflare |  |
| Alpha Manga | https://www.alpha-manga.com | No title page found |  |
| Arc-Relight | https://arc-relight.com | No title page found |  |
| Arknights Comics | https://arknights.global | No title page found |  |
| Athrea Scans | https://athreascans.com | Cloudflare |  |
| Atsumaru | https://atsu.moe | No title page found |  |
| Bakkin | https://bakkin.moe/reader/ | No title page found |  |
| BatCave | https://batcave.biz | 403 Forbidden |  |
| Bbato | https://bato1.com | No title page found |  |
| BookWalker | https://bookwalker.com | Cloudflare |  |
| Borat Scans | https://boratscans.com | 403 Forbidden |  |
| BrainRotComics | https://brainrotcomics.com | 403 Forbidden |  |
| CartoonPorn 🔞 | https://cartoonporn.to | Cloudflare |  |
| Clone Manga | https://manga.clone-army.org | No title page found |  |
| CManhua | https://cmanhua.com | Cloudflare |  |
| Cocomic | https://cocomic.co | Cloudflare |  |
| Collected Curios | https://www.collectedcurios.com | No title page found |  |
| Comic Asura | https://comicasura.net | No title page found |  |
| ComicHubFree | https://comichubfree.com | Cloudflare |  |
| ComicLand | https://comicland.org | No title page found |  |
| Comix | https://comix.to | Cloudflare |  |
| Coolmic | https://coolmic.me | No title page found |  |
| Cutie Comics 🔞 | https://cutiecomics.com | Cloudflare |  |
| Cyanide & Happiness | https://explosm.net | No title page found |  |
| Dark Legacy Comics | https://www.darklegacycomics.com | No title page found |  |
| Darths & Droids | https://www.darthsanddroids.net | No title page found |  |
| Digital Comic Museum | https://digitalcomicmuseum.com | 403 Forbidden |  |
| Diva Scans | https://divascans.org | Cloudflare |  |
| Doujin.io - J18 🔞 | https://doujin.io | No title page found |  |
| DragonTea | https://dragontea.ink | 403 Forbidden |  |
| Eggporncomics 🔞 | https://eggporncomics.com | Cloudflare |  |
| Elan School | https://elan.school | No title page found |  |
| emaqi | https://emaqi.com | No title page found |  |
| Eris Scans | https://erisscans.com | Cloudflare |  |
| Ero18x 🔞 | https://ero18x.com | 403 Forbidden |  |
| Erofus 🔞 | https://www.erofus.com | Cloudflare |  |
| Flame Comics | https://flamecomics.xyz | Cloudflare |  |
| GEDE Comix 🔞 | https://gedecomix.com | Cloudflare |  |
| GingeRTooN 🔞 | https://gingertoon.com | No title page found |  |
| GirlsTop 🔞 | https://en.girlstop.info | No title page found |  |
| Goda | https://manhuascans.org | Cloudflare |  |
| Gourmet Scans | https://gourmetsupremacy.com | Cloudflare |  |
| Gunnerkrigg Court | https://www.gunnerkrigg.com | No title page found |  |
| Hades Scans | https://hadesscans.com | No title page found |  |
| Hentai4Free 🔞 | https://hentai4free.net | Cloudflare |  |
| HentaiFC 🔞 | https://hentaifc.com | No title page found |  |
| HentaiHere 🔞 | https://hentaihere.com | No title page found |  |
| HentaiKun 🔞 | https://hentaikun.com | No title page found |  |
| HentaiNexus 🔞 | https://hentainexus.com | No title page found |  |
| HentaiRead 🔞 | https://hentairead.com | 403 Forbidden |  |
| HentaiSco 🔞 | https://hentaisco.cc | No title page found |  |
| HentaiTnT 🔞 | https://hentaitnt.net | No title page found |  |
| Hiperdex | https://hiperdex.tv | No title page found |  |
| Hive Scans | https://hivetoons.org | Cloudflare |  |
| HotComics 🔞 | https://hotcomics.io | 403 Forbidden |  |
| ILikeComix 🔞 | https://ilikecomix.com | Cloudflare |  |
| InfinityScans | https://infinityscans.org | Cloudflare |  |
| J-Novel | https://j-novel.club | Cloudflare |  |
| Kaizen Scan 🔞 | https://kaizenscan.com | 403 Forbidden |  |
| Kappa Beast | https://kappabeast.com | No title page found |  |
| KingComiX 🔞 | https://kingcomix.com | Cloudflare |  |
| Kissmanga.in | https://kissmanga.in | 403 Forbidden |  |
| Komix | https://komix.to | Cloudflare |  |
| Lagoon Scans | https://lagoonscans.com | Cloudflare |  |
| Leslie&Victims | https://leslie-victims.pages.dev | No title page found |  |
| Lgbtics 🔞 | https://lgbtics.com | 403 Forbidden |  |
| LHTranslation | https://lhtranslation.net | Cloudflare |  |
| Lily Manga | https://lilymanga.net | No title page found |  |
| LinkManga | https://linkmanga.com | Cloudflare |  |
| Loading Artist | https://loadingartist.com | No title page found |  |
| LoLoBun | https://www.lolobun.com | No title page found |  |
| Lua Scans | https://luacomic.org | Cloudflare |  |
| Luminare Translations | https://luminaretranslations.com | Cloudflare |  |
| Luna Toons | https://lunatoons.net | 403 Forbidden |  |
| MadaraDex | https://madaradex.org | Cloudflare |  |
| Magus Manga | https://magustoon.org | 403 Forbidden |  |
| Manga 18x 🔞 | https://manga18x.net | Cloudflare |  |
| Manga Demon | https://demonicscans.org | Cloudflare |  |
| Manga Drama 🔞 | https://mangadrama.com | Cloudflare |  |
| Manga-Bay | https://manga-bay.biz | 403 Forbidden |  |
| Manga.uno | https://manga.uno | Cloudflare |  |
| MangaCloud | https://mangacloud.org | Cloudflare |  |
| MangaDE | https://mangade.io | No title page found |  |
| MangaDot | https://mangadot.net | 403 Forbidden |  |
| MangaFox.fun | https://mangafox.fun | Cloudflare |  |
| MangaHere.onl | https://mangahere.onl | Cloudflare |  |
| MangaHub | https://mangahub.io | Cloudflare |  |
| MangaK | https://mangak.io | No title page found |  |
| Mangakakalot.fun | https://mangakakalot.fun | Cloudflare |  |
| MangaLix | https://mangalix.com | No title page found |  |
| MangaMelon | https://mangamelon.com | Cloudflare |  |
| MangaNel | https://manganel.me | Cloudflare |  |
| MangaNow | https://manganow.to | No title page found |  |
| MangaOnline.fun | https://mangaonline.fun | Cloudflare |  |
| MangaOwl.io (unoriginal) | https://mangaowl.io | Cloudflare |  |
| MangaPanda.onl | https://mangapanda.onl | Cloudflare |  |
| MangaPark.tv (unoriginal) 🔞 | https://mangapark.tv | Cloudflare |  |
| MangaReader.site | https://mangareader.site | Cloudflare |  |
| MangaToday | https://mangatoday.fun | Cloudflare |  |
| Manhua Plus | https://manhuaplus.com | Cloudflare |  |
| ManhuaHot | https://manhuahot.com | Cloudflare |  |
| ManhuaTop | https://manhuatop.org | Cloudflare |  |
| ManhuaUS | https://manhuaus.com | 403 Forbidden |  |
| Manhwa Comics 🔞 | https://manhwacomics.com | No title page found |  |
| Manhwa Reads | https://manhwareads.com | Cloudflare |  |
| Manhwa18.today 🔞 | https://www.manhwa18.today | 403 Forbidden |  |
| Manhwa68 🔞 | https://manhwa68.com | Cloudflare |  |
| Manhwalike 🔞 | https://manhwalike.com | No title page found |  |
| ManhwaRead | https://manhwaread.com | 403 Forbidden |  |
| Manhwatop | https://manhwatop.com | Cloudflare |  |
| ManhwaZone | https://manhwazone.com | No title page found |  |
| Megatokyo | https://megatokyo.com | No title page found |  |
| MeiToon | https://meitoon.org | 403 Forbidden |  |
| Milftoon 🔞 | https://milftoon.xxx | Cloudflare |  |
| MLBB Lore | https://play.mobilelegends.com | No title page found |  |
| Monochrome Custom | https://monochromecms.netlify.app | No title page found |  |
| Monochrome Scans | https://manga.d34d.one | No title page found |  |
| MyAdultComics 🔞 | https://myadultcomics.com | No title page found |  |
| MyHentaiComics 🔞 | https://myhentaicomics.com | Cloudflare |  |
| MyHentaiGallery 🔞 | https://myhentaigallery.com | Cloudflare |  |
| NineHentai 🔞 | https://9hentai.so | No title page found |  |
| Nortverse 🔞 | https://nortverse.com | 403 Forbidden |  |
| NovelCrow 🔞 | https://novelcrow.com | 403 Forbidden |  |
| Oglaf 🔞 | https://www.oglaf.com | No title page found |  |
| OneManga.info | https://onemanga.info | Cloudflare |  |
| Only The Best Hentai 🔞 | https://onlythebesthentai.com | Cloudflare |  |
| oots | https://www.giantitp.com | 403 Forbidden |  |
| Patch Friday | https://patchfriday.com | No title page found |  |
| Philia Scans | https://philiascans.org | Cloudflare |  |
| PornComix 🔞 | https://bestporncomix.com | Cloudflare |  |
| PornhwaDB Reader 🔞 | https://pornhwareader.com | Cloudflare |  |
| Pornhwaz 🔞 | https://www.pornhwaz.com | Cloudflare |  |
| Questionable Content | https://www.questionablecontent.net | No title page found |  |
| Rage Scans | https://ragescans.com | 403 Forbidden |  |
| Raven Scans | https://ravenscans.org | 403 Forbidden |  |
| Read Berserk Manga | https://readberserk.com | Cloudflare |  |
| Read Chainsaw Man Manga Online 🔞 | https://ww6.readchainsawman.com | Cloudflare |  |
| Read Comics Online | https://readcomicsonline.ru | 403 Forbidden |  |
| Read Fairy Tail & Edens Zero Manga Online | https://ww9.readfairytail.com | Cloudflare |  |
| Read Kingdom Manga Online | https://ww6.readkingdom.com | Cloudflare |  |
| Real Life Comics | https://reallifecomics.com | No title page found |  |
| Renascans | https://renascans.net | Cloudflare |  |
| Revival Scans 🔞 | https://www.revivalscans.com | Cloudflare |  |
| Rolia Scan | https://roliascan.com | No title page found |  |
| Rose Squad Scans 🔞 | https://rosesquadscans.aishiteru.org | No title page found |  |
| S2Manga | https://s2read.com | Cloudflare |  |
| Sabrina Online | https://www.sabrina-online.com | No title page found |  |
| SACACHISPA | https://sacachispa.site | No title page found |  |
| ScansGG | https://scans.gg | Cloudflare |  |
| Scythe Scans | https://scythescans.com | Cloudflare |  |
| Setsu Scans | https://setsuscans.com | 403 Forbidden |  |
| SilentQuill | https://silentquill.net | Cloudflare |  |
| Snafu Comics | https://www.snafu-comics.com | No title page found |  |
| Solar and Sundry | https://sas-api.fly.dev | No title page found |  |
| SpyFakku 🔞 | https://hentalk.pw | Cloudflare |  |
| Sunshine Butterfly Scans 🔞 | https://wings.sbs | No title page found |  |
| SUPER MEGA | https://www.supermegacomics.com | No title page found |  |
| Team Shadowi | https://www.team-shadowi.com | 403 Forbidden |  |
| Temple Scan 🔞 | https://templetoons.com | Cloudflare |  |
| The Blank 🔞 | https://theblank.net | 403 Forbidden |  |
| The Property of Hate | https://jolleycomics.com | No title page found |  |
| ToonHey 🔞 | https://toonhey.com | 403 Forbidden |  |
| Toonily | https://toonily.com | Cloudflare |  |
| Toonily.me 🔞 | https://toontop.io | No title page found |  |
| Toonkotsu | https://toonkotsu.com | Cloudflare |  |
| TopManhua.net | https://topmanhua.net | Cloudflare |  |
| Tower Of God Manga Online | https://w82.thetowerofgod.com | Cloudflare |  |
| Valir Scans | https://valirscans.org | Cloudflare |  |
| vgperson | https://vgperson.com | No title page found |  |
| Vision Haze | https://www.visionhaze.com | 403 Forbidden |  |
| VIZ | https://www.viz.com | No title page found |  |
| Voyce.Me | https://www.voyce.me | No title page found |  |
| VyvyManga | https://mangavyvy.net | 403 Forbidden |  |
| War For Rayuba | https://xrabohrok.github.io/WarMap/#/ | No title page found |  |
| Webdex Scans | https://webdexscans.com | Cloudflare |  |
| WebNovel | https://www.webnovel.com | Cloudflare |  |
| WebtoonLib | https://webtoonlib.to | Cloudflare |  |
| WebtoonXYZ | https://www.webtoon.xyz | 403 Forbidden |  |
| Wildtoon 🔞 | https://wildtoon.com | 403 Forbidden |  |
| WuxiaWorld | https://wuxiaworld.site | Cloudflare |  |
| XlecX 🔞 | https://xlecx.one | No title page found |  |
| XoManga | https://www.xomanga.site | 403 Forbidden |  |
| XOXO Comics | https://xoxocomic.com | Cloudflare |  |
| YakshaComics | https://yakshacomics.com | Cloudflare |  |
| YaoiScan | https://yaoiscan.com | 403 Forbidden |  |
| Zinmanga | https://mangazin.org | Cloudflare |  |

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
