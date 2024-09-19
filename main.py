from telebot import TeleBot, types
import requests

TOKEN = "Telegram Bot Token"
bot = TeleBot(token=TOKEN)

API_URL = "https://chatgpt-42.p.rapidapi.com/geminipro"
API_KEY = "API_KEY"

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Hello! Send me a question.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_question = message.text
    payload = {
        "messages": [
            {
                "role": "user",
                "content": user_question
            }
        ],
        "temperature": 0.9,
        "top_k": 5,
        "top_p": 0.9,
        "max_tokens": 256,
        "web_access": False
    }
    headers = {
        "x-rapidapi-key": API_KEY,
        "x-rapidapi-host": "chatgpt-42.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(API_URL, json=payload, headers=headers)
        response_data = response.json()
        print("Response Data:", response_data)

        if response.status_code == 200:
            if 'choices' in response_data and len(response_data['choices']) > 0:
                bot_response = response_data['choices'][0]['message']['content']
            else:
                bot_response = "There is no answer."
        else:
            bot_response = f"There is no result: {response.status_code}"

    except Exception as ex:
        bot_response = f"An error occurred: {str(ex)}"

    bot.send_message(message.chat.id, response_data['result'])


bot.polling()
