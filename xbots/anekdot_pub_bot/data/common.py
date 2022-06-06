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
        random_pdf_page = pdf.pages[random.randint(0, len(pdf.pages) - 1)]
    # TODO: Try to get rid of the red rectangle borders around the sentences
    pdf_page_image = random_pdf_page.to_image(resolution=150)
    # TODO: Check if it possible to save the page as pdf first and then convert to image
    #  in order to fix the red borders
    pdf_page_text_piece = f"... {random_pdf_page.extract_text()[:200]} ..."
    pdf_page_text_piece = pdf_page_text_piece.replace("&", "&amp;")
    pdf_page_text_piece = pdf_page_text_piece.replace("<", "&lt;").replace(">", "&gt;")
    # TODO: Add direct link to pdf file (or site page, not sure) and page (if possible)
    continue_reading = f'<a href="{pdf_url}">Продолжить чтение</a>'
    bot.send_photo(
        chat_id,
        photo=pdf_page_image._repr_png_(),
        caption=f"{pdf_page_text_piece}\n\n{continue_reading}",
        parse_mode="HTML",
    )
