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
from ARYAN.utils import bot_sys_stats
from ARYAN.utils.database import get_served_chats, get_served_users, get_sudoers
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
"https://telegra.ph/file/6dc8554a8dd57db31f1d9.jpg",
"https://telegra.ph/file/322dcf33da4889fe4f4b9.jpg",
"https://telegra.ph/file/639631a508a5f3ecdade0.jpg",
"https://telegra.ph/file/eba6b911d8dc8ba9b80a3.jpg",
"https://telegra.ph/file/af26cd8392bbbea8b6d16.jpg",
"https://telegra.ph/file/8fbb595529f23efdf724e.jpg",
"https://telegra.ph/file/ffc7773eb0ec4c97f97c4.jpg",
"https://telegra.ph/file/440c2c588857358b7652e.jpg",
"https://telegra.ph/file/1d1d40926738f2a5b5d86.jpg",
"https://telegra.ph/file/edc13cfc40f89459c9736.jpg",
"https://telegra.ph/file/7326f6ac9de66076380d7.jpg",
"https://telegra.ph/file/dbd5e80bdc424f0e491b3.jpg",
"https://telegra.ph/file/242ee2b1308e472cb0265.jpg",
"https://telegra.ph/file/421bc9c5fa6845effd5c6.jpg",
"https://telegra.ph/file/e37d9fc989dd930be5c47.jpg",
"https://telegra.ph/file/d135bd10a0e759bb76d4c.jpg",
"https://telegra.ph/file/ad74c305833179b2edbb8.jpg",
"https://telegra.ph/file/3d61bcfc2f884e814664f.jpg",
"https://telegra.ph/file/ff76608499934576bc029.jpg",
"https://telegra.ph/file/933679970002374a0dde7.jpg",
"https://telegra.ph/file/3cd52ef2e99814b29917a.jpg",
"https://telegra.ph/file/1dc71c11762d4c4193128.jpg"
]

EMOJIOS = [
    "👋",
    "✨",
    "❤️",
    "😚",
    "😇",
    "💫",
    "💋",
    "🌿",
    "🚩",
    "👅",
]

STICKER = [
"CAACAgUAAxkBAAEEaoFmQvmHm8XwyuA9-r4ZQbkQfwFmrwAClAkAAuqHMVbcrC536UP9uTUE",
"CAACAgUAAxkBAAEEaoBmQvmGhrqHVtpi6E5E9PKJ9a2_gQACugkAAo69MFae-bG4s_Gv3zUE",
"CAACAgUAAxkBAAEEan9mQvmBkzEF-35gtjndVr011sMnnwACYQgAAuMpMVYiBOEX1pjQSDUE",
"CAACAgUAAxkBAAEEan5mQvl_GiohVEm1HJMOkXknTzPojgACDQoAAj3zKVa_7cKVuhmQqDUE",
"CAACAgUAAxkBAAEEan1mQvl73fx9ow1sgkAXZWov8nZYcAACaysAAqjnqFekxYD_S35p3TUE",
"CAACAgUAAxkBAAEEanxmQvl1qAFu6lauR3A8oTYMexl2QwACFAkAAv1uEFaB9MuGNAYvsTUE",
"CAACAgUAAxkBAAEEantmQvlv-0LuilYfTk-r4OJv_spS7gACVQ0AAq73GFajcdikVQnZozUE"
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
             await asyncio.sleep(2),
             await umm.delete()
             await message.reply_sticker(sticker=random.choice(STICKER))
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
            m = await message.reply_text("🕊️")
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
accha = await message.reply_text(
            text=random.choice(EMOJIOS),
             await asyncio.sleep(2),
        await umm.delete()
        await message.reply_sticker(sticker=random.choice(STICKER))
        await message.reply_photo(
            random.choice(ARYAN_PICS),
            caption=_["start_2"].format(message.from_user.mention, app.mention),
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
            
