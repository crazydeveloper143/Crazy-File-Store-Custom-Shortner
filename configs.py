# # (c) @AbirHasan2005

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID", "0"))
	API_HASH = os.environ.get("API_HASH")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	BOT_USERNAME = os.environ.get("BOT_USERNAME")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-100"))
	BOT_OWNER = [int(owner) for owner in os.environ.get("BOT_OWNER", "").split()]
	DATABASE_URL = os.environ.get("DATABASE_URL")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", None)
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
This is Permanent Files Store Bot!
Send me any file I will save it in my Database. Also works for channel. Add me to channel as Admin with Edit Permission, I will add Save Uploaded File in Channel & add Sharable Button Link.

**My Name:** [𝐅𝐢𝐥𝐞 𝐒𝐭𝐨𝐫𝐞 𝐁𝐨𝐭](https://t.me/{BOT_USERNAME})

**Developer:** [𝐑𝐮𝐛𝐚𝐧𝐝𝐮𝐫𝐚𝐢𝟐𝟕](https://t.me/Rubandurai27) 

**Updates Channel:** [𝐉𝐨𝐤𝐞𝐫 𝐁𝐨𝐭𝐬](https://t.me/JokerBots)

**Support Group: ** [𝐔𝐩𝐝𝐚𝐭𝐞𝐬](https://t.me/TAMILMIRROR)

**Bot Tutorial:** https://youtu.be/HDHFray3yws
"""
	ABOUT_DEV_TEXT = f"""
**🌐 This Bot Was Devloped By** : @JOKERBOTS"""
	HOME_TEXT = """
 Hello [{}](tg://user?id={}) \n\nThis Is A Ultimate Telegram File Store Bot. Send Any File Bot Will Be Send Your Short link.\n\nCurrently Supported Formats: \n\n
1. Images : Images With caption.
2. Audios : Supported upto 4GB
3. Files : Supported upto 4GB
4. Videos : Supported upto 4GB.\n
If You Need Any Support Contact : \n @RubanDurai27 
"""
	SHORTENER_API_MESSAGE = """
To add or update your Shortner Website &amp; Apikey, <code>/shortener base_site apikey</code>
            
Ex: <code>/shortener kpslink.in 26ce257364bf17e38293a6f2dd0e772811abe75a</code>

Current Website: {base_site}

Current Shortener API: <code>{shortener_api}</code>

"""

