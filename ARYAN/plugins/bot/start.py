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
"https://telegra.ph/file/1dc71c11762d4c4193128.jpg",
"https://telegra.ph/file/3d80c1e33dce235713fb0.jpg",
"https://telegra.ph/file/1736b88587588361b1e10.jpg",
"https://telegra.ph/file/67ff63f36e95a72d71238.jpg",
"https://telegra.ph/file/176b1a93bafbdcd479948.jpg",
"https://telegra.ph/file/53451ea34c47ab7029dc7.jpg",
"https://telegra.ph/file/02dee651df192da8d5d0e.jpg",
"https://telegra.ph/file/f7cf21e75a11f1b5d45e0.jpg",
"https://telegra.ph/file/fad444ab7a3eed9f206f9.jpg",
"https://telegra.ph/file/a8f5c6470bcf46a82d8ac.jpg",
"https://telegra.ph/file/36f1c041a0702ebfbd385.jpg",
"https://telegra.ph/file/ac0d854c411918a66aed7.jpg",
"https://telegra.ph/file/a3062b9cf388e78958ba3.jpg",
"https://telegra.ph/file/bb6c79dd3b4e473b68152.jpg",
"https://telegra.ph/file/03ed2b4852ba47946960e.jpg",
"https://telegra.ph/file/850b1b9b9ad58efc4edeb.jpg"
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
            await umm.delete()
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
        if name == "verify":
            await message.reply_text(f"ʜᴇʏ {message.from_user.first_name},\nᴛʜᴀɴᴋs ғᴏʀ ᴠᴇʀɪғʏɪɴɢ ʏᴏᴜʀsᴇʟғ ɪɴ ˹𝐓𝐚𝐫𝐠𝐞𝐭 ✘ 𝐇𝐢𝐭˼, ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ ɢᴏ ʙᴀᴄᴋ ᴀɴᴅ sᴛᴀʀᴛ ᴜsɪɴɢ ᴍᴇ.")
            if await is_on_off(2):
                sender_id = message.from_user.id
                sender_name = message.from_user.first_name
                return await bot.send_message(
                    config.LOG_GROUP_ID,
                    f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ ᴛᴏ <code>ᴠᴇʀɪғʏ ʜɪᴍsᴇʟғ</code>\n\n**ᴜsᴇʀ ɪᴅ:** {sender_id}\n**ᴜsᴇʀɴᴀᴍᴇ:** {sender_name}",
                )
            return    
        if name[0:3] == "inf":
            m = await message.reply_text("🔎")
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
        await umm.delete()
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
