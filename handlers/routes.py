import os
import httpx
import json

from aiogram import Router, F
from aiogram.types import Message, WebAppInfo, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart
from dotenv import load_dotenv


router = Router()

# Load environment variables
load_dotenv()
WEB_APP_URL = os.getenv("WEB_APP_URL")

API_URL = "https://v6.exchangerate-api.com/v6/b076b965e17df6b915c8e3e0/latest"
CURRIENCIES = ["EUR", "GBP", "JPY", "AUD", "CAD"]


async def get_exchange_rates(target_currency: str, base_currency: str = "USD") -> float:
    """Fetch exchange rates for the specified target currency."""
    async with httpx.AsyncClient(timeout=10) as client:
        response = await client.get(f"{API_URL}/{base_currency}")
        data = response.json()
        return round(data["conversion_rates"].get(target_currency, 0), 2)


reply_markup = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Open WebApp", web_app=WebAppInfo(url=WEB_APP_URL))]
])


@router.message(CommandStart())
async def start_handler(message: Message):
    """Handler for the /start command."""
    await message.answer("Hello. Open WebApp!", reply_markup=reply_markup)


@router.message(F.web_app_data)
async def web_app_handler(message: Message):
    """Handler for receiving data from the WebApp."""
    try:
        data = json.loads(message.web_app_data.data)

        from_currency = data.get("from")
        to_currency = data.get("to")
        amount_to_convert = float(data.get("amount"))

        rate = await get_exchange_rates(to_currency, from_currency)
        converted_amount = round(amount_to_convert * rate, 2)

        await message.answer(f"{amount_to_convert} {from_currency} = {converted_amount} {to_currency}")
    except (json.JSONDecodeError, KeyError) as e:
        await message.answer("Invalid data received from the WebApp.")
