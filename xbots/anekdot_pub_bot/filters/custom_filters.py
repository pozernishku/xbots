from telebot import SimpleCustomFilter


class IsCorrectPeriodicityFilter(SimpleCustomFilter):
    key = "is_correct_periodicity"

    def check(self, message):
        return message.text.isdigit() and int(message.text) > 0
