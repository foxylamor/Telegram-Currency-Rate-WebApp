# Telegram Currency Rate WebApp

Telegram Mini App for real-time currency conversion. Users can select currencies and amounts through an interactive web interface, then get instant exchange rates.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![aiogram](https://img.shields.io/badge/aiogram-v3.0%2B-blue?style=for-the-badge&logo=telegram)
![httpx](https://img.shields.io/badge/httpx-async-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

<div style="display: flex; justify-content: center; gap: 20px; flex-wrap: wrap;">
  <img src="https://i.ibb.co/fVjrrB2n/photo-2026-05-30-11-31-07.jpg" width="250" alt="Demo of bot">
  <img src="https://i.ibb.co/nNwmgJnN/photo-2026-05-30-11-31-09.jpg" width="250" alt="Demo of bot">
  <img src="https://i.ibb.co/WpsY8x0z/photo-2026-05-30-11-31-09-2.jpg" width="250" alt="Demo of bot">
</div>

## 🛠️ Tech Stack

- **aiogram** — modern asynchronous framework for Telegram bots
- **httpx** — async HTTP client for API requests
- **python-dotenv** — environment variable management
- **ExchangeRate-API** — free currency conversion API

## 📁 Project Structure

```
telegram-currency-rate-webapp/
├── handlers/
│   └── routes.py        # Command handlers and WebApp data processing
├── middleware/
│   └── rate_limit.py    # Rate limiting middleware
├── website/
│   └── index.html       # Telegram Mini App interface
│   └── style.html       # Styles for the interface
│   └── script.js        # Telegram Mini App script
├── main.py              # Main bot file
└── requirements.txt     # Project dependencies
```

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/foxylamor/telegram-currency-rate-webapp.git
cd telegram-currency-rate-webapp
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
TOKEN=your_telegram_token_from_botfather
WEB_APP_URL=https://your-webapp-url.com/index.html
```

> 💡 **How to get a token?**
> 1. Open Telegram and find the **@BotFather** bot
> 2. Send the `/newbot` command
> 3. Follow the instructions and copy your token

> 🌐 **How to host the WebApp?**
> - Upload `index.html` to a web server
> - Use free hosting like GitHub Pages or Vercel
> - Update `WEB_APP_URL` with your hosted URL

### 5. Run the bot

```bash
python bot.py
```

## 📱 Usage

1. Open Telegram and find your bot
2. Send `/start` to get the WebApp button
3. Click "Open WebApp" to launch the currency converter
4. Select "From" and "To" currencies
5. Enter the amount to convert
6. Click "Get Exchange Rate" to send data back to the bot
7. Bot will reply with the converted amount

## 📖 Documentation

- [aiogram](https://docs.aiogram.dev/)
- [httpx](https://www.python-httpx.org/)
- [Telegram Bot API](https://core.telegram.org/bots/api)
- [Telegram Mini Apps](https://core.telegram.org/bots/webapps)
- [ExchangeRate-API](https://www.exchangerate-api.com/docs)

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
