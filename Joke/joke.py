import telebot
import random
from telebot import types

f = open('data/fun.txt', 'r', encoding='UTF-8')
fun = f.read().split('\n')
f.close()


bot = telebot.TeleBot('5958754149:AAGZR7GbOLWU_--ESFZYqgA6y-bM9A_DJP0')

@bot.message_handler(commands=["start"])
def start(m, res=False):
       
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item=types.KeyboardButton("Анекдот")
       
        markup.add(item)
        
        bot.send_message(m.chat.id, 'Нажми: \nАнекдот - для получения интересного анекдота ',  reply_markup=markup)

@bot.message_handler(content_types=["text"])
def handle_text(message):
   
    if message.text.strip() == 'Анекдот' :
            answer = random.choice(fun)
  
    
    bot.send_message(message.chat.id, answer)

bot.polling(none_stop=True, interval=0)


