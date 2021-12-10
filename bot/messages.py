"""
You can directly filter messages sent to the bot and filter them based on PTB filters.
The filters are located on telegram.ext.Filters module
"""
from telegram.ext import Filters


def echo(update, context):
    update.message.reply_text(
        text=update.message.text
    )


