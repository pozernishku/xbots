import random
import threading
from io import BytesIO

import pdfplumber
import requests
from telebot import TeleBot


def get_anekdot(bot: TeleBot, channel, pdf_list: list) -> None:
    """Send the anekdot message."""
    # TODO: Remove debug info
    print("DEBUG: на потоке %s" % threading.current_thread())
    pdf_url = random.choice(pdf_list)
    pdf_bytes_io = BytesIO(requests.get(pdf_url).content)
    # BytesIO is acceptable and mentioned in the docs (it's ok that PyCharm warns)
    with pdfplumber.open(pdf_bytes_io) as pdf:
        random_page_n = random.randint(0, len(pdf.pages) - 1)
        random_pdf_page = pdf.pages[random_page_n]
    # TODO: Try to get rid of the red rectangle borders around the sentences
    pdf_page_image = random_pdf_page.to_image(resolution=150)
    # TODO: Check if it possible to save the page as pdf first and then convert to image
    #  in order to fix the red borders
    pdf_page_text_piece = f"🧩 ... {random_pdf_page.extract_text()[:200]} ..."
    pdf_page_text_piece = pdf_page_text_piece.replace("&", "&amp;")
    pdf_page_text_piece = pdf_page_text_piece.replace("<", "&lt;").replace(">", "&gt;")
    href = f"{pdf_url}#page={random_page_n + 1}"
    continue_reading = f'<a href="{href}">📖 Продолжить чтение</a>'
    href_file_formats = pdf_url.rsplit("/", 1)[0]
    more_file_formats = f'<a href="{href_file_formats}">🗄️ Читать в другом формате</a>'
    bot.send_photo(
        channel,
        photo=pdf_page_image._repr_png_(),
        caption=f"{pdf_page_text_piece}\n\n{continue_reading}\n{more_file_formats}",
        parse_mode="HTML",
    )
