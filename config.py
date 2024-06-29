import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "25120174"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "89a10ea368b634194752731a7c405e30")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://knight_rider:GODGURU12345@knight.jm59gu9.mongodb.net/?retryWrites=true&w=majority")
