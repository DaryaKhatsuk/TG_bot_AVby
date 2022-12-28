from aiogram import Bot, executor, types
import asyncio
import logging
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Command
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import aiohttp
import config
import keyboard
from bs4 import BeautifulSoup
import re

storage = MemoryStorage()  # FSM
bot = Bot(token=config.botkey, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(
    # указываем название с логами
    filename='log.txt',
    # указываем уровень логирования
    level=logging.INFO,
    # указываем формат сохранения логов
    format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s '
           u'[%(asctime)s] %(message)s')


@dp.message_handler(Command('start'), state=None)
async def welcome(message):
    joinedFile = open('user.txt', 'r')
    joinedUsers = set()
    for line in joinedFile:
        joinedUsers.add(line.strip())

    if not str(message.chat.id) in joinedUsers:
        joinedFile = open('user.txt', 'a')
        joinedFile.write(str(message.chat.id) + '\n')
        joinedUsers.add(message.chat.id)

    await bot.send_message(message.chat.id, f'Здравствуйте, *{message.from_user.first_name},* бот работает\n'
                                            f'Выберите интересующую модель', reply_markup=keyboard.start,
                           parse_mode='Markdown')


@dp.callback_query_handler(text_contains='cancel')
async def cancel(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id, reply_markup=keyboard.start, text="Вы вернулись к странице 1")


@dp.message_handler(content_types='text')
async def get_message(message):

    if message.text == 'Страница 2':
        await bot.send_message(message.chat.id, text='Страница 2', reply_markup=keyboard.motorcycles_add_1,
                               parse_mode='Markdown')
    if message.text == 'Страница 3':
        await bot.send_message(message.chat.id, text='Страница 3', reply_markup=keyboard.motorcycles_add_2)
    if message.text == 'Страница 4':
        await bot.send_message(message.chat.id, text='Страница 4', reply_markup=keyboard.motorcycles_add_3)
    if message.text == 'Страница 5':
        await bot.send_message(message.chat.id, text='Страница 5', reply_markup=keyboard.motorcycles_add_4)
    if message.text == 'Страница 6':
        await bot.send_message(message.chat.id, text='Страница 6', reply_markup=keyboard.motorcycles_add_5)
    if message.text == 'Страница 7':
        await bot.send_message(message.chat.id, text='Страница 7', reply_markup=keyboard.motorcycles_add_6)
    if message.text == 'Страница 8':
        await bot.send_message(message.chat.id, text='Страница 8', reply_markup=keyboard.motorcycles_add_7)
    if message.text == 'Страница 9':
        await bot.send_message(message.chat.id, text='Страница 9', reply_markup=keyboard.motorcycles_add_8)
    if message.text == 'Страница 10':
        await bot.send_message(message.chat.id, text='Страница 10', reply_markup=keyboard.motorcycles_add_9)

    if message.text == 'Вернутся к странице 1':
        await bot.send_message(message.chat.id, text='Страница 1', reply_markup=keyboard.start)
    if message.text == 'Вернутся к странице 2':
        await bot.send_message(message.chat.id, text='Страница 2', reply_markup=keyboard.motorcycles_add_1)
    if message.text == 'Вернутся к странице 3':
        await bot.send_message(message.chat.id, text='Страница 3', reply_markup=keyboard.motorcycles_add_2)
    if message.text == 'Вернутся к странице 4':
        await bot.send_message(message.chat.id, text='Страница 4', reply_markup=keyboard.motorcycles_add_3)
    if message.text == 'Вернутся к странице 5':
        await bot.send_message(message.chat.id, text='Страница 5', reply_markup=keyboard.motorcycles_add_4)
    if message.text == 'Вернутся к странице 6':
        await bot.send_message(message.chat.id, text='Страница 6', reply_markup=keyboard.motorcycles_add_5)
    if message.text == 'Вернутся к странице 7':
        await bot.send_message(message.chat.id, text='Страница 7', reply_markup=keyboard.motorcycles_add_6)
    if message.text == 'Вернутся к странице 8':
        await bot.send_message(message.chat.id, text='Страница 8', reply_markup=keyboard.motorcycles_add_7)
    if message.text == 'Вернутся к странице 9':
        await bot.send_message(message.chat.id, text='Страница 9', reply_markup=keyboard.motorcycles_add_8)

    bike = {'Apollo', 'Aprilia', 'Avantis', 'BAJAJ', 'Baltmotors', 'Benelli', 'Beta', 'BMW', 'Briar', 'BRP', 'BRZ',
            'BSE', 'Buell', 'Cagiva', 'Cezet', 'Daelim', 'Ducati', 'Ekonika Roliz', 'Fuego', 'Gas Gas', 'Gilera', 'GR',
            'Guowei', 'Harley-Davidson', 'Honda', 'Hors', 'Husqvarna', 'Hyosung', 'Indian', 'Irbis', 'Jaguar', 'Jawa',
            'JMC', 'Kangchao', 'Kawasaki', 'Kayo', 'Keeway', 'Kinroad', 'Koshine', 'KTM', 'KXD', 'Kymco', 'Lifan',
            'Linhai', 'Loncin', 'Megelli', 'Motax', 'Moto Guzzi', 'Motoland', 'MV Agusta', 'MZ', 'Nexus', 'Nitro',
            'Pannonia', 'PitsterPro', 'Polini', 'Qingqi', 'Racer', 'Reggy', 'Regulmoto', 'Rieju', 'Royal Enfield',
            'Sherco', 'Skyline', 'Stels', 'Super Soco', 'Suzuki', 'SWM', 'TM Racing', 'Triumph', 'Vento', 'Victory',
            'Viper', 'Virus', 'VOGE', 'Wels', 'Xmotos', 'Yamaha', 'YCF', 'Zipp', 'Zongshen', 'Zuum', 'АВМ', 'Альфамото',
            'Восход', 'Днепр', 'ЗиД', 'ИЖ', 'Минск', 'Урал', 'Эксклюзив'}

    if message.text in bike:
        await bot.send_message(message.chat.id, text=f"Идет поиск, пожалуйста подождите", parse_mode='Markdown')

        async def get_content(session_request, mess):
            """
            :param mess:
            :param session_request: получает всю html информацию со страницы от функции parser.
            :soup: берет данный со страницы отправленные функцией parser
            :items: собирает со всей страницы все div классы под названием listing-item__wrap
            :AttributeError: обрабатывает отсутствие в карточках описания, т.к. это необязательный для
             заполнения пользователем параметр.
            :Exception: общее исключение для обработки внезапных ошибок.
            :return: safe_doc(cards), передает данные для сохранения в форматах json и csv
            """
            moto_rus = {
                'АВМ': 'avm',
                'Альфамото': 'alfamoto',
                'Восход': 'voshod',
                'Днепр': 'dnepr',
                'ЗиД': 'zid',
                'ИЖ': 'izh',
                'Минск': 'minsk',
                'Урал': 'ural',
                'Эксклюзив': 'eksklyuziv',
            }
            if moto_rus.get(mess):
                mess = moto_rus.get(mess)
            mess = str(mess).lower()
            soup = BeautifulSoup(await session_request, 'html.parser')
            items = soup.find_all('div', class_='listing-item__wrap')

            for item in items:
                try:
                    title_car = item.find('span', class_='link-text').text
                    href_car = 'https://moto.av.by' + item.find('a', class_='listing-item__link').get('href')
                    price_car_byn = item.find('div', class_='listing-item__price').text.replace('\xa0', ' ').replace(
                        '\u2009', ' ')
                    price_car_usd = item.find('div', class_='listing-item__priceusd').text.replace('\xa0', ' ').replace(
                        '\u2009', ' ')
                    params_car = item.findNext('div', class_='listing-item__params').text.replace('\n', ' ').replace(
                        '\u2009', ' ').replace('\xa0', ' ')
                    find = f'https+.+/{mess}/+.+\d'
                    if re.findall(pattern=find+'{,11}', string=str(href_car)):
                        href_car_final = href_car
                        print(href_car_final)
                        await bot.send_message(message.chat.id, f"{title_car}\nСсылка: {str(href_car_final)}\n"
                                                                f"Характеристики: {params_car}\n"
                                                                f"Цена в BYN: {price_car_byn}\n"
                                                                f"Цена в USD:{price_car_usd.replace('≈', ' ')}",
                                               parse_mode='Markdown')
                        await asyncio.sleep(0.4)
                except AttributeError:
                    title_car = item.find('span', class_='link-text').text
                    href_car = ['https://moto.av.by' + item.find('a', class_='listing-item__link').get('href')]
                    price_car_byn = item.find('div', class_='listing-item__price').text.replace('\xa0', ' ').replace(
                        '\u2009', ' ')
                    price_car_usd = item.find('div', class_='listing-item__priceusd').text.replace('\xa0', ' ').replace(
                            '\u2009', ' ')
                    find = f'https+.+/{mess}/+.+\d'
                    if re.findall(pattern=find + '{,11}', string=str(href_car)):
                        href_car_final = href_car
                        print(href_car_final)
                        await bot.send_message(message.chat.id, f"{title_car}\nСсылка: {str(href_car_final)}\n"
                                                                f"Характеристики: pass\n"
                                                                f"Цена в BYN: {price_car_byn}\n"
                                                                f"Цена в USD:{price_car_usd.replace('≈', ' ')}",
                                               parse_mode='Markdown')
                        print(f'params_car: pass')
                except Exception as ex:
                    print(f'Some {ex} here.')

        async def parser():
            """
            :async with aiohttp.ClientSession(): позволяет использовать одну сессию несколько раз.
            :session_request (первый): использует данные url и headers сети.
            :session_request.status == 200: проверяет что бы статус подключения на странице был 200,
             т.е. существующей, не пустой страницей.
            :counter: является счетчиком для отсчитывания страниц, в виду использования цикла while
            :session_request (второй): подставляет в открытую сессию точные данные страницы,
             которую нужно сейчас спарсить.
            :asyncio.create_task(get_content(session_request.text())): создает асинхронную задачу
             передачи данных со страницы, в виде текста, в функцию get_content.
            """
            HOST = 'https://av.by/'
            URL = 'https://moto.av.by/filter?category_type=1'
            HEADERS = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0',
            }
            async with aiohttp.ClientSession() as session:
                session_request = await session.get(url=URL, headers=HEADERS)
                counter = 1
                while session_request.status == 200:
                    session_request = await session.get(url=URL + '&page=' + str(counter))
                    print(f'Parsing page {counter}')
                    asyncio.create_task(get_content(session_request.text(), message.text))
                    counter += 1
                else:
                    print(f"Session status: {session_request.status}. Data is finish.")
                    await bot.send_message(message.chat.id, text=f"Поиск завершен", parse_mode='Markdown')
                    await bot.send_message(message.chat.id, text='Что бы вернутся к 1 странице нажмите: ',
                                           reply_markup=keyboard.return_keyb, parse_mode='Markdown')

        loop = asyncio.get_event_loop()
        loop.create_task(parser())


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
