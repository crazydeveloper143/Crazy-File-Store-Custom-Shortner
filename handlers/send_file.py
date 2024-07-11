import asyncio
from configs import *
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import FloodWait
from handlers.helpers import str_to_b64
from urllib.parse import quote_plus
from util.file_properties import get_name, get_hash, get_media_file_size

async def reply_forward(message: Message, file_id: int):
    try:
        await message.reply_text(
            "🗑️ 𝙁𝙞𝙡𝙚𝙨 𝙬𝙞𝙡𝙡 𝙗𝙚 𝙙𝙚𝙡𝙚𝙩𝙚𝙙 𝙞𝙣 10 𝙢𝙞𝙣𝙪𝙩𝙚𝙨 𝙩𝙤 𝙖𝙫𝙤𝙞𝙙 𝙘𝙤𝙥𝙮𝙧𝙞𝙜𝙝𝙩 𝙞𝙨𝙨𝙪𝙚𝙨. 𝙋𝙡𝙚𝙖𝙨𝙚 𝙛𝙤𝙧𝙬𝙖𝙧𝙙 𝙖𝙣𝙙 𝙨𝙖𝙫𝙚 𝙩𝙝𝙚𝙢...\n\n**🔺 कॉपीराइट समस्याओं से बचने के लिए फ़ाइलें 10 मिनट में हटा दी जाएंगी। कृपया अग्रेषित करें और उन्हें सहेजें।**",
            disable_web_page_preview=True,
            quote=True
        )
    except FloodWait as e:
        await asyncio.sleep(e.x)
        await reply_forward(message, file_id)

async def media_forward(bot: Client, user_id: int, file_id: int):
    try:
        if Config.FORWARD_AS_COPY is True:
            return await bot.copy_message(chat_id=user_id, from_chat_id=Config.DB_CHANNEL,
                                          message_id=file_id)
        elif Config.FORWARD_AS_COPY is False:
            return await bot.forward_messages(chat_id=user_id, from_chat_id=Config.DB_CHANNEL,
                                              message_ids=file_id)
    except FloodWait as e:
        await asyncio.sleep(e.value)
        return media_forward(bot, user_id, file_id)
    except Exception as e:
        print(f"An error occurred: {e}")

async def send_media_and_reply(bot: Client, user_id: int, file_id: int):
    sent_message = await media_forward(bot, user_id, file_id)
    await reply_forward(message=sent_message, file_id=file_id)
    asyncio.create_task(delete_after_delay(sent_message, 600))

async def delete_after_delay(message, delay):
    await asyncio.sleep(delay)
    await message.delete()


#async def media_forward(bot: Client, user_id: int, file_id: int):
#    try:
#        if Config.FORWARD_AS_COPY:
#            lazy_file = await bot.copy_message(chat_id=STREAM_LOGS, from_chat_id=Config.DB_CHANNEL, message_id=file_id)
#        else:
#            lazy_file = await bot.forward_messages(chat_id=STREAM_LOGS, from_chat_id=Config.DB_CHANNEL, message_ids=file_id)
#
#        lazy_stream = f"{STREAM_URL}watch/{lazy_file.id}/{quote_plus(get_name(lazy_file))}?hash={get_hash(lazy_file)}"
#        lazy_download = f"{STREAM_URL}{lazy_file.id}/{quote_plus(get_name(lazy_file))}?hash={get_hash(lazy_file)}"
#        fileName = quote_plus(get_name(lazy_file))
#
#        await lazy_file.reply_text(
#            text=f"•• ʟɪɴᴋ ɢᴇɴᴇʀᴀᴛᴇᴅ ꜰᴏʀ ɪᴅ #{user_id} \n\n•• ᖴᎥᒪᗴ Nᗩᗰᗴ : {fileName}",
#            quote=True,
#            disable_web_page_preview=True,
#            reply_markup=InlineKeyboardMarkup([
#                [
#                    InlineKeyboardButton("ꜰᴀsᴛ ᴅᴏᴡɴʟᴏᴀᴅ 📥", url=lazy_download),
#                    InlineKeyboardButton('🖥️ ᴡᴀᴛᴄʜ ᴏɴʟɪɴᴇ', url=lazy_stream)
#                ]
#            ])
 #       )
#        
#        if Config.FORWARD_AS_COPY:
#            return await bot.copy_message(chat_id=user_id, from_chat_id=Config.DB_CHANNEL, message_id=file_id,
#                                          reply_markup=InlineKeyboardMarkup([
#                                              [
#                                                  InlineKeyboardButton("ꜰᴀsᴛ ᴅᴏᴡɴʟᴏᴀᴅ 📥", url=lazy_download),
#                                                  InlineKeyboardButton("🖥️ ᴡᴀᴛᴄʜ ᴏɴʟɪɴᴇ", url=lazy_stream),
#                                              ]
#                                          ]))
#        else:
#            return await bot.forward_messages(chat_id=user_id, from_chat_id=Config.DB_CHANNEL, message_ids=file_id,
 #                                             reply_markup=InlineKeyboardMarkup([
 #                                                 [
 #                                                     InlineKeyboardButton("ꜰᴀsᴛ ᴅᴏᴡɴʟᴏᴀᴅ 📥", url=lazy_download),
# #                                                     InlineKeyboardButton("🖥️ ᴡᴀᴛᴄʜ ᴏɴʟɪɴᴇ", url=lazy_stream),
#                                                  ]
 #                                             ]))
 #   except FloodWait as e:
 #       await asyncio.sleep(e.value)
  #      return await media_forward(bot, user_id, file_id)

