import time

import schedule
from telebot import TeleBot

from xbots.anekdot_pub_bot.handlers.schedule import set_timer, unset_timer
from xbots.anekdot_pub_bot.handlers.user import send_welcome_any_user


def register_handlers(bot: TeleBot):
    bot.register_message_handler(
        send_welcome_any_user, commands=["start"], pass_bot=True
    )


def run_pending():
    while True:
        schedule.run_pending()
        time.sleep(1)
