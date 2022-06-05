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
    # BytesIO is acceptable and mentioned in the docs (it's ok that PyCharm warns)
    with pdfplumber.open(pdf_bytes_io) as pdf:
        # TODO: Get random page below instead of first
        random_pdf_page = pdf.pages[0]
    # TODO: Try to get rid of the red rectangle borders around the sentences
    pdf_page_image = random_pdf_page.to_image(resolution=150)
    # im.save("img.png", format="PNG")
    # bot.send_message(chat_id, text=random_pdf_page.extract_text())
    # TODO: Add caption text (from pdf page) to the message
    bot.send_photo(chat_id, photo=pdf_page_image._repr_png_(), caption="test!")
