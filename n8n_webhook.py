from flask import Flask, request, jsonify
from pinecone_db import find_nearest
import requests

app = Flask(__name__)

TELEGRAM_SERVER_URL = "http://localhost:5000/send_message"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    user_id = data.get('user_id')
    user_message = data.get('message')

    if not user_id or not user_message:
        return jsonify({'error': 'user_id и message обязательны!'}), 400

    result = find_nearest(user_message)
    label = result["matches"][0]["id"]

    if label == "ДА":
        response_text = "УСПЕХ"
    elif label == "НЕТ":
        response_text = "УСПЕХ УСПЕХ"
    else:
        response_text = "ЗОВУ СТАРШЕГО МЕНЕДЖЕРА"

    # Отправляем сообщение через Telegram API
    requests.post(TELEGRAM_SERVER_URL, json={"user_id": user_id, "message": response_text})

    return jsonify({'status': 'Processed', 'response': response_text})

if __name__ == '__main__':
    app.run(port=5001)
