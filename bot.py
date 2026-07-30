from telegram import Update
from telegram.ext import (
    Application,
    MessageHandler,
    ContextTypes,
    filters,
)

from config import TELEGRAM_TOKEN
from llm import ask_llm


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Receives a user's message,
    sends it to Groq,
    returns the response.
    """

    user_message = update.message.text

    print(f"User: {user_message}")

    try:
        answer = ask_llm(user_message)

        print(f"Assistant: {answer}")

        await update.message.reply_text(answer)

    except Exception as e:
        print(e)
        await update.message.reply_text("Something went wrong.")


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