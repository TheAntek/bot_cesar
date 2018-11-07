import telebot
from telebot import types
from bot_cesar.const import token, recipe
from bot_cesar.function import translate
from random import sample

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, '/help - рецепт')


@bot.message_handler(commands=['help'])
def handle_start(message):
    bot.send_message(message.chat.id, recipe, parse_mode='Markdown')


@bot.inline_handler(lambda query: len(query.query) > 0)
def encrypt_text(query):

    num_1, num_2, num_3 = sample(list(filter(lambda x: x != 0, range(-30, 30))), 3)  # 3 числа ( != 0 )

    var_1 = types.InlineQueryResultArticle(id=1, title=f'Зашифровать текущее сообщение [{num_1}]',
                                           input_message_content=types.InputTextMessageContent(message_text=translate(
                                               query.query, num_1)))

    var_2 = types.InlineQueryResultArticle(id=2, title=f'Зашифровать текущее сообщение [{num_2}]', input_message_content=types.
                                           InputTextMessageContent(message_text=translate(query.query, num_2)))

    var_3 = types.InlineQueryResultArticle(id=3, title=f'Зашифровать текущее сообщение [{num_3}]', input_message_content=types.
                                           InputTextMessageContent(message_text=translate(query.query, num_3)))

    bot.answer_inline_query(query.id, [var_1, var_2, var_3])


if __name__ == '__main__':
    bot.polling(none_stop=True)
