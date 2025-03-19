import random
import telebot

TOKEN = 7852993338:AAGyz9bOigiZT5gRZaA4iGJyMAGno5QVB6s
bot = telebot.TeleBot(TOKEN)

# Список случайных инсайтов
insights = [
    "Иногда, чтобы найти ответ, нужно просто отпустить вопрос.",
    "Твой мир — это отражение твоих убеждений.",
    "Тишина внутри — источник настоящего понимания.",
    "Каждый момент — это возможность начать заново.",
    "Не ищи свет во внешнем мире, зажги его внутри себя."
]

@bot.message_handler(commands=['insight'])
def send_insight(message):
    insight = random.choice(insights)
    bot.send_message(message.chat.id, insight)

bot.polling()