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
}

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
