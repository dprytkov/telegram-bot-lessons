from loader import bot, storage


async def on_shutdown(dp):
    await bot.send_message(chat_id=admin_id, text="Бот остановлен")
    await bot.close()
    await storage.close()


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_shutdown=on_shutdown)
