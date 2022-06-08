from telebot import custom_filters, TeleBot


def add_custom_filters(bot: TeleBot):
    bot.add_custom_filter(custom_filters.StateFilter(bot))
    bot.add_custom_filter(custom_filters.IsDigitFilter())
