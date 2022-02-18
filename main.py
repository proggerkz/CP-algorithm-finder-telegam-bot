import telebot
import links
from telebot import types

bot = telebot.TeleBot("5281705986:AAFCCg69u5beK349HhS7KM2kNBuZZOFEWU4", parse_mode="None")

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
    if message.text == '/search':
        bot.reply_to(message, 'Please write down the tag to find algorithm:')
        bot.register_next_step_handler(message, search_algorithm)
    elif message.text == '/algorithms':
        pass
    elif message.text == '/donation':
        pass


@bot.message_handler(func=lambda m: True)
def answer_message(message):
    if message.text == links.search_text:
        bot.reply_to(message, 'Please write down the Algorithm name to find it!')
        bot.register_next_step_handler(message, search_algorithm)
    elif message.text == links.algorithms_text:
        algorithm_list(message)
    elif message.text == links.donation_text:
        pass
    else:
        bot.reply_to(message, 'Sorry. I didnt understand what you wrote. You can use /help to check the commands')


def algorithm_list(message):

    marks = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in range(0, len(links.listOfAlgorithms), 2):
        item1 = types.KeyboardButton(links.listOfAlgorithms[i])
        item2 = types.KeyboardButton(links.listOfAlgorithms[i + 1])
        marks.row(item1, item2)
    item = types.KeyboardButton('Go to the main menu')
    marks.row(item)
    bot.send_message(message.from_user.id, 'Choose the algorithm chapter', reply_markup=marks)


def search_algorithm(message):
    bot.reply_to(message, message.text)


def algorithms(message):
    marks = types.ReplyKeyboardMarkup(resize_keyboard=True)
    marks.row('Go main menu')


bot.infinity_polling()
