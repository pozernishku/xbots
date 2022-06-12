from telebot import custom_filters, TeleBot

from xbots.anekdot_pub_bot.filters.custom_filters import IsCorrectPeriodicityFilter

PDF_URL_LIST_REGEX = r"(?i)https?://.+\.pdf"


def add_custom_filters(bot: TeleBot) -> TeleBot:
    bot.add_custom_filter(custom_filters.StateFilter(bot))
    bot.add_custom_filter(IsCorrectPeriodicityFilter())
    bot.add_custom_filter(custom_filters.ForwardFilter())
    # TODO: Add custom filter 'does bot is admin in your channel?'
    return bot
