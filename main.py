import os

import dotenv
from telebot import TeleBot

# Filter. When communicating in the Group where this bot is a member:
from telebot.custom_filters import IsAdminFilter

# Filter. When communicating Me and Bot:
from anekdot_pub_bot.filters.admin_filter import AdminFilter
from anekdot_pub_bot.handlers.admin import admin_user, is_admin_user
from anekdot_pub_bot.handlers.user import any_user


def register_handlers():
    bot.register_message_handler(
        is_admin_user, commands=["start"], is_chat_admin=True, pass_bot=True
    )
    bot.register_message_handler(
        admin_user, commands=["start"], admin=True, pass_bot=True
    )
    bot.register_message_handler(
        any_user, commands=["start"], admin=False, pass_bot=True
    )


if __name__ == "__main__":
    dotenv.load_dotenv()
    bot = TeleBot(os.environ["ANEKDOT_PUB_BOT_TOKEN"], num_threads=5)
    register_handlers()

    # custom filters
    bot.add_custom_filter(AdminFilter())
    bot.add_custom_filter(IsAdminFilter(bot))

    bot.infinity_polling()
