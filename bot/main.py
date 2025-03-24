from telegram.ext import Updater
from config import BOT_TOKEN
from handlers import register_handlers
from scheduler import start_scheduler

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    register_handlers(dp)  # Register command handlers
    start_scheduler(dp)     # Start scheduled tasks

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
    