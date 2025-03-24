from apscheduler.schedulers.background import BackgroundScheduler
from database import get_tasks
from telegram import Bot
from config import BOT_TOKEN

scheduler = BackgroundScheduler()
scheduler.start()
bot = Bot(token=BOT_TOKEN)

def send_reminder(user_id, goal):
    bot.send_message(chat_id=user_id, text=f"Reminder: Time to work on '{goal}'! Send a photo after completion.")

def start_scheduler(dp):
    cursor.execute("SELECT user_id FROM users")
    users = cursor.fetchall()
    for user in users:
        user_id = user[0]
        tasks = get_tasks(user_id)
        for goal, time_slot in tasks:
            scheduler.add_job(send_reminder, "cron", hour=time_slot.hour, minute=time_slot.minute,
                              args=[user_id, goal])