import os
import asyncio
from telegram import Bot

# Get your bot token and chat ID from environment variables
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

# Initialize the bot
bot = Bot(token=BOT_TOKEN)

async def send_signals():
    # Example signals, replace with your real logic
    xau_signal = "🚀 XAU Signal: BUY"
    otc_signal = "📈 OTC Signal: SELL"

    # Send messages asynchronously
    await bot.send_message(chat_id=CHAT_ID, text=xau_signal)
    await bot.send_message(chat_id=CHAT_ID, text=otc_signal)

# Run the async function
if __name__ == "__main__":
    asyncio.run(send_signals())
