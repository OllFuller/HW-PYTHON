from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def go(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'OK! Let\' s go together! {update.effective_user.first_name}')

async def sum(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
 mess = update.message.text
 items = mess.split()
 a = int(items[1])
 b = int(items[2])
 await update.message.reply_text(a+b)

app = ApplicationBuilder().token("5958754149:AAGZR7GbOLWU_--ESFZYqgA6y-bM9A_DJP0").build()
print("Server start")
app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("go", go))
app.add_handler(CommandHandler("sum" , sum))

app.run_polling()
print("Server Stop")
