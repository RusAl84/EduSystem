from webbrowser import get
import telebot
import get_data as gd
import tester as ts


bot = telebot.TeleBot('5982175377:AAGJU-Qn8gPejnDymRFTpz_-bH_low5aTBI')
global categories, test_data, test_num, mark, cur_cat, cur_theme
categories = gd.load_data()
test_data = ts.load_data()
cur_cat = cur_theme = test_num = mark = 0


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global cur_cat, cur_theme, categories, sub_categories
    splitted_text = str(message.text).lower().split()
    if str(message.text).lower() == "привет":
        bot.send_message(
            message.from_user.id, "Привет, чем я могу тебе помочь? Для информации введите /help.")
    elif cur_cat == -1:
        # str1 = gd.get_sub_categories(sub_categories, cur_cat)
        if str(message.text).isdigit():
            cur_cat = int(message.text)
            str1 = gd.get_sub_categories(categories, cur_cat)
            cur_theme = -1
            bot.send_message(
                message.from_user.id, str1)
        else:
            bot.send_message(
                message.from_user.id, "не верно введен номер раздела")
    elif cur_theme == -1:
        if str(message.text).isdigit():
            cur_theme = int(message.text)
            data = gd.get_desc(categories, cur_cat, cur_theme)
            cur_cat = 0
            cur_theme = 0
            bot.send_message(
                message.from_user.id, data)
        else:
            bot.send_message(
                message.from_user.id, "не верно введен номер темы")
    elif test_num >= 1:
            if str(message.text).isdigit():
                mark += int(message.text)
            
    elif str(message.text).lower() == "/info":
        cur_cat = -1
        str1 = gd.get_categories(categories)
        bot.send_message(
            message.from_user.id, str1)
    elif str(message.text).lower() == "/test":
        test_num = 1
        str1 = ts.get_quest(test_data, test_num)
        bot.send_message(
            message.from_user.id, str1)
    elif str(message.text).lower() == "/help":
        bot.send_message(
            message.from_user.id, "Описание проекта \n Для того чтобы получить информацию введите слово /info. \n Для того чтобы проверить свои знания введите слово /test.")
    else:
        bot.send_message(message.from_user.id, "Для информации введите /help.")


if __name__ == '__main__':

    bot.polling(none_stop=True, interval=0)
