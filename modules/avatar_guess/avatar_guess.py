# ref: https://github.com/GWYOG/GWYOG-Hoshino-plugins/blob/master/pcravatarguess
# Originally written by @GWYOG
# Reflacted by @Ice-Cirno
# GPL-3.0 Licensed
# Thanks to @GWYOG for his great contribution!

import asyncio
import os
import random
from PIL import Image
import qqbot
from qqbot import Message

from . import _pcr_data,chara


from . import GameMaster

PATCH_SIZE = 32
ONE_TURN_TIME = 20
DB_PATH = os.path.join(os.path.dirname(__file__),"pcr_avatar_guess.db")
BLACKLIST_ID = [1072, 1908, 4031, 9000]
res = 'C:/Program Files/apache/public/res/img'

def get_token():
    appid = ""
    token = ""
    token = qqbot.Token(appid, token)
    return token

msg_api = qqbot.AsyncMessageAPI(get_token(),False)
gm = GameMaster(DB_PATH)

'''
@sv.on_fullmatch("猜头像排行", "猜头像排名", "猜头像排行榜", "猜头像群排行")
async def description_guess_group_ranking(bot, ev: CQEvent):
    ranking = gm.db.get_ranking(ev.group_id)
    msg = ["【猜头像小游戏排行榜】"]
    for i, item in enumerate(ranking):
        uid, count = item
        m = await bot.get_group_member_info(
            self_id=ev.self_id, group_id=ev.group_id, user_id=uid
        )
        name = util.filt_message(m["card"]) or util.filt_message(m["nickname"]) or str(uid)
        msg.append(f"第{i + 1}名：{name} 猜对{count}次")
    await bot.send(ev, "\n".join(msg))
'''

async def avatar_guess(ev, message):
    msg = message.content
    cid = message.channel_id
    gid = message.guild_id
    mid = message.id
    if gm.is_playing(gid):
        send = qqbot.MessageSendRequest("游戏仍在进行中…", mid)
        await msg_api.post_message(cid, send)
        return
    with gm.start_game(gid) as game:
        ids = list(_pcr_data.CHARA_NAME.keys())
        game.answer = random.choice(ids), random.choice((3, 6))
        while chara.is_npc(game.answer[0]):
            game.answer = random.choice(ids), random.choice((3, 6))
        c = chara.fromid(game.answer[0], game.answer[1])
        basename = os.path.basename(c.icon.path)
        img = c.icon.open()
        w, h = img.size
        l = random.randint(0, w - PATCH_SIZE)
        u = random.randint(0, h - PATCH_SIZE)
        cropped = img.crop((l, u, l + PATCH_SIZE, u + PATCH_SIZE))
        cropped.save(os.path.join(res,'avatar_guess.png'))
        send = qqbot.MessageSendRequest(f"猜猜这个图片是哪位角色头像的一部分?({ONE_TURN_TIME}s后公布答案)", 
                                        mid,
                                        image='https://img.kokorobot.vip/img/avatar_guess.png')
        await msg_api.post_message(cid, send)
        await asyncio.sleep(ONE_TURN_TIME)
        if game.winner:
            return
        send = qqbot.MessageSendRequest(f"正确答案是：{c.name}\n很遗憾，没有人答对~",
                                        mid,
                                        image=f'https://img.kokorobot.vip/img/priconne/unit/{basename}')
        await msg_api.post_message(cid, send)
async def on_input_chara_name(ev,message):
    gid = message.guild_id
    cid = message.channel_id
    msg = message.content
    mid = message.id

    if gm.is_playing(gid):
        game = gm.get_game(gid)
        if not game or game.winner:
            return
        c = chara.fromname(msg, game.answer[1])
        if c.id != chara.UNKNOWN and c.id == game.answer[0]:
            uid = message.author.id
            basename = os.path.basename(c.icon.path)
            game.winner = uid
            n = game.record()
            send = qqbot.MessageSendRequest(f"正确答案是：{c.name}\n<@{uid}>猜对了，真厉害！TA已经猜对{n}次了~\n(此轮游戏将在几秒后自动结束，请耐心等待)",
                                            mid,
                                            image=f'https://img.kokorobot.vip/img/priconne/unit/{basename}')
            await msg_api.post_message(cid, send)