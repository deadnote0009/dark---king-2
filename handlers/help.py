import logging

from pyrogram.types import Message
from search_engine_parser import GoogleSearch
from youtube_search import YoutubeSearch

from pyrogram import Client as app, filters

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

import pyrogram

logging.getLogger("pyrogram").setLevel(logging.WARNING)

from helpers.decorators import authorized_users_only


@app.on_message(pyrogram.filters.command(["search"]))
@authorized_users_only
async def helpmenu(_, message: Message):
    try:
        await message.reply_text("/play - To Play Song In Voice Chat\n/pause - To Pause Music(Admin & Sudo)\n/resume - To Resume Music(Admin & Sudo)\n/end - To End Music(Admin & Sudo)\n/skip - To Skip Song(Admin & Sudo)\n/userbotjoin | /assistant- To Join User Or Bot Automatically\n/gcast - To Broadcast Your Message(Sudo User)\n/clear | /rmd - To Delete All Download DB\n/clean | /rmw - To Remove Raw File \n/cleanup - To Remove Downloaded Image Sticker\n/pmpermit -To Turn On/Off PM Permit\n.a - To Approve Pm \n/.da - To Disapprove PM \n/repo - To Get Repo \n/song - To Search Song From YouTube\n/search - To Search YouTube Link")
        return
    except Exception as e:
        await message.reply_text(str(e))

