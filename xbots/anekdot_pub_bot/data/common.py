from telebot import TeleBot


def get_anekdot(bot: TeleBot, chat_id) -> None:
    """Send the anekdot message."""
    bot.send_message(chat_id, text="anekdot!")
