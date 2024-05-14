# Importing important modules & bot

from ARYAN import app
from typing import Union
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

#------------------------------------------------------------------------#



# creating first partition of menu

def first_page(_):
	controll_button = [InlineKeyboardButton(text="◁", callback_data=f"emma"), InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data=f"settingsback_helper"), InlineKeyboardButton(text="▷", callback_data=f"aryan")]
	first_page_menu = InlineKeyboardMarkup(
		[
			[InlineKeyboardButton(text=_["H_B_1"], callback_data="help_callback hb1"), InlineKeyboardButton(text=_["H_B_2"], callback_data="help_callback hb2"),InlineKeyboardButton(text=_["H_B_3"], callback_data="help_callback hb3")],
			[InlineKeyboardButton(text=_["H_B_4"], callback_data="help_callback hb4"), InlineKeyboardButton(text=_["H_B_5"], callback_data="help_callback hb5"),InlineKeyboardButton(text=_["H_B_6"], callback_data="help_callback hb6")],
			[InlineKeyboardButton(text=_["H_B_7"], callback_data="help_callback hb7"), InlineKeyboardButton(text=_["H_B_8"], callback_data="help_callback hb8"),InlineKeyboardButton(text=_["H_B_9"], callback_data="help_callback hb9")],
                        [InlineKeyboardButton(text=_["H_B_10"], callback_data="help_callback hb10"), InlineKeyboardButton(text=_["H_B_11"], callback_data="help_callback hb11"), InlineKeyboardButton(text=_["H_B_12"], callback_data="help_callback hb12")],
			controll_button,
		]
	)
	return first_page_menu



# creating second partition of menu

def second_page(_):
	controll_button = [InlineKeyboardButton(text="◁", callback_data=f"settings_back_helper_fixed"), InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data=f"settingsback_helper"), InlineKeyboardButton(text="▷", callback_data=f"settings_back_helper")]
	second_page_menu = InlineKeyboardMarkup(
		[
			[InlineKeyboardButton(text=_["H_B_13"], callback_data="help_callback hb13"), InlineKeyboardButton(text=_["H_B_14"], callback_data="help_callback hb14"), InlineKeyboardButton(text=_["H_B_15"], callback_data="help_callback hb15")],
			
			controll_button,
		]
	)
	return second_page_menu


# Just an common button
def help_back_markup(_):
	upl = InlineKeyboardMarkup([
		[
			InlineKeyboardButton(text=_["BACK_BUTTON"], callback_data=f"settings_back_helper"),
			InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data=f"close"),
		
		
		],
	         ]
		  )
	return upl


# Ease of access 
def private_help_panel(_):
	buttons = [[InlineKeyboardButton(text=_["S_B_4"], url=f"https://t.me/{app.username}?start=help")]]
	return buttons



#----------------------------> NOTE <-----------------------------#
"""
Written By aryan.
"""
