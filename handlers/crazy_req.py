from pyrogram import Client, filters, enums
from pyrogram.types import ChatJoinRequest
from configs import Config

@Bot.on_chat_join_request(filters.chat(Config.UPDATES_CHANNEL))
async def join_reqs(client, message: ChatJoinRequest):
    if not await db.find_join_req(message.from_user.id):
        await db.add_join_req(message.from_user.id)
