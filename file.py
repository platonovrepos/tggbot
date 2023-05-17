import os
from dotenv_vault import load_dotenv
from aiogram import Bot, Dispatcher, executor, types

load_dotenv()
s3_fdf = os.getenv("hello")


# Объект бота
bot = Bot(s3_fdf)
# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения


# Хэндлер на команду /test1
@dp.message_handler(commands="test1")
async def cmd_test1(message: types.Message):
    await message.reply("Test 1")


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)