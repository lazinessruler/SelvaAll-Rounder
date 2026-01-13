from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_photo(
        chat_id=msg.chat.id,
        photo="https://files.catbox.moe/bmu0bv.jpg",
        caption=f"""✦ » ʜᴇʏ  {msg.from_user.mention}  ✤,
✦ » ɪ ᴀᴍ {me2},
✦ » 𝘔𝘦𝘳𝘢 𝘔𝘢𝘯𝘯 𝘕𝘢𝘩𝘪 𝘏𝘢𝘪 𝘞𝘦𝘭𝘤𝘰𝘮𝘦 𝘔𝘴𝘨 𝘓𝘪𝘬𝘩𝘯𝘦 𝘒𝘢 𝘐𝘴 𝘓𝘪𝘺𝘦 𝘕𝘢𝘩𝘪 𝘓𝘪𝘩𝘬 𝘙𝘢𝘩𝘢 𝘎𝘢𝘯𝘥 𝘔𝘢𝘳𝘢𝘰 𝘉𝘩𝘢𝘪 !!
✦ » ɪғ ʏᴏᴜ ɴᴇᴇᴅ ᴀɴʏ ʜᴇʟᴘ, ᴛʜᴇɴ ᴅᴍ ᴛᴏ ᴍʏ ᴏᴡɴᴇʀ: [ᯏ 𝚬 ꧊᱂ 𝛆 ⲛ !! ‹𝟹](tg://user?id={OWNER_ID}) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("˹ sᴜᴘᴘᴏʀᴛ ˼", url="https://t.me/+i9uUE0jq6tA0YWM1"),
                    InlineKeyboardButton("˹ ᴜᴘᴅᴀᴛᴇs ˼", url="https://t.me/ScriptFlix_Bots")
                ],
                [
                    InlineKeyboardButton("˹ ᴍᴜsɪᴄ ʙᴏᴛ ˼", url="https://t.me/SoundFreqBot")
                ]                
            ]
        )
    )
