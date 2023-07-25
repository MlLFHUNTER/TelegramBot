import telebot
import random
from stories import list_with_stories
TOKEN = '6358142376:AAGf3KBI6YHn3GqQPHDyMdkOEWEUPYLjNAk'
bot = telebot.TeleBot(TOKEN)

list_with_jokes = ['Фея від відьми відрізняється тільки настроєм.',
                   '- Що це? Шило?\n- Ні. Це штопор стерся!',
                   '- Хочеш випити?\n- Ні, спасибі.\n- Тоді потримай пляшку.',
                   'Не так страшно, якщо тебе назвуть дурнем, гірше - якщо виявляться праві.',
                   'Корпоратив вдався - це коли трудову книжку тобі привезли відразу додому.',
                   'Якщо цукор ще подорожчає, його можна буде дарувати на ювілеї та весілля.',
                   'Боїшся стрибати з парашутом?\n– Так.\n– Стрибай без нього.',
                   'Ніколи не смійся з цигана, що їде на велосипеді.Це може бути твій велосипед.',
                   'а м’ясокомбінаті одна корова запитує іншу:– Ти тут вперше?\n– Ні, блін, удруге!',
                   'B нашій сім’ї зарядкою займаються лише мобільні телефони…',
                   'Чоловік з дружиною вночі у ліжку:\n– Коханий, візьми мене.\n– Спи, я нікуди не їду.',
                   'Привіт, говорити можеш?\n– Так, з трьох років.',
                   'Що Вам заважає схуднути?\n– Відчуття голоду!',
                   ]


# Game
def play_game(message):
    chat_id = message.chat.id
    user_choice = message.text.lower()
    choices = ['🪨', '✂️', '📋']

    if user_choice not in choices:
        bot.reply_to(message, "Неправильний вибір. Вибери камінь, ножиці або бумагу.")
    else:
        bot_choice = random.choice(choices)
        bot.reply_to(message, f"Ти обрав {user_choice}, а я обрав {bot_choice}.")

        if user_choice == bot_choice:
            bot.send_message(chat_id, "Нічия!")
        elif user_choice == '🪨' and bot_choice == '✂️' or \
                user_choice == '✂️' and bot_choice == '📋' or \
                user_choice == '📋' and bot_choice == '🪨':
            bot.send_message(chat_id, "Ти переміг!")
        else:
            bot.send_message(chat_id, "Я переміг!")

    start(message)


# Function for film recommendation
def rec_film(message):
    dict1 = {'Драма': 'https://www.imdb.com/search/title/?genres=drama&title_type=feature&explore=genres',
             'Тріллер': 'https://www.imdb.com/search/title/?title_type=feature&genres=thriller',
             'Екшн': 'https://www.imdb.com/search/title/?title_type=feature&genres=action&start=51&ref_=adv_nxt',
             'Анімаційний фільм': 'https://www.imdb.com/search/title/?title_type=feature&genres=animation',
             'Документальний фільм': 'https://www.imdb.com/search/title/?genres=documentary',
             'Комедія': 'https://www.imdb.com/search/title/?title_type=feature&genres=comedy'
             }
    for elem in dict1:
        if elem == message.text:
            url_link = dict1[elem]
            markup = telebot.types.InlineKeyboardMarkup()
            button1 = telebot.types.InlineKeyboardButton("Сайт з відповідними фільмами", url=url_link)
            markup.add(button1)
            bot.send_message(message.chat.id, 'Перейди на сайт', reply_markup=markup)

    start(message)


# Function for book recommendation
def rec_books(message):
    dict1 = {'Класика': 'https://www.panmacmillan.com/blogs/classics/classic-books-to-read-before-you-die',
             'Детектив': 'https://prowritingaid.com/detective-books',
             'Роман': 'https://www.goodhousekeeping.com/life/entertainment/g26143680/best-romance-novels/',
             'Фентезі': 'https://time.com/collection/100-best-fantasy-books/',
             'Містика': 'https://www.shortform.com/best-books/genre/best-mysticism-books-of-all-time',
             'Психологія, Саморозвиток': 'https://reedsy.com/discovery/blog/psychology-books'
             }
    for elem in dict1:
        if elem == message.text:
            url_link = dict1[elem]
            markup = telebot.types.InlineKeyboardMarkup()
            button1 = telebot.types.InlineKeyboardButton("Сайт з відповідними книжками", url=url_link)
            markup.add(button1)
            bot.send_message(message.chat.id, 'Перейди на сайт', reply_markup=markup)

    start(message)


# Function for game recommendation
def rec_games(message):
    dict1 = {'Шутер': 'https://www.gamesradar.com/best-shooters/',
             'Платформер': 'https://gamerant.com/best-platformer-games-metacritic/#super-mario-3d-world---93',
             'Стратегія': 'https://www.pcgamer.com/the-best-strategy-games/',
             'Tower Defense': 'https://parade.com/1056226/marynliles/best-tower-defense-games/',
             'Пригоди': 'https://www.gamesradar.com/best-adventure-games/',
             'Спорт': 'https://www.gamesradar.com/best-sports-games/'
             }
    for elem in dict1:
        if elem == message.text:
            url_link = dict1[elem]
            markup = telebot.types.InlineKeyboardMarkup()
            button1 = telebot.types.InlineKeyboardButton("Сайт з відповідними іграми", url=url_link)
            markup.add(button1)
            bot.send_message(message.chat.id, 'Перейди на сайт', reply_markup=markup)

    start(message)


# Function for songs recommendation
def rec_songs(message):
    dict1 = {'Рок': 'https://open.spotify.com/playlist/37i9dQZF1DX6KANutsQaVe',
             'Поп': 'https://open.spotify.com/playlist/3ZgmfR6lsnCwdffZUan8EA',
             'Реп': 'https://open.spotify.com/playlist/6p3IRyXLrl28mu33AHtqnj',
             'Електро': 'https://open.spotify.com/playlist/1zsMB814a8VhwohGe2ZTpd',
             'Рейв': 'https://open.spotify.com/playlist/3ybZkcoA09pYekp0DIo1OP',
             'Фонк': 'https://open.spotify.com/playlist/37i9dQZF1DWWY64wDtewQt'
             }
    for elem in dict1:
        if elem == message.text:
            url_link = dict1[elem]
            markup = telebot.types.InlineKeyboardMarkup()
            button1 = telebot.types.InlineKeyboardButton("Відповідний  плейліст у Spotify", url=url_link)
            markup.add(button1)
            bot.send_message(message.chat.id, 'Перейди на сайт', reply_markup=markup)

    start(message)


def jokes(message):
    global list_with_jokes
    random_val = random.randint(1, len(list_with_jokes) - 1)
    random_joke = list_with_jokes[random_val]
    bot.send_message(message.chat.id, random_joke)


list1 = list_with_stories


def story(message):
    global list1
    rand_val = random.randint(1, len(list1) - 1)
    rand_story = list1[rand_val]
    bot.send_message(message.chat.id, rand_story)


@bot.message_handler(commands=['start'])
def start(message):
    typ = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = telebot.types.KeyboardButton('😆Випадковий жарт')
    item2 = telebot.types.KeyboardButton('📚Яку книжку мені прочитати?')
    item3 = telebot.types.KeyboardButton('🎮В яку гру мені пограти?')
    item4 = telebot.types.KeyboardButton('🗣Розкажи цікаву історію')
    item5 = telebot.types.KeyboardButton('🎸Яку музику послухати?')
    item6 = telebot.types.KeyboardButton('🎲Давай пограємо!')
    item7 = telebot.types.KeyboardButton('🎬Який фільм подивитись?')
    typ.add(item1, item2, item3, item4, item5, item6, item7)

    bot.send_message(message.chat.id, " {0.first_name}, Обери пункт в меню.".format(message.from_user),
                     reply_markup=typ)


@bot.message_handler(content_types=['text', 'number'])
def bot_message(message):
    if message.chat.type == 'private':
        # Back
        if message.text == '⬅️Назад':
            typ = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = telebot.types.KeyboardButton('😆Випадковий жарт')
            item2 = telebot.types.KeyboardButton('📚Яку книжку мені прочитати?')
            item3 = telebot.types.KeyboardButton('🎮В яку гру мені пограти?')
            item4 = telebot.types.KeyboardButton('🗣Розкажи цікаву історію')
            item5 = telebot.types.KeyboardButton('🎸Яку музику послухати?')
            item6 = telebot.types.KeyboardButton('🎲Давай пограємо!')
            item7 = telebot.types.KeyboardButton('🎬Який фільм подивитись?')
            typ.add(item1, item2, item3, item4, item5, item6, item7)

            bot.send_message(message.chat.id, "Обери дію", reply_markup=typ)

        # Film recommendation
        elif message.text == '🎬Який фільм подивитись?':
            typ = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            item_1 = telebot.types.KeyboardButton('Драма')
            item_2 = telebot.types.KeyboardButton('Тріллер')
            item_3 = telebot.types.KeyboardButton('Екшн')
            item_4 = telebot.types.KeyboardButton('Анімаційний фільм')
            item_5 = telebot.types.KeyboardButton('Документальний фільм')
            item_6 = telebot.types.KeyboardButton('Комедія')
            back = telebot.types.KeyboardButton('⬅️Назад')

            typ.add(item_1, item_2, item_3, item_4, item_5, item_6, back)
            msg = bot.send_message(message.chat.id, 'Обери жанр: ', reply_markup=typ)
            bot.register_next_step_handler(msg, rec_film)

        # Book recommendation
        elif message.text == '📚Яку книжку мені прочитати?':
            typ = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            item_1 = telebot.types.KeyboardButton('Класика')
            item_2 = telebot.types.KeyboardButton('Детектив')
            item_3 = telebot.types.KeyboardButton('Роман')
            item_4 = telebot.types.KeyboardButton('Фентезі')
            item_5 = telebot.types.KeyboardButton('Містика')
            item_6 = telebot.types.KeyboardButton('Психологія, Саморозвиток')
            back = telebot.types.KeyboardButton('⬅️Назад')

            typ.add(item_1, item_2, item_3, item_4, item_5, item_6, back)
            msg = bot.send_message(message.chat.id, 'Обери жанр: ', reply_markup=typ)
            bot.register_next_step_handler(msg, rec_books)

        # Game recommendation
        elif message.text == '🎮В яку гру мені пограти?':
            typ = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            item_1 = telebot.types.KeyboardButton('Шутер')
            item_2 = telebot.types.KeyboardButton('Платформер')
            item_3 = telebot.types.KeyboardButton('Стратегія')
            item_4 = telebot.types.KeyboardButton('Tower Defense')
            item_5 = telebot.types.KeyboardButton('Пригоди')
            item_6 = telebot.types.KeyboardButton('Спорт')
            back = telebot.types.KeyboardButton('⬅️Назад')

            typ.add(item_1, item_2, item_3, item_4, item_5, item_6, back)
            msg = bot.send_message(message.chat.id, 'Обери жанр: ', reply_markup=typ)
            bot.register_next_step_handler(msg, rec_games)

        # Music recommendation
        elif message.text == '🎸Яку музику послухати?':
            typ = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            item_1 = telebot.types.KeyboardButton('Рок')
            item_2 = telebot.types.KeyboardButton('Поп')
            item_3 = telebot.types.KeyboardButton('Реп')
            item_4 = telebot.types.KeyboardButton('Електро')
            item_5 = telebot.types.KeyboardButton('Рейв')
            item_6 = telebot.types.KeyboardButton('Фонк')
            back = telebot.types.KeyboardButton('⬅️Назад')

            typ.add(item_1, item_2, item_3, item_4, item_5, item_6, back)
            msg = bot.send_message(message.chat.id, 'Обери жанр: ', reply_markup=typ)
            bot.register_next_step_handler(msg, rec_songs)

        # Game
        elif message.text == '🎲Давай пограємо!':
            typ = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            item_1 = telebot.types.KeyboardButton('🪨')
            item_2 = telebot.types.KeyboardButton('✂️')
            item_3 = telebot.types.KeyboardButton('📋')
            back = telebot.types.KeyboardButton('⬅️Назад')

            typ.add(item_1, item_2, item_3, back)
            bot.send_message(message.chat.id, 'Гра: Камінь Ножиці Бумага')
            msg = bot.send_message(message.chat.id, 'Обери чим зіграєш', reply_markup=typ)
            bot.register_next_step_handler(msg, play_game)

        # Jokes
        elif message.text == '😆Випадковий жарт':
            bot.send_message(message.chat.id, 'Ось жарт який може тобі сподобатися')
            jokes(message)

        # Interesting story
        elif message.text == '🗣Розкажи цікаву історію':
            bot.send_message(message.chat.id, 'Ось цікава історія')
            story(message)


bot.polling(none_stop=True)
