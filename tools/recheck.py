"""Re-checks surveyed sites for comment systems added after the first survey.

Reads tools/survey.jsonl, re-opens the title page of every site still marked "rule" or "none"
in checklist.json, and adds what it finds as `systems2` to tools/recheck.jsonl.
"""
import concurrent.futures as cf
import json
import re
import sys
import urllib.request

UA = "Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1"
MARKERS = [
    ("Manga Comments Pro", r'id="mcp-list"|class="mcp-thread'),
    ("Manga Comments System", r'class="mcs-comment"'),
    ("Article comments", r'<article id="div-comment-\d+" class="comment-body'),
    ("Livewire discussion", r'data-testid="comment-discussion"'),
    ("Discourse", r'data-discourse-url=|DiscourseEmbed|discourse-comments'),
    ("Blogger", r"<meta content=['\"]blogger['\"] name=['\"]generator|name=['\"]generator['\"] content=['\"]blogger"),
    ("zmio", r"zmio\.org/post"),
    ("QQ Comment Service", r'id="comment-wrapper"\s+data-model='),
    ("Koe comments", r"<koe-comments"),
]


def check(row):
    url = row.get("title") or row.get("home")
    if not url:
        return {"pkg": row["pkg"], "systems2": []}
    try:
        request = urllib.request.Request(url, headers={"User-Agent": UA})
        page = urllib.request.urlopen(request, timeout=15).read(1_500_000).decode("utf-8", "replace")
    except Exception as error:
        return {"pkg": row["pkg"], "systems2": [], "error": str(error)[:80]}
    return {"pkg": row["pkg"], "systems2": [name for name, pattern in MARKERS if re.search(pattern, page, re.I)]}


def main():
    survey, checklist, out = sys.argv[1], sys.argv[2], sys.argv[3]
    rows = {json.loads(line)["pkg"]: json.loads(line) for line in open(survey)}
    wanted = [rows[e["pkg"]] for e in json.load(open(checklist)) if e["status"] in ("rule", "none") and e["pkg"] in rows]
    print(len(wanted), "to re-check", flush=True)
    with open(out, "w") as handle, cf.ThreadPoolExecutor(16) as pool:
        for result in pool.map(check, wanted):
            handle.write(json.dumps(result) + "\n")


if __name__ == "__main__":
    main()
