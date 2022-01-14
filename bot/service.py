from enum import auto
import qqbot
import re
from qqbot import Message
from . import bot_api
from .modules.avatar_guess.avatar_guess import avatar_guess, on_input_chara_name
from .modules.aichat.aichat import ai_reply
from .modules.pcr_rank.rank import pcr_rank_choose, pcr_rank_bili, pcr_rank_tw
from .modules.pokemanpcr.poke_man_pcr import (poke_back, storage)

async def on_message(ev, message: Message):
    msg = message.content
    if msg is None:
        return
    #猜头像
    if msg == '猜头像':
        await avatar_guess(ev,message)

        #猜头像获取答案
    await on_input_chara_name(ev,message)


    #ai对话
    await ai_reply(ev,message)


    #rank表
        #选择rank表
    if msg == ('rank' or 'rank表'):
        await pcr_rank_choose(ev,message)

        #B服rank
    if msg == ('brank' or 'Brank' or '国rank' or '陆rank'):
        await pcr_rank_bili(ev,message)

        #台服rank
    if msg == '台rank':
        await pcr_rank_tw(ev,message)

    
    #戳一戳集卡
        #融合卡片
    #if msg == ('一键献祭' or '一键合成' or '一键融合' or '全部献祭' or '全部合成' or '全部融合'):
    #    await auto_mix_card(ev,message)
    
    if msg == '查看仓库':
        await storage(ev,message)


async def on_message_atme(ev,message: Message):
    msg = message.content
    if msg is None:
        return
    _re = re.match(r'<(.*)>  (.*)',msg)
    msg = _re.group(2)
    #戳一戳集卡
    if msg == '戳':
        await poke_back(ev,message)
