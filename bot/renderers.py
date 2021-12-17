"""
A renderer returns a tuple of (text, keyboard) which is sent to the user.
I advice you to follow this structure.
"""

from telegram import InlineKeyboardButton,InlineKeyboardMarkup


# Write your renderers here


# Example:
def example_markup():
    text = 'Example text'

    keyboard = [
        [InlineKeyboardButton(text='Example button', url='https://xxx.com')]
    ]

    return InlineKeyboardMarkup(text, keyboard)
