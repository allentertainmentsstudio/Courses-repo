from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command("start"))
async def start(client, message):

    text = """
Hi i am All in One Extractor Bot.

Press buttons below 👇
"""

    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Physics Wallah", callback_data="pw"),
            InlineKeyboardButton("E1 Coaching", callback_data="e1")
        ],
        [
            InlineKeyboardButton("Vidya Bihar", callback_data="vidya"),
            InlineKeyboardButton("Ocean Gurukul", callback_data="ocean")
        ],
        [
            InlineKeyboardButton("Winners Institute", callback_data="winners"),
            InlineKeyboardButton("Rgvikramjeet", callback_data="rgvikramjeet")
        ],
        [
            InlineKeyboardButton("TXT Apps", callback_data="txt"),
            InlineKeyboardButton("Classplus", callback_data="cp")
        ],
        [
            InlineKeyboardButton("Careerwill", callback_data="cw"),
            InlineKeyboardButton("Khan GS", callback_data="khan")
        ],
        [
            InlineKeyboardButton("Exampur", callback_data="exampur"),
            InlineKeyboardButton("Samyak IAS", callback_data="samyak")
        ],
        [
            InlineKeyboardButton("Chandra", callback_data="chandra"),
            InlineKeyboardButton("MGConcept", callback_data="mgconcept")
        ],
        [
            InlineKeyboardButton("Download Url List", callback_data="down"),
            InlineKeyboardButton("Forward", callback_data="forward")
        ]
    ])

    await message.reply_text(text, reply_markup=buttons)
