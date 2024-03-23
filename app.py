from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN: Final = '7039548223:AAEGeepdTrNXEzQ1Gab_nWJws-fOFqPu420'
BOT_USERNAME: Final = '@ravisAI_bot'


#Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Greetings, i am the noble Ravis an intelligence crafted by my liege im_rahim. ')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('You who seek guidance, shall see your demands met.')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command.')

#Message Handlers
def provide_response(promt: str) -> str:
    processed: str = promt.lower()
    
    #This is where the AI Operate
    
    return "Message processed successfully..."



async def handle_newmessage(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_author: str = update.message.chat.id
    message_type: str = update.message.chat.type
    message_text: str = update.message.text

    #log message sent by user
    print(f'User {message_author} in {message_type}: "{message_text}"')

    if message_type=="group":
        #if the message was sent in group chat, process the message content without the bot username tag.
        if BOT_USERNAME in message_text:
            new_text: str = message_text.replace(BOT_USERNAME,'').strip()
            response: str = provide_response(new_text)
        else:
            return
    else:
        #if the message was sent in private chat, process the whole message content
        response: str = provide_response(message_text)

    #log message sent by bot in response
    print(f'Bot: {response}')

    #Post answer
    await update.message.reply_text(response)



async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'update {update} caused error {context.error}')


if __name__=='__main__':
    print("Initialising Ravis Bot...")
    app = Application.builder().token(BOT_TOKEN).build()

    #Command Handlers
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    #Message Handler
    app.add_handler(MessageHandler(filters.TEXT, handle_newmessage))

    #Error Handler
    app.add_error_handler(error)

    #Polling
    print("Listening...")
    app.run_polling(poll_interval=3)