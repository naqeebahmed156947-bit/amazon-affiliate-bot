import json, os, requests

TOKEN=os.getenv("TELEGRAM_TOKEN")
CHANNEL=os.getenv("TELEGRAM_CHANNEL")

if not TOKEN:
    raise Exception("TELEGRAM_TOKEN is missing")
if not CHANNEL:
    raise Exception("TELEGRAM_CHANNEL is missing")

with open("posts.json","r",encoding="utf-8") as f:
    posts=json.load(f)

for post in posts:
    text=post.get("text")
    if not text:
        continue
    r=requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={"chat_id":CHANNEL,"text":text}
    )
    print(r.status_code,r.text)
