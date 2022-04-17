from telebot.custom_filters import SimpleCustomFilter

from anekdot_pub_bot.models.users_model import Admin


class AdminFilter(SimpleCustomFilter):
    """
    Filter for admin users
    """

    key = "admin"

    def check(self, message):

        return int(message.chat.id) == int(Admin.ADMIN.value)