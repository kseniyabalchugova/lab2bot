from aiogram import Bot, Dispatcher, executor, types
import openpyxl
import random

TOKEN = "6288253508:AAGaI6QFwiG4RHYzeTlYCy-Xfh0z8WQ7o-c"
bot = Bot(TOKEN)
dp = Dispatcher(bot)
book=openpyxl.open("file1.xlsx",read_only=True)
sheet=book.active
file1=[]
for row in range(1,4):
    file=(sheet[row][0].value)
    file1.append(file)
vybor=random.choice(file1)
a=file1.index(vybor)
b=a
file2=[]
for row in range(1,4):
    file3=(sheet[row][1].value)
    file2.append(file3)
g=file2[b]

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(text="Привет, это игра кто хочет стать миллионером!\n"
                              "чтобы начать напишите 'начать игру'")

@dp.message_handler(text=['начать игру'])
async def start1(message: types.Message):
    await message.answer(text="Итак, первый вопрос\n 100 рублей")
    await message.answer(vybor)
    @dp.message_handler()
    async def otvetik(message: types.Message):
        if message.text==g:
            await message.answer("Это правильный ответ!\nВаш баланс:100\nЧтобы перейти к следующему вопросу напишите 'вопрос 2'")
        else:
            await message.answer("Это неверный ответ\n Чтобы начать сначала напишите 'начать игру'")
book=openpyxl.open("file1.xlsx",read_only=True)
sheet=book.active
file1=[]
for row in range(1,4):
    file=(sheet[row][0].value)
    file1.append(file)
vybor2=random.choice(file1)
if vybor2!=vybor:
    a=file1.index(vybor2)
    b=a
    file2=[]
    for row in range(1,4):
        file3=(sheet[row][1].value)
        file2.append(file3)
    g=file2[b]
else:
    vybor2 = random.choice(file1)
    a = file1.index(vybor2)
    b = a
    file2 = []
    for row in range(1, 4):
        file3 = (sheet[row][1].value)
        file2.append(file3)
    g = file2[b]
@dp.message_handler(text=['вопрос 2'])
async def start2(message: types.Message):
    await message.answer(text="второй вопрос\n 1000 рублей")
    await message.answer(vybor2)
    @dp.message_handler()
    async def otvetik2(message: types.Message):
        if message.text == g:
            await message.answer("Это правильный ответ!\nВаш баланс:1100\nЧтобы перейти к следующему вопросу напишите 'вопрос 3'")
        else:
            await message.answer("Это неверный ответ\n Чтобы начать сначала напишите 'начать игру'")
book=openpyxl.open("file1.xlsx",read_only=True)
sheet=book.active
file1=[]
for row in range(1,4):
    file=(sheet[row][0].value)
    file1.append(file)
vybor3=random.choice(file1)
if vybor3!=vybor2 and vybor3!=vybor:
    a=file1.index(vybor3)
    b=a
    file2=[]
    for row in range(1,4):
        file3=(sheet[row][1].value)
        file2.append(file3)
    g=file2[b]
else:
    vybor3 = random.choice(file1)
    a = file1.index(vybor3)
    b = a
    file2 = []
    for row in range(1, 4):
        file3 = (sheet[row][1].value)
        file2.append(file3)
    g = file2[b]
@dp.message_handler(text=['вопрос 3'])
async def start3(message: types.Message):
    await message.answer(text="третий вопрос\n10000 рублей")
    await message.answer(vybor3)
    @dp.message_handler()
    async def otvetik3(message: types.Message):
        if message.text == g:
            await message.answer(
                "Это правильный ответ!\nВаш баланс:11100\nЧтобы перейти к следующему вопросу напишите 'вопрос 4'")
        else:
            await message.answer("Это неверный ответ\n Чтобы начать сначала напишите 'начать игру'")
book=openpyxl.open("file1.xlsx",read_only=True)
sheet=book.active
file1=[]
for row in range(1,4):
    file=(sheet[row][0].value)
    file1.append(file)
vybor4=random.choice(file1)
if vybor4!=vybor3 and vybor4!=vybor2 and vybor4!=vybor:
    a=file1.index(vybor4)
    b=a
    file2=[]
    for row in range(1,4):
        file3=(sheet[row][1].value)
        file2.append(file3)
    g=file2[b]
else:
    vybor4 = random.choice(file1)
    a = file1.index(vybor4)
    b = a
    file2 = []
    for row in range(1, 4):
        file3 = (sheet[row][1].value)
        file2.append(file3)
    g = file2[b]
@dp.message_handler(text=['вопрос 4'])
async def start4(message: types.Message):
    await message.answer(text="четвертыый вопрос\n100000 рублей")
    await message.answer(vybor4)
    @dp.message_handler()
    async def otvetik3(message: types.Message):
        if message.text == g:
            await message.answer(
                "Это правильный ответ!\nВаш баланс:\nЧтобы перейти к следующему вопросу напишите 'вопрос 5'")
        else:
            await message.answer("Это неверный ответ\n Чтобы начать сначала напишите 'начать игру'")
book=openpyxl.open("file1.xlsx",read_only=True)
sheet=book.active
file1=[]
for row in range(1,4):
    file=(sheet[row][0].value)
    file1.append(file)
vybor5=random.choice(file1)
if vybor5!=vybor4 and vybor5!=vybor3 and vybor5!=vybor2 and vybor5!=vybor:
    a=file1.index(vybor5)
    b=a
    file2=[]
    for row in range(1,4):
        file3=(sheet[row][1].value)
        file2.append(file3)
    g=file2[b]
else:
    vybor5 = random.choice(file1)
    a = file1.index(vybor5)
    b = a
    file2 = []
    for row in range(1, 4):
        file3 = (sheet[row][1].value)
        file2.append(file3)
    g = file2[b]
@dp.message_handler(text=['вопрос 5'])
async def start4(message: types.Message):
    await message.answer(text="пятый вопрос\n1000000 рублей")
    await message.answer(vybor5)
    @dp.message_handler()
    async def otvetik3(message: types.Message):
        if message.text == g:
            await message.answer(
                "Это правильный ответ!\nВаш баланс:1111100\nПоздравляем, вы победили")
        else:
            await message.answer("Это неверный ответ\n Чтобы начать сначала напишите 'начать игру'")