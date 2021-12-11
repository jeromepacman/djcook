"""
Command handlers
https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.commandhandler.html?highlight=CommandHandler
"""
import random

from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode
from telegram.ext import ConversationHandler

from .quotes import QUOTES_STRINGS
from .authentication import authenticate


# Write your command handlers here

# Example: /start
def start(update, context):
    update.message.reply_text(
        text=" 'What if' ?"
    )


def help(update, context):
    update.message.reply_text(
        text='ouchhh.. hard!'
    )


# Example: /cancel
def cancel(update, context):
    update.message.reply_text(
        text='The action is cancelled.'
    )
    return ConversationHandler.END


def quote(update, context):
    text = random.choice(QUOTES_STRINGS)
    update.message.reply_text(text)


def myview(update, context):
    user = authenticate(update.effective_message)
    update.message.reply_text(user)

