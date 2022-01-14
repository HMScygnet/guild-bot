import qqbot
from qqbot import Message
from . import bot_api
from .modules.avatar_guess.avatar_guess import avatar_guess, on_input_chara_name
from .modules.aichat.aichat import ai_reply
from .modules.pcr_rank.rank import pcr_rank_choose, pcr_rank_bili, pcr_rank_tw

async def on_message(ev, message: Message):
    msg = message.content

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

    

    