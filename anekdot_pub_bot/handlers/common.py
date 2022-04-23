from telebot import TeleBot

from anekdot_pub_bot.handlers.admin import send_welcome_admin
from anekdot_pub_bot.handlers.schedule import set_timer, unset_timer
from anekdot_pub_bot.handlers.user import send_welcome_any_user


def register_handlers(bot: TeleBot):
    bot.register_message_handler(
        send_welcome_admin, commands=["help", "start"], admin=True, pass_bot=True
    )
    bot.register_message_handler(
        send_welcome_any_user, commands=["help", "start"], admin=False, pass_bot=True
    )
    bot.register_message_handler(set_timer, commands=["set"], admin=True, pass_bot=True)
    bot.register_message_handler(
        unset_timer, commands=["unset"], admin=True, pass_bot=True
    )
