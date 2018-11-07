import telebot
from telebot import types
from bot_cesar.const import token

bot = telebot.TeleBot(token)


@bot.inline_handler(lambda query: len(query.query) > 0)
def encrypt_text(query):

    result = types.InlineQueryResultArticle(id=1, title='отправить зашифрованное послание',
                                            input_message_content=types.InputTextMessageContent(message_text='qqq'))

    bot.answer_inline_query(query.id, [result])


if __name__ == '__main__':
    bot.polling(none_stop=True)
