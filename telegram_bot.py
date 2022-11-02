import json

import telegram


def telegram_bot_send_message(
        message,
        telegram_pars="C:/Users/seang/PycharmProjects/API_keys/telegram_tutor_bot_api.json"
):
    try:
        with open(telegram_pars) as f:
            pars = json.load(f)
        bot = telegram.Bot(pars['api_key'])
        bot.sendMessage(
            chat_id=pars["chat_id"],
            text=message,
        )
    except:
        print("Telegram struggled to send a message, continuing...")


if __name__ == '__main__':
    telegram_bot_send_message(f"Hello World")
