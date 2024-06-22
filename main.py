# pipenv install python-telegram-bot
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
    CallbackQueryHandler
)
from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup
)
import requests
import json
import shutil
import logging
KEY = "6764640289:AAG0DQU2or3RQNv1UpIwD-MVTLjV9hHxfa0"
API = "97d4c0c662b252ce56c7e55f03632316"
APPID = "а5c94c69"
# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(bot: Update, context: ContextTypes):
    await bot.message.reply_text(f"Hi this bot the all in one 😉 \nthis is all commands: \nstart - Start dialog with the bot \nhelp - if bot the glichet pls send the message \njoke - Random joke😂 \nidea - Random idea in the life \nbtc - price  \nltcbtc - price \nrancitat - random citates \nranqust - random question \nranpass - made the random password")


async def help(bot: Update, context: ContextTypes):
    await bot.message.reply_text(f"Пожалуйста напишите поддержке бота @onlymoneyl зарание спасибо за обращение!!")


async def ranjoke(bot: Update, context: ContextTypes):
    api_url = 'https://api.api-ninjas.com/v1/dadjokes?'
    response = requests.get(api_url, headers={'X-Api-Key': 'CgHMp/QhWB2/m7QK6d2lAA==jRQRAR4fAu9YqTxi'})
    data = json.loads(response.text)
    application = data[0]
    await bot.message.reply_text(f"Random joke is: {application.get('joke')}" )

async def ranidea(bot: Update, context: ContextTypes):
    api_url = 'https://api.api-ninjas.com/v1/bucketlist'
    response = requests.get(api_url, headers={'X-Api-Key': 'CgHMp/QhWB2/m7QK6d2lAA==jRQRAR4fAu9YqTxi'})
    data = json.loads(response.text)
    await bot.message.reply_text(f"Random idea in life is: {data['item']}" )

async def ltcbtc(bot: Update, context: ContextTypes):
    symbol = 'LTCBTC'
    api_url = 'https://api.api-ninjas.com/v1/cryptoprice?symbol={}'.format(symbol)
    response = requests.get(api_url, headers={'X-Api-Key': 'CgHMp/QhWB2/m7QK6d2lAA==jRQRAR4fAu9YqTxi'})
    data = json.loads(response.text)
    await bot.message.reply_text(f"Price for LTCBTC: {data.get('price')}")

async def btc(bot: Update, context: ContextTypes):
    symbol = 'BTCUSD'
    api_url = 'https://api.api-ninjas.com/v1/cryptoprice?symbol={}'.format(symbol)
    response = requests.get(api_url, headers={'X-Api-Key': 'CgHMp/QhWB2/m7QK6d2lAA==jRQRAR4fAu9YqTxi'})
    data = json.loads(response.text)
    await bot.message.reply_text(f"Price for BTC: {data.get('price')}")


async def rancitat(bot: Update, context: ContextTypes):
    api_url = 'https://api.api-ninjas.com/v1/quotes?'
    response = requests.get(api_url, headers={'X-Api-Key': 'CgHMp/QhWB2/m7QK6d2lAA==jRQRAR4fAu9YqTxi'})
    data = json.loads(response.text)
    application = data[0]
    await bot.message.reply_text(f"Random citation: {application.get('quote')} \nAuthor: {application.get('author')}")

async def ranqust(bot: Update, context: ContextTypes):
    api_url = 'https://api.api-ninjas.com/v1/riddles'
    response = requests.get(api_url, headers={'X-Api-Key': 'CgHMp/QhWB2/m7QK6d2lAA==jRQRAR4fAu9YqTxi'})
    data = json.loads(response.text)
    application =  data[0]
    await bot.message.reply_text(f"Random question: {application.get('question')} \nAnswer is: {application.get('answer')}")

async def ranpass(bot: Update, context: ContextTypes):
    length = '16'
    api_url = 'https://api.api-ninjas.com/v1/passwordgenerator?length={}'.format(length)
    response = requests.get(api_url, headers={'X-Api-Key': 'CgHMp/QhWB2/m7QK6d2lAA==jRQRAR4fAu9YqTxi'})
    data = json.loads(response.text)
    await bot.message.reply_text(f"Random password: {data.get('random_password')}")




if __name__ == "__main__":
    app = ApplicationBuilder().token(KEY).build()
    print("Bot is running...")

    # Commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help))
    app.add_handler(CommandHandler("joke", ranjoke)) 
    app.add_handler(CommandHandler("idea", ranidea)) 
    app.add_handler(CommandHandler("ltcbtc", ltcbtc))
    app.add_handler(CommandHandler("btc", btc))
    app.add_handler(CommandHandler("rancitat", rancitat))
    app.add_handler(CommandHandler("ranqust", ranqust))
    app.add_handler(CommandHandler("ranpass", ranpass))
    print("Polling...")
    app.run_polling(poll_interval=1)
