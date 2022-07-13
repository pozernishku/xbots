import queue
import threading
from functools import partial

import jmespath
import schedule
from telebot import TeleBot

from xbots.anekdot_pub_bot.data.common import get_anekdot


def prepare_settings_message(data: dict) -> str:
    empty_value = "<пусто>"
    pdf_list = data.get("pdf_list", [])
    pdf_list_str = "\n".join([f"- {pdf_url}" for pdf_url in pdf_list]) or empty_value
    pdf_list_str = "\n" + pdf_list_str if pdf_list_str != empty_value else pdf_list_str
    channel = data.get("channel", {empty_value: empty_value}).copy().popitem()
    # TODO: Bold the values
    settings_msg = (
        f"Ваши настройки:\n"
        f"Канал: {channel[1]} ({channel[0]})\n"
        f"Периодичность, мин: {data.get('periodicity', empty_value)}\n"
        f"PDF-файлы: {pdf_list_str}"
    )
    tip_commands_message = "\n\n" + "\n".join(
        [
            "/start - изменить настройки",
            "/delete - удалить настройки",
            "/settings - просмотреть настройки",
        ]
    )
    return settings_msg + tip_commands_message


def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()


job_queue = queue.Queue()


def worker_main():
    while True:
        job_func = job_queue.get()
        job_func()
        job_queue.task_done()


def activate_job_schedule_in_channels(bot: TeleBot, debug_activate) -> TeleBot:
    if not debug_activate:
        return bot
    states_data = bot.current_states.data
    params = jmespath.search("*.*.data[]", states_data)
    for param in params:
        # FIXME: Add param validation
        channel = list(param["channel"].keys())[0]
        periodicity = param["periodicity"]
        pdf_list = param["pdf_list"]
        get_anekdot_activate = partial(
            get_anekdot, bot=bot, channel=channel, pdf_list=pdf_list
        )
        # Threads idea https://schedule.readthedocs.io/en/stable/parallel-execution.html
        schedule.every(periodicity).minutes.do(job_queue.put, get_anekdot_activate).tag(
            channel
        )
        # TODO: Check if daemon=True is ok
        worker_thread = threading.Thread(target=worker_main, daemon=True)
        worker_thread.start()
    return bot
