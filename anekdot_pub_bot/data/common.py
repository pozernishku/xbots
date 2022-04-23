from telebot import TeleBot


def beep(bot: TeleBot, chat_id) -> None:
    """Send the beep message."""
    bot.send_message(chat_id, text="Beep!")
