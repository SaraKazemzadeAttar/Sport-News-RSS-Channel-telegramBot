# Sport-News-RSS-Channel-telegramBot
This Python bot fetches the latest post from an RSS feed every 10 minutes and sends it to a Telegram channel. It is good for notifying subscribers the news.

Features

Fetches posts from an RSS feed (in this code: Varzesh3.com)

Sends only new posts to a specified Telegram channel

Uses a local file to track the last sent post

Runs automatically every 10 minutes

Requirements

Python 3

telebot library (for Telegram bot interaction)

feedparser library (for parsing RSS feeds)

Installation

Clone this repository or copy the script.

Install dependencies:

pip install pyTelegramBotAPI feedparser

Set up environment variables:

API_TOKEN: Your Telegram bot token

CHANNEL_ID: Your Telegram channel ID

Usage

Run the script using:

python bot.py

The bot will check for new posts every 10 minutes and send them to the Telegram channel if they haven't been sent before.

Configuration

Change RSS_FEED_URL in the script to monitor a different RSS feed.

Adjust time.sleep(600) to modify the checking interval.

Notes

Ensure the bot is an admin in the Telegram channel to send messages.
