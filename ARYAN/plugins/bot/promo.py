from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from ARYAN import app
from ARYAN.utils.errors import capture_err
import httpx 
import config
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

promo_txt = """
<b><u>💰 Dᴏɴᴀᴛᴇ ғᴏʀ ᴘᴀɪᴅ ᴘʀᴏᴍᴏᴛɪᴏɴ 💸</b></u>\n\n\nᴜᴘɪ ɪᴅ : <b><u>teammadmaxop@axl</b></u>
"""





@app.on_message(filters.command(["romo","romo","promo"], prefixes=["p", "P","/"])) 
async def start(_, msg):
    buttons = [
        [
              InlineKeyboardButton(
                        text="ᴅᴇᴠᴇʟᴏᴘᴇʀ", user_id=config.OWNER_ID
                    ),
              ],
               ]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/2866697eebaa53ca899f4.jpg", has_spoiler=True,
        caption=promo_txt,
        reply_markup=reply_markup
    )
 
   
# --------------
