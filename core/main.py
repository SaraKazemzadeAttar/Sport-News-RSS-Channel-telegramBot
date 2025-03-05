import telebot
import logging
import os
import time
import feedparser

API_TOKEN = os.environ.get('API_TOKEN')
CHAT_ID = os.environ.get('CHANNEL_ID')
RSS_FEED_URL = "https://www.varzesh3.com/rss"
LAST_POST_FILE = "last_post_id.txt"

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)
bot = telebot.TeleBot(API_TOKEN)

def read_last_post_id():
    if os.path.exists(LAST_POST_FILE):
        with open(LAST_POST_FILE, 'r', encoding="utf-8") as f:
            return f.read().strip()
    return None

def save_last_post_id(post_id):
    """Save the last post ID to a file."""
    with open(LAST_POST_FILE, "w", encoding="utf-8") as f:
        f.write(post_id)

def check_and_send_post():
    last_post_id = read_last_post_id()
    print(f"📌 Last stored post ID: {last_post_id}")

    try:
        feed = feedparser.parse(RSS_FEED_URL)
        
        if not feed.entries:
            print("⚠️ No entries found in the RSS feed.")
            return

        latest_entry = feed.entries[0]
        
        post_id = latest_entry.get("id") or latest_entry.get("guid") or latest_entry.get("link") or latest_entry.get("title")

        if not post_id:
            print("🚨 Could not determine a unique post ID.")
            return

        print(f"🔔 Latest post ID: {post_id}")

        if post_id != last_post_id:
            message = f"📰 {latest_entry.title}\n\n🔗 {latest_entry.link}"
            bot.send_message(CHAT_ID, message)
            print("✅ New post sent.")
            save_last_post_id(post_id)
        else:
            print("⏳ This post has already been sent.")

    except Exception as e:
        print(f"❌ Error fetching or sending data: {e}")

def run_rss_checker():
    try:
        while True:
            print(f"📡 Checking RSS feed for channel {CHAT_ID} ...")
            check_and_send_post()
            print("🕒 Waiting for the next 10 minutes...\n")
            time.sleep(600)  # 10 minutes
    except KeyboardInterrupt:
        print("🚪 Bot stopped.")

if __name__ == "__main__":
    run_rss_checker()