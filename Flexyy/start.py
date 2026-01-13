
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# ========= IMAGES =========
START_PHOTO = "https://files.catbox.moe/mkuv1d.jpg"
HELP_PHOTO = "https://files.catbox.moe/k9et29.jpg"

# ========= BUTTONS =========
start_buttons = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("📢 Support Channel", url="https://t.me/ScriptFlix_Bots"),
            InlineKeyboardButton("💬 Support GC", url="https://t.me/+mdTWp_9iEo8yMWQ0")
        ],
        [
            InlineKeyboardButton("❓ Help & Commands", callback_data="help_page")
        ]
    ]
)

help_buttons = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("🔙 Back", callback_data="back_start")
        ]
    ]
)

# ========= /start =========
@Client.on_message(filters.command("start"))
async def start_cmd(client, message):
    await message.reply_photo(
        photo=START_PHOTO,
        caption="**🚀 Coming Soon!**",
        reply_markup=start_buttons
    )

# ========= HELP PAGE =========
@Client.on_callback_query(filters.regex("help_page"))
async def help_page(client, callback):
    await callback.message.edit_media(
        media=HELP_PHOTO,
        reply_markup=help_buttons
    )
    await callback.message.edit_caption(
        caption=""  # empty msg for clean UI
    )
    await callback.answer()

# ========= BACK TO START =========
@Client.on_callback_query(filters.regex("back_start"))
async def back_start(client, callback):
    await callback.message.edit_media(
        media=START_PHOTO,
        reply_markup=start_buttons
    )
    await callback.message.edit_caption(
        caption="**🚀 Coming Soon!**"
    )
    await callback.answer()
