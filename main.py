import os
import threading
import time

import dotenv
import schedule
from telebot import TeleBot

# Filter. When communicating in the Group where this bot is a member:
from telebot.custom_filters import IsAdminFilter

# Filter. When communicating Me and Bot:
from anekdot_pub_bot.filters.admin_filter import AdminFilter
from anekdot_pub_bot.handlers.admin import admin_user, is_admin_user
from anekdot_pub_bot.handlers.schedule import send_welcome, set_timer, unset_timer
from anekdot_pub_bot.handlers.user import any_user


def register_handlers():
    bot.register_message_handler(
        send_welcome, commands=["help", "start"], pass_bot=True
    )
    bot.register_message_handler(set_timer, commands=["set"], pass_bot=True)
    bot.register_message_handler(unset_timer, commands=["unset"], pass_bot=True)

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

    # bot.infinity_polling()
    threading.Thread(
        target=bot.infinity_polling, name="bot_infinity_polling", daemon=True
    ).start()
    while True:
        schedule.run_pending()
        time.sleep(1)
