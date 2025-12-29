import asyncio
import aiohttp
from datetime import datetime
from telegram import Bot, ParseMode
from telegram.ext import ApplicationBuilder, CommandHandler

# ====== CONFIG ======
TELEGRAM_TOKEN = "8296491026:AAHVDaxvaNRAY2pBPvkQ1GgewwIA6Jc8JfM"
CHAT_ID = 123456789  # استبدل برقم الـ chat id الخاص بك أو المجموعة
UPDATE_INTERVAL = 300  # تحديث كل 5 دقائق
SYMBOLS = ["XAUUSD", "EURUSD"]  # XAU/USD + Binary sample
# ====================

bot = Bot(token=TELEGRAM_TOKEN)

# ====== HELPER FUNCTIONS ======

async def fetch_market_data(session, symbol):
    url = f"https://api.exchangerate.host/latest?base={symbol[:3]}&symbols={symbol[3:]}"
    async with session.get(url) as response:
        data = await response.json()
        return float(data["rates"][symbol[3:]])

def analyze_signal(price_history):
    if len(price_history) < 2:
        return None
    if price_history[-1] > price_history[-2]:
        return "BUY"
    else:
        return "SELL"

async def send_signal(symbol, signal):
    message = f"🚀 {symbol} Signal: *{signal}*\n🕒 {datetime.utcnow().strftime('%H:%M:%S UTC')}"
    await bot.send_message(chat_id=CHAT_ID, text=message, parse_mode=ParseMode.MARKDOWN)

# ====== MAIN LOOP ======

async def main_loop():
    price_history = {sym: [] for sym in SYMBOLS}

    async with aiohttp.ClientSession() as session:
        while True:
            for sym in SYMBOLS:
                price = await fetch_market_data(session, sym)
                price_history[sym].append(price)
                if len(price_history[sym]) > 50:
                    price_history[sym].pop(0)

                signal = analyze_signal(price_history[sym])
                if signal:
                    await send_signal(sym, signal)

            await asyncio.sleep(UPDATE_INTERVAL)

# ====== TELEGRAM COMMANDS ======

async def start(update, context):
    await update.message.reply_text("✅ XAU5Pro Bot Running!")

# ====== RUN BOT ======
if __name__ == "__main__":
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    asyncio.run(main_loop())
