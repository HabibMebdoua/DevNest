import requests
from accounts.models import CustomUser
from django.contrib import messages

bot_token = '7954237550:AAGtxE5sW-pmlc33tf2oY61sGQK7JDBoEIc'


def send_telegram_message(message , chat_id): 
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


def fetch_telegram_updates_and_link_users(user):
    url = f"https://api.telegram.org/bot{bot_token}/getUpdates"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError if the status is 4xx, 5xx
        data = response.json()

        for update in data.get("result", []):
            message = update.get("message")
            if not message:
                continue

            chat = message.get("chat")
            username = chat.get("username")
            chat_id = chat.get("id")

            if username:
                if user.chat_id:
                    print(f"ℹ️ المستخدم {user.username} مرتبط مسبقًا بـ chat_id {user.chat_id}")
                    return  # Exit the function if the user is already linked

                # Link the user to the chat_id
                user.chat_id = chat_id
                user.save()
                print(f"✅ Linked {username} to chat_id {chat_id}")

                # Send a confirmation message
                send_telegram_message(
                    f'✅ تم ربط حسابك بنجاح {user.username}. ستتلقى هنا كل التحديثات التي تخص مشاريعك.',
                    chat_id
                )
                return  # Exit the function after successful linking

        print("❌ لم يتم العثور على تحديثات مناسبة لربط المستخدم.")
    except requests.exceptions.RequestException as e:
        print(f"❌ خطأ في الاتصال بـ Telegram API: {e}")
    except Exception as e:
        print(f"❌ حدث خطأ غير متوقع: {e}")
