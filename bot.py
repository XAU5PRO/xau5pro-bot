import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# =========================
# CONFIG
# =========================
BOT_TOKEN = os.getenv("BOT_TOKEN")

DISCLAIMER = (
    "⚠️ Educational market analysis only.\n"
    "Not financial advice. Trade at your own risk."
)

# =========================
# COMMANDS
# =========================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 Welcome to XAU5Pro\n\n"
        "Professional XAUUSD market structure analysis.\n\n"
        "Commands:\n"
        "/analyze – Get latest XAUUSD setup\n"
        "/status – System status\n\n"
        f"{DISCLAIMER}"
    )

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✅ XAU5Pro Engine Status\n"
        "• Bot: Online\n"
        "• Market: XAUUSD\n"
        "• Mode: Automated Structure Analysis"
    )

async def analyze(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # ---- Static example (will be automated later) ----
    analysis = (
        "💹 XAU/USD – 5 Minute Timeframe\n\n"
        "🟢 Support: 1975\n"
        "🔴 Resistance: 1985\n\n"
        "📌 Entry Conditions:\n"
        "1️⃣ RSI < 30\n"
        "2️⃣ Price near support\n"
        "3️⃣ Rejection / reversal candle\n\n"
        "↗️ Tip: Wait for confirmation before entry\n\n"
        f"{DISCLAIMER}"
    )

    await update.message.reply_text(analysis)

# =========================
# APP INIT
# =========================

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(CommandHandler("analyze", analyze))

    app.run_polling()

if __name__ == "__main__":
    main()
