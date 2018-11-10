import telebot
from telebot import types
from bot_cesar.const import token, recipe, help_text
from bot_cesar.function import translate
from bot_cesar.text_check import check, only_text
from random import sample
from re import match

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, '*Привет!*\n\n/help - возможности бота', parse_mode='Markdown')


@bot.message_handler(commands=['help'])
def handle_start(message):
    bot.send_message(message.chat.id, help_text, parse_mode='Markdown')


@bot.message_handler(commands=['recipe'])
def handle_start(message):
    bot.send_message(message.chat.id, recipe, parse_mode='Markdown')


@bot.message_handler(content_types=['text'])
def translate_text(message):

    if check(message.text):
        bot.send_message(message.from_user.id, f'{translate(only_text(message.text), check(message.text))} '
                                               f'[{-check(message.text)}]')
        # bot.send_message(message.from_user.id, f'{translate(message.text, check(message.text))}')

    else:
        bot.send_message(message.from_user.id, 'Введите коректный текст!')


@bot.inline_handler(lambda query: len(query.query) > 0 and match('\[-?\d+\]', query.query.rstrip().split()[-1]))
def encrypt_text(query):
    # функция срабатывает, если в конце текста юзер указывает ключ ( привет [4] )
    var_1 = types.InlineQueryResultArticle(id=1, title=f'< Шифрование >',
                                           description=f'{translate(only_text(query.query), check(query.query))}'
                                                       f' [{-check(query.query)}]',
                                           input_message_content=types.InputTextMessageContent
                                           (message_text=f'{translate(only_text(query.query), check(query.query))}'
                                                         f' [{-check(query.query)}]'))

    bot.answer_inline_query(query.id, [var_1])


@bot.inline_handler(lambda query: len(query.query) > 0)
def encrypt_text(query):

    num_1, num_2, num_3 = sample(list(filter(lambda x: x != 0, range(-30, 30))), 3)  # 3 числа ( != 0 )

    var_1 = types.InlineQueryResultArticle(id=1, title=f'Зашифровать текущее сообщение [{num_1}]',
                                           input_message_content=types.InputTextMessageContent
                                           (message_text=f'{translate(query.query, num_1)} [{-num_1}]'))

    var_2 = types.InlineQueryResultArticle(id=2, title=f'Зашифровать текущее сообщение [{num_2}]',
                                           input_message_content=types.InputTextMessageContent(
                                            message_text=f'{translate(query.query, num_2)} [{-num_2}]'))

    var_3 = types.InlineQueryResultArticle(id=3, title=f'Зашифровать текущее сообщение [{num_3}]',
                                           input_message_content=types.InputTextMessageContent(
                                            message_text=f'{translate(query.query, num_3)} [{-num_3}]'))

    bot.answer_inline_query(query.id, [var_1, var_2, var_3])


if __name__ == '__main__':
    bot.polling(none_stop=True)
