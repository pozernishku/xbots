import os
import threading

from telebot import StatePickleStorage, TeleBot

from xbots.anekdot_pub_bot.filters.common import add_custom_filters
from xbots.anekdot_pub_bot.handlers.common import register_handlers, run_pending

if __name__ == "__main__":
    bot = TeleBot(
        os.environ["ANEKDOT_PUB_BOT_TOKEN"],
        num_threads=5,
        state_storage=StatePickleStorage(),
    )
    bot = register_handlers(bot)
    add_custom_filters(bot)
    threading.Thread(target=run_pending, name="run_pending", daemon=True).start()
    bot.infinity_polling(skip_pending=True)
