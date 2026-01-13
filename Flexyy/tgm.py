import os
import requests
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def upload_file(file_path):
    url = "https://catbox.moe/user/api.php"
    data = {"reqtype": "fileupload", "json": "true"}
    files = {"fileToUpload": open(file_path, "rb")}
    response = requests.post(url, data=data, files=files)
    if response.status_code == 200:
        return True, response.text.strip()
    else:
        return False, f"Error: {response.status_code} - {response.text}"

@Client.on_message(filters.command(["tgm"]))
async def get_link_group(client, message):
    if not message.reply_to_message:
        return await message.reply_text("Pʟᴇᴀsᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇᴅɪᴀ")

    media = message.reply_to_message
    file_size = 0
    if media.photo:
        file_size = media.photo.file_size
    elif media.video:
        file_size = media.video.file_size
    elif media.document:
        file_size = media.document.file_size

    if file_size > 200 * 1024 * 1024:
        return await message.reply_text("Pʟᴇᴀsᴇ ᴜᴘʟᴏᴀᴅ ᴜɴᴅᴇʀ 200MB.")

    text = await message.reply("❍ ʜᴏʟᴅ ᴏɴ ʙᴀʙʏ....♡")

    async def progress(current, total):
        try:
            await text.edit_text(f"☘️ 𝖽𝗈𝗐𝗇𝗅𝗈𝖺𝖽𝗂𝗇𝗀... {current * 100 / total:.1f}%")
        except Exception:
            pass

    local_path = await media.download(progress=progress)
    await text.edit_text("📤 𝗎𝗉𝗅𝗈𝖺𝖽𝗂𝗇𝗀...")

    success, upload_url = upload_file(local_path)
    if success:
        await text.edit_text(
            f"🌐 | <a href='{upload_url}'>👉 ʏᴏᴜʀ ʟɪɴᴋ ᴛᴀᴘ ʜᴇʀᴇ 👈</a>",
            disable_web_page_preview=False,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("🌍 ᴘʀᴇss ᴀɴᴅ ʜᴏʟᴅ ᴛᴏ ᴠɪᴇᴡ", url=upload_url)]]
            ),
        )
    else:
        await text.edit_text(f"⚠️ Upload failed\n{upload_url}")

    try:
        os.remove(local_path)
    except Exception:
        pass
