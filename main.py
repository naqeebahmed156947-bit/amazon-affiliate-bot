import json
import os
import requests
from datetime import datetime

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHANNEL = os.getenv("TELEGRAM_CHANNEL")

if not TOKEN:
    raise Exception("TELEGRAM_TOKEN is missing")

if not CHANNEL:
    raise Exception("TELEGRAM_CHANNEL is missing")


# قراءة المنتجات
with open("posts.json", "r", encoding="utf-8") as f:
    posts = json.load(f)


# اختيار أول منتج لم يتم نشره
selected = None

for post in posts:
    if not post.get("posted", False):
        selected = post
        break


if not selected:
    # إعادة التدوير عند انتهاء المنتجات
    for post in posts:
        post["posted"] = False

    selected = posts[0]


text = f"""
🔥 عرض اليوم

📦 {selected.get('name','منتج مميز')}

⭐ منتج مطلوب وعليه عروض

🛒 اطلبه الآن:
{selected.get('url')}

#أمازون
#عروض
"""


# النشر في تيليجرام
r = requests.post(
    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    data={
        "chat_id": CHANNEL,
        "text": text
    }
)

print(r.status_code, r.text)


# تحديث حالة النشر
selected["posted"] = True
selected["last_post"] = str(datetime.now())


with open("posts.json", "w", encoding="utf-8") as f:
    json.dump(posts, f, ensure_ascii=False, indent=4)
