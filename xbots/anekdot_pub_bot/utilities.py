def prepare_settings_message(data: dict) -> str:
    empty_value = "<пусто>"
    # TODO: Bold the values
    settings_msg = (
        f"Ваши настройки:\n"
        f"Канал: {data.get('channel', empty_value)}\n"
        f"Периодичность: {data.get('periodicity', empty_value)}\n"
        f"PDF-файлы: {data.get('pdf_list', empty_value)}"
    )
    return settings_msg
