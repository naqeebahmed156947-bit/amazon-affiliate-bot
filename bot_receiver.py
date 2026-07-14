import os
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN = os.getenv("TELEGRAM_TOKEN")

if not TOKEN:
    raise Exception("TELEGRAM_TOKEN is missing")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 أهلاً بك في Amazon Affiliate Bot Pro\n\n"
        "📩 أرسل رابط منتج أمازون (Affiliate Link)\n"
        "وسأقوم بجلب بيانات المنتج ونشره في القناة."
    )


async def add_product(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()

    # التأكد أن الرسالة عبارة عن رابط أمازون
    if "amazon." not in text and "amzn.to" not in text:
        await update.message.reply_text(
            "❌ أرسل رابط أمازون أو رابط الأفلييت فقط."
        )
        return

    print(f"New Amazon Link: {text}")

    await update.message.reply_text(
        "✅ تم استلام الرابط.\n\n"
        "⏳ جاري استخراج بيانات المنتج..."
    )

    # المرحلة القادمة:
    # 1- استخراج بيانات المنتج
    # 2- جلب الصورة والسعر
    # 3- النشر في القناة


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "الأوامر المتاحة:\n\n"
        "/start - تشغيل البوت\n"
        "/help - المساعدة\n\n"
        "ثم أرسل رابط منتج أمازون."
    )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, add_product)
    )

    print("✅ Amazon Affiliate Bot Pro is running...")

    app.run_polling()


if __name__ == "__main__":
    main()
