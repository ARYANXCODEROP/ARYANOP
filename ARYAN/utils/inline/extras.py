from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from ARYAN import app

import config

from config import SUPPORT_CHAT


def botplaylist_markup(_):
    buttons = [
        [
            InlineKeyboardButton(text=_["S_B_9"], url=SUPPORT_CHAT),
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close"),
        ],
    ]
    return buttons


def close_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                ),
            ]
        ]
    )
    return upl


def supp_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["S_B_9"],
                    url=SUPPORT_CHAT,
                ),
            ]
        ]
    )
    return upl

def add_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ", url=f"https://t.me/{app.username}?startgroup=True&admin=delete_messages+invite_users"),
           ],
        ]
    )
    return upl

def suppclose_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                 InlineKeyboardButton(
                    text=_["S_B_9"],
                    url=SUPPORT_CHAT,
            ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                ),
            ]
        ]
    )
    return upl

def source_markup(_):
    upl = InlineKeyboardMarkup(
        [
           [ 
                InlineKeyboardButton(
                        text="ʀᴇᴘᴏ", callback_data=f"gib_source"
                    ),
                    InlineKeyboardButton(
                        text="ʟᴏᴠᴇ", callback_data=f"love"
                    ),
           ],
               [ 
                InlineKeyboardButton(
                        text="ʙᴀᴄᴋ", callback_data=f"settingsback_helper"
                ),
           ],
               
           ],
    )
    return upl

def lood_markup(_):
    upl = InlineKeyboardMarkup(
        [
                [
                    InlineKeyboardButton(
                        text="ᴄʜᴀɴɴᴇʟ", url="https://t.me/STATUSDAIRY2"
                    ),

                    InlineKeyboardButton(
                        text="ᴍᴜsɪᴄ ɢʀᴏᴜᴘ", url="https://t.me/vohmusic"
                    ),
                    
                ],
                [
                    InlineKeyboardButton(
                        text="ᴅᴇᴠᴇʟᴏᴘᴇʀ", user_id=config.OWNER_ID
                    ),

                    InlineKeyboardButton(
                        text="sᴜᴘᴘᴏʀᴛ", url="https://t.me/VOICEOFHEART0"
                    ),
                    
                ],
                [
                    InlineKeyboardButton(
                        text="ʙᴀᴄᴋ", callback_data=f"settingsback_helper"
                    )
                ],
            ]
    )
    return upl

def source1_markup(_):
    upl = InlineKeyboardMarkup(
        [
           [ 
                InlineKeyboardButton(
                        text="◁", callback_data=f"repoxlove"
                ),
           ],
        ]
    )
    return upl

def source2_markup(_):
    upl = InlineKeyboardMarkup(
        [
           [ 
                InlineKeyboardButton(
                        text="◁", callback_data=f"repoxlove"
                ),
           ],
        ]
    )
    return upl
