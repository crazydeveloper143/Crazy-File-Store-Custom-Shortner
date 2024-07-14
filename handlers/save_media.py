

import asyncio
from configs import Config
from pyrogram import Client
from pyrogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from pyrogram.errors import FloodWait
from handlers.helpers import get_short_link, str_to_b64
from handlers.users_api import get_user

def humanbytes(size):
    if not size:
        return ""
    power = 2**10
    n = 0
    Dic_powerN = {0: ' ', 1: 'Ki', 2: 'Mi', 3: 'Gi', 4: 'Ti'}
    while size > power:
        size /= power
        n += 1
    return str(round(size, 2)) + " " + Dic_powerN[n] + 'B'

async def forward_to_channel(bot: Client, message: Message, editable: Message):
    try:
        __SENT = await message.copy(Config.DB_CHANNEL)
        return __SENT
    except FloodWait as sl:
        if sl.value > 45:
            await asyncio.sleep(sl.value)
            await bot.send_message(
                chat_id=int(Config.LOG_CHANNEL),
                text=f"#FloodWait:\nGot FloodWait of `{str(sl.value)}s` from `{str(editable.chat.id)}` !!",
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("Ban User", callback_data=f"ban_user_{str(editable.chat.id)}")]
                    ]
                )
            )
        return await forward_to_channel(bot, message, editable)


async def save_batch_media_in_channel(bot: Client, editable: Message, message_ids: list, cmd):
    try:
        message_ids_str = ""
        for message in (await bot.get_messages(chat_id=editable.chat.id, message_ids=message_ids)):
            sent_message = await forward_to_channel(bot, message, editable)
            if sent_message is None:
                continue
            message_ids_str += f"{str(sent_message.id)} "
            await asyncio.sleep(2)

        SaveMessage = await bot.send_message(
            chat_id=Config.DB_CHANNEL,
            text=message_ids_str,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("Delete Batch", callback_data="closeMessage")
            ]])
        )

        user_id = cmd.from_user.id
        user = await get_user(user_id)
        main_url = f"https://filescrazy.blogspot.com/2024/07/files.html?link=Crazybotz_{str_to_b64(str(SaveMessage.id))}"
        short_url = None

        if user["shortener_api"]:
            short_url = await get_short_link(user, main_url)

        message_text = (
            f"**\nYour Files Uploaded Successfully \n\n ⚜️ 𝙔𝙤𝙪𝙧 𝙁𝙞𝙡𝙚 𝙇𝙞𝙣𝙠 : <code>{main_url}</code>\n"
        )

        buttons = [
            [InlineKeyboardButton("ᴍᴀɪɴ ʟɪɴᴋ", url=main_url)]
        ]

        if short_url:
            message_text += f"\n\n♻️ 𝙨𝙝𝙤𝙧𝙩𝙣ᴇᴅ 𝙡ɪɴᴋ : <code>{short_url}</code>\n"
            buttons.append([InlineKeyboardButton("ꜱʜᴏʀᴛɴᴇᴅ ʟɪɴᴋ 🔁", url=short_url)])

        message_text += "\n**ᴊᴜꜱᴛ ᴄʟɪᴄᴋ ᴛʜᴇ ʟɪɴᴋ ᴀɴᴅ ᴄʟɪᴄᴋ ꜱᴛᴀʀᴛ ɢᴇᴛ ʏᴏᴜʀ ꜰɪʟᴇꜱ!**"

        await editable.edit(
            message_text,
            reply_markup=InlineKeyboardMarkup(buttons),
            disable_web_page_preview=True
        )

        await bot.send_message(
            chat_id=int(Config.LOG_CHANNEL),
            text=f"#BATCH_SAVE:\n\n[{editable.reply_to_message.from_user.first_name}](tg://user?id={editable.reply_to_message.from_user.id}) Got Batch Link!",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons)
        )
    except Exception as err:
        await editable.edit(f"Something Went Wrong!\n\n**Error:** `{err}`")
        await bot.send_message(
            chat_id=int(Config.LOG_CHANNEL),
            text=f"#ERROR_TRACEBACK:\nGot Error from `{str(editable.chat.id)}` !!\n\n**Traceback:** `{err}`",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("Ban User", callback_data=f"ban_user_{str(editable.chat.id)}")]
                ]
            )
        )


async def save_media_in_channel(bot: Client, editable: Message, message: Message):
    try:
        forwarded_msg = await message.copy(Config.DB_CHANNEL)
        file_er_id = str(forwarded_msg.id)
        await forwarded_msg.reply_text(
            f"#PRIVATE_FILE:\n\n[{message.from_user.first_name}](tg://user?id={message.from_user.id}) Got File Link!",
            disable_web_page_preview=True)

        user_id = message.from_user.id
        user = await get_user(user_id)
        main_url = f"https://filescrazy.blogspot.com/2024/07/files.html?link=Crazybotz_{str_to_b64(file_er_id)}"
        short_url = None
        
        if user["shortener_api"]:
            short_url = await get_short_link(user, main_url)
        
        # get media type
        media_type = message.document or message.video or message.audio
        # get file name
        file_name = media_type.file_name
        # get file size 
        f_size = humanbytes(media_type.file_size)
        # get caption (if any)
        caption = message.caption or ""

        message_text = (
            "\n**Your File Uploaded Successfully **\n\n"
            f"**🔐 𝙛𝙞𝙡𝙚 𝙣𝙖𝙢𝙚 : <code>{file_name}</code>\n\n🔺 𝙛𝙞𝙡𝙚 𝙎𝙞𝙯𝙚 : <code>{f_size}</code> \n\n⚜️ 𝙔𝙤𝙪𝙧 𝙁𝙞𝙡𝙚 𝙇𝙞𝙣𝙠 : <code>{main_url}</code>\n"
        )

        buttons = [
            [InlineKeyboardButton("ᴍᴀɪɴ ʟɪɴᴋ", url=main_url)]
        ]

        if short_url:
            message_text += f"\n\n♻️ 𝙨𝙝𝙤𝙧𝙩𝙣ᴇᴅ 𝙡ɪɴᴋ : <code>{short_url}</code>\n"
            buttons.append([InlineKeyboardButton("ꜱʜᴏʀᴛɴᴇᴅ ʟɪɴᴋ 🔁", url=short_url)])

        message_text += "\n**ꜱʜᴀʀᴇ ʟɪɴᴋ ᴀɴᴅ ᴇᴀʀɴ ...💡**"

        await editable.edit(
            message_text,
            reply_markup=InlineKeyboardMarkup(buttons),
            disable_web_page_preview=True
        )

    except FloodWait as sl:
        if sl.value > 45:
            print(f"Sleep of {sl.value}s caused by FloodWait ...")
            await asyncio.sleep(sl.value)
            await bot.send_message(
                chat_id=int(Config.LOG_CHANNEL),
                text="#FloodWait:\n"
                     f"Got FloodWait of `{str(sl.value)}s` from `{str(editable.chat.id)}` !!",
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("Ban User", callback_data=f"ban_user_{str(editable.chat.id)}")]
                    ]
                )
            )
        await save_media_in_channel(bot, editable, message)
    except Exception as err:
        await editable.edit(f"Something Went Wrong!\n\n**Error:** `{err}`")
        await bot.send_message(
            chat_id=int(Config.LOG_CHANNEL),
            text="#ERROR_TRACEBACK:\n"
                 f"Got Error from `{str(editable.chat.id)}` !!\n\n"
                 f"**Traceback:** `{err}`",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("Ban User", callback_data=f"ban_user_{str(editable.chat.id)}")]
                ]
            )
        )
