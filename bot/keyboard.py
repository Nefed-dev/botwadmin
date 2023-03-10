from aiogram.types.inline_keyboard import InlineKeyboardMarkup, InlineKeyboardButton

from model import Message


class KeyboardMaker(object):
    @staticmethod
    def make_kb(parent: Message, data: list[Message]):
        ikm = InlineKeyboardMarkup(row_width=1)
        for msg in data:
            btn = InlineKeyboardButton(msg.button_text, callback_data=f"msg_{msg.id}")
            ikm.add(btn)
        if parent.parent_id is not None:
            btn = InlineKeyboardButton("Назад", callback_data=f"msg_{parent.parent_id}")
            ikm.add(btn)
        return ikm
