import os
import threading
import time

import schedule
from telebot import TeleBot

# Filter. When communicating Me and Bot:
from anekdot_pub_bot.filters.admin_filter import AdminFilter
from anekdot_pub_bot.handlers.schedule import set_timer, unset_timer
from anekdot_pub_bot.handlers.admin import send_welcome_admin
from anekdot_pub_bot.handlers.user import send_welcome_any_user


def register_handlers():
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


if __name__ == "__main__":
    bot = TeleBot(os.environ["ANEKDOT_PUB_BOT_TOKEN"], num_threads=5)
    register_handlers()

    # custom filters
    bot.add_custom_filter(AdminFilter())

    # bot.infinity_polling()
    threading.Thread(
        target=bot.infinity_polling, name="bot_infinity_polling", daemon=True
    ).start()
    while True:
        schedule.run_pending()
        time.sleep(1)
