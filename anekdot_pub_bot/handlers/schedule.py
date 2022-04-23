import os

import schedule
from telebot import TeleBot
from telebot.types import Message

from anekdot_pub_bot.data.common import beep

ANEKDOT_PUB = os.environ["ANEKDOT_PUB"]


def set_timer(message: Message, bot: TeleBot):
    args = message.text.split()
    if len(args) > 1 and args[1].isdigit():
        sec = int(args[1])
        schedule.every(sec).seconds.do(beep, bot, ANEKDOT_PUB).tag(ANEKDOT_PUB)
    else:
        bot.reply_to(message, "Usage: /set <seconds>")


def unset_timer(message: Message, bot: TeleBot):
    schedule.clear(ANEKDOT_PUB)
