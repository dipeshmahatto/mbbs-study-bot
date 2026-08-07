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
TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = 8209025344
def is_admin(user_id):
    return user_id == ADMIN_ID
# ---------------- HOME ----------------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.effective_user

    add_user(
    user.id,
    user.first_name,
    user.username
)

    keyboard = [
        [InlineKeyboardButton("📚 Medicine", callback_data="medicine")],
        # [InlineKeyboardButton("📖 Basic Sciences", callback_data="basic")],
        # [InlineKeyboardButton("ℹ️ About", callback_data="about")]
    ]

    await update.message.reply_photo(
        photo=open("banner.jpeg", "rb"),
        caption=
        "🏥 *Welcome to MBBS Study Bot*\n\n"
        "Your medical learning companion.\n\n"
        "📚 Available Subjects:\n"
        "• Cardiology\n"
        "• Hematology\n"
        "• Respiratory Medicine\n"
        "• Neurology\n"
        "• Endocrinology\n"
        "• Anatomy\n\n"
        "Choose a category below 👇",

        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

# users count 
async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not is_admin(update.effective_user.id):

        await update.message.reply_text(
            "❌ You are not authorized."
        )
        return


    total = count_users()

    await update.message.reply_text(
        f"📊 Admin Statistics\n\n"
        f"👥 Total Users: {total}"
    )
# /users 
async def users(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not is_admin(update.effective_user.id):

        await update.message.reply_text(
            "❌ Access denied."
        )
        return


    data = get_users()


    if not data:

        await update.message.reply_text(
            "No users found."
        )
        return


    message = "👥 Registered Users\n\n"


    for user in data[:20]:

        user_id, name, username, date = user

        message += (
            f"🆔 {user_id}\n"
            f"👤 {name}\n"
            f"📱 @{username}\n"
            f"📅 {date}\n\n"
        )


    await update.message.reply_text(message)
# ---------------- BUTTONS ----------------

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    # Medicine
    if query.data == "medicine":

        keyboard = [

            [InlineKeyboardButton("🫀 Cardiology", url="https://t.me/+yci7xliWMnA5ZTM1")],

            [InlineKeyboardButton("🩸 Hematology", url="https://t.me/+yci7xliWMnA5ZTM1")],

            [InlineKeyboardButton("🫁 Respiratory", url="https://t.me/+Pnqb5Jt8hW1mNjhl")],

            [InlineKeyboardButton("🧠 Neurology", url="https://t.me/+R4mzKiCx9ZExZDk1")],

            [InlineKeyboardButton("🩺 Endocrinology", url="https://t.me/+7nsEiDWhvt1lNzNl")],

            [InlineKeyboardButton("🍽 Gastroenterology", url="https://t.me/+X65WJGd7L_s4NTBl")],

            [InlineKeyboardButton("🧬 Hepatology", url="https://t.me/+6Ci-qdO8-aE3OGY1")],

            [InlineKeyboardButton("💧 Nephrology", url="https://t.me/+p7TYsQ25dhUxZTQ9")],

            [InlineKeyboardButton("🦴 Rheumatology", url="https://t.me/+nK3sanY7h9xjNDVl")],

            [InlineKeyboardButton("⬅️ Back", callback_data="home")]

        ]

        await query.edit_message_caption(
    caption="📚 *Medicine Subjects*",
    parse_mode="Markdown",
    reply_markup=InlineKeyboardMarkup(keyboard)
)

    # Basic Sciences
    # elif query.data == "basic":

    #     keyboard = [

    #         [InlineKeyboardButton("📖 Anatomy", url="https://t.me/+jD9lMXeLvZI2ZDg1")],

    #         [InlineKeyboardButton("⬅️ Back", callback_data="home")]

    #     ]

    #     await query.edit_message_text(
    #         "📖 *Basic Sciences*",
    #         parse_mode="Markdown",
    #         reply_markup=InlineKeyboardMarkup(keyboard)
    #     )

    # About
    # elif query.data == "about":

    #     keyboard = [
    #         [InlineKeyboardButton("⬅️ Back", callback_data="home")]
    #     ]

    #     await query.edit_message_text(
    #         "🏥 *MBBS Study Bot*\n\n"
    #         "Join subject-wise Telegram channels and study smarter.\n\n"
    #         "Made with ❤️ for MBBS students.",
    #         parse_mode="Markdown",
    #         reply_markup=InlineKeyboardMarkup(keyboard)
    #     )

    # Home
    elif query.data == "home":

        keyboard = [
            [InlineKeyboardButton("📚 Medicine", callback_data="medicine")],
            # [InlineKeyboardButton("📖 Basic Sciences", callback_data="basic")],
            # [InlineKeyboardButton("ℹ️ About", callback_data="about")]
        ]

        await query.edit_message_caption(
    caption=
    "🏥 *Welcome to MBBS Study Bot*\n\n"
    "Your medical learning companion.\n\n"
    "📚 Available Subjects:\n"
    "• Cardiology\n"
    "• Hematology\n"
    "• Respiratory Medicine\n"
    "• Neurology\n"
    "• Endocrinology\n"
    "• Anatomy\n\n"
    "Choose a category below 👇",

    parse_mode="Markdown",
    reply_markup=InlineKeyboardMarkup(keyboard)
)

app = Application.builder().token(TOKEN).build()
create_table()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("stats", stats))
app.add_handler(CommandHandler("users",users))
app.add_handler(CallbackQueryHandler(buttons))

print("✅ Bot Running...")

app.run_polling()