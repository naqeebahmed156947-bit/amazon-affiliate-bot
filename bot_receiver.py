import os
import json
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("TELEGRAM_TOKEN")

if not TOKEN:
    raise Exception("TELEGRAM_TOKEN is missing")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "أهلاً 👋\n"
        "أرسل رابط منتج أمازون لإضافته للقائمة."
    )


async def add_product(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text.strip()

    products = []

    if os.path.exists("posts.json"):
        with open("posts.json", "r", encoding="utf-8") as f:
            products = json.load(f)

    products.append({
        "name": "منتج جديد",
        "url": url,
        "posted": False
    })

    with open("posts.json", "w", encoding="utf-8") as f:
        json.dump(products, f, ensure_ascii=False, indent=4)

    await update.message.reply_text(
        "✅ تم إضافة المنتج بنجاح"
    )


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, add_product))

print("Bot receiver is running...")
app.run_polling()
