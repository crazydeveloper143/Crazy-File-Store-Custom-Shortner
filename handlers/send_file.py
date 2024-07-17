import asyncio
from configs import Config
from pyrogram import Client
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from handlers.helpers import str_to_b64
from handlers.save_media import get_file_caption

#strram
from urllib.parse import quote_plus
from util.file_properties import get_name, get_hash, get_media_file_size
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
        
async def media_forward(bot: Client, user_id: int, file_id: int):
    try:
        markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🔺 ᴊᴏɪɴ ᴍʏ ᴄʜᴀɴɴᴇʟ 🔺", url="https://t.me/OTT_BANGLA_BOGURA")
                ],
            ]
        )

        caption = await get_file_caption(file_id)
        if Config.FORWARD_AS_COPY:
            sent_message = await bot.copy_message(
                chat_id=user_id,
                from_chat_id=Config.DB_CHANNEL,
                message_id=file_id,
                reply_markup=markup
            )
        else:
            sent_message = await bot.forward_messages(
                chat_id=user_id,
                from_chat_id=Config.DB_CHANNEL,
                message_ids=file_id,
                reply_markup=markup
            )

        if caption:
            await bot.edit_message_caption(
                chat_id=sent_message.chat.id,
                message_id=sent_message.message_id,
                caption=caption,
                reply_markup=markup
            )

    except FloodWait as e:
        await asyncio.sleep(e.value)
        return await media_forward(bot, user_id, file_id)
    except Exception as e:
        print(f"An error occurred: {e}")

async def send_media_and_reply(bot: Client, user_id: int, file_id: int):
    await media_forward(bot, user_id, file_id)
