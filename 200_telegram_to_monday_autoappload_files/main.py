import telepot
import requests

# Set up Telegram bot
telegram_bot_token = 'YOUR_TELEGRAM_BOT_TOKEN'
bot = telepot.Bot(telegram_bot_token)

# Set up Monday.com API
monday_api_key = 'YOUR_MONDAY_API_KEY'
board_id = 'YOUR_BOARD_ID'

# Telegram message handler
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'document':
        file_id = msg['document']['file_id']
        file_info = bot.getFile(file_id)
        file_url = f'https://api.telegram.org/file/bot{telegram_bot_token}/{file_info["file_path"]}'

        # Download file
        response = requests.get(file_url)
        with open('downloaded_file.zip', 'wb') as f:
            f.write(response.content)

        # Upload file to Monday.com (simplified example)
        headers = {
            'Authorization': monday_api_key,
            'Content-Type': 'application/json',
        }
        url = f'https://api.monday.com/v2/file'

        # Adjust this payload based on your Monday.com board structure
        payload = {
            'query': 'mutation ($file: File!) { add_file_to_column (file: $file, item_id: <YOUR_ITEM_ID>, column_id: <YOUR_COLUMN_ID>) { id } }',
        }

        with open('downloaded_file.zip', 'rb') as f:
            files = {'file': (f.name, f)}
            response = requests.post(url, headers=headers, data=payload, files=files)

        print(response.json())

# Set up message handler
bot.message_loop(handle)

# Keep the program running
while True:
    pass
