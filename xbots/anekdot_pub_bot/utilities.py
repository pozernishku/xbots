def prepare_settings_message(data: dict) -> str:
    empty_value = "<пусто>"
    pdf_list = data.get("pdf_list", [])
    pdf_list_str = "\n".join([f"- {pdf_url}" for pdf_url in pdf_list]) or empty_value
    pdf_list_str = "\n" + pdf_list_str if pdf_list_str != empty_value else pdf_list_str
    # TODO: Bold the values
    settings_msg = (
        f"Ваши настройки:\n"
        f"Канал: {data.get('channel', empty_value)}\n"
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
