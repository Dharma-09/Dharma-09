import requests
from datetime import datetime

USERNAME = "YOUR_GITHUB_USERNAME"
MAX_ITEMS = 10

events = requests.get(
    f"https://api.github.com/users/{USERNAME}/events/public"
).json()

items = []

for e in events:
    if e["type"] != "PullRequestEvent":
        continue

    pr = e["payload"]["pull_request"]
    repo = e["repo"]["name"]
    number = pr["number"]
    url = pr["html_url"]

    if pr["merged"]:
        icon = "🎉"
        status = "Merged PR"
    elif e["payload"]["action"] == "closed":
        icon = "📫"
        status = "Closed PR"
    else:
        continue

    items.append(f"- {icon} **{status}** [#{number}]({url}) — `{repo}`")

    if len(items) >= MAX_ITEMS:
        break

content = "\n".join(items)

with open("README.md", "r") as f:
    readme = f.read()

start = "<!-- ACTIVITY:START -->"
end = "<!-- ACTIVITY:END -->"

block = f"{start}\n{content}\n{end}"

if start in readme:
    import re
    readme = re.sub(
        f"{start}[\\s\\S]*?{end}",
        block,
        readme,
    )
else:
    readme += "\n\n## 🚀 Open Source Activity\n\n" + block

with open("README.md", "w") as f:
    f.write(readme)
