import json
import os
import random

import requests
from telebot import TeleBot

PDF_URL_LIST = json.loads(os.environ["PDF_URL_LIST"])


def get_anekdot(bot: TeleBot, chat_id) -> None:
    """Send the anekdot message."""
    pdf_url = random.choice(PDF_URL_LIST)
    pdf = requests.get(pdf_url).content
    bot.send_message(chat_id, text="anekdot!")
