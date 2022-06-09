from telebot import custom_filters, TeleBot


def add_custom_filters(bot: TeleBot) -> TeleBot:
    bot.add_custom_filter(custom_filters.StateFilter(bot))
    bot.add_custom_filter(custom_filters.IsDigitFilter())
    # TODO: Add custom filter IsURL for channel URL checking
    # TODO: Add custom filter 'does bot is admin in your channel?'
    return bot
