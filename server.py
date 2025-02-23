from flask import Flask, request, jsonify
from telethon import TelegramClient
import asyncio

app = Flask(__name__)

# Укажи свои API-ключи Telegram (замени на свои значения)
api_id = 'здесь мой ключ'
api_hash = 'здесь мой ключ'

client = TelegramClient('session_name', api_id, api_hash)

@app.route('/send_message', methods=['POST'])
async def send_message():
    data = request.json
    user_id = data.get('user_id')
    message = data.get('message')

    if not user_id or not message:
        return jsonify({'error': 'user_id и message обязательны!'}), 400

    async with client:
        await client.send_message(user_id, message)

    return jsonify({'status': 'Message sent!'})

async def main():
    await client.start()
    app.run(port=5000)

if __name__ == '__main__':
    asyncio.run(main())
