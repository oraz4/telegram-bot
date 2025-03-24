from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, MessageHandler, CallbackQueryHandler, Filters, CallbackContext
from database import add_user, add_task, get_tasks

def start(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    name = update.message.from_user.first_name
    add_user(user_id, name)
    update.message.reply_text("Welcome! Use /set_goals to define your goals.")

def set_goals(update: Update, context: CallbackContext):
    update.message.reply_text("Send your goal in this format:\n`goal_name, duration_in_minutes, HH:MM`", parse_mode="Markdown")

def save_goal(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    try:
        goal, duration, time_slot = update.message.text.split(", ")
        add_task(user_id, goal, int(duration), time_slot)
        update.message.reply_text(f"Goal '{goal}' saved! You will be reminded at {time_slot}.")
    except:
        update.message.reply_text("Invalid format! Use: `goal_name, duration_in_minutes, HH:MM`")

def register_handlers(dp):
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("set_goals", set_goals))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, save_goal))
