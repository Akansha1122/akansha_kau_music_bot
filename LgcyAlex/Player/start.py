
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from LgcyAlex.config import BOT_NAME as bn
from Process.filters import other_filters2
from time import time
from datetime import datetime
from Process.decorators import authorized_users_only
from LgcyAlex.config import BOT_USERNAME, ASSISTANT_USERNAME

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 ** 2 * 24),
    ("hour", 60 ** 2),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(other_filters2)
async def start(_, message: Message):
        await message.reply_text(
        f"""**I ᴀᴍ 𝙇𝙂𝙘𝙔・𝘽𝙊𝙏
ʙᴏᴛ ʜᴀɴᴅʟᴇ ʙʏ [𝙇𝙂𝙘𝙔・𝘼𝙇𝙀𝙓](https://t.me/lgcyalex)**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝘾𝙤𝙣𝙩𝙖𝙘𝙩 𝙈𝙚", url="https://t.me/lgcyalex"
                    ),
                    InlineKeyboardButton(
                        "𝘾𝙤𝙢𝙢𝙖𝙣𝙙 𝙇𝙞𝙨𝙩🛠", url="https://telegra.ph/%C5%81GcYA%C5%81EX-02-18"
                    )
                  ],[
                    InlineKeyboardButton(
                       "𝙅𝙤𝙞𝙣 𝙂𝙧𝙤𝙪𝙥", url="https://t.me/LGCY_OFFICIAL"
                    ),
                    InlineKeyboardButton(
                        "𝐆𝐫𝐨𝐮𝐩 𝐒𝐮𝐩𝐩𝐨𝐫𝐭", url="https://t.me/Clan8Xofficial"
                    )
                ],[
                    InlineKeyboardButton(
                        "➕ 𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )
