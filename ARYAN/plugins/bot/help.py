from typing import Union

from pyrogram import filters, types
from pyrogram.types import InlineKeyboardMarkup, Message

from ARYAN import app
from ARYAN.utils import first_page, second_page
from ARYAN.utils.database import get_lang
from ARYAN.utils.decorators.language import LanguageStart, languageCB
from ARYAN.utils.inline.help import help_back_markup, private_help_panel
from config import BANNED_USERS, START_IMG_URL, SUPPORT_CHAT
from strings import get_string, helpers
from ARYAN.misc import SUDOERS


@app.on_message(filters.command(["help"]) & filters.private & ~BANNED_USERS)
@app.on_callback_query(filters.regex("settings_back_helper") & ~BANNED_USERS)
async def helper_private(client: app, update: Union[types.Message, types.CallbackQuery]):
    is_callback = isinstance(update, types.CallbackQuery)
    if is_callback:
        try:
            await update.answer()
        except:
            pass
        chat_id = update.message.chat.id
        language = await get_lang(chat_id)
        _ = get_string(language)
        keyboard = first_page(_)
        await update.edit_message_text(
            _["help_1"].format(SUPPORT_CHAT), reply_markup=keyboard
        )
    else:
        try:
            await update.delete()
        except:
            pass
        language = await get_lang(update.chat.id)
        _ = get_string(language)
        keyboard = first_page(_)
        await update.reply_photo(
            photo=START_IMG_URL,
            caption=_["help_1"].format(SUPPORT_CHAT),
            reply_markup=keyboard,
        )

@app.on_callback_query(filters.regex("settings_back_helper_fixed") & ~BANNED_USERS)
async def helper_private(client: app, update: Union[types.Message, types.CallbackQuery]):
    is_callback = isinstance(update, types.CallbackQuery)
    if is_callback:
        try:
            await update.answer()
        except:
            pass
        chat_id = update.message.chat.id
        language = await get_lang(chat_id)
        _ = get_string(language)
        keyboard = first_page(_)
        await update.edit_message_text(_["help_1"].format(SUPPORT_CHAT), reply_markup=keyboard)
    else:
        try:
            await update.delete()
        except:
            pass
        language = await get_lang(update.chat.id)
        _ = get_string(language)
        keyboard = first_page(_)
        await update.reply_photo(photo=START_IMG_URL, caption=_["help_1"].format(SUPPORT_CHAT), reply_markup=keyboard)
    



@app.on_message(filters.command(["help"]) & filters.group & ~BANNED_USERS)
@LanguageStart
async def help_com_group(client, message: Message, _):
    keyboard = private_help_panel(_)
    await message.reply_text(_["help_2"], reply_markup=InlineKeyboardMarkup(keyboard))


@app.on_callback_query(filters.regex("help_callback") & ~BANNED_USERS)
@languageCB
async def helper_cb(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    cb = callback_data.split(None, 1)[1]
    keyboard = help_back_markup(_)
    if cb == "hb14":
        if CallbackQuery.from_user.id not in SUDOERS:
            return await CallbackQuery.answer(
                   "ᴛʜɪs ʙᴜᴛᴛᴏɴ ᴏɴʟʏ ғᴏʀ sᴜᴅᴏᴇʀs\n\n\nᴄʜᴀʟ ʜᴀᴀᴛ ʙʜᴏsᴅɪᴋᴇ.", show_alert=True
            )
        else:
            await CallbackQuery.edit_message_text(
                helpers.HELP_14, reply_markup=keyboard
            )
            return await CallbackQuery.answer()
    try:
        await CallbackQuery.answer()
    except:
        pass
    if cb == "hb1":
        await CallbackQuery.edit_message_text(helpers.HELP_1, reply_markup=keyboard)
    elif cb == "hb2":
        await CallbackQuery.edit_message_text(helpers.HELP_2, reply_markup=keyboard)
    elif cb == "hb3":
        await CallbackQuery.edit_message_text(helpers.HELP_3, reply_markup=keyboard)
    elif cb == "hb4":
        await CallbackQuery.edit_message_text(helpers.HELP_4, reply_markup=keyboard)
    elif cb == "hb5":
        await CallbackQuery.edit_message_text(helpers.HELP_5, reply_markup=keyboard)
    elif cb == "hb6":
        await CallbackQuery.edit_message_text(helpers.HELP_6, reply_markup=keyboard)
    elif cb == "hb7":
        await CallbackQuery.edit_message_text(helpers.HELP_7, reply_markup=keyboard)
    elif cb == "hb8":
        await CallbackQuery.edit_message_text(helpers.HELP_8, reply_markup=keyboard)
    elif cb == "hb9":
        await CallbackQuery.edit_message_text(helpers.HELP_9, reply_markup=keyboard)
    elif cb == "hb10":
        await CallbackQuery.edit_message_text(helpers.HELP_10, reply_markup=keyboard)
    elif cb == "hb11":
        await CallbackQuery.edit_message_text(helpers.HELP_11, reply_markup=keyboard)
    elif cb == "hb12":
        await CallbackQuery.edit_message_text(helpers.HELP_12, reply_markup=keyboard)
    elif cb == "hb13":
        await CallbackQuery.edit_message_text(helpers.HELP_13, reply_markup=keyboard)
    elif cb == "hb15":
        await CallbackQuery.edit_message_text(helpers.HELP_15, reply_markup=keyboard)
    
@app.on_callback_query(filters.regex("aryan") & ~BANNED_USERS)
@languageCB
async def first_pagexx(client, CallbackQuery, _):
    menu_next = second_page(_)
    try:
        await CallbackQuery.message.edit_text(_["help_1"].format(SUPPORT_CHAT), reply_markup=menu_next)
        return
    except:
        return

@app.on_callback_query(filters.regex("emma") & ~BANNED_USERS)
@languageCB
async def first_pagee(client, CallbackQuery, _):
    menu_next = second_page(_)
    try:
        await CallbackQuery.message.edit_text(_["help_1"].format(SUPPORT_CHAT), reply_markup=menu_next)
        return
    except:
        return


# Do not try to change whole code, just add or remove what you want.
