from pyrogram.types import InlineKeyboardButton

import config
from ARYAN import app



def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text=_["S_B_4"], callback_data="amhelper")],
        [
            InlineKeyboardButton(text=_["S_B_2"], callback_data="lood"),
            InlineKeyboardButton(text=_["S_B_7"], callback_data="repoxlove"),
            
        ],
        [
            InlineKeyboardButton(text=_["ST_B_4"], callback_data="bot_info_data"),
        ],
    ]
    return buttons
