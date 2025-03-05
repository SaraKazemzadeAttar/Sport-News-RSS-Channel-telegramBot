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
        with open(LAST_POST_FILE, 'r') as f:
            return f.read().strip()
    return None

def save_last_post_id(post_id):
    with open("last_post_id.txt", "w", encoding="utf-8") as f:
        f.write(post_id)

def check_and_send_post():
    last_post_id = read_last_post_id()
    print(f"Last post ID: {last_post_id}")

    feed = feedparser.parse(RSS_FEED_URL)
    
    if not feed.entries:
        print("No entries found in RSS feed.")
        return

    latest_entry = feed.entries[0]

    post_id = latest_entry.get("id") or latest_entry.get("guid") or latest_entry.get("link") or latest_entry.get("title")

    if not post_id:
        print("Could not determine a unique post ID.")
        return

    print(f"Latest post ID: {post_id}")

    if post_id != last_post_id:
        bot.send_message(CHAT_ID, f"{latest_entry.title}\n\n{latest_entry.link}")
        save_last_post_id(post_id)


def run_rss_checker():
    try:
        while True:
            print(f"CHAT_ID: {CHAT_ID}")
            check_and_send_post()
            time.sleep(600)
    except KeyboardInterrupt:
        print("Bot stopped gracefully.")


if __name__ == "__main__":
    run_rss_checker()