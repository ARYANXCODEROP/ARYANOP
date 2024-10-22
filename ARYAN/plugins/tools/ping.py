import random
from datetime import datetime

from pyrogram import filters
from pyrogram.types import Message

from ARYAN import app
from ARYAN.core.call import ARYAN
from ARYAN.utils import bot_sys_stats
from ARYAN.plugins.bot.start import ARYAN_PICS
from ARYAN.utils.decorators.language import language
from ARYAN.utils.inline import add_markup
from config import BANNED_USERS


@app.on_message(filters.command(["ping", "alive"]) & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    start = datetime.now()
    response = await message.reply_photo(random.choice(ARYAN_PICS),
        caption=_["ping_1"].format(app.mention),
    )
    pytgping = await ARYAN.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await response.edit_text(
        _["ping_2"].format(resp, app.mention, UP, RAM, CPU, DISK, pytgping),
        reply_markup=add_markup(_),
    )
