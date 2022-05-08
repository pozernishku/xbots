from telebot import TeleBot
from telebot.types import Message


def send_welcome_admin(message: Message, bot: TeleBot):
    """You can create a function and use parameter pass_bot."""
    bot.reply_to(message, "Hi! Use /set <seconds> to set a timer")
