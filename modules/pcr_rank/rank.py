import qqbot
from asyncio import sleep
from qqbot import Message
from ..priconne import bot_api

msg_send = bot_api.msg_send


async def pcr_rank_choose(ev,message: Message):
    mid = message.id
    cid = message.channel_id
    await msg_send(mid,cid,"请选择对应区服:\n*B服：brank\n*台服：台rank")


async def pcr_rank_bili(ev,message: Message):
    mid = message.id
    cid = message.channel_id
    await msg_send(mid,cid,"表格仅供参考※\n不定期搬运自B站专栏\n※制作byFF半音:\n","https://img.kokorobot.vip/img/priconne/rank/bili/bili_1.png")
    await msg_send(mid,cid,image="https://img.kokorobot.vip/img/priconne/rank/bili/bili_2.png")

async def pcr_rank_tw(ev,message: Message):
    mid = message.id
    cid = message.channel_id
    await msg_send(mid,cid,"表格仅供参考※\n不定期搬运自巴哈姆特论坛\n※制作by無羽:\n","https://img.kokorobot.vip/img/priconne/rank/tw/tw_1.png")
    await msg_send(mid,cid,image="https://img.kokorobot.vip/img/priconne/rank/tw/tw_2.png")
    await msg_send(mid,cid,image="https://img.kokorobot.vip/img/priconne/rank/tw/tw_3.png")