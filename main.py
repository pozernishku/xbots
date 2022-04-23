import os
import threading
import time

import schedule
from telebot import TeleBot

# Filter. When communicating Me and Bot:
from anekdot_pub_bot.filters.admin_filter import AdminFilter
from anekdot_pub_bot.handlers.common import register_handlers

if __name__ == "__main__":
    bot = TeleBot(os.environ["ANEKDOT_PUB_BOT_TOKEN"], num_threads=5)
    register_handlers(bot)

    # custom filters
    bot.add_custom_filter(AdminFilter())

    # bot.infinity_polling()
    threading.Thread(
        target=bot.infinity_polling, name="bot_infinity_polling", daemon=True
    ).start()
    while True:
        schedule.run_pending()
        time.sleep(1)
