import telebot
import links
import config
import DB
from telebot import types


bot = telebot.TeleBot(config.TOKEN, parse_mode="None")

user = bot.get_me()

updates = bot.get_updates()


@bot.message_handler(commands=['start'])
def send_welcome(message):
    marks = types.ReplyKeyboardMarkup(resize_keyboard=True )
    item1 = types.KeyboardButton(links.search_text)
    item2 = types.KeyboardButton(links.algorithms_text)
    item3 = types.KeyboardButton(links.donation_text)
    marks.row(item1)
    marks.row(item2, item3)
    bot.send_message(message.from_user.id, links.welcome_text, reply_markup=marks, parse_mode='MarkDown')


@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.from_user.id, links.help_text)


@bot.message_handler(commands=['search', 'algorithms', 'donation'])
def commands(message):
    message.text = links.rqToText.get(message.text)
    answer_message(message)


@bot.message_handler(func=lambda m: True)
def answer_message(message):
    if message.text == 'Go to the main menu':
        message.text = links.welcome_text
        return send_welcome(message)
    if message.text in links.idForAlgorithms.keys():
        get_algo(message, links.idForAlgorithms.get(message.text))
    elif message.text == links.algorithms_text:
        algorithm_list(message)
    elif message.text == links.donation_text:
        bot.reply_to(message, links.donation_answer)
    elif message.text == links.search_text:
        bot.reply_to(message, links.search_message_text)
        bot.register_next_step_handler(message, search_algorithm)
    else:
        bot.reply_to(message, 'Sorry. I didnt understand what you wrote. You can use /help to check the commands')


@bot.callback_query_handler(func=lambda call: True)
def get_algo(message):
    for i in range(len(DB.algos)):
        if message.data in DB.algos[i]:
            bot.send_message(message.from_user.id, message.data + "  -  " + DB.algos[i].get(message.data))
            return


def get_algo(message, algo_id):
    graph_list = list(DB.algos[algo_id].keys())
    markup = types.InlineKeyboardMarkup()
    for i in range(len(graph_list)):
        item = types.InlineKeyboardButton(text=graph_list[i], callback_data=graph_list[i])
        markup.add(item)
    bot.send_message(message.from_user.id, 'Choose algorithm link you want to see:', reply_markup=markup)


def algorithm_list(message):
    marks = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in range(0, len(links.listOfAlgorithms), 2):
        item1 = types.KeyboardButton(links.listOfAlgorithms[i])
        item2 = types.KeyboardButton(links.listOfAlgorithms[i + 1])
        marks.row(item1, item2)
    item = types.KeyboardButton('Go to the main menu')
    marks.row(item)
    bot.send_message(message.from_user.id, 'Choose the algorithm chapter', reply_markup=marks)


def lcs(x, y, m, n):
    if m == 0 or n == 0:
        return 0;
    elif x[m - 1] == y[n - 1]:
        return 1 + lcs(x, y, m - 1, n - 1);
    else:
        return max(lcs(x, y, m, n - 1), lcs(x, y,    m - 1, n));


def search_algorithm(message):
    sorted_list = []
    markup = types.InlineKeyboardMarkup()
    for i in range(len(DB.algos)):
        chapter = list(DB.algos[i].keys())
        for j in range(len(chapter)):
            edit_dist = lcs(message.text, chapter[j], len(message.text), len(chapter[j]))
            # print(edit_dist)
            sorted_list.append([edit_dist, chapter[j]])
    sorted_list.sort(reverse=True)
    markup = types.InlineKeyboardMarkup()

    for i in range(min(len(sorted_list), 6)):
        item = types.InlineKeyboardButton(text=sorted_list[i][1], callback_data=sorted_list[i][1])
        markup.add(item)
    bot.send_message(message.from_user.id, 'Choose algorithm link you want to see:', reply_markup=markup)


bot.infinity_polling()
