import schedule
from telebot import TeleBot
from telebot.types import Message

from xbots.anekdot_pub_bot.data.common import get_anekdot


def set_timer(message: Message, bot: TeleBot):
    state_context = bot.retrieve_data(message.from_user.id, message.chat.id)
    err_msg = "Запустить авто-публикацию невозможно. Начните настройку с команды /start"
    if not hasattr(state_context, "data"):
        bot.send_message(message.chat.id, err_msg)
        return
    if hasattr(state_context, "data") and not state_context.data:
        bot.send_message(message.chat.id, err_msg)
        return
    if hasattr(state_context, "data"):
        channel = state_context.data.get("channel", {})
        periodicity = state_context.data.get("periodicity", 0)
        if not (len(channel) == 1 and periodicity > 0):
            bot.send_message(message.chat.id, err_msg)
            return
        channel = list(channel.keys())[0]
        # FIXME: Add pdf_list below
        schedule.every(periodicity).minutes.do(get_anekdot, bot, channel).tag(channel)


def unset_timer(message: Message, bot: TeleBot):
    state_context = bot.retrieve_data(message.from_user.id, message.chat.id)
    # FIXME: Clear schedule correctly
    channel = -100
    schedule.clear(channel)
