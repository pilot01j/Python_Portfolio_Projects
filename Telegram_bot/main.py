import requests
from datetime import datetime
import telebot
from auth_data import token

# 1. use func requests.get(api_adres+param on the end), we get the current price of BTC


def get_data():
    req = requests.get('https://yobit.net/api/3/ticker/btc_usd')
    response = req.json()
    # print(response)
    sell_price = response['btc_usd']['sell']
    print(f'{datetime.now().strftime("%Y-%m-%d %H:%M")}\nSell BTC price: {sell_price}')

# 2. Create Telegram Bot: Search on telegram BotFather and send the ext commands:
    #  /newbot
    #   <bot Name>
    #   <username for your bot. It must end in `bot`> ex: mybot20113_bot
    #   coppy HTTP API of your bot


def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=["start"])
    def start_message(mesasge):
        bot.send_message(mesasge.chat.id, "Hello friend! Write the 'price' to find aut the cost of BTC!")

    # -- need to set as params - content_types , to respond
    @bot.message_handler(content_types=["text"])
    def send_text(message):
        if message.text.lower() == 'price':
            try:
                req = requests.get('https://yobit.net/api/3/ticker/btc_usd')
                response = req.json()
                sell_price = response['btc_usd']['sell']
                bot.send_message(
                    message.chat.id,
                    f'{datetime.now().strftime("%Y-%m-%d %H:%M")}\nSell BTC price: {sell_price}'
                    )
            except Exception as ex:
                print(ex)
                bot.send_message(
                    message.chat.id,
                    "Something is going wrong!..."
                )
        else:
            bot.send_message(message.chat.id, "Check your command")

# --to send the message
    bot.polling()


if __name__ == '__main__':
    # get_data()
    telegram_bot(token)
