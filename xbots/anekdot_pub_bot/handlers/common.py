import time

import schedule
from telebot import TeleBot

from xbots.anekdot_pub_bot.filters.common import PDF_URL_LIST_REGEX
from xbots.anekdot_pub_bot.handlers.user import (
    ask_channel,
    ask_pdf_list,
    ask_periodicity,
    channel_incorrect,
    delete_settings_from_any_state,
    periodicity_incorrect,
    show_result,
    show_settings_from_any_state,
)
from xbots.anekdot_pub_bot.states.register_state import Register


def register_handlers(bot: TeleBot) -> TeleBot:
    bot.register_message_handler(ask_channel, commands=["start"], pass_bot=True)
    bot.register_message_handler(
        delete_settings_from_any_state, state="*", commands=["delete"], pass_bot=True
    )
    bot.register_message_handler(
        show_settings_from_any_state, state="*", commands=["settings"], pass_bot=True
    )
    bot.register_message_handler(
        ask_periodicity, is_forwarded=True, state=Register.channel, pass_bot=True
    )
    bot.register_message_handler(
        channel_incorrect, is_forwarded=False, state=Register.channel, pass_bot=True
    )
    bot.register_message_handler(
        ask_pdf_list, state=Register.periodicity, is_digit=True, pass_bot=True
    )
    bot.register_message_handler(
        periodicity_incorrect, state=Register.periodicity, is_digit=False, pass_bot=True
    )
    bot.register_message_handler(
        show_result,
        regexp=PDF_URL_LIST_REGEX,
        state=Register.pdf_list,
        pass_bot=True,
    )
    # TODO: Register one more handler w/o regex to message user if input is incorrect
    return bot


def run_pending():
    while True:
        schedule.run_pending()
        time.sleep(1)
