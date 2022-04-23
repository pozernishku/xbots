import os

import dotenv
import schedule
from telebot import TeleBot
from telebot.types import Message

dotenv.load_dotenv()

ANEKDOT_PUB = os.environ["ANEKDOT_PUB"]


def send_welcome(message: Message, bot: TeleBot):
    bot.reply_to(message, "Hi! Use /set <seconds> to set a timer")


def set_timer(message: Message, bot: TeleBot):
    def beep(chat_id) -> None:
        """Send the beep message."""
        bot.send_message(chat_id, text="Beep!")

    args = message.text.split()
    if len(args) > 1 and args[1].isdigit():
        sec = int(args[1])
        schedule.every(sec).seconds.do(beep, ANEKDOT_PUB).tag(ANEKDOT_PUB)
    else:
        bot.reply_to(message, "Usage: /set <seconds>")


def unset_timer(message: Message, bot: TeleBot):
    schedule.clear(ANEKDOT_PUB)
