"""Builds TweComments' CHECKLIST.md and checklist.json from the survey results.

Statuses:
  complete  - rule written and every feature it supports checked by hand
  works     - rule written (or a comment system Twe reads everywhere); reading checked or expected
  rule      - comments found, but Twe needs a rule for them
  none      - no comments found on the site
  check     - the site blocks scripts (Cloudflare); check in the app
  unsupported - a comment system Twe can't read (Facebook)
  down      - the site didn't answer
"""
import json
import sys

SURVEY, OUT_MD, OUT_JSON = sys.argv[1], sys.argv[2], sys.argv[3]

# Rules written and checked by hand. Feature values: yes, no (site has none), wait (written,
# needs a signed-in account to confirm), "-" (not supported by the rule yet).
MANUAL = {
    "eu.kanade.tachiyomi.extension.en.mangareadorg": dict(system="wpDiscuz", rule="madara-wpdiscuz", read="yes", replies="yes",
                                                          like="wait", comment="wait", login="WordPress", status="works",
                                                          note="886 title / 436 chapter comments read; View replies checked"),
    "eu.kanade.tachiyomi.extension.en.mangarawclub": dict(system="Own API", rule="mangageko", read="yes", replies="yes",
                                                          like="wait", comment="wait", login="Site", status="works",
                                                          note="title and chapter comments read; actions need sign-in to confirm"),
    "eu.kanade.tachiyomi.extension.en.asurascans": dict(system="Own API", rule="asura", read="yes", replies="yes", like="-",
                                                        comment="-", login="-", status="complete",
                                                        note="331 title / 323 chapter comments, paging, GIFs"),
    "eu.kanade.tachiyomi.extension.all.mangadex": dict(system="Forum", rule="mangadex", read="yes", replies="-", like="-",
                                                       comment="-", login="-", status="complete",
                                                       note="forum threads via MangaDex API; quotes inline"),
    "eu.kanade.tachiyomi.extension.en.weebcentral": dict(system="Own", rule="weebcentral", read="yes", replies="-", like="-",
                                                         comment="-", login="-", status="complete", note="title and chapter"),
    "eu.kanade.tachiyomi.extension.en.mangakatana": dict(system="Own API", rule="mangakatana", read="yes", replies="yes",
                                                         like="-", comment="-", login="-", status="complete", note="71 comments read"),
    # English pass (2026-11-04): platforms checked and ruled.
    "eu.kanade.tachiyomi.extension.en.asmotoon": dict(system="zmio", rule="zmio", read="yes", replies="yes", like="-", comment="-",
                                                      login="-", status="complete", note="zmio API; 2 comments read on a sample"),
    "eu.kanade.tachiyomi.extension.en.sirenscans": dict(system="zmio", rule="zmio", read="yes", replies="yes", like="-", comment="-",
                                                        login="-", status="works", note="same zmio setup as Asmodeus"),
    "eu.kanade.tachiyomi.extension.en.mangabat": dict(system="QQ Comment Service", rule="qq-comments", read="yes", replies="yes",
                                                      like="wait", comment="wait", login="Site", status="works", note="API read; like/reply written"),
    "eu.kanade.tachiyomi.extension.en.mangakakalot": dict(system="QQ Comment Service", rule="qq-comments", read="yes", replies="yes",
                                                          like="wait", comment="wait", login="Site", status="works", note="API answers"),
    "eu.kanade.tachiyomi.extension.en.kunmangaonline": dict(system="QQ Comment Service", rule="qq-comments", read="yes", replies="yes",
                                                            like="wait", comment="wait", login="Site", status="works", note="API answers"),
    "eu.kanade.tachiyomi.extension.en.zinmanganet": dict(system="QQ Comment Service", rule="qq-comments", read="yes", replies="yes",
                                                         like="wait", comment="wait", login="Site", status="works", note="API answers"),
    "eu.kanade.tachiyomi.extension.all.comicfury": dict(system="Own (in page)", rule="comicfury", read="yes", replies="-", like="-",
                                                        comment="-", login="-", status="complete", note="comments in the page"),
    "eu.kanade.tachiyomi.extension.all.saymanhwa": dict(system="Own (in page)", rule="saymanhwa", read="yes", replies="-", like="-",
                                                        comment="-", login="-", status="complete", note="comments in the page"),
    "eu.kanade.tachiyomi.extension.en.shojoscans": dict(system="Manga Comments System", rule="global: mcs", read="yes", replies="yes",
                                                        like="-", comment="-", login="-", status="complete", note="17 comments on a sample"),
    "eu.kanade.tachiyomi.extension.en.yaoiscanme": dict(system="Article comments", rule="global: comment-body-articles", read="yes",
                                                        replies="-", like="-", comment="-", login="-", status="complete",
                                                        note="posting needs a guest name (not in Twe yet)"),
}

# Checked by hand: what's there and what a rule still needs.
NOTES = {
    "eu.kanade.tachiyomi.extension.en.zazamanga": "QQ Comment Service, but its list API refuses (405)",
    "eu.kanade.tachiyomi.extension.en.manhwaonline": "Article comments platform (global rule); none on the sampled title",
    "eu.kanade.tachiyomi.extension.en.myreadingcomic": "Article comments platform (global rule); none on the sampled title",
    "eu.kanade.tachiyomi.extension.en.fourporncomic": "Article comments platform (global rule); none on the sampled title",
    "eu.kanade.tachiyomi.extension.all.manga18me": "same /api/comment platform as ManhwaOnline (unconfirmed)",
    "eu.kanade.tachiyomi.extension.all.mangadna": "same /api/comment platform as ManhwaOnline (unconfirmed)",
    "eu.kanade.tachiyomi.extension.en.manga18club": "/api/comments (unconfirmed)",
    "eu.kanade.tachiyomi.extension.en.aethonwebcomics": "WordPress REST: /wp-json/modfarm/v1/comments/{id}/batch",
    "eu.kanade.tachiyomi.extension.en.otranslations": "Own API: /api/comments/v1",
    "eu.kanade.tachiyomi.extension.en.artlapsa": "React discussion component (same as RitharScans, Kitsune Dawn)",
    "eu.kanade.tachiyomi.extension.en.ritharscans": "React discussion component (same as Art Lapsa)",
    "eu.kanade.tachiyomi.extension.en.kitsunedawn": "React discussion component (same as Art Lapsa)",
    "eu.kanade.tachiyomi.extension.en.aquamanga": "Manga Comments Pro WordPress plugin",
    "eu.kanade.tachiyomi.extension.en.kensscan": "Own WordPress plugin (kensscan-comments)",
    "eu.kanade.tachiyomi.extension.en.coffeemangaunoriginal": "Comments behind a sign-in gate",
    "eu.kanade.tachiyomi.extension.en.swordscomic": "Discourse embed",
    "eu.kanade.tachiyomi.extension.en.manhwaz": "Astro CommentPanel",
    "eu.kanade.tachiyomi.extension.en.kaliscansorg": "Loaded by script (getComments)",
    "eu.kanade.tachiyomi.extension.en.mangamob": "Loaded by script",
}

# Flagged by the survey, but checked: no comment section.
NO_COMMENTS = {"Toonizy", "KaliScan.org (unoriginal)", "Qi Scans", "Omoi"}

OTHER_SYSTEMS = {"Commento", "Remark42", "Cusdis", "Giscus", "Utterances", "Hyvor", "GraphComment", "Valine", "Twikoo"}

ICON = {"yes": "✅", "no": "—", "wait": "⏳", "-": "—", None: "—"}
STATUS = {
    "complete": ("✅ Complete", "Rule written and checked by hand for everything it supports."),
    "works": ("🟢 Works", "Reading works (checked, or through a comment system Twe reads on any site). Liking and posting need a signed-in check."),
    "rule": ("🔍 Needs rule", "The site has comments, but in a form Twe needs a rule for."),
    "unsupported": ("⚠️ Unsupported", "Facebook comments: only shown inside Facebook's frame. Twe offers WebView."),
    "check": ("🛡️ Check in app", "The site blocks scripts (Cloudflare), so this survey couldn't see it. Open Comments in Twe to check."),
    "none": ("➖ No comments", "No comment section found on the site."),
    "down": ("❌ Site down", "The site didn't answer, or the extension has no site."),
}
ORDER = ["complete", "works", "rule", "unsupported", "check", "none", "down"]


def classify(row):
    pkg = row["pkg"]
    if pkg in MANUAL:
        return dict(MANUAL[pkg])
    if row.get("name") in NO_COMMENTS:
        return dict(status="none", note="checked by hand")
    result = row.get("result")
    if result in ("unreachable", "no-site"):
        return dict(status="down", note=row.get("error", "")[:60])
    if result in ("blocked", "blocked-title"):
        return dict(status="check", note="Cloudflare")
    systems = row.get("systems") or []
    if "wpDiscuz" in systems:
        return dict(status="works", system="wpDiscuz", rule="global: wpdiscuz", read="yes", replies="yes", like="wait",
                    comment="wait", login="WordPress", note="recognised on the page")
    if "Disqus" in systems:
        return dict(status="works", system="Disqus", rule="global: disqus", read="yes", replies="yes", like="-", comment="-",
                    login="-", note="recognised on the page")
    if "WordPress" in systems:
        return dict(status="works", system="WordPress", rule="global: wordpress", read="yes", replies="yes", like="-",
                    comment="-", login="-", note="recognised on the page")
    if "Facebook" in systems:
        return dict(status="unsupported", system="Facebook")
    other = [s for s in systems if s in OTHER_SYSTEMS]
    if other:
        return dict(status="rule", system=other[0])
    if row.get("endpoints") or (row.get("commentWords", 0) >= 8 and row.get("title")):
        hint = ", ".join(row.get("endpoints") or [])[:80]
        return dict(status="rule", system="Own", note=hint or f'{row.get("commentWords")} mentions of "comment"')
    if not row.get("title"):
        return dict(status="check", note="no title page found from the home page")
    return dict(status="none")


def main():
    rows = [json.loads(line) for line in open(SURVEY)]
    entries = []
    for row in rows:
        info = classify(row)
        entries.append({**{k: row.get(k) for k in ("pkg", "name", "lang", "nsfw", "home", "sources", "theme")}, **info})
    for entry in entries:
        if entry["pkg"] in NOTES and entry["status"] in ("rule", "check", "none"):
            entry["status"] = "rule"
            entry["note"] = "Checked: " + NOTES[entry["pkg"]]
    entries.sort(key=lambda e: (ORDER.index(e["status"]), e["lang"], e["name"].lower()))
    json.dump(entries, open(OUT_JSON, "w"), indent=1, ensure_ascii=False)

    counts = {status: sum(1 for e in entries if e["status"] == status) for status in ORDER}
    lines = ["# Comment support checklist", "",
             f"Every extension in keiyoushi's repository ({len(entries)}), surveyed for its site's comment system.",
             "Each site was opened once (home page, then one title page) and checked for known comment systems.",
             "Rows marked by hand were tested in a browser; update them here when something is confirmed or changes.", "",
             "| Status | Count | Meaning |", "|---|---|---|"]
    for status in ORDER:
        label, meaning = STATUS[status]
        lines.append(f"| {label} | {counts[status]} | {meaning} |")
    lines += ["", "Feature columns: ✅ works · ⏳ written, needs a signed-in check · — not available.", ""]
    for status in ORDER:
        group = [e for e in entries if e["status"] == status]
        if not group:
            continue
        label, _ = STATUS[status]
        lines += [f"## {label} ({len(group)})", ""]
        if status in ("complete", "works"):
            lines += ["| Extension | Lang | Comments | Rule | Read | Replies | Like | Comment / reply | Sign-in | Notes |",
                      "|---|---|---|---|---|---|---|---|---|---|"]
            for e in group:
                lines.append(f'| {e["name"]}{" 🔞" if e.get("nsfw") else ""} | {e["lang"]} | {e.get("system", "")} | {e.get("rule", "")} | '
                             f'{ICON[e.get("read")]} | {ICON[e.get("replies")]} | {ICON[e.get("like")]} | {ICON[e.get("comment")]} | '
                             f'{e.get("login", "—")} | {e.get("note", "")} |')
        else:
            lines += ["| Extension | Lang | Site | Template | Notes |", "|---|---|---|---|---|"]
            for e in group:
                lines.append(f'| {e["name"]}{" 🔞" if e.get("nsfw") else ""} | {e["lang"]} | {e.get("home") or ""} | {e.get("theme") or ""} | '
                             f'{(e.get("system") + ": " if e.get("system") else "") + (e.get("note") or "")} |')
        lines.append("")
    lines += ["---", "", "Regenerate after a new survey with `checklist.py` (see the repo history); edit rows by hand when you confirm a feature.", ""]
    open(OUT_MD, "w").write("\n".join(lines))
    print(counts)


if __name__ == "__main__":
    main()
