# XAU Signal
xau_signal = analyze_xau()
bot.send_message(chat_id=CHAT_ID, text=xau_signal)

# OTC Signal
otc_signal = analyze_otc()
bot.send_message(chat_id=CHAT_ID, text=otc_signal)
