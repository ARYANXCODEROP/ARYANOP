from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from ARYAN import app
from ARYAN.utils.errors import capture_err
import httpx 
from ARYAN.plugins.bot.start import ARYAN_PICS
import random
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ʀᴇᴘᴏ
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", url=f"HTTPS://GITHUB.COM/ARYANXCODEROP/ARYANOP")
        ],
        ]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/55ac2f4cd6ca1ade482e6.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
