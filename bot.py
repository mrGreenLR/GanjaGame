from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackContext

TOKEN = "7091168264:AAEPtpStjE_kulwfmNm3KrO_itQO8ue7OSU"  # замініть на ваш токен

async def start(update: Update, context: CallbackContext) -> None:
    keyboard = [[InlineKeyboardButton("GanjaCoin", url="https://mrgreenlr.github.io/GanjaCoin/")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Натисніть, щоб перейти до гри:", reply_markup=reply_markup)

def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()

if __name__ == "__main__":
    main()
