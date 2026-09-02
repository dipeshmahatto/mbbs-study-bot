from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,

)
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)
from database import create_table, add_user, count_users, get_users
import os
import threading
from flask import Flask

TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = 8209025344
def is_admin(user_id):
    return user_id == ADMIN_ID

# ---------------- FLASK HEALTH SERVER ----------------
flask_app = Flask(__name__)

@flask_app.route('/')
def health():
    return "Bot is running", 200

def run_web():
    port = int(os.environ.get('PORT', 10000))
    flask_app.run(host='0.0.0.0', port=port)

# ---------------- HOME ----------------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # ... (unchanged, keep all your existing handler code exactly as is)
