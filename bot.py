from telegram import Update
from telegram.ext import (
    Application,
    MessageHandler,
    ContextTypes,
    filters,
)
from agent import agent

from config import TELEGRAM_TOKEN


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    chat_id = update.effective_chat.id
    user_message = update.message.text

    try:
        answer = agent.process_message(chat_id, user_message)

        await update.message.reply_text(answer)

    except Exception as e:
        print(e)

        await update.message.reply_text("Internal Error")

def main():

    app = Application.builder().token(TELEGRAM_TOKEN).build()

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            handle_message,
        )
    )

    print("Bot Started...")

    app.run_polling()


if __name__ == "__main__":
    main()