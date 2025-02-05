# Telegram Bot with API Integration

## Project Overview
This project is a simple Telegram bot built using the `TeleBot` library and an external API for generating responses to user questions. The bot receives a user's message, sends it to an AI service via API, and returns the generated response.

## Features
- Handles user messages in Telegram
- Sends user questions to an API for processing
- Returns intelligent AI-generated responses

## Requirements
To run this project, you'll need:

- Python 3.x
- The following Python libraries:
  ```bash
  pip install pyTelegramBotAPI requests
  ```

## Configuration
Before running the bot, configure the following:

1. **Telegram Bot Token:** Replace `TOKEN` with your Telegram bot token, obtained from [BotFather](https://core.telegram.org/bots#botfather).
2. **API Key:** Replace `API_KEY` with your RapidAPI key.
3. **API URL:** Ensure the correct API endpoint is set for the `API_URL`.

## How to Run
1. Clone this repository or download the project files.
2. Navigate to the project folder.
3. Run the script:
   ```bash
   python main.py
   ```
4. Start a chat with your bot in Telegram and send questions to receive AI-generated responses.

## Key Script Components
- **Start Command:** The bot responds with a welcome message when a user sends the `/start` command.
- **Message Handler:** Captures user messages and sends them to the external API for response generation.
- **Error Handling:** Provides appropriate error messages when API calls fail.

## Example Usage
User: *Hello, bot! What's the weather like today?*

Bot: *I'm here to help! Send me a question.*

## Future Improvements
- Improve error handling and API response validation
- Add support for multiple API services
- Implement conversation history management
- Support rich response types (images, links)

## License
This project is open-source and available for educational and personal use.
