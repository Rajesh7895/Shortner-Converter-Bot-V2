# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("29810598", "Your Api Id"))
API_HASH = os.environ.get("4f6367a57aeebcf48b58c179684c8250", "Your Api Hash")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6173762846:AAG0GIofueMkVNzU1iqS79wJO8WMDkKQjyI")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("5257526759")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Mdisksite")
DATABASE_URL = os.getenv("DATABASE_URL", "https://studio.mogenius.com/studio/cloud-space/cloud-space-overview") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "5257526759")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(5257526759)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001321562085")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "mdisk site") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
