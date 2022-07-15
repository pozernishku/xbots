import asyncio
import os

import dotenv
from aiogram import Bot, Dispatcher, executor, types

dotenv.load_dotenv()

BOT_TOKEN = os.environ["ANEKDOT_PUB_BOT_TOKEN"]
BOT = Bot(token=BOT_TOKEN)
BOT_DISPATCHER = Dispatcher(bot=BOT)


@BOT_DISPATCHER.message_handler()
async def new_timer_message(message: types.Message):
    try:
        timer_seconds = int(message.text)
        if timer_seconds <= 0:
            raise ValueError()
    except (ValueError, TypeError):
        await BOT.send_message(chat_id=message.chat.id, text="Write valid integer")
        return

    new_message = await BOT.send_message(
        chat_id=message.chat.id, text=f"Your timer is at: {timer_seconds}"
    )

    for seconds_left in range(timer_seconds - 1, -1, -1):
        await asyncio.sleep(1)
        await new_message.edit_text(f"Your timer is at: {seconds_left}")

    await BOT.send_message(
        chat_id=message.chat.id, text=f"Your timer for {timer_seconds} seconds finished"
    )


if __name__ == "__main__":
    executor.start_polling(BOT_DISPATCHER, skip_updates=True)
