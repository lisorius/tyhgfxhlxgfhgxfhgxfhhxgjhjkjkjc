import time
from aiogram import types
from aiogram.types import InputFile
from PIL import Image, ImageFont, ImageDraw

from main import dp

token = ''


@dp.message_handler(content_types=['photo'])
async def handle_docs_photo(message: types.Message):
    await message.photo[-1].download('r1.png')
    time.sleep(1)
    sample = Image.open('r1.png')
    font = ImageFont.truetype('Minecraft.otf', size=154, encoding='ASCII')
    draw = ImageDraw.Draw(sample)
    draw.text((250, 500), font=font, text="Hello world", align="center", fill='blue')
    sample.save('r3.png')
    sample1 = Image.open('r1.png')
    font1 = ImageFont.truetype('tahoma.ttf', size=154, encoding='ASCII')
    draw1 = ImageDraw.Draw(sample1)
    draw1.text((250, 500), font=font1, text="Hello world", align="center", fill='blue')
    sample1.save('r2.png')
    await message.answer_photo(InputFile('r3.png'))
    await message.answer_photo(InputFile('r2.png'))
