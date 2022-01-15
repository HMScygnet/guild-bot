from enum import auto
import qqbot
import re
from functools import wraps
from qqbot import Message
from . import bot_api
from .modules.avatar_guess.avatar_guess import avatar_guess, on_input_chara_name
from .modules.aichat.aichat import ai_reply
from .modules.pcr_rank.rank import pcr_rank_choose, pcr_rank_bili, pcr_rank_tw
from .modules.pokemanpcr.poke_man_pcr import (poke_back, storage)

chan_avatar = '' #猜头像子频道
chan_poke = ''   #戳一戳子频道


on_fullmatch = bot_api.on_fullmatch


async def handler_message(ev, message: Message):
    msg = message.content
    cid = message.channel_id
    gid = message.guild_id
    if msg is None:
        return
    #猜头像
    await on_fullmatch('猜头像',avatar_guess,ev,message,chan_avatar)
        #猜头像获取答案
    await on_input_chara_name(ev,message)


    #ai对话
    await ai_reply(ev,message)


    #rank表
        #选择rank表
    await on_fullmatch(['rank','rank表'],pcr_rank_choose,ev,message)

        #B服rank
    await on_fullmatch(['brank','Brank','国rank','陆rank'],pcr_rank_bili,ev,message)

        #台服rank
    await on_fullmatch('台rank',pcr_rank_tw,ev,message)
    

    #戳一戳集卡
        #戳
    await on_fullmatch('戳',poke_back,ev,message,chan_poke,True)
        #查看仓库
    await on_fullmatch('查看仓库',storage,ev,message,chan_poke)