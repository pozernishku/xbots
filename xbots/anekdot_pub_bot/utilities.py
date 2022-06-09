def prepare_settings_message(data: dict) -> str:
    settings_msg = (
        f"Ваши настройки:\n"
        f"Канал: {data['channel']}\n"
        f"Периодичность: {data['periodicity']}\n"
        f"PDF-файлы: {data['pdf_list']}"
    )
    return settings_msg
