import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "7092980872:AAFBjX87iiFT_KpUher6vEslGeTxOKY_ZGg")

API_ID = int(os.environ.get("API_ID", "21551881"))

API_HASH = os.environ.get("API_HASH", "6e83e9e1aee5accd4868dc29aa59ebaa")

STRING = os.environ.get("STRING", "")



bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
