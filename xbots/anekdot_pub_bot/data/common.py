import os

from telebot import TeleBot

PDF_URL_LIST = os.environ["PDF_URL_LIST"]


def get_anekdot(bot: TeleBot, chat_id) -> None:
    """Send the anekdot message."""
    bot.send_message(chat_id, text="anekdot!")
