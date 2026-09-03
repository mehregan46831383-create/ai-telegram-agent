import os
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from agents.news_agent import build_daily_posts

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 AI News Agent فعال است.\n"
        "/news — تولید پست آزمایشی\n"
        "/status — وضعیت بات"
    )

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🟢 Bot online")

async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    posts = await build_daily_posts()
    for post in posts:
        await update.message.reply_text(post, disable_web_page_preview=False)

async def scheduled_publish(context: ContextTypes.DEFAULT_TYPE):
    if not CHAT_ID:
        return
    posts = await build_daily_posts()
    for post in posts:
        await context.bot.send_message(chat_id=CHAT_ID, text=post, disable_web_page_preview=False)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(CommandHandler("news", news))

    # سه زمان نمونه: 09:00، 15:00، 20:00 به وقت سرور
    app.job_queue.run_daily(scheduled_publish, time=__import__("datetime").time(9, 0), name="ai_news")
    app.job_queue.run_daily(scheduled_publish, time=__import__("datetime").time(15, 0), name="robotics")
    app.job_queue.run_daily(scheduled_publish, time=__import__("datetime").time(20, 0), name="prompt")

    app.run_polling()

if __name__ == "__main__":
    main()
