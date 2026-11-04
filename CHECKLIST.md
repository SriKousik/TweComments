# Comment support checklist

Every extension in keiyoushi's repository (1458), surveyed for its site's comment system.
Each site was opened once (home page, then one title page) and checked for known comment systems.
Rows marked by hand were tested in a browser; update them here when something is confirmed or changes.

| Status | Count | Meaning |
|---|---|---|
| ✅ Complete | 14 | Rule written and checked by hand for everything it supports. |
| 🟢 Works | 199 | Reading works (checked, or through a comment system Twe reads on any site). Liking and posting need a signed-in check. |
| 🔍 Needs rule | 158 | The site has comments, but in a form Twe needs a rule for. |
| ⚠️ Unsupported | 13 | Facebook comments: only shown inside Facebook's frame. Twe offers WebView. |
| 🛡️ Check in app | 583 | The site blocks scripts (Cloudflare), so this survey couldn't see it. Open Comments in Twe to check. |
| ➖ No comments | 178 | No comment section found on the site. |
| ❌ Site down | 313 | The site didn't answer, or the extension has no site. |

Feature columns: ✅ works · ⏳ written, needs a signed-in check · — not available.

## ✅ Complete (14)

| Extension | Lang | Comments | Rule | Read | Replies | Like | Comment / reply | Sign-in | Notes |
|---|---|---|---|---|---|---|---|---|---|
| Comic Fury | all | Own (in page) | comicfury | ✅ | — | — | — | - | comments in the page |
| MangaDex | all | Forum | mangadex | ✅ | — | — | — | - | forum threads via MangaDex API; quotes inline |
| SayManhwa | all | Own (in page) | saymanhwa | ✅ | — | — | — | - | comments in the page |
| Aethon Webcomics | en | ModFarm (WordPress) | aethon | ✅ | — | — | — | - | comments read from its API/page |
| Aqua Manga | en | Manga Comments Pro | global: manga-comments-pro | ✅ | ✅ | — | — | - | 1 comment read |
| Asmodeus Scans | en | zmio | zmio | ✅ | ✅ | — | — | - | zmio API; 2 comments read on a sample |
| Asura Scans | en | Own API | asura | ✅ | ✅ | — | — | - | 331 title / 323 chapter comments, paging, GIFs |
| MangaKatana | en | Own API | mangakatana | ✅ | ✅ | — | — | - | 71 comments read |
| O Translations | en | Koe comments | otranslations | ✅ | ✅ | — | — | - | 5 comments read |
| RitharScans | en | Livewire discussion | global: livewire-discussion | ✅ | — | — | — | - | 10 comments read |
| Swords Comic | en | Discourse | global: discourse | ✅ | — | — | — | - | embed read with the comic as referer |
| Violet Scans | en | Manga Comments System | global: mcs | ✅ | ✅ | — | — | - | 17 comments on a sample |
| Weeb Central | en | Own | weebcentral | ✅ | — | — | — | - | title and chapter |
| YaoiScan (Unoriginal) | en | Article comments | global: comment-body-articles | ✅ | — | — | — | - | posting needs a guest name (not in Twe yet) |

## 🟢 Works (199)

| Extension | Lang | Comments | Rule | Read | Replies | Like | Comment / reply | Sign-in | Notes |
|---|---|---|---|---|---|---|---|---|---|
| Manga Omega | all | wpDiscuz | global: wpdiscuz | ✅ | ✅ | ⏳ | ⏳ | WordPress | recognised on the page |
| Sandra and Woo | all | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| Vinne Veritas - CCC | all | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| 3asq | ar | wpDiscuz | global: wpdiscuz | ✅ | ✅ | ⏳ | ⏳ | WordPress | recognised on the page |
| ArbxComix 🔞 | ar | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| Comic Verse | ar | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| Loner Translations | ar | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| Manga Ai Land | ar | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| MangaHub 🔞 | ar | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| Manhatok | ar | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| Niji Translations | ar | wpDiscuz | global: wpdiscuz | ✅ | ✅ | ⏳ | ⏳ | WordPress | recognised on the page |
| Orca Manga | ar | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| Yokai | ar | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| Yona Bar 🔞 | ar | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| Yuri Moon Sub 🔞 | ar | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| 18 Porn Comic 🔞 | en | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| Akaza Scans | en | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| AP Comics 🔞 | en | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| Art Lapsa | en | Livewire discussion | global: livewire-discussion | ✅ | — | — | — | - | same platform as RitharScans |
| Aster Scans | en | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| aurora | en | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| Bun Manga | en | wpDiscuz | global: wpdiscuz | ✅ | ✅ | ⏳ | ⏳ | WordPress | recognised on the page |
| buttsmithy 🔞 | en | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| Clown Corps | en | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| Cucumber Manga 🔞 | en | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| Decadence Scans | en | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| GakaMangas | en | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| GalaxyDegenScans | en | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| Genz Toons | en | zmio | zmio | ✅ | ✅ | — | — | - | found on a second check |
| Grim Scans | en | zmio | zmio | ✅ | ✅ | — | — | - | found on a second check |
| Grrl Power Comic | en | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| Hentai1.io 🔞 | en | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| Hentai20 (Unoriginal) 🔞 | en | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| Hentai3z.CC 🔞 | en | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| HentaiRead.io 🔞 | en | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| Hijala Scans | en | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| Hyakuro Translations | en | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| I'm An Evil God | en | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| Jinmangas | en | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| Kaiji Manga Online | en | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| Ken Scans | en | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| Kewn Scans | en | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| King of Shojo | en | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| Kitsune Dawn 🔞 | en | Livewire discussion | global: livewire-discussion | ✅ | — | — | — | - | same platform as RitharScans |
| KokoMangas | en | wpDiscuz | global: wpdiscuz | ✅ | ✅ | ⏳ | ⏳ | WordPress | recognised on the page |
| KSGroupScans | en | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| Kun Manga Online | en | QQ Comment Service | qq-comments | ✅ | ✅ | ⏳ | ⏳ | Site | API answers |
| Lovesjane Scans | en | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| Manga Dass | en | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| Manga District | en | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| Manga Eclipse | en | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| Manga Trend | en | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| Mangabat | en | QQ Comment Service | qq-comments | ✅ | ✅ | ⏳ | ⏳ | Site | API read; like/reply written |
| Mangack | en | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| Mangafree 🔞 | en | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| MangaGeko | en | Own API | mangageko | ✅ | ✅ | ⏳ | ⏳ | Site | title and chapter comments read; actions need sign-in to confirm |
| MangaGG | en | wpDiscuz | global: wpdiscuz | ✅ | ✅ | ⏳ | ⏳ | WordPress | recognised on the page |
| Mangakakalot | en | QQ Comment Service | qq-comments | ✅ | ✅ | ⏳ | ⏳ | Site | API answers |
| MangaManiacs 🔞 | en | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| MangaRead.org | en | wpDiscuz | madara-wpdiscuz | ✅ | ✅ | ⏳ | ⏳ | WordPress | 886 title / 436 chapter comments read; View replies checked |
| Mangasushi | en | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| Mangatown | en | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| ManhuaPlus (Unoriginal) | en | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| Manhwa Toon | en | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| ManhwaBuddy | en | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| ManhwaNex | en | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| Mehgazone 🔞 | en | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| Mist Scans | en | zmio | zmio | ✅ | ✅ | — | — | - | found on a second check |
| Multporn 🔞 | en | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| MurimScan | en | Blogger | global: blogger | ✅ | — | — | — | - | found on a second check |
| Nux Scans | en | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| Nyanu Kafe | en | zmio | zmio | ✅ | ✅ | — | — | - | found on a second check |
| Nyx Scans | en | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| OctopusManga 🔞 | en | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| Omega Scans 🔞 | en | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| Orion Scans | en | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| Rackus | en | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| Randowiz | en | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| Read Maid Sama Manga Online | en | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| Read The Beginning After The End Manga Online | en | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| Read The Exiled Heavy Knight Manga Online | en | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| ReadManga18 🔞 | en | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| Rinko Comics | en | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| Rizz Comic | en | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| RokariComics | en | wpDiscuz | global: wpdiscuz | ✅ | ✅ | ⏳ | ⏳ | WordPress | recognised on the page |
| Ruby Comics 🔞 | en | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| RuriDragon Manga Online | en | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| Sana Scans | en | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| Siren Scans | en | zmio | zmio | ✅ | ✅ | — | — | - | same zmio setup as Asmodeus |
| Sleepy Translations | en | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| TCB Scans | en | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| Thunder Scans | en | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| TimelessToons | en | zmio | zmio | ✅ | ✅ | — | — | - | found on a second check |
| Top Manhua | en | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| TritiniaScans | en | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| Vixen Logic 🔞 | en | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| Vortex Scans | en | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| Writer Scans | en | zmio | zmio | ✅ | ✅ | — | — | - | found on a second check |
| YaoiHot 🔞 | en | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| Zinmanga.net | en | QQ Comment Service | qq-comments | ✅ | ✅ | ⏳ | ⏳ | Site | API answers |
| Cerberus Series | es | wpDiscuz | global: wpdiscuz | ✅ | ✅ | ⏳ | ⏳ | WordPress | recognised on the page |
| Dat-Gar Scan | es | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| DoujinsHell 🔞 | es | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| HeavenManga | es | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| Inventario Oculto | es | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| Kazoku Den | es | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| LectorJPG | es | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| Monopoly Scan | es | wpDiscuz | global: wpdiscuz | ✅ | ✅ | ⏳ | ⏳ | WordPress | recognised on the page |
| NekoScans | es | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| Rakuen Translations | es | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| RavenManga | es | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| RichtoScan | es | wpDiscuz | global: wpdiscuz | ✅ | ✅ | ⏳ | ⏳ | WordPress | recognised on the page |
| Temple Scan 🔞 | es | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| Uchuujin Projects | es | wpDiscuz | global: wpdiscuz | ✅ | ✅ | ⏳ | ⏳ | WordPress | recognised on the page |
| UnderTranslations | es | wpDiscuz | global: wpdiscuz | ✅ | ✅ | ⏳ | ⏳ | WordPress | recognised on the page |
| Hentai-Scantrad 🔞 | fr | wpDiscuz | global: wpdiscuz | ✅ | ✅ | ⏳ | ⏳ | WordPress | recognised on the page |
| Scantrad Union | fr | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| Sushiscan.fr | fr | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| Aarlas | id | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| Astral Scans 🔞 | id | wpDiscuz | global: wpdiscuz | ✅ | ✅ | ⏳ | ⏳ | WordPress | recognised on the page |
| Dojing.net 🔞 | id | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| IsekaiKomik | id | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| Izanami Scans | id | wpDiscuz | global: wpdiscuz | ✅ | ✅ | ⏳ | ⏳ | WordPress | recognised on the page |
| Kanzenin 🔞 | id | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| Kombatch 🔞 | id | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| Komik Next G Online | id | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| Komiktap 🔞 | id | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| KumaPoi 🔞 | id | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| Maid - Manga | id | wpDiscuz | global: wpdiscuz | ✅ | ✅ | ⏳ | ⏳ | WordPress | recognised on the page |
| Mangasusu 🔞 | id | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| Manhwa List | id | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| Mihentai 🔞 | id | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| MirrorKomik | id | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| NgamenKomik | id | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| Noromax | id | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| Ota Scans | id | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| ReYume | id | Blogger | global: blogger | ✅ | — | — | — | - | found on a second check |
| Rosyscans | id | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| Sekte Doujin 🔞 | id | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| Sekte Komik | id | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| ShiyuraSub | id | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| Tooncubus 🔞 | id | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| AnimeShinigami | it | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| Shinobi Scans | it | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| Raw1001 | ja | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| AnimeXNovel | pt | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| Boruto Explorer | pt | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| Brasil Hentai 🔞 | pt | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| Café com Yaoi | pt | wpDiscuz | global: wpdiscuz | ✅ | ✅ | ⏳ | ⏳ | WordPress | recognised on the page |
| Coven Scan 🔞 | pt | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| Euphoria Scan 🔞 | pt | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| GALAX Scans | pt | Blogger | global: blogger | ✅ | — | — | — | - | found on a second check |
| Hanmokku Scan | pt | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| Hentai Comics 🔞 | pt | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| Hentai Kai 🔞 | pt | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| Hot Cabaret Scan | pt | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| Kami Sama Explorer | pt | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| Ler 999 | pt | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| Manga Livre.to | pt | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| Nebulosa Scan | pt | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| Ninja Scan | pt | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| Nocturne Summer | pt | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| Traduções do Lipe | pt | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| Tsundoku Traduções | pt | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| Doujin Moon 🔞 | th | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| DoujinZa 🔞 | th | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| Ecchi-Doujin 🔞 | th | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| Fin Manga | th | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| Go Manga | th | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| Manga-Neko | th | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| NTR-Manga 🔞 | th | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| Amanga Planet | tr | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| DiamondFansub | tr | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| GhosToon | tr | wpDiscuz | global: wpdiscuz | ✅ | ✅ | ⏳ | ⏳ | WordPress | recognised on the page |
| KazeScans | tr | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| Koreli Manga | tr | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| Kuroi Manga 🔞 | tr | wpDiscuz | global: wpdiscuz | ✅ | ✅ | ⏳ | ⏳ | WordPress | recognised on the page |
| Lavinia Fansub 🔞 | tr | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| Luna Scans 🔞 | tr | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| MangaWOW | tr | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| Moon Daisy Scans 🔞 | tr | wpDiscuz | global: wpdiscuz | ✅ | ✅ | ⏳ | ⏳ | WordPress | recognised on the page |
| Ori Manga | tr | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| Ragnar Scans | tr | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| Shadow Çeviri | tr | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| Shijie Scans | tr | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| TonizuToon | tr | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| Türkçe Manga Oku | tr | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| Webtoonia 🔞 | tr | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| Zenith Scans | tr | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |
| Mangarama | uk | wpDiscuz | global: wpdiscuz | ✅ | ✅ | ⏳ | ⏳ | WordPress | recognised on the page |
| Dilib | vi | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| DocTruyen5s | vi | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| Jelly Comics 🔞 | vi | wpDiscuz | global: wpdiscuz | ✅ | ✅ | ⏳ | ⏳ | WordPress | recognised on the page |
| TeleTruyen | vi | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| TruyenTini | vi | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| TruyenTuoiTho | vi | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| TuSachXinhXinh | vi | WordPress | global: wordpress | ✅ | ✅ | — | — | - | recognised on the page |
| ZetTruyen | vi | QQ Comment Service | qq-comments | ✅ | ✅ | ⏳ | ⏳ | Site | found on a second check |
| HANMAN18 🔞 | zh | Disqus | global: disqus | ✅ | ✅ | — | — | - | recognised on the page |

## 🔍 Needs rule (158)

| Extension | Lang | Site | Template | Notes |
|---|---|---|---|---|
| AllPornComics.co 🔞 | all | https://allporncomics.co | Madara | Own: 14 mentions of "comment" |
| Comics Valley 🔞 | all | https://comicsvalley.com | Madara | Own: 11 mentions of "comment" |
| DeviantArt | all | https://www.deviantart.com |  | Own: 382 mentions of "comment" |
| e621 🔞 | all | https://e621.net |  | Own: /comments |
| Everia.club 🔞 | all | https://everia.club |  | Own: 15 mentions of "comment" |
| Manga Draft | all | https://www.mangadraft.com |  | Own: 8 mentions of "comment" |
| Manga UP! | all | https://global.manga-up.com | Next.js | Own: 1550 mentions of "comment" |
| Manga18Me 🔞 | all | https://manga18.me |  | Own: Checked: same /api/comment platform as ManhwaOnline (unconfirmed) |
| MangaDNA | all | https://mangadna.com | MangaThemesia | Own: Checked: same /api/comment platform as ManhwaOnline (unconfirmed) |
| MangaForFree.net 🔞 | all | https://mangaforfree.net | Madara | Own: 11 mentions of "comment" |
| ManhwaClub.net 🔞 | all | https://manhwaclub.net | Madara | Own: 16 mentions of "comment" |
| Miau Scan | all | https://leemiau.com | MangaThemesia | Own: 63 mentions of "comment" |
| MissKon 🔞 | all | https://misskon.com |  | Own: 8 mentions of "comment" |
| NamiComi | all | https://namicomi.com | Iken | Own: 28 mentions of "comment" |
| PornPics 🔞 | all | https://www.pornpics.com |  | Own: /comments/ |
| SeraphicDeviltry 🔞 | all | https://seraphic-deviltry.com | Madara | Own: 110 mentions of "comment" |
| Tappytoon | all | https://www.tappytoon.com/en | Next.js | Own: 70 mentions of "comment" |
| AR Hentai 🔞 | ar | https://arhentai.net | Madara | Own: 12 mentions of "comment" |
| AsgardScans | ar | https://asgardscans.com |  | Own: /assets/CommentsSection-BTCDjoFu.js, /assets/comment-banners-CtP_gVp5.js |
| Azora | ar | https://azorafly.com |  | Own: 18 mentions of "comment" |
| Hentai Lek 🔞 | ar | https://hentailek.com |  | Own: 21 mentions of "comment" |
| Manga Tales | ar | https://www.mangatales.com |  | Own: /comments |
| Mangalek | ar | https://mangalik.net | Madara | Own: 17 mentions of "comment" |
| MangaTuk | ar | https://mangatuk.com | Next.js | Commento:  |
| ProComic | ar | https://procomic.pro | Madara | Own: 67 mentions of "comment" |
| Rocks Manga | ar | https://rocksmanga.com | Madara | Own: 9 mentions of "comment" |
| 4PornComic 🔞 | en | https://4porncomic.com |  | Own: Checked: Article comments platform (global rule); none on the sampled title |
| AllPornComic.io 🔞 | en | https://allporncomic.io | Madara | Own: 13 mentions of "comment" |
| Arena Scans | en | https://arenascan.com | MangaThemesia | Own: 8 mentions of "comment" |
| Coffee Manga (Unoriginal) | en | https://coffeemanga.net | Liliana | Own: Checked: Comments behind a sign-in gate |
| Comivex | en | https://comivex.com |  | Commento: Checked: Loaded by script |
| Doujins 🔞 | en | https://doujins.com |  | Own: /comments, /comments/antispam, /comments?post_id=8488 |
| Dynasty Scans | en | https://dynasty-scans.com |  | Own: /forum/topics/915-sweet-little-devil-series-discussion |
| Eva Scans | en | https://evascans.net | MangaThemesia | Own: 69 mentions of "comment" |
| Gensura 🔞 | en | https://gensura.net |  | Own: /static/comments/css/custom.02958b3eb9b0.css |
| Hentai Desi 🔞 | en | https://hentaidesi.com | MangaThemesia | Own: 8 mentions of "comment" |
| HentaiXComic 🔞 | en | https://hentaixcomic.com | Madara | Own: 11 mentions of "comment" |
| HentaiXDickgirl 🔞 | en | https://hentaixdickgirl.com | Madara | Own: 15 mentions of "comment" |
| HentaiXYuri 🔞 | en | https://hentaixyuri.com | Madara | Own: 13 mentions of "comment" |
| HM2D 🔞 | en | https://doujindistrict.com | Madara | Own: 28 mentions of "comment" |
| Hunlight Comics | en | https://hunlightcomics.com | Madara | Own: 8 mentions of "comment" |
| INKR | en | https://comics.inkr.com | Next.js | Own: 35 mentions of "comment" |
| K Manga | en | https://kmanga.kodansha.com |  | Own: 20 mentions of "comment" |
| KaliScans.org (unoriginal) | en | https://kaliscans.org |  | Own: Checked: Loaded by script (getComments) |
| Kensscan | en | https://kensscan.com | Madara | Own: Checked: Own WordPress plugin (kensscan-comments); no comments on sampled titles to read its markup |
| Madara Scans | en | https://madarascans.net | Madara | Own: 69 mentions of "comment" |
| Manga18.Club 🔞 | en | https://manga18.club |  | Own: Checked: /api/comments (unconfirmed) |
| Manga18Free 🔞 | en | https://manga18free.com | Madara | Own: 16 mentions of "comment" |
| Mangaforfree.com 🔞 | en | https://mangaforfree.com | Madara | Own: 16 mentions of "comment" |
| Manhuanext | en | https://manhuanext.com | Madara | Own: 25 mentions of "comment" |
| ManhwaDen 🔞 | en | https://www.manhwaden.com | Madara | Own: 26 mentions of "comment" |
| ManhwaHub.to 🔞 | en | https://manhwahub.to | Madara | Own: 12 mentions of "comment" |
| ManhwaOnline | en | https://manhwaonline.org |  | Own: Checked: Article comments platform (global rule); none on the sampled title |
| ManhwaZ | en | https://manhwaz.cc | Iken | Own: Checked: Astro CommentPanel with a private /api/v1 |
| Mgread.io | en | https://mgread.io | Madara | Commento:  |
| MyReadingComic 🔞 | en | https://myreadingcomic.com |  | Own: Checked: Article comments platform (global rule); none on the sampled title |
| Orchisasia 🔞 | en | https://www.orchisasia.org | Madara | Own: 15 mentions of "comment" |
| Paritehaber 🔞 | en | https://www.paritehaber.com | Madara | Own: 17 mentions of "comment" |
| Petrotechsociety 🔞 | en | https://www.petrotechsociety.org | Madara | Own: 13 mentions of "comment" |
| Read Horimiya Online | en | https://read-horimiya.online | MangaBox | Own: 11 mentions of "comment" |
| StoneScape | en | https://stonescape.xyz |  | Own: /api/comments/recent |
| Tailspace 🔞 | en | https://tailspace.com |  | Own: /assets/comment-utils-CI9ItubT.js |
| Zazamanga | en | https://www.zazamanga.com | Madara | Own: Checked: older QQ Comment Service: draws comments as HTML (no list API); rule pending |
| ApollComics 🔞 | es | https://apollcomics.es | Madara | Own: 33 mentions of "comment" |
| Asia Lotus 🔞 | es | https://asialotuss.com | MangaThemesia | Own: 17 mentions of "comment" |
| Bymichi Scan 🔞 | es | https://bymichiby.com | MangaThemesia | Own: 8 mentions of "comment" |
| Dynasty | es | https://manhuako.net |  | Own: /_nuxt/CommentActionDialog.lNf0Ah_w.css, /_nuxt/CommentCard.C78yGPd4.css |
| Hades no Fansub | es | https://lectorhades.latamtoon.com | Madara | Remark42:  |
| House Of Otakus | es | https://houseofotakusv2.xyz | Madara | Own: 17 mentions of "comment" |
| Inmortal Scan | es | https://scan-inmortal.com | Madara | Own: 27 mentions of "comment" |
| InsanosScan | es | https://insanoslibrary.com |  | Own: /css/comment-media.css?v=20261102.1, /js/comment-media.js?v=20261102.1, /js/comm |
| LectorManga.lat | es | https://lector-mangas.lat |  | Own: 9 mentions of "comment" |
| Marmota | es | https://marmota.me | Madara | Own: 17 mentions of "comment" |
| MHScans | es | https://mhscans.com |  | Own: /_astro/CommentsIsland.Vzr8-J0n.css |
| Platinum Lily Scan | es | https://platinumlilyscan.com | Next.js | Own: 81 mentions of "comment" |
| Dassou Scan | fr | https://dassouscan.com |  | Own: 18 mentions of "comment" |
| FMTEAM | fr | https://fmteam.fr |  | Own: /comments/1439, /comments/1445, /comments/1449 |
| Hentai Origines 🔞 | fr | https://hentai-origines.com | Madara | Own: 31 mentions of "comment" |
| MangaNova | fr | https://www.manga-nova.com | Next.js | Own: 143 mentions of "comment" |
| Poseidon Scans | fr | https://poseidon-scans.net | Next.js | Own: 31 mentions of "comment" |
| Komiku | id | https://komiku.org |  | Commento:  |
| ManhwaDesu 🔞 | id | https://manhwadesu.rest | MangaThemesia | Own: 9 mentions of "comment" |
| Pramramadhan | id | https://01.pramramadhan.my.id | Iken | Own: /images/comments.svg |
| VoraToon | id | https://voratoon.co | Iken | Own: 300 mentions of "comment" |
| West Manga | id | https://v1.westmanga.my |  | Own: /assets/comment-CsWYXIYf.js |
| Wurmz | id | https://wurmz.net | Next.js | Valine:  |
| Ameba Manga | ja | https://dokusho-ojikan.jp |  | Own: 14 mentions of "comment" |
| Flower Comics | ja | https://flowercomics.jp | Next.js | Own: /assets/comment.svg, /comment/134953, /comment/137161, /comment/138328, /comment |
| Jump Toon | ja | https://jumptoon.com | Next.js | Own: 10 mentions of "comment" |
| Love4u | ja | https://love4u.net |  | Own: /manga-list-genre-social-commentary.html |
| Magazine Pocket | ja | https://pocket.shonenmagazine.com |  | Own: 15 mentions of "comment" |
| Manga-Park | ja | https://manga-park.com |  | Own: /assets/img/comment_title_icon.svg, /assets/img/mangadetail_icon_comment.svg, /a |
| Nicomanga | ja | https://nicomanga.com | Next.js | Own: /app/manga/themes/dark/assets/js/comment-v2.js?v=1.0.6 |
| NihonKuni | ja | https://nihonkuni.com | Blogger | Own: /manga-list-genre-social-commentary.html |
| GoodToon | ko | https://www.goodtoon008.com | Madara | Own: 9 mentions of "comment" |
| NewXToon | ko | https://newxtoon1.com |  | Own: 80 mentions of "comment" |
| RawDEX 🔞 | ko | https://rawdex.net | Madara | Own: 12 mentions of "comment" |
| AcervoEremita | pt | https://acervoeremita.com | Next.js | Own: 29 mentions of "comment" |
| Azuretoons | pt | https://azuretoons.com | Iken | Commento:  |
| Bakai 🔞 | pt | https://bakai.org |  | Own: 21 mentions of "comment" |
| Capitoons | pt | https://capitoons.com |  | Own: 18 mentions of "comment" |
| Hanami Heaven 🔞 | pt | https://hanamiheaven.org | Madara | Own: 25 mentions of "comment" |
| Hentai Fusion 🔞 | pt | https://hentaifusion.me |  | Own: 11 mentions of "comment" |
| Hora Hentai 🔞 | pt | https://horahentai.com |  | Own: 99 mentions of "comment" |
| Hunters Scans | pt | https://readhunters.xyz | Madara | Own: 25 mentions of "comment" |
| Monte Tai | pt | https://montetaiscanlator.xyz | Madara | Own: 96 mentions of "comment" |
| MR Tenzus 🔞 | pt | https://mrtenzus.com | Madara | Own: 52 mentions of "comment" |
| Mundo Hentai 🔞 | pt | https://mundohentaioficial.com |  | Own: 8 mentions of "comment" |
| Tankou Hentai 🔞 | pt | https://tankouhentai.com | Madara | Own: 12 mentions of "comment" |
| Universo Hentai 🔞 | pt | https://universohentai.com |  | Own: 20 mentions of "comment" |
| AstraManga | ru | https://astramanga.org | Next.js | Own: 180 mentions of "comment" |
| Desu | ru | https://desu.uno |  | Own: /js/AniManga/comment.js?_v=63 |
| InkStory | ru | https://inkstory.net |  | Own: /content/the-remarried-empress-2019/comments, /content/the-remarried-empress-201 |
| Mangahub | ru | https://mangahub.ru |  | Own: /title/loqp/comments |
| MangaPoisk | ru | https://mangapoisk.me |  | Own: 13 mentions of "comment" |
| PureManga | ru | https://v1.puremanga.me |  | Own: /assets/comment-section-DyAgbJ3W.js, /discussion |
| Inu Manga | th | https://www.inu-manga.net | MangaThemesia | Own: 8 mentions of "comment" |
| Makimaaaaa | th | https://makimaaaaa.com | MangaThemesia | Own: 8 mentions of "comment" |
| MangaIsekaiThai | th | https://www.mangaisekaithai.net | Madara | Own: 19 mentions of "comment" |
| Speed Manga | th | https://speed-manga.net | MangaThemesia | Own: 200 mentions of "comment" |
| Tanuki-Manga | th | https://www.tanuki-manga.net | MangaThemesia | Own: 8 mentions of "comment" |
| Anikiga | tr | https://anikiga.com | Madara | Own: 22 mentions of "comment" |
| Elder Manga | tr | https://eldermanga.com |  | Own: 8 mentions of "comment" |
| Eski Mangalar | tr | https://eskimangalar.com |  | Own: 8 mentions of "comment" |
| Limon Manga | tr | https://limonmanga.com |  | Own: 9 mentions of "comment" |
| Mangadusleri 🔞 | tr | https://mangadusleri.mom |  | Own: 117 mentions of "comment" |
| MangaTilkisi | tr | https://www.tilkiscans.com | Madara | GraphComment:  |
| Opiatoon 🔞 | tr | https://opiatoon.shop | Madara | GraphComment:  |
| Rüya Manga | tr | https://www.ruyamanga2.com | Madara | Own: 33 mentions of "comment" |
| SummerToon | tr | https://summertoons.net | MangaThemesia | Own: 27 mentions of "comment" |
| Sunset Manga | tr | https://sunsetscans.com.tr |  | Own: 346 mentions of "comment" |
| Tortuga Ceviri | tr | https://tortugaceviri.com | Madara | GraphComment:  |
| Tr Manga | tr | https://trmanga.com |  | Own: /assets/v3/comments-ui.js?v=e383768e04, /assets/v3/comments.js?v=a70ff3c1b4 |
| Uzay Manga | tr | https://uzaymanga.com |  | Own: 15 mentions of "comment" |
| WebtoonOku | tr | https://webtoonoku.org |  | Own: 13 mentions of "comment" |
| CoTruyenDay | vi | https://cotruyenday1.com |  | Own: 11 mentions of "comment" |
| DamCoNuong 🔞 | vi | https://damconuong.icu |  | Own: 21 mentions of "comment" |
| Dua Leo Truyen 🔞 | vi | https://dualeotruyenday.com |  | Own: 103 mentions of "comment" |
| LoppyToon | vi | https://loppytoonn.com |  | Own: /comment/${id}/like, /truyen-comment/${STORY_ID}/comment, /truyen-comment/${STOR |
| LXManga 🔞 | vi | https://lxmanga.top |  | Own: 14 mentions of "comment" |
| MeHentai 🔞 | vi | https://mehentai.live | Madara | Own: 15 mentions of "comment" |
| MeoSua | vi | https://meosua.org |  | Own: 122 mentions of "comment" |
| NavyTeam | vi | https://navyteamz.com |  | Own: /comment/${id}/like, /truyen-comment/${STORY_ID}/comment, /truyen-comment/${STOR |
| NetTruyenS (unoriginal) | vi | https://nettruyen15s.com |  | Own: 27 mentions of "comment" |
| Rùa Hấp Chanh Dây | vi | https://ruahapchanhday2.com | Madara | Own: 14 mentions of "comment" |
| SangChanhTeam | vi | https://sangchanhteam.com |  | Commento:  |
| TruyenTVN 🔞 | vi | https://truyentvn.net |  | Own: /comments |
| TuiTruyen | vi | https://tuitruyen.top |  | Own: /comment-emoji.js?t=786d1ef9db7ab055, /comments.js?t=786d1ef9db7ab055, /fast-nav |
| VinaHentai 🔞 | vi | https://vinahentai.beer | Iken | Own: /assets/comment-detail-DeezZOgW.js, /assets/comment-reaction-D4xAKJkl.js |
| 6Manhua 🔞 | zh | https://www.liumanhua.com |  | Own: /user/comment |
| Dongman Manhua | zh | https://www.dongmanmanhua.cn |  | Own: /js/comment/likeItTitle.js?t=20200714 |
| FavComic | zh | https://www.favcomic.com |  | Own: 16 mentions of "comment" |
| Ikanmh 🔞 | zh | https://ikanmh.xyz |  | Own: /static/images/detail-comment-logo.png, /static/js/comment.js |
| Manga Xiao Si 🔞 | zh | https://www.jjmhw2.top |  | Own: /static/images/detail-comment-logo.png, /static/js/comment.js |
| Manhuawu | zh | https://www.mhua5.com |  | Own: 10 mentions of "comment" |
| Manwa | zh | https://manwa.me |  | Own: 62 mentions of "comment" |
| Manwa Manhua | zh | https://manwadz.cc |  | Own: /static/mh/css/comment.css, /static/mh/js/comment.js?v=20260411 |
| MH1234 | zh | https://m.wmh1234.com |  | Own: 9 mentions of "comment" |

## ⚠️ Unsupported (13)

| Extension | Lang | Site | Template | Notes |
|---|---|---|---|---|
| MangaFox | en | https://fanfox.net | Iken | Facebook:  |
| Mangahere | en | https://www.mangahere.cc | Iken | Facebook:  |
| 108Read 🔞 | th | https://www.108read.com | MangaThemesia | Facebook:  |
| Cat300 🔞 | th | https://cat-300.com | Madara | Facebook:  |
| Doujinx-H 🔞 | th | https://doujinx-h.com | Madara | Facebook:  |
| Flash-Manga | th | https://www.flash-manga.net | MangaThemesia | Facebook:  |
| God-Doujin 🔞 | th | https://god-doujin.com | MangaThemesia | Facebook:  |
| Mangastep | th | https://mangastep.com | MangaThemesia | Facebook:  |
| OreManga | th | https://www.oremanga.net |  | Facebook:  |
| ReaperTrans | th | https://reapertrans.com | MangaThemesia | Facebook:  |
| Slow Manga | th | https://www.slow-manga.net | MangaThemesia | Facebook:  |
| ToomTam-Manga | th | https://toomtam-manga.com | MangaThemesia | Facebook:  |
| ToonHunter 🔞 | th | https://toonhunter.com | MangaThemesia | Facebook:  |

## 🛡️ Check in app (583)

| Extension | Lang | Site | Template | Notes |
|---|---|---|---|---|
| 3Hentai 🔞 | all | https://3hentai.net |  | no title page found from the home page |
| 4KHD 🔞 | all | https://www.4khd.com |  | Cloudflare |
| AHottie 🔞 | all | https://ahottie.top |  | no title page found from the home page |
| AsmHentai 🔞 | all | https://asmhentai.com |  | Cloudflare |
| BaoBua 🔞 | all | https://baobua.net |  | no title page found from the home page |
| Buon Dua 🔞 | all | https://buondua.com |  | Cloudflare |
| Comikey | all | https://comikey.com |  | Cloudflare |
| Coomer 🔞 | all | https://coomer.st |  | no title page found from the home page |
| Cubari | all | https://cubari.moe |  | no title page found from the home page |
| DB New Hope | all | https://dbnewhope.com |  | no title page found from the home page |
| Dragon Ball Multiverse | all | https://www.dragonball-multiverse.com |  | no title page found from the home page |
| Elite Babes 🔞 | all | https://www.elitebabes.com |  | Cloudflare |
| EveriaClub (unoriginal) 🔞 | all | https://www.everiaclub.com |  | no title page found from the home page |
| Femjoy Hunter 🔞 | all | https://www.femjoyhunter.com |  | Cloudflare |
| FoamGirl 🔞 | all | https://foamgirl.net |  | Cloudflare |
| FSI Comics 🔞 | all | https://fsicomics.com |  | Cloudflare |
| FTV Hunter 🔞 | all | https://www.ftvhunter.com |  | Cloudflare |
| GlobalComix | all | https://globalcomix.com |  | no title page found from the home page |
| Grabber Zone | all | https://grabber.zone | Madara | Cloudflare |
| HDoujin 🔞 | all | https://hdoujin.org |  | no title page found from the home page |
| Hentai Cosplay 🔞 | all | https://hentai-cosplay-xxx.com |  | Cloudflare |
| HentaiEnvy 🔞 | all | https://hentaienvy.com |  | no title page found from the home page |
| HentaiEra 🔞 | all | https://hentaiera.com |  | Cloudflare |
| HentaiFox 🔞 | all | https://hentaifox.com | Iken | no title page found from the home page |
| HentaiRox 🔞 | all | https://hentairox.com |  | no title page found from the home page |
| HentaiZap 🔞 | all | https://hentaizap.com |  | Cloudflare |
| HNI-Scantrad | all | https://hni-scantrad.net |  | no title page found from the home page |
| HOLONOMETRIA | all | https://holoearth.com |  | no title page found from the home page |
| IMHentai 🔞 | all | https://imhentai.xxx |  | Cloudflare |
| INKRUSH | all | https://inkrush.site | Next.js | no title page found from the home page |
| JJCOS 🔞 | all | https://jjcos.com |  | no title page found from the home page |
| Joymii Hub 🔞 | all | https://www.joymiihub.com |  | Cloudflare |
| Junmeitu 🔞 | all | https://meijuntu.com |  | no title page found from the home page |
| Kagane | all | https://kagane.moe | Next.js | no title page found from the home page |
| Kemono 🔞 | all | https://kemono.cr |  | no title page found from the home page |
| Kiutaku 🔞 | all | https://kiutaku.com |  | no title page found from the home page |
| Kodoku Studio | all | https://kodokueasyaccess.com |  | no title page found from the home page |
| Lunar Manga | all | https://lunarx.to |  | Cloudflare |
| Manga Ball | all | https://mangaball.com |  | Cloudflare |
| Manga Million | all | https://mangamillion.shueisha.co.jp | Next.js | no title page found from the home page |
| MANGA Plus by SHUEISHA | all | https://mangaplus.shueisha.co.jp |  | no title page found from the home page |
| MANGA Plus Creators by SHUEISHA | all | https://mangaplus-creators.jp |  | no title page found from the home page |
| MangaCrazy 🔞 | all | https://mangacrazy.net |  | Cloudflare |
| MangaFire | all | https://mangafire.to |  | Cloudflare |
| MangaTaro | all | https://mangataro.org |  | no title page found from the home page |
| MangaToon (Limited) | all | https://mangatoon.mobi |  | no title page found from the home page |
| Manhwa18.net 🔞 | all | https://manhwa18.net |  | no title page found from the home page |
| Manta Comics | all | https://manta.net/en | Next.js | no title page found from the home page |
| MayoTune | all | https://mayochuu.xyz |  | Cloudflare |
| Metart Hunter 🔞 | all | https://www.metarthunter.com |  | Cloudflare |
| Mitaku 🔞 | all | https://mitaku.net |  | Cloudflare |
| NHentai.to 🔞 | all | https://nhentai.to |  | no title page found from the home page |
| NHentai.xxx 🔞 | all | https://nhentai.xxx |  | Cloudflare |
| NovelCool | all | https://www.novelcool.com |  | no title page found from the home page |
| One Piece Fans | all | https://one-piece-fans2.com |  | no title page found from the home page |
| OSOSEDKI 🔞 | all | https://ososedki.com |  | Cloudflare |
| PandaChaika 🔞 | all | https://panda.chaika.moe |  | no title page found from the home page |
| Pawchive 🔞 | all | https://pawchive.pw |  | no title page found from the home page |
| Pepper&Carrot | all | https://www.peppercarrot.com |  | no title page found from the home page |
| Photos18 🔞 | all | https://www.photos18.com |  | Cloudflare |
| Pixiv | all | https://www.pixiv.net |  | Cloudflare |
| Playmate Hunter 🔞 | all | https://pmatehunter.com |  | Cloudflare |
| Project Suki | all | https://projectsuki.com |  | Cloudflare |
| RokuHentai 🔞 | all | https://rokuhentai.com |  | Cloudflare |
| SchaleNetwork 🔞 | all | https://shupogaki.moe |  | no title page found from the home page |
| Swarm | all | https://swarm.ws | Iken | no title page found from the home page |
| Taddy INK (Webtoons) | all | https://taddy.org |  | no title page found from the home page |
| The Library of Ohara | all | https://thelibraryofohara.com |  | no title page found from the home page |
| ToonLook 🔞 | all | https://toonlook.com |  | Cloudflare |
| Twicomi | all | https://twicomi.com |  | no title page found from the home page |
| Webcomics | all | https://webcomicsapp.com |  | no title page found from the home page |
| Webtoons.com | all | https://www.webtoons.com |  | no title page found from the home page |
| XArt Hunter 🔞 | all | https://www.xarthunter.com |  | Cloudflare |
| Xiutaku 🔞 | all | https://xiutaku.com |  | Cloudflare |
| Yaoi Manga Online 🔞 | all | https://yaoimangaonline.com |  | Cloudflare |
| Yaoi.me 🔞 | all | https://yaoi.me |  | Cloudflare |
| YellowNote 🔞 | all | https://xchina.co |  | Cloudflare |
| Anyone Manga | ar | https://anyonemanga.com |  | Cloudflare |
| Arab Toons 🔞 | ar | https://arabtoons.net |  | Cloudflare |
| ArabManhwa 🔞 | ar | https://arabmanhwa.com |  | Cloudflare |
| AriaToon | ar | https://ariatoon.com |  | Cloudflare |
| Dilar | ar | https://dilar.tube |  | Cloudflare |
| Duskoryvile | ar | https://duskoryvile.com |  | no title page found from the home page |
| Empire Webtoon 🔞 | ar | https://webtoonempire-bl.com |  | Cloudflare |
| EShadow | ar | https://eshadow.net | Next.js | no title page found from the home page |
| Hentai Slayer 🔞 | ar | https://hentaislayer.net |  | Cloudflare |
| HizoManga | ar | https://hizomanga.net |  | Cloudflare |
| Kawii Manga | ar | https://kawaiimanga.org |  | Cloudflare |
| Lava Scans | ar | https://lavascans.com |  | Cloudflare |
| Manga Bab 🔞 | ar | https://mangabab.com |  | Cloudflare |
| Manga Starz | ar | https://starzmanga.com |  | Cloudflare |
| Mangalink | ar | https://link-manga.net |  | Cloudflare |
| MangaLionz | ar | https://manga-lionz.org |  | Cloudflare |
| MangaSpark | ar | https://sparkmanga.net |  | Cloudflare |
| MangaSwat | ar | https://meshmanga.com | MangaThemesia | no title page found from the home page |
| MangaTik | ar | https://mangatik.com |  | Cloudflare |
| Murim | ar | https://www.murim.site |  | no title page found from the home page |
| NeverScans | ar | https://neverscans.com |  | no title page found from the home page |
| Oduto | ar | https://nb19u.blogspot.com | Blogger | no title page found from the home page |
| Team X | ar | https://olympustaff.com |  | Cloudflare |
| XSano Manga | ar | https://www.xsano-manga.com | ZeistManga | no title page found from the home page |
| Fansubs.cat | ca | https://manga.fansubs.cat |  | no title page found from the home page |
| Hentai.cat 🔞 | ca | https://manga.hentai.cat |  | no title page found from the home page |
| Manga Tube | de | https://manga-tube.me |  | no title page found from the home page |
| 1Manga.co | en | https://1manga.co |  | Cloudflare |
| 8Muses 🔞 | en | https://comics.8muses.com |  | no title page found from the home page |
| AllManga | en | https://mkissa.to |  | no title page found from the home page |
| AllPornComic 🔞 | en | https://allporncomic.com |  | Cloudflare |
| Alpha Manga | en | https://www.alpha-manga.com |  | no title page found from the home page |
| Arc-Relight | en | https://arc-relight.com |  | no title page found from the home page |
| Arknights Comics | en | https://arknights.global |  | no title page found from the home page |
| Athrea Scans | en | https://athreascans.com |  | Cloudflare |
| Atsumaru | en | https://atsu.moe |  | no title page found from the home page |
| Bakkin | en | https://bakkin.moe/reader/ |  | no title page found from the home page |
| Bbato | en | https://bato1.com |  | no title page found from the home page |
| BookWalker | en | https://bookwalker.com |  | Cloudflare |
| CartoonPorn 🔞 | en | https://cartoonporn.to |  | Cloudflare |
| Clone Manga | en | https://manga.clone-army.org |  | no title page found from the home page |
| CManhua | en | https://cmanhua.com |  | Cloudflare |
| Cocomic | en | https://cocomic.co |  | Cloudflare |
| Collected Curios | en | https://www.collectedcurios.com |  | no title page found from the home page |
| Comic Asura | en | https://comicasura.net | MangaBox | no title page found from the home page |
| ComicHubFree | en | https://comichubfree.com |  | Cloudflare |
| ComicLand | en | https://comicland.org |  | no title page found from the home page |
| Comix | en | https://comix.to |  | Cloudflare |
| Coolmic | en | https://coolmic.me |  | no title page found from the home page |
| Cutie Comics 🔞 | en | https://cutiecomics.com |  | Cloudflare |
| Cyanide & Happiness | en | https://explosm.net | Next.js | no title page found from the home page |
| Dark Legacy Comics | en | https://www.darklegacycomics.com |  | no title page found from the home page |
| Darths & Droids | en | https://www.darthsanddroids.net |  | no title page found from the home page |
| Diva Scans | en | https://divascans.org |  | Cloudflare |
| Doujin.io - J18 🔞 | en | https://doujin.io |  | no title page found from the home page |
| Eggporncomics 🔞 | en | https://eggporncomics.com |  | Cloudflare |
| Elan School | en | https://elan.school |  | no title page found from the home page |
| emaqi | en | https://emaqi.com |  | no title page found from the home page |
| Eris Scans | en | https://erisscans.com |  | Cloudflare |
| Erofus 🔞 | en | https://www.erofus.com |  | Cloudflare |
| Flame Comics | en | https://flamecomics.xyz |  | Cloudflare |
| GEDE Comix 🔞 | en | https://gedecomix.com |  | Cloudflare |
| GingeRTooN 🔞 | en | https://gingertoon.com | Madara | no title page found from the home page |
| GirlsTop 🔞 | en | https://en.girlstop.info |  | no title page found from the home page |
| Goda | en | https://manhuascans.org |  | Cloudflare |
| Gourmet Scans | en | https://gourmetsupremacy.com |  | Cloudflare |
| Gunnerkrigg Court | en | https://www.gunnerkrigg.com |  | no title page found from the home page |
| Hades Scans | en | https://hadesscans.com |  | no title page found from the home page |
| Hentai4Free 🔞 | en | https://hentai4free.net |  | Cloudflare |
| HentaiFC 🔞 | en | https://hentaifc.com |  | no title page found from the home page |
| HentaiHere 🔞 | en | https://hentaihere.com |  | no title page found from the home page |
| HentaiKun 🔞 | en | https://hentaikun.com |  | no title page found from the home page |
| HentaiNexus 🔞 | en | https://hentainexus.com |  | no title page found from the home page |
| HentaiSco 🔞 | en | https://hentaisco.cc |  | no title page found from the home page |
| HentaiTnT 🔞 | en | https://hentaitnt.net |  | no title page found from the home page |
| Hiperdex | en | https://hiperdex.tv |  | no title page found from the home page |
| Hive Scans | en | https://hivetoons.org |  | Cloudflare |
| ILikeComix 🔞 | en | https://ilikecomix.com |  | Cloudflare |
| InfinityScans | en | https://infinityscans.org |  | Cloudflare |
| J-Novel | en | https://j-novel.club |  | Cloudflare |
| Kappa Beast | en | https://kappabeast.com |  | no title page found from the home page |
| KingComiX 🔞 | en | https://kingcomix.com |  | Cloudflare |
| Komix | en | https://komix.to |  | Cloudflare |
| Lagoon Scans | en | https://lagoonscans.com |  | Cloudflare |
| Leslie&Victims | en | https://leslie-victims.pages.dev |  | no title page found from the home page |
| LHTranslation | en | https://lhtranslation.net |  | Cloudflare |
| Lily Manga | en | https://lilymanga.net |  | no title page found from the home page |
| LinkManga | en | https://linkmanga.com |  | Cloudflare |
| Loading Artist | en | https://loadingartist.com |  | no title page found from the home page |
| LoLoBun | en | https://www.lolobun.com |  | no title page found from the home page |
| Lua Scans | en | https://luacomic.org |  | Cloudflare |
| Luminare Translations | en | https://luminaretranslations.com |  | Cloudflare |
| MadaraDex | en | https://madaradex.org |  | Cloudflare |
| Manga 18x 🔞 | en | https://manga18x.net |  | Cloudflare |
| Manga Demon | en | https://demonicscans.org |  | Cloudflare |
| Manga Drama 🔞 | en | https://mangadrama.com | Iken | Cloudflare |
| Manga.uno | en | https://manga.uno |  | Cloudflare |
| MangaCloud | en | https://mangacloud.org |  | Cloudflare |
| MangaDE | en | https://mangade.io |  | no title page found from the home page |
| MangaFox.fun | en | https://mangafox.fun |  | Cloudflare |
| MangaHere.onl | en | https://mangahere.onl |  | Cloudflare |
| MangaHub | en | https://mangahub.io | MangaBox | Cloudflare |
| MangaK | en | https://mangak.io |  | no title page found from the home page |
| Mangakakalot.fun | en | https://mangakakalot.fun |  | Cloudflare |
| MangaLix | en | https://mangalix.com |  | no title page found from the home page |
| MangaMelon | en | https://mangamelon.com |  | Cloudflare |
| MangaNel | en | https://manganel.me |  | Cloudflare |
| MangaNow | en | https://manganow.to |  | no title page found from the home page |
| MangaOnline.fun | en | https://mangaonline.fun | MangaBox | Cloudflare |
| MangaOwl.io (unoriginal) | en | https://mangaowl.io |  | Cloudflare |
| MangaPanda.onl | en | https://mangapanda.onl |  | Cloudflare |
| MangaPark.tv (unoriginal) 🔞 | en | https://mangapark.tv |  | Cloudflare |
| MangaReader.site | en | https://mangareader.site |  | Cloudflare |
| MangaToday | en | https://mangatoday.fun | MangaBox | Cloudflare |
| Manhua Plus | en | https://manhuaplus.com |  | Cloudflare |
| ManhuaHot | en | https://manhuahot.com |  | Cloudflare |
| ManhuaTop | en | https://manhuatop.org |  | Cloudflare |
| Manhwa Comics 🔞 | en | https://manhwacomics.com | Madara | no title page found from the home page |
| Manhwa Reads | en | https://manhwareads.com |  | Cloudflare |
| Manhwa68 🔞 | en | https://manhwa68.com |  | Cloudflare |
| Manhwalike 🔞 | en | https://manhwalike.com |  | no title page found from the home page |
| Manhwatop | en | https://manhwatop.com |  | Cloudflare |
| ManhwaZone | en | https://manhwazone.com |  | no title page found from the home page |
| Megatokyo | en | https://megatokyo.com |  | no title page found from the home page |
| Milftoon 🔞 | en | https://milftoon.xxx |  | Cloudflare |
| MLBB Lore | en | https://play.mobilelegends.com |  | no title page found from the home page |
| Monochrome Custom | en | https://monochromecms.netlify.app |  | no title page found from the home page |
| Monochrome Scans | en | https://manga.d34d.one |  | no title page found from the home page |
| MyAdultComics 🔞 | en | https://myadultcomics.com |  | no title page found from the home page |
| MyHentaiComics 🔞 | en | https://myhentaicomics.com |  | Cloudflare |
| MyHentaiGallery 🔞 | en | https://myhentaigallery.com |  | Cloudflare |
| NineHentai 🔞 | en | https://9hentai.so |  | no title page found from the home page |
| Oglaf 🔞 | en | https://www.oglaf.com |  | no title page found from the home page |
| OneManga.info | en | https://onemanga.info |  | Cloudflare |
| Only The Best Hentai 🔞 | en | https://onlythebesthentai.com |  | Cloudflare |
| Patch Friday | en | https://patchfriday.com |  | no title page found from the home page |
| Philia Scans | en | https://philiascans.org |  | Cloudflare |
| PornComix 🔞 | en | https://bestporncomix.com |  | Cloudflare |
| PornhwaDB Reader 🔞 | en | https://pornhwareader.com |  | Cloudflare |
| Pornhwaz 🔞 | en | https://www.pornhwaz.com |  | Cloudflare |
| Questionable Content | en | https://www.questionablecontent.net |  | no title page found from the home page |
| Read Berserk Manga | en | https://readberserk.com |  | Cloudflare |
| Read Chainsaw Man Manga Online 🔞 | en | https://ww6.readchainsawman.com |  | Cloudflare |
| Read Fairy Tail & Edens Zero Manga Online | en | https://ww9.readfairytail.com |  | Cloudflare |
| Read Kingdom Manga Online | en | https://ww6.readkingdom.com |  | Cloudflare |
| Real Life Comics | en | https://reallifecomics.com |  | no title page found from the home page |
| Renascans | en | https://renascans.net |  | Cloudflare |
| Revival Scans 🔞 | en | https://www.revivalscans.com |  | Cloudflare |
| Rolia Scan | en | https://roliascan.com |  | no title page found from the home page |
| Rose Squad Scans 🔞 | en | https://rosesquadscans.aishiteru.org |  | no title page found from the home page |
| S2Manga | en | https://s2read.com |  | Cloudflare |
| Sabrina Online | en | https://www.sabrina-online.com |  | no title page found from the home page |
| SACACHISPA | en | https://sacachispa.site |  | no title page found from the home page |
| ScansGG | en | https://scans.gg |  | Cloudflare |
| Scythe Scans | en | https://scythescans.com |  | Cloudflare |
| SilentQuill | en | https://silentquill.net |  | Cloudflare |
| Snafu Comics | en | https://www.snafu-comics.com |  | no title page found from the home page |
| Solar and Sundry | en | https://sas-api.fly.dev |  | no title page found from the home page |
| SpyFakku 🔞 | en | https://hentalk.pw |  | Cloudflare |
| Sunshine Butterfly Scans 🔞 | en | https://wings.sbs |  | no title page found from the home page |
| SUPER MEGA | en | https://www.supermegacomics.com |  | no title page found from the home page |
| Temple Scan 🔞 | en | https://templetoons.com |  | Cloudflare |
| The Property of Hate | en | https://jolleycomics.com |  | no title page found from the home page |
| Toonily | en | https://toonily.com |  | Cloudflare |
| Toonily.me 🔞 | en | https://toontop.io |  | no title page found from the home page |
| Toonkotsu | en | https://toonkotsu.com |  | Cloudflare |
| TopManhua.net | en | https://topmanhua.net |  | Cloudflare |
| Tower Of God Manga Online | en | https://w82.thetowerofgod.com |  | Cloudflare |
| Valir Scans | en | https://valirscans.org | Next.js | Cloudflare |
| vgperson | en | https://vgperson.com |  | no title page found from the home page |
| VIZ | en | https://www.viz.com |  | no title page found from the home page |
| Voyce.Me | en | https://www.voyce.me | Next.js | no title page found from the home page |
| War For Rayuba | en | https://xrabohrok.github.io/WarMap/#/ |  | no title page found from the home page |
| Webdex Scans | en | https://webdexscans.com |  | Cloudflare |
| WebNovel | en | https://www.webnovel.com |  | Cloudflare |
| WebtoonLib | en | https://webtoonlib.to |  | Cloudflare |
| WuxiaWorld | en | https://wuxiaworld.site |  | Cloudflare |
| XlecX 🔞 | en | https://xlecx.one |  | no title page found from the home page |
| XOXO Comics | en | https://xoxocomic.com |  | Cloudflare |
| YakshaComics | en | https://yakshacomics.com |  | Cloudflare |
| Zinmanga | en | https://mangazin.org |  | Cloudflare |
| Catharsis World | es | https://newcatharsis.dig-it.info |  | no title page found from the home page |
| Catoons 🔞 | es | https://cattoons.org |  | no title page found from the home page |
| Code Arc Mangas 🔞 | es | https://mangas.codearctraducciones.com | Next.js | no title page found from the home page |
| Dark Room Fansub 🔞 | es | https://lector-darkroomfansub.blogspot.com | ZeistManga | no title page found from the home page |
| EnchiladaScan | es | https://enchiladascan.github.io/enchiladaweb |  | no title page found from the home page |
| EternalMangas | es | https://eternalmangas.org |  | Cloudflare |
| Falco Scan 🔞 | es | https://falcoscan.net |  | Cloudflare |
| Ikigai Mangas | es | https://visorikigai.gettocaboca.com |  | Cloudflare |
| InfraFandub | es | https://infrafandub.com |  | Cloudflare |
| InManga | es | https://inmanga.com |  | Cloudflare |
| Jeaz Scans | es | https://lectorhub.j5z.xyz |  | Cloudflare |
| LectorTMO (unoriginal) | es | https://lectortmo.vip |  | Cloudflare |
| LeerCapitulo | es | https://www.leercapitulo.co |  | no title page found from the home page |
| LeerMangaEsp | es | https://mangalect.org |  | no title page found from the home page |
| Manga TV | es | https://mangatv.net |  | Cloudflare |
| Mangas.in | es | https://m440.in |  | Cloudflare |
| MangoLibreria | es | https://lectorfenix.com |  | Cloudflare |
| ManhwaWeb | es | https://manhwaweb.com |  | no title page found from the home page |
| Menudo-Fansub | es | https://www.menudo-fansub.com | Blogger | no title page found from the home page |
| NexusScanlation 🔞 | es | https://nexusscanlation.com |  | Cloudflare |
| Olympus Scanlation | es | https://olympusxyz.com |  | Cloudflare |
| ONF MANGAS | es | https://onfmangas.com |  | Cloudflare |
| Ragna Scans | es | https://lector.ragnascan.xyz |  | no title page found from the home page |
| Ragnarok Scanlation | es | https://ragnarokscanlation.org |  | Cloudflare |
| Reizu Comics 🔞 | es | https://reizucomics.com |  | no title page found from the home page |
| Rncalation | es | https://rncalation.online |  | Cloudflare |
| Shadow Manga | es | https://shademanga.com |  | Cloudflare |
| Submanhwa 🔞 | es | https://submanhwa.com |  | Cloudflare |
| TopComicPorno 🔞 | es | https://topcomicporno.com |  | Cloudflare |
| Yupmanga | es | https://www.yupmanga.com |  | Cloudflare |
| Yuri-Online | es | https://yuri-online.com |  | Cloudflare |
| ZonaTMO.org (unoriginal) | es | https://zonatmo.org |  | Cloudflare |
| Zonatmo.to (unoriginal) | es | https://zonatmo.to |  | no title page found from the home page |
| AralosBD | fr | https://aralosbd.fr |  | no title page found from the home page |
| BDplus | fr | https://bdplus.cc |  | Cloudflare |
| Blue Solo | fr | https://bluesolo.org |  | no title page found from the home page |
| ChaosTrad | fr | https://chaostrad.fr |  | Cloudflare |
| Hana Book 🔞 | fr | https://www.hana-book.fr |  | no title page found from the home page |
| Harmony-Scan | fr | https://harmony-scan.fr |  | Cloudflare |
| Hentai Scan Reader 🔞 | fr | https://hentai.scanreader.net |  | Cloudflare |
| HistoireDHentai 🔞 | fr | https://hhentai.fr |  | Cloudflare |
| Japscan | fr | https://www.japscan.foo |  | Cloudflare |
| LanorTrad | fr | https://lanortrad.com |  | no title page found from the home page |
| Lelmanga | fr | https://www.lelmanga.com |  | Cloudflare |
| Lelscan-VF | fr | https://www.lelscanfr.com |  | Cloudflare |
| Les Poroiniens | fr | https://lesporoiniens.org |  | no title page found from the home page |
| Manga-Corporation | fr | https://manga-corporation.com |  | Cloudflare |
| Mangakawaii | fr | https://www.mangakawaii.fr |  | Cloudflare |
| Ono | fr | https://www.ono.live |  | no title page found from the home page |
| Ortega Scans 🔞 | fr | https://ortegascans.fr |  | Cloudflare |
| Pantheon Scan | fr | https://pantheon-scan.com | Madara | no title page found from the home page |
| Rimu Scans | fr | https://rimuscan.fr |  | Cloudflare |
| Scan Reader | fr | https://scanreader.net |  | Cloudflare |
| ScanR | fr | https://teamscanr.fr |  | no title page found from the home page |
| Twatt | fr | https://twatt.fr |  | no title page found from the home page |
| Ainz Scans ID | id | https://v3.ainzscans01.com |  | Cloudflare |
| Area Komik 🔞 | id | https://areakomik.com |  | Cloudflare |
| BacaKomik | id | https://bacakomik.my |  | Cloudflare |
| CGBUM | id | https://cgbum.com |  | Cloudflare |
| Comicaso | id | https://v3.comicaso.pro |  | no title page found from the home page |
| CosmicScans | id | https://04.cosmicscans.to |  | Cloudflare |
| CrotPedia 🔞 | id | https://crotpedia.net |  | Cloudflare |
| Doujindesu 🔞 | id | https://doujin.desu.xxx |  | Cloudflare |
| Hentai Crot 🔞 | id | https://hentaicrot.com |  | Cloudflare |
| Holotoon | id | https://holodek.run | Astro | Cloudflare |
| Ikiru | id | https://09.ikiru.wtf |  | Cloudflare |
| Kiryuu | id | https://v7.kiryuu.to |  | Cloudflare |
| KlikManga | id | https://klikmanga.org |  | Cloudflare |
| Komik Dewasa 🔞 | id | https://komikdewasa.mom |  | Cloudflare |
| Komik Station | id | https://komikstation.org |  | Cloudflare |
| Komikindo 🔞 | id | https://2.komikindo.shop |  | Cloudflare |
| KomikIndoID | id | https://komikindo.ch |  | Cloudflare |
| Komikmu 🔞 | id | https://komikmu.top |  | Cloudflare |
| KomikNesia | id | https://v2.komiknesiaku.com |  | Cloudflare |
| Komiku.com | id | https://01.komiku.asia |  | Cloudflare |
| KoronaxScan | id | https://project.koronaxscan.my.id | Iken | no title page found from the home page |
| KumoPoi 🔞 | id | https://beta.kumopoi.com | Next.js | no title page found from the home page |
| Kuro Manga | id | https://kuromanga.id |  | Cloudflare |
| LepoyTL | id | https://www.lepoytl.my.id | ZeistManga | no title page found from the home page |
| LianScans 🔞 | id | https://www.lianscans.com | MangaThemesia | no title page found from the home page |
| LumosKomik | id | https://03.lumosgg.com |  | Cloudflare |
| Manga Can | id | https://mangacanblog.com |  | Cloudflare |
| Mangalay | id | http://mangalay.blogspot.com | Blogger | no title page found from the home page |
| Manhwa Indo | id | https://www.manhwaindo.my |  | Cloudflare |
| MikoRoku | id | https://mikoroku.com |  | no title page found from the home page |
| Narasi Ninja | id | https://narasininja.net |  | Cloudflare |
| Ngomik (unoriginal) | id | https://02.ngomik.cc |  | Cloudflare |
| Omicaso | id | https://omicaso.org | Iken | no title page found from the home page |
| Pix Hentai 🔞 | id | https://pixhentai.com |  | Cloudflare |
| Riztranslation | id | https://riztranslation.pages.dev |  | no title page found from the home page |
| Ryukomik 🔞 | id | https://ryukomik.my.id |  | Cloudflare |
| Sasangeyou 🔞 | id | https://sasangeyou.net |  | Cloudflare |
| Siikomik | id | https://siikomik.id |  | Cloudflare |
| Softkomik | id | https://softkomik.app | Next.js | no title page found from the home page |
| Ulas Comic | id | https://www.ulascomic01.xyz | Blogger | no title page found from the home page |
| Anime GDR Club | it | http://www.agcscanlation.it |  | no title page found from the home page |
| GTO The Great Site | it | https://reader.gtothegreatsite.net |  | no title page found from the home page |
| Hentai ITA 🔞 | it | https://hentai-ita.net |  | no title page found from the home page |
| LupiTeam | it | https://lupiteam.net |  | no title page found from the home page |
| Mangaworld | it | https://www.mangaworld.mx |  | no title page found from the home page |
| MangaworldAdult 🔞 | it | https://www.mangaworldadult.net |  | no title page found from the home page |
| NIFTeam | it | https://read-nifteam.info |  | no title page found from the home page |
| Phoenix Scans | it | https://www.phoenixscans.com |  | no title page found from the home page |
| TuttoAnimeManga | it | https://tuttoanimemanga.net |  | no title page found from the home page |
| Alphapolis | ja | https://www.alphapolis.co.jp |  | no title page found from the home page |
| BookLive | ja | https://booklive.jp |  | no title page found from the home page |
| Comic Action | ja | https://comic-action.com | Next.js | no title page found from the home page |
| Comic Boost | ja | https://comic-boost.com |  | no title page found from the home page |
| Comic Border | ja | https://comicborder.com | Iken | no title page found from the home page |
| Comic Days | ja | https://comic-days.com | Next.js | no title page found from the home page |
| Comic Earth Star | ja | https://comic-earthstar.com | Next.js | no title page found from the home page |
| Comic Festa | ja | https://comic.iowl.jp | Next.js | no title page found from the home page |
| COMIC FUZ | ja | https://comic-fuz.com | Next.js | no title page found from the home page |
| Comic Gardo | ja | https://comic-gardo.com | Next.js | no title page found from the home page |
| Comic Ogyaaa | ja | https://comic-ogyaaa.com | Next.js | no title page found from the home page |
| Comic Seasons | ja | https://comic-seasons.com | Next.js | no title page found from the home page |
| Comic Trail | ja | https://comic-trail.com |  | no title page found from the home page |
| Comic Y-OURs | ja | https://comic-y-ours.com | Next.js | no title page found from the home page |
| Corocoro Online | ja | https://www.corocoro.jp | Next.js | no title page found from the home page |
| DMM/FANZA | ja | https://book.dmm.com | Next.js | no title page found from the home page |
| Docomo | ja | https://dbook.docomo.ne.jp |  | no title page found from the home page |
| Dokiraw | ja | https://dokiraw.city |  | no title page found from the home page |
| eBookJapan | ja | https://ebookjapan.yahoo.co.jp |  | no title page found from the home page |
| Feel Web | ja | https://feelweb.jp |  | no title page found from the home page |
| FireCross | ja | https://firecross.jp |  | no title page found from the home page |
| GANMA! | ja | https://ganma.jp | Next.js | no title page found from the home page |
| Gaugau Monster Plus | ja | https://gaugau.futabanet.jp |  | no title page found from the home page |
| Goraku Web | ja | https://gorakuweb.com | Next.js | no title page found from the home page |
| Hakusensha e-net | ja | https://www.hakusensha-e.net |  | no title page found from the home page |
| Idol. gravureprincess .date 🔞 | ja | https://idol.gravureprincess.date | Blogger | no title page found from the home page |
| Jestful | ja | https://jestful.net |  | no title page found from the home page |
| Jmanga | ja | https://jmanga.cool |  | no title page found from the home page |
| KissLove | ja | https://klz9.com |  | Cloudflare |
| Klto9 | ja | https://klto9.com |  | no title page found from the home page |
| Kmansin09 | ja | https://kmansin09.top |  | Cloudflare |
| MAGCOMI | ja | https://magcomi.com | Next.js | no title page found from the home page |
| Manga One | ja | https://manga-one.com | Next.js | no title page found from the home page |
| Manga Rw | ja | https://mangarw.com |  | no title page found from the home page |
| Manga Saison | ja | https://mechacomi.jp |  | no title page found from the home page |
| Manga Time Square | ja | https://mangatime-square.com | Next.js | no title page found from the home page |
| Manga UP! (Japan) | ja | https://www.manga-up.com | Next.js | no title page found from the home page |
| Manga-5 | ja | https://manga-5.com |  | no title page found from the home page |
| Manga1000 | ja | https://hachiraw.win |  | no title page found from the home page |
| MangaBox | ja | https://www.mangabox.me | MangaBox | no title page found from the home page |
| MangaMee | ja | https://manga-mee.jp | Next.js | no title page found from the home page |
| MangaNo | ja | https://manga-no.com | Next.js | no title page found from the home page |
| MangaRaw | ja | https://mangaraw.co.uk |  | no title page found from the home page |
| Mecha Comic | ja | https://mechacomic.jp |  | no title page found from the home page |
| MiuRaw | ja | https://miuraw.net |  | Cloudflare |
| Mokuro | ja | https://mokuro.moe |  | no title page found from the home page |
| Music Book Japan | ja | https://music-book.jp |  | no title page found from the home page |
| Nicovideo Seiga | ja | https://sp.manga.nicovideo.jp | Next.js | no title page found from the home page |
| Ohta Web Comic | ja | https://webcomic.ohtabooks.com |  | no title page found from the home page |
| Our Feel | ja | https://ourfeel.jp | Next.js | no title page found from the home page |
| Pash Up! | ja | https://pash-up.jp |  | no title page found from the home page |
| Piccoma | ja | https://piccoma.com |  | no title page found from the home page |
| Pixiv Comic | ja | https://comic.pixiv.net |  | Cloudflare |
| Raw18 🔞 | ja | https://raw18.guru |  | no title page found from the home page |
| RawBaka | ja | https://rawbaka.site |  | Cloudflare |
| RawINU | ja | https://rawinu.com |  | Cloudflare |
| Rawkuma | ja | https://rawkuma.net |  | Cloudflare |
| Sen Manga | ja | https://raw.senmanga.com |  | no title page found from the home page |
| Sugo Comics | ja | https://nadeshiko-shoten.jp |  | no title page found from the home page |
| Sunday Web Every | ja | https://www.sunday-webry.com |  | no title page found from the home page |
| U-NEXT | ja | https://video.unext.jp | Next.js | no title page found from the home page |
| WeLoveManga | ja | https://weloma.net |  | no title page found from the home page |
| Yomonga | ja | https://www.yomonga.com |  | no title page found from the home page |
| Zebrack | ja | https://zebrack-comic.shueisha.co.jp |  | no title page found from the home page |
| Zerosum Online | ja | https://zerosumonline.com | Next.js | no title page found from the home page |
| 11toon | ko | https://www.11toon.com |  | no title page found from the home page |
| BlackToon | ko | https://blacktoon426.com |  | no title page found from the home page |
| Toonkor | ko | https://toonkor0.org |  | no title page found from the home page |
| Wolf.com | ko | https://wfwf507.com |  | no title page found from the home page |
| Animy | pt | https://animy.net |  | no title page found from the home page |
| Apenas Uma Fã | pt | https://apenasuma-fa.blogspot.com | Blogger | no title page found from the home page |
| Argos Scan | pt | https://argoscomics.online |  | no title page found from the home page |
| Arthur Scan | pt | https://arthurscan.xyz | Madara | Cloudflare |
| Astratoons | pt | https://new.astratoons.com |  | Cloudflare |
| BenDezOmniHero | pt | https://bendezomnihero.blogspot.com | Blogger | no title page found from the home page |
| Blackout Comics 🔞 | pt | https://blackoutcomics.com |  | Cloudflare |
| BR Yaoi 🔞 | pt | https://bryaoi.com |  | no title page found from the home page |
| Ego Toons | pt | https://egotoons.com |  | Cloudflare |
| Fliptru 🔞 | pt | https://fliptru.com.br |  | Cloudflare |
| FlowerManga.net | pt | https://flowermangas.net |  | Cloudflare |
| Geass Comics | pt | https://geasscomics.xyz |  | Cloudflare |
| HipercooL 🔞 | pt | https://lerhentais.com |  | no title page found from the home page |
| HQ Now! | pt | https://www.hq-now.com |  | no title page found from the home page |
| Inkapk 🔞 | pt | https://inkapk.net |  | Cloudflare |
| Leitura Manga | pt | https://leituramanga.net |  | Cloudflare |
| Manga Livre Blog | pt | https://mangalivre.blog |  | Cloudflare |
| Manga Online | pt | https://mangaonline.green |  | Cloudflare |
| ManGeek | pt | https://mangeek.app | Next.js | no title page found from the home page |
| Mango Toons | pt | https://mangotoons.com | Next.js | no title page found from the home page |
| Manhastro 🔞 | pt | https://manhastro.net |  | Cloudflare |
| Mediocre Toons | pt | https://mediocrescan.com |  | no title page found from the home page |
| Nexus Mangás | pt | https://www.nexusmangas.com |  | Cloudflare |
| OneReader | pt | https://onereader.net |  | no title page found from the home page |
| Pink Rosa | pt | https://scanpinkrosa.blogspot.com | Blogger | no title page found from the home page |
| Pink Sea Unicorn 🔞 | pt | https://psunicorn.com |  | no title page found from the home page |
| Pluma Comics | pt | https://plumacomics.cloud | Next.js | no title page found from the home page |
| Point Zero Toons | pt | https://kitsuneyako.com |  | Cloudflare |
| Revistas e Quadrinhos 🔞 | pt | https://revistasequadrinhos.com |  | Cloudflare |
| RF Dragon Scan | pt | https://rfdragonscan.net | Next.js | no title page found from the home page |
| Risentoons | pt | https://risentoons.xyz |  | no title page found from the home page |
| Roxinha | pt | https://roxinha.online |  | Cloudflare |
| Sagrado Império da Britannia | pt | https://imperiodabritannia.net |  | no title page found from the home page |
| Shirai Scans | pt | https://shiraixis.space |  | Cloudflare |
| Super Ecchi 🔞 | pt | https://superecchi.com |  | no title page found from the home page |
| Taiyō | pt | https://taiyo.moe | Next.js | no title page found from the home page |
| Tao Sect | pt | https://taosect.com |  | Cloudflare |
| Temaki mangás 🔞 | pt | https://temakimangas.blogspot.com | ZeistManga | no title page found from the home page |
| ToonBr | pt | https://beta.toonbr.com | Next.js | no title page found from the home page |
| Vegitoons | pt | https://vegitoons.black |  | no title page found from the home page |
| Verdinha | pt | https://verdinha.wtf |  | no title page found from the home page |
| Yomu Mangás | pt | https://yomumangas.com | Next.js | no title page found from the home page |
| Yuri on Air | pt | https://yurionair.top |  | Cloudflare |
| AComics | ru | https://acomics.ru |  | Cloudflare |
| AllHentai 🔞 | ru | https://20.allhen.online | MangaBox | no title page found from the home page |
| HentaiLib 🔞 | ru | https://hentailib.me |  | Cloudflare |
| ReadManga | ru | https://a.zazaza.me | MangaBox | no title page found from the home page |
| SeiManga | ru | https://1.seimanga.me | MangaBox | no title page found from the home page |
| SelfManga | ru | https://1.selfmanga.live | MangaBox | no title page found from the home page |
| SlashLib | ru | https://v2.shlib.life |  | no title page found from the home page |
| Tomilo-lib | ru | https://tomilo-lib.ru | Next.js | no title page found from the home page |
| 1668Manga | th | https://1668manga.com |  | Cloudflare |
| Bully Manga | th | https://bully-manga.com |  | no title page found from the home page |
| Doodmanga | th | https://www.doodmanga.com |  | Cloudflare |
| Doujin-Lc 🔞 | th | https://doujin-lc.net |  | Cloudflare |
| Doujin69 🔞 | th | https://doujin69.com |  | Cloudflare |
| GodhMan 🔞 | th | https://www.godhman.net |  | Cloudflare |
| HentaiThai 🔞 | th | https://hentaithai.com | Iken | no title page found from the home page |
| HentaiThai.net 🔞 | th | https://hentaithai.net |  | Cloudflare |
| Manga-Lc | th | https://manga-lc.net |  | Cloudflare |
| MangaKimi | th | https://www.mangakimi.com |  | Cloudflare |
| ManhuaBug | th | https://www.manhuabug.com |  | Cloudflare |
| ManhuaThai | th | https://www.manhuathai.com |  | Cloudflare |
| ManhwaBreakup | th | https://www.manhwabreakup.com |  | Cloudflare |
| MikuDoujin 🔞 | th | https://miku-doujin.com |  | Cloudflare |
| Nekopost | th | https://www.nekopost.net |  | no title page found from the home page |
| Niceoppai | th | https://www.niceoppai.net |  | Cloudflare |
| Singmanga | th | https://www.sing-manga.com |  | Cloudflare |
| Sodsaime | th | https://www.xn--l3c0azab5a2gta.com |  | Cloudflare |
| ThaiManga | th | https://www.thaimanga.net |  | Cloudflare |
| ArazNovel | tr | https://manga.araznovel.com |  | Cloudflare |
| Holy Scans 🔞 | tr | https://holyscans.com.tr |  | Cloudflare |
| Manga Bahçesi | tr | https://mangabahcesi.com |  | Cloudflare |
| Manga Diyarı | tr | https://mangadiyari.com | Next.js | no title page found from the home page |
| Manga Ruhu | tr | https://mangaruhu.com |  | Cloudflare |
| MangaciX | tr | https://mangacix.net |  | no title page found from the home page |
| Mikrokosmos Fansub 🔞 | tr | https://mikrokosmos.fans |  | no title page found from the home page |
| Mono Manga | tr | https://monomanga.com.tr |  | Cloudflare |
| Nemesis scans | tr | https://nemesisscans.com |  | no title page found from the home page |
| Raindrop Fansub | tr | https://www.raindropteamfan.com |  | no title page found from the home page |
| Slept Manga | tr | https://sleptmanga.com.tr |  | Cloudflare |
| Tarot Scans | tr | https://www.tarotscans.com |  | Cloudflare |
| Toontaku | tr | https://toontaku.com | Next.js | no title page found from the home page |
| DGManga | uk | https://dgmanga.app |  | Cloudflare |
| Faust | uk | https://faust-web.com |  | Cloudflare |
| HoneyManga | uk | https://honey-manga.com.ua | Next.js | no title page found from the home page |
| MangaInUa | uk | https://manga.in.ua |  | Cloudflare |
| Zenko | uk | https://zenko.online |  | Cloudflare |
| CuuTruyen | vi | https://cuutruyen.net |  | Cloudflare |
| CuuTruyen (unoriginal) | vi | https://cuutruyen.moe |  | Cloudflare |
| HongTraTeam | vi | https://hongtrateam.com |  | no title page found from the home page |
| Học Viện 2Ten 🔞 | vi | https://hv2tcomics.net |  | no title page found from the home page |
| KiraKira | vi | https://truyenkira.net |  | no title page found from the home page |
| LavibitWindroom | vi | https://lavibitwindroomgl.fun | Next.js | no title page found from the home page |
| LeesinComic | vi | https://leesincomic.com |  | Cloudflare |
| LuotTruyen | vi | https://luottruyen999.com |  | Cloudflare |
| Luvaholic | vi | https://luvaholic.website |  | no title page found from the home page |
| LxManga.org (unoriginal) 🔞 | vi | https://lxmanga.org |  | no title page found from the home page |
| MangaMori | vi | https://mangamori.dev |  | Cloudflare |
| MeDamTruyen | vi | https://saytongtaii.site |  | no title page found from the home page |
| MeoSSS | vi | https://meosss.com |  | Cloudflare |
| MiMi 🔞 | vi | https://mimihentai.moe |  | Cloudflare |
| MinoTruyen | vi | https://minotruyenv5.xyz | Next.js | no title page found from the home page |
| Otakusic | vi | https://otakusic.com |  | Cloudflare |
| OTruyen | vi | https://otruyen.cc |  | no title page found from the home page |
| QuaDaoCute | vi | https://qadcuteo.cc |  | Cloudflare |
| Roads Team 🔞 | vi | https://nhaduong.com |  | Cloudflare |
| SayHentai 🔞 | vi | https://sayhentai.cx |  | Cloudflare |
| Seikowo | vi | https://seikowo-app.blogspot.com | ZeistManga | no title page found from the home page |
| SinhSieuSao 🔞 | vi | https://sinhsieusao.com |  | no title page found from the home page |
| SoaiCaComic | vi | https://soaicacomic2.top |  | no title page found from the home page |
| SuicaoDex | vi | https://suicaodex.com |  | Cloudflare |
| Team Lanh Lung | vi | https://lanhlungteam3.top |  | no title page found from the home page |
| Thỏ Ham Ngủ | vi | https://thohamngu.xyz |  | no title page found from the home page |
| Truyen tranh dam my 🔞 | vi | https://truyentranhdammyy.site |  | Cloudflare |
| TruyenHentaivn 🔞 | vi | https://truyenhentaivn.store |  | no title page found from the home page |
| TruyenHentaiz 🔞 | vi | https://truyenhentaiz.net |  | Cloudflare |
| ViHentai 🔞 | vi | https://vi-hentai.moe |  | Cloudflare |
| ViTruyen | vi | https://vitruyen1.com | Next.js | no title page found from the home page |
| YuriGarden | vi | https://yurigarden.moe |  | Cloudflare |
| YuriNeko | vi | https://yurinekoz.com |  | Cloudflare |
| BiliManga | zh | https://www.bilimanga.net |  | no title page found from the home page |
| Cartoon18 🔞 | zh | https://www.cartoon18.com |  | Cloudflare |
| Creative Comic Collection | zh | https://www.creative-comic.tw |  | no title page found from the home page |
| Dm5 | zh | https://www.dm5.com | Iken | no title page found from the home page |
| GoDa | zh | https://baozimh.org |  | Cloudflare |
| Guazimanhua | zh | https://www.guazimanhua.com |  | no title page found from the home page |
| H-Comic 🔞 | zh | https://h-comic.com |  | no title page found from the home page |
| Hanime1 🔞 | zh | https://hanimeone.me |  | Cloudflare |
| Hikarinagi | zh | https://www.hikarinagi.org |  | Cloudflare |
| Iqiyi | zh | https://bud.m.iqiyi.com |  | no title page found from the home page |
| JComic 🔞 | zh | https://jcomic.net |  | no title page found from the home page |
| Komiic | zh | https://komiic.com |  | Cloudflare |
| Kuaikanmanhua | zh | https://www.kuaikanmanhua.com |  | no title page found from the home page |
| Mangabz | zh | https://mangabz.com |  | no title page found from the home page |
| Manhua160 | zh | https://www.mh160mh.com |  | no title page found from the home page |
| Manhuaren | zh | https://mangaapi.manhuaren.com |  | no title page found from the home page |
| Manhuashe | zh | https://www.311s.com |  | no title page found from the home page |
| Miaoqu Manhua | zh | https://www.miaoqumh.org |  | Cloudflare |
| Picacomic 🔞 | zh | https://manhuabika.com |  | no title page found from the home page |
| Roumanwu 🔞 | zh | https://rouman5.com |  | no title page found from the home page |
| Shenshi Huisuo | zh | https://www.hentaiclub.net |  | Cloudflare |
| Tencent Comics (ac.qq.com) | zh | https://m.ac.qq.com |  | no title page found from the home page |
| Terra Historicus | zh | https://comic.hypergryph.com |  | no title page found from the home page |
| Tongli | zh | https://ebook.tongli.com.tw |  | Cloudflare |
| Utifa | zh | https://bx.yaimer.com |  | Cloudflare |
| vomic | zh | https://vomicmh.com | Next.js | no title page found from the home page |
| WNACG 🔞 | zh | https://www.wnacg.buzz |  | no title page found from the home page |
| Xipi Manhua | zh | https://m.hipmh.com |  | Cloudflare |
| Zaimanhua | zh | https://manhua.zaimanhua.com |  | no title page found from the home page |
| Zazhimi | zh | https://www.zazhimi.net |  | no title page found from the home page |
| Zerobyw | zh | http://www.zerobyw33.com |  | no title page found from the home page |

## ➖ No comments (178)

| Extension | Lang | Site | Template | Notes |
|---|---|---|---|---|
| Comick (Unoriginal) | all | https://comick.live |  |  |
| ComicsKingdom | all | https://wp.comicskingdom.com | Next.js |  |
| Commit Strip | all | https://www.commitstrip.com |  |  |
| CosplayTele 🔞 | all | https://cosplaytele.com |  |  |
| Hennojin 🔞 | all | https://hennojin.com | Iken |  |
| HentaiHand 🔞 | all | https://hentaihand.com |  |  |
| HentaiLoop 🔞 | all | https://hentailoop.com |  |  |
| Honeytoon | all | https://honeytoon.com |  |  |
| Magical Translators | all | https://mahoushoujobu.com |  |  |
| Manga18fx 🔞 | all | https://manga18fx.com | MangaThemesia |  |
| Manhwa18.cc 🔞 | all | https://manhwa18.cc |  |  |
| Niadd | all | https://br.niadd.com |  |  |
| Rawkuma.me | all | https://rawkuma.me | Iken |  |
| Toomics 🔞 | all | https://global.toomics.com |  |  |
| XCOMIC | all | https://xcomic.me |  |  |
| xkcd | all | https://xkcd.com |  |  |
| YSK Comics | all | https://www.ysk-comics.com |  |  |
| Goon Scans 🔞 | ar | https://goonscans.org |  |  |
| MangaTime | ar | https://mangatime.org |  |  |
| Arven Scans | en | https://arvenscans.net |  |  |
| Battle In 5 Seconds After Meeting | en | https://www.deatte5.com | Madara |  |
| Broccoli Soup | en | https://politeandgood.com |  |  |
| Colorized Mangas | en | https://colorizedmangas.com | Next.js |  |
| Danke fürs Lesen | en | https://danke.moe |  |  |
| Dark Science | en | https://dresdencodak.com |  |  |
| Death Toll Scans | en | https://reader.deathtollscans.net |  |  |
| Drake Scans | en | https://drakecomic.net | Next.js |  |
| Elf Toon | en | https://elftoon.net | Next.js |  |
| Existential Comics | en | https://existentialcomics.com |  |  |
| EZmanga | en | https://ezmanga.org |  |  |
| Frieren Online | en | https://www.frieren.online | Madara |  |
| Guya | en | https://guya.cubari.moe | Blogger |  |
| Hachirumi | en | https://hachirumi.com |  |  |
| HentaiKisu 🔞 | en | https://hentaikisu.com |  |  |
| HentaiPill 🔞 | en | https://hentaipill.com |  |  |
| Hentara 🔞 | en | https://hentara.com |  |  |
| Hiveworks Comics | en | https://hiveworkscomics.com |  |  |
| HonkaiImpact3 | en | https://manga.honkaiimpact3.com |  |  |
| I Roved Out 🔞 | en | https://www.irovedout.com |  |  |
| KaliScan.org (unoriginal) | en | https://kaliscan.org | Madara | checked by hand |
| Kayn Scans | en | https://kaynscans.com | Next.js |  |
| keenspot | en | https://twokinds.keenspot.com |  |  |
| KeroScans | en | https://keroscans.net | Next.js |  |
| Kill Six Billion Demons | en | https://killsixbilliondemons.com |  |  |
| Kodansha | en | https://kodansha.us |  |  |
| KuraManga | en | https://kuramanga.com |  |  |
| LustToon | en | https://lustoon.com | Next.js |  |
| LuxManga | en | https://luxmanga.org | Liliana |  |
| Mahouirexnohentaikarte 🔞 | en | https://mahouirexnohentaikarte.com |  |  |
| MangaBolt | en | https://mangabolt.com |  |  |
| Mangafreak | en | https://ww3.mangafreak.me | Iken |  |
| Mangago | en | https://www.mangago.me | Iken |  |
| Mangamo | en | https://www.mangamo.com |  |  |
| Manganato | en | https://www.natomanga.com | MangaBox |  |
| MangaPill | en | https://mangapill.com |  |  |
| MangaPlaza | en | https://mangaplaza.com |  |  |
| MangaYi | en | https://mangayi.com |  |  |
| Manhwa18 🔞 | en | https://manhwa18.com |  |  |
| Manhwa18TX | en | https://manhwa18tx.com |  |  |
| Manhwaddict | en | https://manhwaddict.com |  |  |
| ManhwaGalaxy | en | https://manhwagalaxy.com |  |  |
| ManhwaUS 🔞 | en | https://manhwaus.net |  |  |
| NexComic | en | https://nexcomic.com | Iken |  |
| Oh Joy Sex Toy 🔞 | en | https://www.ohjoysextoy.com |  |  |
| Omoi | en | https://www.omoi.com |  | checked by hand |
| One Punch Man Online | en | https://w20.1punchman.com |  |  |
| Paradise Scans 🔞 | en | https://paradisescans.com |  |  |
| Qi Scans | en | https://qimanga.com |  | checked by hand |
| Read Attack on Titan Shingeki no Kyojin Manga | en | https://ww12.readsnk.com |  |  |
| Read Jujutsu Kaisen Manga Online | en | https://ww6.readjujutsukaisen.com |  |  |
| Read Nanatsu no Taizai 7 Deadly Sins Manga Online | en | https://ww8.read7deadlysins.com |  |  |
| Read One Piece Manga Online | en | https://ww13.readonepiece.com |  |  |
| Read One-Punch Man Manga Online | en | https://ww7.readopm.com |  |  |
| Read Solo Leveling Manga Manhwa Online | en | https://ww4.readsololeveling.org |  |  |
| Read Tokyo Ghoul Re & Tokyo Ghoul Manga Online | en | https://ww12.tokyoghoulre.com |  |  |
| Read Vagabond Manga | en | https://readbagabondo.com |  |  |
| ReiManga | en | https://reimanga.net | Next.js |  |
| Schale Scans | en | https://www.schalescans.com | Blogger |  |
| Schlock Mercenary | en | https://www.schlockmercenary.com |  |  |
| Tapas | en | https://tapas.io | Next.js |  |
| The Duck Webcomics | en | https://www.theduckwebcomics.com |  |  |
| The Girl from Random Chatting Manga Online | en | https://thegirlfromrandomchatting.com |  |  |
| ToonGod (Unoriginal) | en | https://toongod.cc |  |  |
| ToonGrab | en | https://toongrab.com | Next.js |  |
| Toonizy | en | https://toonizy.com | Madara | checked by hand |
| Toonz/Toonx | en | https://toonz.to | Next.js |  |
| TopManhua.fan | en | https://www.topmanhua.fan | Madara |  |
| Webnex | en | https://webnex.cc | Madara |  |
| WebtoonClub | en | https://webtoonclub.com | Next.js |  |
| WitchScans | en | https://witchtoons.net | Next.js |  |
| AKAYA | es | https://akaya.io |  |  |
| AnzManga | es | https://www.anzmanga25.com | Iken |  |
| Celestial Moon | es | https://lecturacelestialmoon.site |  |  |
| Colorcito Scan 🔞 | es | https://coloresito.site | Next.js |  |
| DoujinHentai 🔞 | es | https://doujinhentai.net |  |  |
| HentaiMode 🔞 | es | https://hentaimode.com |  |  |
| Ikuhentai 🔞 | es | https://ikuhentai.net | Madara |  |
| Lector Asteria | es | https://visor.chifa-tong.online | Next.js |  |
| LeerManhwas 🔞 | es | https://leermanhwas.com |  |  |
| Lolivault 🔞 | es | https://lector.lolivault.net |  |  |
| Manga Mukai | es | https://mangamukai.com |  |  |
| Mantraz Scan | es | https://mantrazscanss.lat | Next.js |  |
| Pzykosis666HFansub 🔞 | es | https://lector.pzykosis666hfansub.com |  |  |
| SkyMangas | es | https://skymangas.com |  |  |
| Spicy Scan | es | https://spicyseries.com | Next.js |  |
| TmoManhwa 🔞 | es | https://tmomanhwa.com |  |  |
| Traducciones Moonlight | es | https://traduccionesmoonlight.com | Next.js |  |
| FuryoSquad | fr | https://www.furyosociety.com |  |  |
| DreamTeams Scans 🔞 | id | https://dreamteams.space | Iken |  |
| Natsu | id | https://natsu.one |  |  |
| Pornhwa18 🔞 | id | https://pornhwa18.com |  |  |
| HentaiArchive 🔞 | it | https://www.hentai-archive.com |  |  |
| HentaiFantasy 🔞 | it | https://hentaifantasy.it |  |  |
| Juin Jutsu Team Reader | it | https://www.juinjutsureader.ovh |  |  |
| ZeurelScan | it | https://www.zeurelscan.com |  |  |
| BookWalker Japan | ja | https://bookwalker.jp |  |  |
| Ciao Plus | ja | https://ciao.shogakukan.co.jp |  |  |
| Comic Nettai | ja | https://www.comicnettai.com |  |  |
| Corona EX | ja | https://to-corona-ex.com | Next.js |  |
| CyComi | ja | https://cycomi.com | Next.js |  |
| Gangan Online | ja | https://www.ganganonline.com | Next.js |  |
| Ichicomi | ja | https://ichicomi.com | Next.js |  |
| Jump Rookie! | ja | https://rookie.shonenjump.com |  |  |
| KadoComi | ja | https://comic-walker.com | Next.js |  |
| Kiraboshi | ja | https://kirapo.jp | Iken |  |
| Kurage Bunch | ja | https://kuragebunch.com |  |  |
| Manga Kingdom | ja | https://comic.k-manga.jp |  |  |
| Manga Toshokan Z | ja | https://www.mangaz.com |  |  |
| MangaKuro | ja | https://mangakuro.net |  |  |
| MangaMeets | ja | https://manga-meets.jp | Next.js |  |
| MomonGA 🔞 | ja | https://momon-ga.com |  |  |
| Nikkangecchan | ja | https://nikkangecchan.jp |  |  |
| Raw UwU | ja | https://rawuwu.net |  |  |
| Rawdevart.art | ja | https://rawdevart.art |  |  |
| RawSakura | ja | https://rawsakura.org |  |  |
| Reader Store | ja | https://ebookstore.sony.jp | Next.js |  |
| Shonen Jump+ | ja | https://shonenjumpplus.com |  |  |
| Tonari no Young Jump | ja | https://tonarinoyj.jp |  |  |
| Twi4 | ja | https://sai-zen-sen.jp/comics/twi4 |  |  |
| Weekly Young Magazine | ja | https://yanmaga.jp |  |  |
| Young Jump+ | ja | https://ynjn.jp |  |  |
| Zenon | ja | https://comic-zenon.com |  |  |
| Naver Comic | ko | https://comic.naver.com |  |  |
| Argos Comics | pt | https://aniargos.com | Next.js |  |
| BRScans | pt | https://brscans.vercel.app | Next.js |  |
| ExHentai.net.br 🔞 | pt | https://exhentai.net.br |  |  |
| Fenix Project 🔞 | pt | https://fenixproject.website |  |  |
| Hentai Teca 🔞 | pt | https://hentaiteca.online | Madara |  |
| Hentai Tokyo 🔞 | pt | https://hentaitokyo.net |  |  |
| Mangas Brasuka | pt | https://mangasbrasuka.org | Next.js |  |
| Mugiwaras Oficial | pt | https://mugiwarasoficial.org | Next.js |  |
| Muito Hentai 🔞 | pt | https://www.muitohentai.com |  |  |
| PizzariaScan | pt | https://pizzariacomics.com | Iken |  |
| Portal Yaoi 🔞 | pt | https://portalyaoi.com | Madara |  |
| ZettaHQ 🔞 | pt | https://zettahq.com |  |  |
| Manga-shi | ru | https://manga-shi.org |  |  |
| NineGrid | ru | https://9grid.cc | Next.js |  |
| UniComics | ru | https://unicomics.ru |  |  |
| WaManga | ru | https://wamanga.ru |  |  |
| Manga168 | th | https://manga168x.com | Iken |  |
| MangaBlackCat | th | https://mangablackcat.com |  |  |
| Afrodit Scans | tr | https://afroditscans.com |  |  |
| Manga Kulesi | tr | https://mangakulesi.com |  |  |
| MangaDenizi | tr | https://mangadenizi.net |  |  |
| Tenshi Manga | tr | https://tenshimanga.com |  |  |
| ComixTopia | uk | https://comixtopia.in.ua | Next.js |  |
| DaoMeoDen | vi | https://daomeoden.net | Next.js |  |
| ThienThaiTruyen 🔞 | vi | https://thienthaitruyen16.com |  |  |
| Truyen Hentai 18+ 🔞 | vi | https://truyenhentai18.net |  |  |
| Truyen18 🔞 | vi | https://truyen18.co | Next.js |  |
| 92Manhua | zh | http://www.92mh.com |  |  |
| BH3 | zh | https://comic.bh3.com |  |  |
| BoyLove 🔞 | zh | https://boylove.cc |  |  |
| Comicabc | zh | https://www.8comic.com |  |  |
| Ikmmh 🔞 | zh | https://ymcdnyfqdapp.ikmmh.com |  |  |
| ManHuaGui | zh | https://www.manhuagui.com |  |  |
| NNHanman 🔞 | zh | https://nnhanman.xyz |  |  |
| Toptoon.net | zh | https://www.toptoon.net |  |  |

## ❌ Site down (313)

| Extension | Lang | Site | Template | Notes |
|---|---|---|---|---|
| Akuma 🔞 | all | https://akuma.moe |  | HTTP Error 403: Forbidden |
| BookOrbit | all | http://127.0.0.1:3000 |  | <urlopen error [Errno 111] Connection refused> |
| Comic Growl | all | https://comic-growl.com |  | HTTP Error 403: Forbidden |
| Danbooru 🔞 | all | https://danbooru.donmai.us |  | HTTP Error 403: Forbidden |
| Doujiva 🔞 | all | https://doujiva.com |  | HTTP Error 403: Forbidden |
| FoolSlide Customizable | all | https://127.0.0.1 |  | <urlopen error [Errno 111] Connection refused> |
| Komga | all | https://127.0.0.1:25600 |  | <urlopen error [Errno 111] Connection refused> |
| Kyokotsu | all | https://kyokotsu.com |  | <urlopen error timed out> |
| LANraragi | all | http://127.0.0.1:3000 |  | <urlopen error [Errno 111] Connection refused> |
| League of Legends | all | https://universe.leagueoflegends.com/en_us/comic/ |  | HTTP Error 404: Not Found |
| Luscious 🔞 | all | https://www.luscious.net |  | <urlopen error [Errno 104] Connection reset by peer> |
| Mango | all | http://127.0.0.1:9000 |  | <urlopen error [Errno 111] Connection refused> |
| Manhuarm | all | https://manhuarmtl.com |  | HTTP Error 403: Forbidden |
| Manhwa-raw 🔞 | all | https://manhwa-raw.com |  | HTTP Error 403: Forbidden |
| MyReadingManga 🔞 | all | https://myreadingmanga.info |  | HTTP Error 403: Forbidden |
| nHentai.com (unoriginal) 🔞 | all | https://nhentai.com |  | <urlopen error [Errno 104] Connection reset by peer> |
| OniSaga | all | https://onisaga.com |  | HTTP Error 403: Forbidden |
| Simply Hentai 🔞 | all | https://www.simply-hentai.com |  | <urlopen error [Errno 104] Connection reset by peer> |
| StashApp 🔞 | all | http://localhost:9999 |  | <urlopen error [Errno 111] Connection refused> |
| V2PH 🔞 | all | https://www.v2ph.com |  | HTTP Error 403: Forbidden |
| Xasiat Albums 🔞 | all | https://www.xasiat.com |  | HTTP Error 404: Not Found |
| Yabai 🔞 | all | https://yabai.si |  | HTTP Error 403: Forbidden |
| Arabs Hentai 🔞 | ar | https://arabshentai.com |  | HTTP Error 403: Forbidden |
| Area Manga | ar | https://ar.kenmanga.com |  | HTTP Error 403: Forbidden |
| Despair Manga | ar | https://despair-world.com |  | HTTP Error 403: Forbidden |
| Detective Conan Ar | ar | https://manga.detectiveconanar.com |  | HTTP Error 403: Forbidden |
| HentaiMan 🔞 | ar | https://hentaiman.net |  | HTTP Error 500: Internal Server Error |
| Hijala | ar | https://hijala.com |  | HTTP Error 403: Forbidden |
| MangaCloud | ar | https://mangacloud.online |  | <urlopen error [Errno -5] No address associated with hostnam |
| MangaDar | ar | https://mangadar.com |  | HTTP Error 403: Forbidden |
| MangaTek | ar | https://mangatek.com |  | HTTP Error 403: Forbidden |
| Onma | ar | https://onma.top |  | <urlopen error [Errno 111] Connection refused> |
| Paradise BL 🔞 | ar | https://paradise-bl.com |  | HTTP Error 403: Forbidden |
| StellarSaber | ar | https://stellarsaber.pro |  | HTTP Error 403: Forbidden |
| Utsukushii | bg | https://utsukushii-bg.com |  | <urlopen error timed out> |
| Evil production 🔞 | cs | https://evil-manga.eu |  | HTTP Error 403: Forbidden |
| Assorted Scans | en | https://assortedscans.com |  | <urlopen error [Errno 101] Network is unreachable> |
| Aunt Manhwa 🔞 | en | https://auntmanhwa.com |  | <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate  |
| Bakkin Self-hosted | en | http://127.0.0.1/ |  | <urlopen error [Errno 111] Connection refused> |
| BatCave | en | https://batcave.biz |  | HTTP Error 403: Forbidden |
| Borat Scans | en | https://boratscans.com |  | HTTP Error 403: Forbidden |
| BrainRotComics | en | https://brainrotcomics.com |  | HTTP Error 403: Forbidden |
| ComicK Fanmade | en | https://comickfan.com |  | The read operation timed out |
| Digital Comic Museum | en | https://digitalcomicmuseum.com |  | HTTP Error 403: Forbidden |
| DragonTea | en | https://dragontea.ink |  | HTTP Error 403: Forbidden |
| EbookRenta | en | https://www.ebookrenta.com |  | HTTP Error 503: Service Temporarily Unavailable |
| El Goonish Shive | en | https://www.egscomics.com |  | HTTP Error 426: Upgrade Required |
| Ero18x 🔞 | en | https://ero18x.com |  | HTTP Error 403: Forbidden |
| Gone with the Blastwave | en | https://www.blastwave-comic.com |  | <urlopen error [Errno -2] Name or service not known> |
| HentaiRead 🔞 | en | https://hentairead.com |  | HTTP Error 403: Forbidden |
| HotComics 🔞 | en | https://hotcomics.io |  | HTTP Error 403: Forbidden |
| Kaizen Scan 🔞 | en | https://kaizenscan.com |  | HTTP Error 403: Forbidden |
| Kissmanga.in | en | https://kissmanga.in |  | HTTP Error 403: Forbidden |
| Lgbtics 🔞 | en | https://lgbtics.com |  | HTTP Error 403: Forbidden |
| Luna Toons | en | https://lunatoons.net |  | HTTP Error 403: Forbidden |
| Madokami | en | https://manga.madokami.al |  | HTTP Error 401: Unauthorized |
| Magus Manga | en | https://magustoon.org |  | HTTP Error 403: Forbidden |
| Manga-Bay | en | https://manga-bay.biz |  | HTTP Error 403: Forbidden |
| MangaDot | en | https://mangadot.net |  | HTTP Error 403: Forbidden |
| MangaHe | en | https://mangahe.com |  | HTTP Error 404: Not Found |
| Mangatellers | en | https://reader.mangatellers.gr |  | HTTP Error 500: Internal Server Error |
| Manhua Zonghe 🔞 | en | https://www.manhuazonghe.com |  | HTTP Error 503: Service Unavailable |
| ManhuaUS | en | https://manhuaus.com |  | HTTP Error 403: Forbidden |
| Manhwa18.today 🔞 | en | https://www.manhwa18.today |  | HTTP Error 403: Forbidden |
| ManhwaManhua 🔞 | en | https://manhwamanhua.com |  | <urlopen error [Errno 104] Connection reset by peer> |
| ManhwaRead | en | https://manhwaread.com |  | HTTP Error 403: Forbidden |
| MeiToon | en | https://meitoon.org |  | HTTP Error 403: Forbidden |
| New Manhwa | en | https://saymanhwa.com |  | <urlopen error [Errno -2] Name or service not known> |
| Nortverse 🔞 | en | https://nortverse.com |  | HTTP Error 403: Forbidden |
| NovelCrow 🔞 | en | https://novelcrow.com |  | HTTP Error 403: Forbidden |
| Nuvia Toon | en | https://nuviatoon.net |  | <urlopen error [Errno -2] Name or service not known> |
| oots | en | https://www.giantitp.com |  | HTTP Error 403: Forbidden |
| Oppai Stream | en | https://read.oppai.stream |  | <urlopen error [Errno -2] Name or service not known> |
| OriYami | en | https://oriyami.com |  | The read operation timed out |
| Rage Scans | en | https://ragescans.com |  | HTTP Error 403: Forbidden |
| Raven Scans | en | https://ravenscans.org |  | HTTP Error 403: Forbidden |
| Read Black Clover Manga Online | en | https://ww10.readblackclover.com |  | <urlopen error [Errno -2] Name or service not known> |
| Read Comics Online | en | https://readcomicsonline.ru |  | HTTP Error 403: Forbidden |
| Saturday Morning Breakfast Comics | en | https://smbc-comics.com |  | HTTP Error 500: Internal Server Error |
| Setsu Scans | en | https://setsuscans.com |  | HTTP Error 403: Forbidden |
| Team Shadowi | en | https://www.team-shadowi.com |  | HTTP Error 403: Forbidden |
| The Blank 🔞 | en | https://theblank.net |  | HTTP Error 403: Forbidden |
| TodayManga | en | https://todaymanga.com |  | HTTP Error 502: Bad Gateway |
| ToonGod | en | https://www.toongod.org |  | HTTP Error 403: Forbidden |
| ToonHey 🔞 | en | https://toonhey.com |  | HTTP Error 403: Forbidden |
| Vision Haze | en | https://www.visionhaze.com |  | HTTP Error 403: Forbidden |
| VyvyManga | en | https://mangavyvy.net |  | HTTP Error 403: Forbidden |
| WebtoonScan | en | https://webtoonscan.com |  | <urlopen error timed out> |
| WebtoonXYZ | en | https://www.webtoon.xyz |  | HTTP Error 403: Forbidden |
| Wildtoon 🔞 | en | https://wildtoon.com |  | HTTP Error 403: Forbidden |
| XoManga | en | https://www.xomanga.site |  | HTTP Error 403: Forbidden |
| XYZ Comics 🔞 | en | https://xyzcomics.com |  | <urlopen error [Errno 104] Connection reset by peer> |
| Yaoihub 🔞 | en | https://yaoihub.org |  | HTTP Error 502: Bad Gateway |
| YaoiScan | en | https://yaoiscan.com |  | HTTP Error 403: Forbidden |
| BarManga | es | https://archiviumbar.com |  | HTTP Error 403: Forbidden |
| Bega Translation | es | https://begatranslation.com |  | HTTP Error 403: Forbidden |
| Bloom Scans | es | https://bloomscans.com |  | HTTP Error 403: Forbidden |
| BokugenTranslation | es | https://bokugents.com |  | HTTP Error 403: Forbidden |
| CapibaraTraductor | es | https://capibaratraductor.com |  | HTTP Error 403: Forbidden |
| ChoChoX 🔞 | es | https://chochox.com |  | HTTP Error 403: Forbidden |
| DragonTranslation.org | es | https://dragontranslation.org |  | HTTP Error 403: Forbidden |
| Emperor Scan | es | https://imperiomanhwa.com |  | HTTP Error 403: Forbidden |
| Es.Mi2Manga 🔞 | es | https://es.mi2manga.com |  | <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate  |
| Kumanga | es | https://www.kumanga.com |  | HTTP Error 403: Forbidden |
| LectorXD | es | https://lectorxd.com |  | HTTP Error 403: Forbidden |
| Lmtos | es | https://lmtos.net |  | HTTP Error 403: Forbidden |
| Manga Crab | es | https://es.mangacrab.org |  | HTTP Error 403: Forbidden |
| Manga Romance | es | https://mangaromance19.com |  | HTTP Error 403: Forbidden |
| MangaOni | es | https://manga-oni.com |  | HTTP Error 403: Forbidden |
| Mangas No Sekai | es | https://mangasnosekai.com |  | HTTP Error 403: Forbidden |
| Manhwa-Latino | es | https://manhwa-latino.com |  | HTTP Error 403: Forbidden |
| ManhwaOnline 🔞 | es | https://manhwa-online.com |  | HTTP Error 403: Forbidden |
| Mundo Manhwa 🔞 | es | https://mundomanhwa.com |  | <urlopen error [Errno -2] Name or service not known> |
| OrckuMangas 🔞 | es | https://orckumangas.com |  | HTTP Error 403: Forbidden |
| Plot Twist No Fansub | es | https://plotnofansub.com |  | HTTP Error 403: Forbidden |
| Taurus Fansub | es | https://lectortaurus.com |  | HTTP Error 403: Forbidden |
| TMOHentai (unoriginal) 🔞 | es | https://tmohentai.app |  | HTTP Error 403: Forbidden |
| Toon-es 🔞 | es | https://toon-es.com |  | HTTP Error 403: Forbidden |
| TopComicPorno.net 🔞 | es | https://topcomicporno.net |  | HTTP Error 403: Forbidden |
| VCPVMP 🔞 | es | https://vercomicsporno.com |  | HTTP Error 403: Forbidden |
| Ver Manhwas 🔞 | es | https://vermanhwa.com |  | HTTP Error 403: Forbidden |
| AnimeSama | fr | https://anime-sama.to |  | HTTP Error 403: Forbidden |
| Aniverse | fr | https://aniverse.fr |  | HTTP Error 403: Forbidden |
| Astral-Manga | fr | https://astral-manga.fr |  | HTTP Error 403: Forbidden |
| Banchan Scan | fr | https://banchanscan.fr |  | HTTP Error 403: Forbidden |
| BigSolo | fr | https://bigsolo.org |  | HTTP Error 403: Forbidden |
| Blossom Scans | fr | https://blossom-scans.com |  | HTTP Error 403: Forbidden |
| CrunchyScan | fr | https://crunchyscan.st |  | HTTP Error 403: Forbidden |
| Epsilon Scan 🔞 | fr | https://epsilonscan.to |  | HTTP Error 403: Forbidden |
| HentaiZone 🔞 | fr | https://hentaizone.xyz |  | HTTP Error 403: Forbidden |
| HentaiZone (Beta) 🔞 | fr | https://beta.hentaizone.xyz |  | HTTP Error 403: Forbidden |
| Lelscan | fr | https://lelscans.net |  | HTTP Error 404: Not Found |
| Ma Brute 🔞 | fr | https://mabrute.com |  | HTTP Error 403: Forbidden |
| Manga-Scantrad | fr | https://manga-scantrad.io |  | HTTP Error 403: Forbidden |
| MangaHub.fr | fr | https://mangahub.fr |  | HTTP Error 403: Forbidden |
| MangaMoins | fr | https://mangamoins.com |  | HTTP Error 403: Forbidden |
| Mangas-Origines.fr | fr | https://mangas-origines.fr |  | HTTP Error 403: Forbidden |
| Scan VF | fr | https://www.scan-vf.net |  | HTTP Error 403: Forbidden |
| Scan-Manga | fr | https://m.scan-manga.com |  | HTTP Error 404: Not Found |
| Soft Epsilon Scan | fr | https://epsilonsoft.to |  | HTTP Error 403: Forbidden |
| Solaris Scans | fr | https://solaris-scans.fr |  | HTTP Error 503: Service Unavailable |
| Sushi-Scan | fr | https://sushiscan.net |  | HTTP Error 403: Forbidden |
| Toon FR 🔞 | fr | https://toonfr.com |  | HTTP Error 403: Forbidden |
| X-Manga 🔞 | fr | https://x-manga.org |  | HTTP Error 403: Forbidden |
| YaoiScan 🔞 | fr | https://yaoiscan.fr |  | HTTP Error 504: Gateway Time-out |
| APKOMIK | id | https://01.apkomik.com |  | HTTP Error 403: Forbidden |
| Bacami | id | https://v1.bacami.site |  | HTTP Error 403: Forbidden |
| Doujinku 🔞 | id | https://doujinku.org |  | HTTP Error 403: Forbidden |
| Hwago | id | https://02.hwago.xyz |  | <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occur |
| Kaguya 🔞 | id | https://02.kaguya.pro |  | HTTP Error 403: Forbidden |
| Komik Dewasa Art 🔞 | id | https://komikdewasa.art |  | HTTP Error 403: Forbidden |
| Komikzoid | id | https://01.komikzoid.id |  | HTTP Error 403: Forbidden |
| Luvyaa | id | https://v5.luvyaa.co |  | HTTP Error 403: Forbidden |
| Mangakuri 🔞 | id | https://lc2.mangakuri.online |  | HTTP Error 403: Forbidden |
| ManhwaLand.mom 🔞 | id | https://02.manhwaland.land |  | HTTP Error 523: <none> |
| MG Komik | id | https://web1.mgkomik.cc |  | HTTP Error 403: Forbidden |
| OkyyKomik | id | https://www.okyykomik.my.id |  | <urlopen error [Errno -2] Name or service not known> |
| Roseveil | id | https://roseveil.org |  | <urlopen error [Errno -3] Temporary failure in name resoluti |
| Shinigami | id | https://11.shinigami.asia |  | HTTP Error 403: Forbidden |
| Shiro Doujin 🔞 | id | https://shirodoujin.com |  | HTTP Error 403: Forbidden |
| Soul Scans | id | https://v1.soulscans.org |  | <urlopen error [Errno -2] Name or service not known> |
| TheManga | id | https://themanga.site |  | HTTP Error 403: Forbidden |
| DDT Team | it | https://ddt.hastateam.com |  | HTTP Error 403: Forbidden |
| Hasta Team | it | https://reader.hastateam.com |  | HTTP Error 403: Forbidden |
| Hentai Zone 🔞 | it | https://hentaizone.me |  | HTTP Error 403: Forbidden |
| Walpurgi Scan | it | https://www.walpurgiscan.it |  | HTTP Error 403: Forbidden |
| Asacomi | ja | https://asacomi.jp |  | HTTP Error 403: Forbidden |
| Bibibi Comic | ja | https://bibibi-comic.com |  | HTTP Error 403: Forbidden |
| Big Comics | ja | https://bigcomics.jp |  | HTTP Error 403: Forbidden |
| Booklista Studio | ja | https://studio.booklista.co.jp |  | HTTP Error 403: Forbidden |
| C'moA | ja | https://www.cmoa.jp |  | HTTP Error 503: Service Temporarily Unavailable |
| Champion Cross | ja | https://championcross.jp |  | HTTP Error 403: Forbidden |
| Comic Grast | ja | https://novema.jp |  | HTTP Error 403: Forbidden |
| Comic Pash | ja | https://comicpash.jp |  | HTTP Error 403: Forbidden |
| Comic Ride | ja | https://comicride.jp |  | HTTP Error 403: Forbidden |
| Comic Room Base | ja | https://comic-room-base.com |  | HTTP Error 403: Forbidden |
| Comic Ryu | ja | https://comic-ryu.jp |  | HTTP Error 403: Forbidden |
| Comirela | ja | https://comirela.com |  | HTTP Error 403: Forbidden |
| DreComi+ | ja | https://drecomi-plus.jp |  | HTTP Error 403: Forbidden |
| FOD | ja | https://manga.fod.fujitv.co.jp |  | HTTP Error 403: Forbidden |
| G-Comi | ja | https://g-comi.jp |  | HTTP Error 403: Forbidden |
| Hachiraw | ja | https://hachiraw.net |  | HTTP Error 403: Forbidden |
| Hana To Yume+ | ja | https://hanayume.com |  | HTTP Error 403: Forbidden |
| HAYA Comic | ja | https://hayacomic.jp |  | HTTP Error 403: Forbidden |
| HERO'S Web | ja | https://heros-web.com |  | HTTP Error 403: Forbidden |
| Honto | ja | https://honto.jp |  | HTTP Error 403: Forbidden |
| J-N Books | ja | https://comic.j-nbooks.jp |  | HTTP Error 403: Forbidden |
| KimiComi | ja | https://kimicomi.com |  | HTTP Error 403: Forbidden |
| Kumaraw | ja | https://kumaraw.com |  | HTTP Error 403: Forbidden |
| Line Manga | ja | https://manga.line.me |  | HTTP Error 412: Precondition Failed |
| MagKan | ja | https://kansai.mag-garden.co.jp |  | HTTP Error 403: Forbidden |
| Manga SPA | ja | https://mangaspa.nikkan-spa.jp |  | HTTP Error 403: Forbidden |
| Manga Zegra | ja | https://manga-zegra.com |  | HTTP Error 403: Forbidden |
| MangaBang Comics | ja | https://comics.manga-bang.com |  | HTTP Error 403: Forbidden |
| MangaBu | ja | https://mangabu.jp |  | HTTP Error 403: Forbidden |
| Mangalt | ja | https://mangalt.jp |  | HTTP Error 403: Forbidden |
| Nami Comic | ja | https://namicomic.jp |  | HTTP Error 403: Forbidden |
| PiaComic | ja | https://piacomic.jp |  | HTTP Error 403: Forbidden |
| Raw Otaku | ja | https://rawotaku.com |  | The read operation timed out |
| RimacomiPlus | ja | https://rimacomiplus.jp |  | HTTP Error 403: Forbidden |
| Sokuyomi | ja | https://sokuyomi.jp |  | HTTP Error 405: Not Allowed |
| SoraRaw | ja | https://soraraw.com |  | HTTP Error 403: Forbidden |
| TakeComic | ja | https://takecomic.jp |  | HTTP Error 403: Forbidden |
| Young Animal | ja | https://younganimal.com |  | HTTP Error 403: Forbidden |
| Young Champion | ja | https://youngchampion.jp |  | HTTP Error 403: Forbidden |
| Newtoki (SBXH) | ko | https://sbxh9.com |  | HTTP Error 403: Forbidden |
| Acervo Hentai 🔞 | pt | https://acervohentai.com |  | HTTP Error 403: Forbidden |
| Amuy | pt | https://apenasmaisumyaoi.com |  | HTTP Error 403: Forbidden |
| Bladetoons | pt | https://bladetoons.com |  | HTTP Error 404: Not Found |
| Cerise Scan | pt | https://loverstoon.net |  | The read operation timed out |
| Fleur Blanche 🔞 | pt | https://fbsquadx.com |  | <urlopen error [Errno -2] Name or service not known> |
| Hentai Season 🔞 | pt | https://hentaiseason.com |  | HTTP Error 403: Forbidden |
| Hentai Teca.net 🔞 | pt | https://hentaiteca.net |  | HTTP Error 403: Forbidden |
| Hipertoon | pt | https://hipertoon.com |  | HTTP Error 403: Forbidden |
| KivaraToons | pt | https://kivaratoons.com |  | <urlopen error [SSL: TLSV1_ALERT_INTERNAL_ERROR] tlsv1 alert |
| KuroMangas | pt | https://kuromangas.com |  | HTTP Error 403: Forbidden |
| Leitor de Mangas | pt | https://leitordemangas.com |  | HTTP Error 403: Forbidden |
| Little Tyrant | pt | https://tiraninha.world |  | HTTP Error 403: Forbidden |
| Lura Toon | pt | https://luratoons.net |  | HTTP Error 403: Forbidden |
| Lycan Toons | pt | https://lycantoons.com |  | HTTP Error 403: Forbidden |
| Maid Scan | pt | https://empreguetes.wtf |  | HTTP Error 403: Forbidden |
| Manga Flix | pt | https://mangaflix.net |  | HTTP Error 403: Forbidden |
| Manga NXY | pt | https://manganyx.com |  | HTTP Error 403: Forbidden |
| Manga Stop | pt | https://mangastop.net |  | HTTP Error 403: Forbidden |
| MangaDash | pt | https://mangadash.net |  | HTTP Error 403: Forbidden |
| MiniTwo Scan | pt | https://minitwoscan.com |  | HTTP Error 403: Forbidden |
| Nexus Toons | pt | https://nexustoons.com |  | HTTP Error 403: Forbidden |
| NoxManga | pt | https://noxmangas.org |  | HTTP Error 403: Forbidden |
| Saikai Scan | pt | https://housesaikai.net |  | HTTP Error 403: Forbidden |
| Starlight Scan 🔞 | pt | https://starligthscan.com |  | <urlopen error [Errno 111] Connection refused> |
| TaimuMangas | pt | https://beta.taimumangas.com |  | HTTP Error 403: Forbidden |
| Tia Manhwa 🔞 | pt | https://tiamanhwa.com |  | HTTP Error 403: Forbidden |
| ToonLivre | pt | https://toonlivre.net |  | <urlopen error [Errno -2] Name or service not known> |
| XXX Yaoi 🔞 | pt | https://3xyaoi.com |  | HTTP Error 403: Forbidden |
| Yaoi Fan Club | pt | https://yaoifanclub.com |  | HTTP Error 403: Forbidden |
| Yomu Comics | pt | https://yomu.com.br |  | HTTP Error 403: Forbidden |
| Com-X | ru | https://ru.com-x.life |  | HTTP Error 403: Forbidden |
| HenChan 🔞 | ru | https://xxl.hentaichan.live |  | The read operation timed out |
| MangaBuff | ru | https://mangabuff.ru |  | HTTP Error 403: Forbidden |
| MangaChan | ru | https://im.manga-chan.me |  | HTTP Error 502: Bad Gateway |
| MangaLib | ru | https://mangalib.me |  | HTTP Error 403: Forbidden |
| MangaMen | ru | https://mangamen.com |  | HTTP Error 403: Forbidden |
| MintManga | ru | https://2.mintmanga.one |  | HTTP Error 404: Not Found |
| Nude-Moon 🔞 | ru | https://nude-moon.org |  | HTTP Error 403: Forbidden |
| Senkognito 🔞 | ru | https://senkuro.me |  | HTTP Error 403: Forbidden |
| Senkuro | ru | https://senkuro.me |  | HTTP Error 403: Forbidden |
| Usagi | ru | https://web.usagi.one |  | HTTP Error 404: Not Found |
| YagamiProject | ru | https://read.yagami.me |  | <urlopen error timed out> |
| YaoiChan 🔞 | ru | https://yaoi-chan.me |  | The read operation timed out |
| Arcura Fansub | tr | https://arcurafansub.com |  | HTTP Error 403: Forbidden |
| gafeland | tr | https://gafeland.com |  | HTTP Error 403: Forbidden |
| Gaiatoon | tr | https://gaiatoon.com |  | HTTP Error 403: Forbidden |
| Gölge Bahçesi | tr | https://golgebahcesi.com |  | HTTP Error 403: Forbidden |
| Hattori Manga 🔞 | tr | https://hattorimanga.net |  | HTTP Error 403: Forbidden |
| Hattori Scans | tr | https://hattoriscans.com |  | HTTP Error 403: Forbidden |
| Hayalistic | tr | https://hayalistic.online |  | HTTP Error 403: Forbidden |
| JuraTempest | tr | https://juratempe.st |  | HTTP Error 530: <none> |
| Koreli Scans | tr | https://www.nabicix.com |  | HTTP Error 403: Forbidden |
| Manga Kusu | tr | https://mangakusu.com |  | HTTP Error 403: Forbidden |
| Manga Portalı | tr | https://www.mangaportali.com |  | HTTP Error 403: Forbidden |
| Manga-TR | tr | https://manga-tr.com |  | HTTP Error 403: Forbidden |
| MangaWT | tr | https://mangawt.com |  | HTTP Error 403: Forbidden |
| Mangitto 🔞 | tr | https://mangtto.com |  | HTTP Error 403: Forbidden |
| Merlin Scans | tr | https://merlintoon.com |  | HTTP Error 403: Forbidden |
| MilaSub | tr | https://millascan.com |  | HTTP Error 403: Forbidden |
| Minda Fansub 🔞 | tr | https://mindafansub.dev |  | HTTP Error 502: Bad Gateway |
| Nirvana Manga | tr | https://nirvanamanga.com |  | HTTP Error 521: <none> |
| Nivera Fansub | tr | https://niverafansub.dev |  | HTTP Error 403: Forbidden |
| Nora Scans | tr | https://norascans.com |  | HTTP Error 502: Bad Gateway |
| OkuToon | tr | https://okutoon.com |  | HTTP Error 403: Forbidden |
| Paradox Scans | tr | https://paradoxscans.com |  | HTTP Error 403: Forbidden |
| Pati Manga | tr | https://www.patimanga.com |  | HTTP Error 403: Forbidden |
| Serein Scan | tr | https://sereinscan.com |  | HTTP Error 403: Forbidden |
| Siyah Melek 🔞 | tr | https://siyahmelek.my |  | HTTP Error 403: Forbidden |
| Stray Fansub 🔞 | tr | https://strayfansub.buzz |  | HTTP Error 403: Forbidden |
| Webtoon Hatti | tr | https://webtoonhatti.club |  | HTTP Error 403: Forbidden |
| Yaoi Flix 🔞 | tr | https://yaoiflix.fit |  | HTTP Error 500: Internal Server Error |
| Yaoi Manga Oku 🔞 | tr | https://yaoimangaoku.net |  | HTTP Error 403: Forbidden |
| CBHentai 🔞 | vi | https://2tencb.pro |  | HTTP Error 403: Forbidden |
| DocTruyen3Q | vi | https://doctruyen3qhub.fit |  | HTTP Error 403: Forbidden |
| FastScan | vi | https://fastscan.org |  | HTTP Error 403: Forbidden |
| FoxTruyen | vi | https://foxtruyen2.com |  | HTTP Error 403: Forbidden |
| Goc Truyen Tranh | vi | https://goctruyentranh.com |  | The read operation timed out |
| Goc Truyen Tranh Vui | vi | https://goctruyentranhvui41.com |  | HTTP Error 403: Forbidden |
| HentaiVN.plus 🔞 | vi | https://hentaivn.show |  | HTTP Error 530: <none> |
| HentaiVNx 🔞 | vi | https://www.hentaivnx.com |  | HTTP Error 403: Forbidden |
| KhoManhwa 🔞 | vi | https://khomanhwa.com |  | The read operation timed out |
| LuvEvaLand | vi | https://luvevalands2.co |  | HTTP Error 403: Forbidden |
| MiMiHentai 🔞 | vi | https://mimihentai.net |  | HTTP Error 403: Forbidden |
| MoeTruyen | vi | https://moetruyen.net |  | HTTP Error 403: Forbidden |
| MoeTruyenSuiCao (unoriginal) | vi | https://moe.suicaodex.com |  | HTTP Error 502: Bad Gateway |
| NetTruyenCO (unoriginal) | vi | https://nettruyenar.com |  | HTTP Error 403: Forbidden |
| NetTruyenViet (unoriginal) | vi | https://nettruyenviet10.com |  | HTTP Error 403: Forbidden |
| NetTruyenX (unoriginal) | vi | https://nettruyenx.net |  | HTTP Error 403: Forbidden |
| NhatTruyen | vi | https://nhattruyenqq.com |  | HTTP Error 403: Forbidden |
| Panomic | vi | https://panomic.online |  | HTTP Error 403: Forbidden |
| Top Truyen | vi | https://www.toptruyenzone13.com |  | HTTP Error 403: Forbidden |
| Tranh18 🔞 | vi | https://tranh18.cc |  | The read operation timed out |
| TruyenGGVN | vi | https://truyenggvn.com |  | HTTP Error 403: Forbidden |
| TruyenQQ | vi | https://truyenqqko.com |  | HTTP Error 403: Forbidden |
| TruyenQQ VN | vi | https://truyenqq.com.vn |  | HTTP Error 403: Forbidden |
| TuLinhTruyen | vi | https://api.tulinh.workers.dev |  | HTTP Error 404: Not Found |
| UmeTruyen 🔞 | vi | https://umetruyenz.org |  | <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occur |
| 18Manhua | zh | https://18mh.org |  | HTTP Error 403: Forbidden |
| Baka Manhua 🔞 | zh | https://bakamh.com |  | HTTP Error 403: Forbidden |
| Baozi Manhua | zh | https://cn.baozimh.com |  | HTTP Error 403: Forbidden |
| Dumanwu | zh | https://m.dumanwu1.com |  | <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate  |
| HanabiManga | zh | https://uhkvqrxmcapgtpspglrp.moedot.net |  | HTTP Error 404: Not Found |
| Jinman Tiantang 🔞 | zh | https://18comic.vip |  | HTTP Error 403: Forbidden |
| MyComic | zh | https://mycomic.com |  | HTTP Error 403: Forbidden |
| NoyAcg | zh | https://api.noyteam.online |  | HTTP Error 404: Not Found |
| Rumanhua | zh | https://m.rumanhua2.com |  | <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate  |
| YKMH | zh | https://www.ykmh.net |  | HTTP Error 403: Forbidden |

---

Regenerate after a new survey with `checklist.py` (see the repo history); edit rows by hand when you confirm a feature.
