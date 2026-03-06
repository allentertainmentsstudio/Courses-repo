from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

# --- Main Menu ---
@Client.on_message(filters.command("start"))
async def start(client, message):
    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("📚 Courses", callback_data="menu_courses")],
        [InlineKeyboardButton("⚙️ Tools", callback_data="menu_tools")],
        [InlineKeyboardButton("👨‍💻 Developer", url="https://t.me/arafta_hindi_dubbed_webseries")]
    ])
    await message.reply_text("Welcome! Choose an option:", reply_markup=buttons)

# --- Handle Button Clicks ---
@Client.on_callback_query()
async def handle_query(client: Client, query: CallbackQuery):

    if query.data == "menu_courses":
        buttons = InlineKeyboardMarkup([
            [InlineKeyboardButton("Physics Wallah", callback_data="pw")],
            [InlineKeyboardButton("E1 Coaching", callback_data="e1")],
            [InlineKeyboardButton("Back ⬅️", callback_data="menu_back")]
        ])
        await query.message.edit_text("📚 Courses:", reply_markup=buttons)

    elif query.data == "menu_tools":
        buttons = InlineKeyboardMarkup([
            [InlineKeyboardButton("Download Url List", callback_data="down")],
            [InlineKeyboardButton("Forward", callback_data="forward")],
            [InlineKeyboardButton("Back ⬅️", callback_data="menu_back")]
        ])
        await query.message.edit_text("⚙️ Tools:", reply_markup=buttons)

    elif query.data == "menu_back":
        buttons = InlineKeyboardMarkup([
            [InlineKeyboardButton("📚 Courses", callback_data="menu_courses")],
            [InlineKeyboardButton("⚙️ Tools", callback_data="menu_tools")],
            [InlineKeyboardButton("👨‍💻 Developer", url="https://t.me/arafta_hindi_dubbed_webseries")]
        ])
        await query.message.edit_text("Welcome! Choose an option:", reply_markup=buttons)

    # --- Add individual course/tool handling if needed ---
    elif query.data == "pw":
        await query.answer("Physics Wallah Selected!")
