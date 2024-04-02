from telethon.sync import TelegramClient
from telethon.errors.rpcerrorlist import PeerFloodError
import re

# Replace these with your own values
api_id = 000
api_hash = ''
phone_number = ''
chat_id = 777000

# Create a Telegram client
client = TelegramClient('1.session', api_id, api_hash)

async def main():
    await client.start(phone_number)

    print("Listening for incoming messages...")

    async for message in client.iter_messages(chat_id):
        if message.sender_id:  # Check if the message has a sender ID
            sign_in_code = re.search(r'\b\d{5}\b', message.message)
            if sign_in_code:
                print(f"Time: {message.date}, Sign-in code: {sign_in_code.group()}")


try:
    client.loop.run_until_complete(main())
except KeyboardInterrupt:
    print("Program terminated by user.")
except PeerFloodError as e:
    print(f"Error: {e}")
finally:
    client.disconnect()
