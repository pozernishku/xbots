import json
import os
import random
from io import BytesIO

import pdfplumber
import requests
from telebot import TeleBot

PDF_URL_LIST = json.loads(os.environ["PDF_URL_LIST"])


def get_anekdot(bot: TeleBot, chat_id) -> None:
    """Send the anekdot message."""
    pdf_url = random.choice(PDF_URL_LIST)
    pdf_bytes_io = BytesIO(requests.get(pdf_url).content)
    with pdfplumber.open(pdf_bytes_io) as pdf:
        first_page = pdf.pages[0]
    bot.send_message(chat_id, text=first_page.extract_text())
