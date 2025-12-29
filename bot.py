import os
from telegram import Bot
from datetime import datetime
import random

# =========================
# CONFIG
# =========================
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
bot = Bot(token=BOT_TOKEN)

# =========================
# XAU ANALYSIS
# =========================
def analyze_xau():
    support = 1975 + random.randint(-2,2)
    resistance = 1985 + random.randint(-2,2)
    analysis = (
        f"XAU/USD Automated Analysis\n\n"
        f"Support: {support}\n"
        f"Resistance: {resistance}\n"
        f"Time: {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}\n\n"
        f"Conditions:\n"
        f"- RSI near oversold\n"
        f"- Price reaction at support\n"
        f"- Session active\n"
    )
    return analysis

# =========================
# POCKET OTC SIMULATION
# =========================
def analyze_otc():
    pairs = ["EUR/USD","GBP/USD","USD/JPY"]
    pair = random.choice(pairs)
    direction = random.choice(["BUY","SELL"])
    analysis = (
        f"Pocket OTC Signal\n\n"
        f"Pair: {pair}\n"
        f"Direction: {direction}\n"
        f"Next Candle Entry\n"
        f"Expiry: 1M\n"
        f"Time: {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}\n"
    )
    return analysis

# =========================
# MAIN EXECUTION
# =========================
def main():
    # XAU Signal
    xau_signal = analyze_xau()
    bot.send_message(chat_id=CHAT_ID, text=xau_signal)

    # OTC Signal
    otc_signal = analyze_otc()
    bot.send_message(chat_id=CHAT_ID, text=otc_signal)

if __name__ == "__main__":
    main()
