import os

# DO NOT FILL ANYTHING HERE, FILL EVERYTHING IN ENVIRONMENT ITSELF !

# mandatory vars
BOT_TOKEN = os.getenv("BOT_TOKEN", "6119848095:AAGoolcRaxOoaatLvDlHfy0yHL0YcYqVdQQ") # Get it from @BotFather [Telegram]
MONGO_DB_URI = os.getenv("MONGO_DB_URI", "mongodb+srv://sakilanowar78:atIAQ0iJ2bwlMig7@cluster0.1mqytch.mongodb.net/?retryWrites=true&w=majority") # Get it from mongodb.com
OWNER_ID = int(os.getenv("OWNER_ID", "5827787578") # Get it from @SpL_Levi_Ackerman_Bot [Telegram]

# non-mandatory vars
API_ID = os.getenv("API_ID", None)
API_HASH = os.getenv("API_HASH", None)
BACKGROUND_IMAGE_URL = os.getenv("BACKGROUND_IMAGE_URL", None) # use Telegraph 
WORD_SPAWN_TIME = os.getenv("WORD_SPAWN_TIME", None) # must be in seconds, Ex :- 900, Minimum :- 900
SUPPORT_GROUP = os.getenv("SUPPORT_GROUP", "Vip_Sakil_Bio") # Ex :- 'Spoiled_Community' 
SUPPORT_CHANNEL = os.getenv("SUPPORT_CHANNEL", "Vip_Sakil_Bio") # Ex :- 'SpLBots'
