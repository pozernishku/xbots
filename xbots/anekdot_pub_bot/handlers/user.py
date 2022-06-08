from telebot import TeleBot
from telebot.types import Message

from xbots.anekdot_pub_bot.states.register_state import Register


def send_welcome_any_user(message: Message, bot: TeleBot):
    """You can create a function and use parameter pass_bot."""
    bot.reply_to(message, "Hi! You're not an admin and cannot set a timer")


def start(message: Message, bot: TeleBot):
    bot.set_state(message.from_user.id, Register.channel, message.chat.id)
    bot.send_message(
        message.chat.id,
        "Пришлите ссылку на Ваш канал в котором этот бот является администратором. "
        "Например: https://t.me/my_channel",
    )


def any_state(message: Message, bot: TeleBot):
    bot.send_message(message.chat.id, "Ваши изменения отменены")
    bot.delete_state(message.from_user.id, message.chat.id)


def channel(message: Message, bot: TeleBot):
    # TODO: Handle the min & max values
    bot.send_message(
        message.chat.id, "С какой периодичностью (в минутах) публиковать в Ваш канал?"
    )
    bot.set_state(message.from_user.id, Register.periodicity, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data["channel"] = message.text
