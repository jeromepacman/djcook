"""
You can directly filter messages sent to the bot and filter them based on PTB filters.
The filters are located on telegram.ext.Filters module
"""
from telegram.ext import Filters

from .authentication import authenticate


def to_db(update, context):
    user = update.effective_user
    authenticate(user)
