import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from ARYAN import LOGGER, app, userbot
from ARYAN.core.call import ARYAN
from ARYAN.misc import sudo
from ARYAN.plugins import ALL_MODULES
from ARYAN.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("ARYAN.plugins" + all_module)
    LOGGER("ARYAN.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await ARYAN.start()
    try:
        await Anony.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("ARYAN").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass
    await ARYAN.decorators()
    LOGGER("ARYAN").info(
        "Music Bot Started Successfully, Now Give your girlfriend chumt to @SASHIKANT_XD"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("ARYAN").info("Stopping ARYAN Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
