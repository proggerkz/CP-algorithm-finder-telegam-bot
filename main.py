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
    item4 = types.KeyboardButton(links.credentials_title)
    marks.row(item1)
    marks.row(item2, item4)
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
    if message.text == links.go_back_text:
        message.text = links.welcome_text
        return send_welcome(message)
    if message.text in links.idForAlgorithms.keys():
        get_algo(message, links.idForAlgorithms.get(message.text), 0)
    elif message.text == links.credentials_title:
        bot.reply_to(message, links.credentials_text)
    elif message.text == links.algorithms_text:
        algorithm_list(message)
    elif message.text == links.donation_text:
        bot.reply_to(message, links.donation_answer)
    elif message.text == links.search_text:
        bot.reply_to(message, links.search_message_text)
        bot.register_next_step_handler(message, search_algorithm)
    else:
        search_algorithm(message)


@bot.callback_query_handler(func=lambda call: True)
def get_algo(message):
    if '0' <= message.data[0] <= '9':
        id, algo_id, msg_type = message.data.split()
        if msg_type == 'Next':
            get_algo(message, int(algo_id), int(id) + 5)
        else:
            get_algo(message, int(algo_id), int(id) - 5)
    else:
        for i in range(len(DB.algos)):
            if message.data in DB.algos[i]:
                bot.send_message(message.from_user.id, message.data + "  -  " + DB.algos[i].get(message.data))
                return


def get_algo(message, algo_id, id):
    graph_list = list(DB.algos[algo_id].keys())
    markup = types.InlineKeyboardMarkup()
    for i in range(id, min(len(graph_list), id + 5)):
        item = types.InlineKeyboardButton(text=graph_list[i], callback_data=graph_list[i])
        markup.add(item)
    if id != 0 and id + 5 < len(graph_list):
        item = types.InlineKeyboardButton(text='Prev', callback_data=str(id) + ' ' + str(algo_id) + ' Prev')
        item2 = types.InlineKeyboardButton(text='Next', callback_data=str(id) + ' ' + str(algo_id) + ' Next')
        markup.add(item, item2)
    elif id != 0:
        item = types.InlineKeyboardButton(text='Prev', callback_data=str(id) + ' ' + str(algo_id) + ' Prev')
        markup.add(item)
    elif id + 5 < len(graph_list):
        item2 = types.InlineKeyboardButton(text='Next', callback_data=str(id) + ' ' + str(algo_id) + ' Next')
        markup.add(item2)
    bot.send_message(message.from_user.id, 'Choose algorithm link you want to see:', reply_markup=markup)


def algorithm_list(message):
    marks = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in range(0, len(links.listOfAlgorithms), 2):
        item1 = types.KeyboardButton(links.listOfAlgorithms[i])
        item2 = types.KeyboardButton(links.listOfAlgorithms[i + 1])
        marks.row(item1, item2)
    item = types.KeyboardButton(links.go_back_text)
    marks.row(item)
    bot.send_message(message.from_user.id, 'Choose the algorithm chapter', reply_markup=marks)


def lcs(x, y, m, n):
    m = len(x)
    n = len(y)
    lst = [[0] * (n + 1) for i in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                lst[i][j] = 0
            elif x[i - 1] == y[j - 1]:
                lst[i][j] = lst[i - 1][j - 1] + 1
            else:
                lst[i][j] = max(lst[i - 1][j], lst[i][j - 1])
    return lst[m][n]


def search_algorithm(message):
    if message.text in [links.search_text, links.credentials_title, links.algorithms_text]:
        answer_message(message)
        return
    sorted_list = []
    for i in range(len(DB.algos)):
        chapter = list(DB.algos[i].keys())
        for j in range(len(chapter)):
            edit_dist = lcs(message.text, chapter[j], len(message.text), len(chapter[j]))
            sorted_list.append([edit_dist, chapter[j]])
    sorted_list.sort(reverse=True)
    markup = types.InlineKeyboardMarkup()
    if sorted_list[0][0] < 3:
        bot.send_message(message.from_user.id, links.try_again_text)
        return
    for i in range(min(len(sorted_list), 6)):
        item = types.InlineKeyboardButton(text=sorted_list[i][1], callback_data=sorted_list[i][1])
        markup.add(item)
    bot.send_message(message.from_user.id, 'Choose algorithm link you want to see:', reply_markup=markup)


bot.infinity_polling()