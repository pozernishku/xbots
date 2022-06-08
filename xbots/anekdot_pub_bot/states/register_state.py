from telebot.handler_backends import State, StatesGroup


class Register(StatesGroup):
    channel = State()
    periodicity = State()
    pdf_list = State()
