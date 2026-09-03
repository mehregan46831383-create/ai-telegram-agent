import os
import httpx

# نسخه پایه: برای شروع از RSSهای عمومی استفاده می‌کند.
RSS_FEEDS = [
    "https://feeds.arstechnica.com/arstechnica/technology-lab",
    "https://www.theverge.com/rss/index.xml",
]

async def fetch_feed(url):
    async with httpx.AsyncClient(timeout=20, follow_redirects=True) as client:
        r = await client.get(url)
        r.raise_for_status()
        return r.text

async def build_daily_posts():
    # این نسخه پایه است؛ در مرحله بعد می‌توان AI summarizer و فیلتر تکراری را وصل کرد.
    return [
        "📰 اخبار AI\n\nنسخه پایه ایجنت فعال است. مرحله بعد: جمع‌آوری RSS، خلاصه‌سازی با مدل AI و فیلتر خبرهای تکراری.",
        "🦾 رباتیک\n\nنسخه پایه فعال است. مرحله بعد: منابع تخصصی رباتیک به ایجنت اضافه می‌شوند.",
        "🧠 Prompt روز\n\nنقش: یک دستیار پژوهشی دقیق.\n\nوظیفه: موضوع داده‌شده را به پرسش‌های تحقیقاتی، منابع پیشنهادی و یک برنامه تحقیق مرحله‌ای تبدیل کن."
    ]
