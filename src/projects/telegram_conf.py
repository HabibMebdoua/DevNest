import requests


# Sending the message to the admin
def send_telegram_message(message):
    bot_token = '7954237550:AAGtxE5sW-pmlc33tf2oY61sGQK7JDBoEIc'
    chat_id = '1329523161'
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': message,
        'parse_mode': 'Markdown'
    }
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print("Telegram Error:", e)