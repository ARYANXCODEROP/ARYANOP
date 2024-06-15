import time
import random 
from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from youtubesearchpython.__future__ import VideosSearch
import asyncio
import config
from ARYAN import app
from ARYAN.misc import _boot_
from ARYAN.plugins.sudo.sudoers import sudoers_list
from ARYAN.aryan import EMOJIOS, STICKER
from ARYAN.utils.database import get_served_chats, get_served_users, get_sudoers
from ARYAN.utils import bot_sys_stats
from ARYAN.utils.database import (
    add_served_chat,
    add_served_user,
    blacklisted_chats,
    get_lang,
    is_banned_user,
    is_on_off,
)
from ARYAN.utils.decorators.language import LanguageStart
from ARYAN.utils.formatters import get_readable_time
from ARYAN.utils.inline import first_page, private_panel, start_panel
from config import BANNED_USERS
from strings import get_string



ARYAN_PICS = [
"https://telegra.ph/file/55ac2f4cd6ca1ade482e6.jpg",
"https://telegra.ph/file/b3dd8b4ed17bc7f366b20.jpg",
"https://telegra.ph/file/13b32f3dd1fed15c13164.jpg",
"https://telegra.ph/file/6e30a33196c093097265b.jpg",
"https://telegra.ph/file/e1aeb1ebded70406859ef.jpg",
"https://telegra.ph/file/176ce8872c97f6a25dcd6.jpg",
"https://telegra.ph/file/3d97be98f8b5ca220f051.jpg",
"https://telegra.ph/file/4d0c4ace34eac767f9891.jpg",
"https://telegra.ph/file/d539250f753cd14774160.jpg",
"https://telegra.ph/file/19e439ab0e20764cce37e.jpg",
"https://telegra.ph/file/a3859ec69554c9c4e35cc.jpg",
"https://telegra.ph/file/391fad19034af768e9bc1.jpg",
"https://telegra.ph/file/c81878dd5648594890222.jpg",
"https://telegra.ph/file/1d1d40926738f2a5b5d86.jpg",
"https://telegra.ph/file/edc13cfc40f89459c9736.jpg",
"https://telegra.ph/file/e37d9fc989dd930be5c47.jpg"
]


@app.on_message(filters.command(["start"]) & filters.private & ~BANNED_USERS)
@LanguageStart
async def start_pm(client, message: Message, _):
    await add_served_user(message.from_user.id)
    if len(message.text.split()) > 1:
        name = message.text.split(None, 1)[1]
        if name[0:4] == "help":
            keyboard = first_page(_)
            accha = await message.reply_text(
            text=random.choice(EMOJIOS),
            )
            await asyncio.sleep(1.3)
            await accha.edit("ᴅιиg ᴅσиg ꨄ︎ ѕтαятιиg.....")
            await asyncio.sleep(0.2)
            await accha.edit("ᴅιиg ᴅσиg ꨄ sтαятιиg.........")
            await asyncio.sleep(0.2)
            await accha.edit("ᴅιиg ᴅσиg ꨄ︎ sтαятιиg.....")
            await asyncio.sleep(0.2)
            await accha.delete()
            umm = await message.reply_sticker(sticker=random.choice(STICKER))
            await asyncio.sleep(2)
            return await message.reply_photo(
                random.choice(ARYAN_PICS),
                caption=_["help_1"].format(config.SUPPORT_CHAT),
                reply_markup=keyboard,
            )
        if name[0:3] == "sud":
            await sudoers_list(client=client, message=message, _=_)
            if await is_on_off(2):
                return await app.send_message(
                    chat_id=config.LOGGER_ID,
                    text=f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ ᴛᴏ ᴄʜᴇᴄᴋ <b>sᴜᴅᴏʟɪsᴛ</b>.\n\n<b>ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>\n<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}",
                )
            return
        if name[0:3] == "inf":
            m = await message.reply_text("🌿")
            query = (str(name)).replace("info_", "", 1)
            query = f"https://www.youtube.com/watch?v={query}"
            results = VideosSearch(query, limit=1)
            for result in (await results.next())["result"]:
                title = result["title"]
                duration = result["duration"]
                views = result["viewCount"]["short"]
                thumbnail = result["thumbnails"][0]["url"].split("?")[0]
                channellink = result["channel"]["link"]
                channel = result["channel"]["name"]
                link = result["link"]
                published = result["publishedTime"]
            searched_text = _["start_6"].format(
                title, duration, views, published, channellink, channel, app.mention
            )
            key = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text=_["S_B_8"], url=link),
                        InlineKeyboardButton(text=_["S_B_9"], url=config.SUPPORT_CHAT),
                    ],
                ]
            )
            await m.delete()
            await app.send_photo(
                chat_id=message.chat.id,
                photo=thumbnail,
                caption=searched_text,
                reply_markup=key,
            )
            if await is_on_off(2):
                return await app.send_message(
                    chat_id=config.LOGGER_ID,
                    text=f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ ᴛᴏ ᴄʜᴇᴄᴋ <b>ᴛʀᴀᴄᴋ ɪɴғᴏʀᴍᴀᴛɪᴏɴ</b>.\n\n<b>ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>\n<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}",
                )
    else:
        out = private_panel(_)
        served_chats = len(await get_served_chats())
        served_users = len(await get_served_users())
        UP, CPU, RAM, DISK = await bot_sys_stats()
        accha = await message.reply_text(
            text=random.choice(EMOJIOS),
        )
        await asyncio.sleep(1.3)
        await accha.edit("ᴅιиg ᴅσиg ꨄ︎ ѕтαятιиg........")
        await asyncio.sleep(0.2)
        await accha.edit("ᴅιиg ᴅσиg ꨄ sтαятιиg........")
        await asyncio.sleep(0.2)
        await accha.edit("ᴅιиg ᴅσиg ꨄ︎ sтαятιиg......")
        await asyncio.sleep(0.2)
        await accha.delete()
        umm = await message.reply_sticker(sticker=random.choice(STICKER))
        await asyncio.sleep(2)
        await message.reply_photo(
            random.choice(ARYAN_PICS),
            caption=_["start_2"].format(message.from_user.mention, app.mention, UP, DISK, CPU, RAM,served_users,served_chats),
            reply_markup=InlineKeyboardMarkup(out),
        )
        if await is_on_off(2):
            return await app.send_message(
                chat_id=config.LOGGER_ID,
                text=f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ.\n\n<b>ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>\n<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}",
            )


@app.on_message(filters.command(["start"]) & filters.group & ~BANNED_USERS)
@LanguageStart
async def start_gp(client, message: Message, _):
    out = start_panel(_)
    uptime = int(time.time() - _boot_)
    await message.reply_photo(
        random.choice(ARYAN_PICS),
        caption=_["start_1"].format(app.mention, get_readable_time(uptime)),
        reply_markup=InlineKeyboardMarkup(out),
    )
    return await add_served_chat(message.chat.id)


@app.on_message(filters.new_chat_members, group=-1)
async def welcome(client, message: Message):
    for member in message.new_chat_members:
        try:
            language = await get_lang(message.chat.id)
            _ = get_string(language)
            if await is_banned_user(member.id):
                try:
                    await message.chat.ban_member(member.id)
                except:
                    pass
            if member.id == app.id:
                if message.chat.type != ChatType.SUPERGROUP:
                    await message.reply_text(_["start_4"])
                    return await app.leave_chat(message.chat.id)
                if message.chat.id in await blacklisted_chats():
                    await message.reply_text(
                        _["start_5"].format(
                            app.mention,
                            f"https://t.me/{app.username}?start=sudolist",
                            config.SUPPORT_CHAT,
                        ),
                        disable_web_page_preview=True,
                    )
                    return await app.leave_chat(message.chat.id)

                out = start_panel(_)
                await message.reply_photo(
                    random.choice(ARYAN_PICS),
                    caption=_["start_3"].format(
                        message.from_user.mention,
                        app.mention,
                        message.chat.title,
                        app.mention,
                    ),
                    reply_markup=InlineKeyboardMarkup(out),
                )
                await add_served_chat(message.chat.id)
                await message.stop_propagation()
        except Exception as ex:
            print(ex)
