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
        schedule.every(periodicity).minutes.do(get_anekdot, bot, channel, pdf_list).tag(
            channel
        )
    return bot
