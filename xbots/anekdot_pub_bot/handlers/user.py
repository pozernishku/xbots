from telebot import TeleBot
from telebot.types import Message

from xbots.anekdot_pub_bot.states.register_state import Register
from xbots.anekdot_pub_bot.utilities import prepare_settings_message


def send_welcome_any_user(message: Message, bot: TeleBot):
    """You can create a function and use parameter pass_bot."""
    bot.reply_to(message, "Hi! You're not an admin and cannot set a timer")


def ask_channel(message: Message, bot: TeleBot):
    bot.set_state(message.from_user.id, Register.channel, message.chat.id)
    bot.send_message(
        message.chat.id,
        "Пришлите ссылку на Ваш канал в котором этот бот является администратором. "
        "Например: https://t.me/my_channel",
    )


def delete_from_any_state(message: Message, bot: TeleBot):
    bot.send_message(message.chat.id, "Ваши настройки удалены")
    bot.delete_state(message.from_user.id, message.chat.id)


def ask_periodicity(message: Message, bot: TeleBot):
    # TODO: Handle the min & max values
    bot.send_message(
        message.chat.id, "С какой периодичностью (в минутах) публиковать в Ваш канал?"
    )
    bot.set_state(message.from_user.id, Register.periodicity, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data["channel"] = message.text


def ask_pdf_list(message: Message, bot: TeleBot):
    bot.send_message(
        message.chat.id,
        "Пришлите список PDF-файлов. Каждый файл с новой строки, например:\n"
        "https://example.com/my-file1.pdf\n"
        "https://example.com/my-file1.pdf",
    )
    bot.set_state(message.from_user.id, Register.pdf_list, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data["periodicity"] = message.text


def periodicity_incorrect(message: Message, bot: TeleBot):
    bot.send_message(message.chat.id, "Некорректное значение. Пожалуйста введите число")


def show_result(message: Message, bot: TeleBot):
    bot.set_state(message.from_user.id, Register.end, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data["pdf_list"] = message.text
    settings_msg = prepare_settings_message(data)
    bot.send_message(message.chat.id, settings_msg)


def show_settings_from_any_state(message: Message, bot: TeleBot):
    state_context = bot.retrieve_data(message.from_user.id, message.chat.id)
    if hasattr(state_context, "data") and state_context.data:
        settings_msg = prepare_settings_message(state_context.data)
    else:
        settings_msg = "Бот не настроен. Используйте команду /start для настройки"
    bot.send_message(message.chat.id, settings_msg)
