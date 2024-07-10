import asyncio
from configs import Config
from pyrogram import Client
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from handlers.helpers import str_to_b64

#strram
from urllib.parse import quote_plus
from util.file_properties import get_name, get_hash, get_media_file_size
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
        
async def media_forward(bot: Client, user_id: int, file_id: int):
    try:
        markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🔻 ᴡᴀᴛᴄʜ & ᴅᴏᴡɴʟᴏᴀᴅ 🔻", callback_data=f"stream#{file_id}")
                ],
            ]
        )

        if Config.FORWARD_AS_COPY:
            return await bot.copy_message(
                chat_id=user_id,
                from_chat_id=Config.DB_CHANNEL,
                message_id=file_id,
                reply_markup=markup
            )
        else:
            return await bot.forward_messages(
                chat_id=user_id,
                from_chat_id=Config.DB_CHANNEL,
                message_ids=file_id,
                reply_markup=markup
            )
    except FloodWait as e:
        await asyncio.sleep(e.value)
        return await media_forward(bot, user_id, file_id)
    except Exception as e:
        print(f"An error occurred: {e}")

async def send_media_and_reply(bot: Client, user_id: int, file_id: int):
    await media_forward(bot, user_id, file_id)

@Bot.on_callback_query(filters.regex(r"^stream#"))
async def stream_download(bot, query):
    file_id = query.data.split('#', 1)[1] 
    lazy_file = await media_forward(bot, Config.STREAM_LOGS, file_id)
    file_name = quote_plus(get_name(lazy_file))
    lazy_stream = f"{Config.STREAM_URL}watch/{str(lazy_file.id)}/{file_name}?hash={get_hash(lazy_file)}"
    lazy_download = f"{Config.STREAM_URL}{str(lazy_file.id)}/{file_name}?hash={get_hash(lazy_file)}"
    await query.edit_message_reply_markup(
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("📥 ᴅᴏᴡɴʟᴏᴀᴅ 📥", url=lazy_stream),
                    InlineKeyboardButton("🖥️ ꜱᴛʀᴇᴇᴍ 🖥️", url=lazy_download)
                ],
                [
                    InlineKeyboardButton('⁉️ ᴄʟᴏsᴇ ⁉️', callback_data='close_data')
                ]
            ]
        )
    )
