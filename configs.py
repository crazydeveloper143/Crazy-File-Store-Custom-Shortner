import os
from os import getenv, environ

STREAM_URL = os.environ.get("STREAM_URL", "https://shivam.koyeb.app/")
STREAM_LOGS = environ.get('STREAM_LOGS','-1001890815456')

class Config(object):
	API_ID = int(os.environ.get("API_ID", "29499299"))
	API_HASH = os.environ.get("API_HASH", "d2a224d0d84bf24b6b82e887a4f1559a")
	BOT_TOKEN = os.environ.get("BOT_TOKEN", "6530848860:AAH3HpuUmuofZR9HjQlOWP0gjkGUM9RUZUA")
	BOT_USERNAME = os.environ.get("BOT_USERNAME", "MFileStorebot")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1001799438122"))
	BOT_OWNER = [int(owner) for owner in os.environ.get("BOT_OWNER", "6249148586").split()]
	DATABASE_URL = os.environ.get('DATABASE_URI', "mongodb+srv://Animestorebot:Animestorebot@cluster0.kzwrcpo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001600537706")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", -1001799438122)
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", False))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", False))
	
	ABOUT_BOT_TEXT = f"""<b>
╭────[ *𝙁𝙞𝙡𝙚 𝙎𝙩𝙤𝙧𝙚 𝘽𝙤𝙩*]────⍟
│
├🔸🤖 **𝙈𝙮 𝙉𝙖𝙢𝙚:** [𝙁𝙞𝙡𝙚 𝙎𝙩𝙤𝙧𝙚 𝘽𝙤𝙩](https://t.me/{BOT_USERNAME})
├🔸📝 **𝙇𝙖𝙣𝙜𝙪𝙖𝙜𝙚:** [𝗣𝘆𝘁𝗵𝗼𝗻](https://www.python.org)
├🔹📚 **𝙇𝙞𝙗𝙧𝙖𝙧𝙮:** [𝗣𝙮𝙧𝙤𝙜𝙧𝙖𝙢](https://docs.pyrogram.org)
├🔹📡 **𝙃𝙤𝙨𝙩𝙚𝙙 𝙊𝙣:** [𝘾𝙧𝙖𝙯𝙮](https://t.me/Crazybotz)
├🔸👨‍💻 **𝘿𝙚𝙫𝙚𝙡𝙤𝙥𝙚𝙧:** [𝘾𝙧𝙖𝙯𝙮 𝘿𝙚𝙫𝙚𝙡𝙤𝙥𝙚𝙧](https://t.me/heartlesssn) 
╰──────[ 😎 ]───────────⍟</b>
"""
	ABOUT_DEV_TEXT = f"""
<b>───[ 𝙊𝙬𝙣𝙚𝙧 𝘿𝙚𝙩𝙖𝙞𝙡𝙨 ]───
    
• 𝙁𝙪𝙡𝙡 𝙣𝙖𝙢𝙚 : 𝙎𝙝𝙞𝙫𝙖𝙢
• 𝙐𝙨𝙚𝙧𝙣𝙖𝙢𝙚 : @heartlesssn
• 𝙋𝙖𝙧𝙢𝙖𝙣𝙚𝙣𝙩 𝘿𝙈 𝙡𝙞𝙣𝙠 : <a href='https://t.me/heartlesssn'>𝘾𝙧𝙖𝙯𝙮 𝘿𝙚𝙫𝙚𝙡𝙤𝙥𝙚𝙧</a></b>
"""
	HOME_TEXT = """
👋 𝙃𝙚𝙮 [{}](tg://user?id={})\n\n𝙏𝙝𝙞𝙨 𝙞𝙨 𝙖 𝙋𝙚𝙧𝙢𝙖𝙣𝙚𝙣𝙩 𝙁𝙞𝙡𝙚𝙎𝙩𝙤𝙧𝙚 𝘽𝙤𝙩

𝙎𝙚𝙣𝙙 𝙢𝙚 𝙖𝙣𝙮 𝙛𝙞𝙡𝙚 [ 𝘿𝙤𝙘𝙪𝙢𝙚𝙣𝙩, 𝙑𝙞𝙙𝙚𝙤 , 𝘼𝙪𝙙𝙞𝙤, 𝙋𝙝𝙤𝙩𝙤, 𝙎𝙩𝙞𝙘𝙠𝙚𝙧 & 𝘼𝙣𝙞𝙢𝙖𝙩𝙞𝙤𝙣 ] 𝙄 𝙬𝙞𝙡𝙡 𝙨𝙩𝙤𝙧𝙚 𝙞𝙩 𝙞𝙣 𝙢𝙮 𝘿𝙖𝙩𝙖𝙗𝙖𝙨𝙚 𝙘𝙝𝙖𝙣𝙣𝙚𝙡 𝙖𝙣𝙙 𝙜𝙞𝙫𝙚 𝙮𝙤𝙪𝙧 𝙨𝙝𝙖𝙧𝙚𝙗𝙡𝙚 𝙡𝙞𝙣𝙠 𝙩𝙤 𝙖𝙘𝙘𝙚𝙨𝙨 𝙩𝙝𝙖𝙩 𝙛𝙞𝙡𝙚...

⚠️ 𝙉𝙤𝙩𝙚: 𝙎𝙚𝙣𝙙𝙞𝙣𝙜 𝙥𝙤𝙧𝙣𝙤𝙜𝙧𝙖𝙥𝙝𝙞𝙘/𝙞𝙡𝙡𝙚𝙜𝙖𝙡 𝙘𝙤𝙣𝙩𝙚𝙣𝙩𝙨 𝙩𝙤 𝙗𝙤𝙩 𝙢𝙖𝙮 𝙡𝙚𝙖𝙙𝙨 𝙩𝙤 𝙥𝙚𝙧𝙢𝙖𝙣𝙚𝙣𝙩 𝙗𝙖𝙣 𝙖𝙣𝙙 𝙛𝙞𝙡𝙚 𝙡𝙞𝙣𝙠 𝙬𝙞𝙡𝙡 𝙗𝙚 𝙧𝙚𝙫𝙤𝙠𝙚𝙙.
"""
	SHORTENER_API_MESSAGE = """𝙁𝙞𝙧𝙨𝙩 𝘾𝙤𝙣𝙣𝙚𝙘𝙩 𝙒𝙞𝙩𝙝 𝙔𝙤𝙪𝙧 𝙎𝙝𝙤𝙧𝙩𝙣𝙚𝙧 𝘼𝙘𝙘𝙤𝙪𝙣𝙩 🤑\n\n <b><u>ʜᴏᴡ ᴛᴏ ᴀᴅᴅ sʜᴏʀᴛɴᴇʀ 👨‍💻</u> \n\n 👉 <code>/set_shortner your_shortener_website your_shortener_api</code> \n\n <u>♻️ ᴇxᴀᴍᴘʟᴇ</u> \n\n 👉 /set_shortner omegaLinks.in 33cebb615b95e76d797862d76d0f9352acd0fcc9\n\n ⚠️ ᴛʜɪꜱ ʙᴏᴛ ᴡɪʟʟ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴄᴏɴᴠᴇʀᴛꜱ ʟɪɴᴋꜱ ᴡɪᴛʜ ʏᴏᴜʀ ᴀᴘɪ ᴀɴᴅ ᴡɪʟʟ ᴘʀᴏᴠɪᴅᴇ ʏᴏᴜʀ ʟɪɴᴋꜱ.</b>"""

