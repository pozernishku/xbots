import time

import schedule
from telebot import TeleBot

from xbots.anekdot_pub_bot.handlers.user import (
    any_state,
    channel,
    periodicity,
    periodicity_incorrect,
    start,
)
from xbots.anekdot_pub_bot.states.register_state import Register


def register_handlers(bot: TeleBot):
    bot.register_message_handler(start, commands=["start"], pass_bot=True)
    bot.register_message_handler(
        any_state, state="*", commands=["cancel"], pass_bot=True
    )
    bot.register_message_handler(channel, state=Register.channel, pass_bot=True)
    bot.register_message_handler(
        periodicity, state=Register.periodicity, is_digit=True, pass_bot=True
    )
    bot.register_message_handler(
        periodicity_incorrect, state=Register.periodicity, is_digit=False, pass_bot=True
    )


def run_pending():
    while True:
        schedule.run_pending()
        time.sleep(1)
