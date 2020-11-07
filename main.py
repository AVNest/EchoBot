# Bot Weather In... (v.0.1.1  4.11.2020)

import settings
import config
from pyowm.owm import OWM
import telebot


bot = telebot.TeleBot(config.token)
owm = OWM('b6374ac85952d51a4daa5baf0f867ec4', config.config_dict) # your token in pyOWN
mgr = owm.weather_manager()


@bot.message_handler(content_types=['text'])
def send_welcome(message):
    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    wind_dict_in_meters_per_sec = w.wind()
    temp = w.temperature('celsius')["temp"]

    answer = "В городе " + message.text + " так то " + w.detailed_status + "\n"
    answer += "Ветер сегодня " + str(wind_dict_in_meters_per_sec.get('speed')) + " метра в секунду" + "\n"
    answer += "Тепература сейчас где то " + str(temp) + "°C" + "\n\n"

    if temp < -30:
        answer += "Чот походу из дома лучше не выходить..."
    elif temp < -5:
        answer += "Походу лучше одеться тепло ))"
    elif temp < 8:
        answer += "Ты же вкурсе, что уже холодно, надень шапку )))"
    elif temp < 15:
        answer += "Самое время искать теплые вещи"
    elif temp < 22:
        answer += "Не знаю как тебе, но мне пока комфортно"
    elif temp < 28:
        answer += "Погода нишьяяяяяк!"
    else:
        answer += "Ташкееееент"

    bot.send_message(message.chat.id, answer)


if __name__ == '__main__':
    bot.polling(none_stop=True)
