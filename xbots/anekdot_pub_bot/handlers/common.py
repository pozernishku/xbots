import time

import schedule
from telebot import TeleBot

from xbots.anekdot_pub_bot.handlers.user import (
    ask_channel,
    ask_pdf_list,
    ask_periodicity,
    delete_from_any_state,
    periodicity_incorrect,
    show_result,
)
from xbots.anekdot_pub_bot.states.register_state import Register


def register_handlers(bot: TeleBot) -> TeleBot:
    bot.register_message_handler(ask_channel, commands=["start"], pass_bot=True)
    bot.register_message_handler(
        delete_from_any_state, state="*", commands=["delete"], pass_bot=True
    )
    bot.register_message_handler(ask_periodicity, state=Register.channel, pass_bot=True)
    bot.register_message_handler(
        ask_pdf_list, state=Register.periodicity, is_digit=True, pass_bot=True
    )
    bot.register_message_handler(
        periodicity_incorrect, state=Register.periodicity, is_digit=False, pass_bot=True
    )
    bot.register_message_handler(show_result, state=Register.pdf_list, pass_bot=True)
    return bot


def run_pending():
    while True:
        schedule.run_pending()
        time.sleep(1)
