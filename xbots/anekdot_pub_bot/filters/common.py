from telebot import TeleBot

from xbots.anekdot_pub_bot.filters.admin_filter import AdminFilter


def add_custom_filters(bot: TeleBot):
    # Filter. When communicating Me and Bot:
    bot.add_custom_filter(AdminFilter())
