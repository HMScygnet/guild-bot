import qqbot
from qqbot import Message
from .avatar_guess.avatar_guess import avatar_guess,on_input_chara_name
from .aichat.aichat import ai_reply


def get_token():
    appid = ""
    token = ""
    token = qqbot.Token(appid, token)
    return token

def msg_api():
    _msg_api = qqbot.AsyncMessageAPI(get_token(),False)
    return _msg_api


async def on_message(ev, message: Message):
    msg = message.content
    if msg == '猜头像':
        await avatar_guess(ev,message)
    await on_input_chara_name(ev,message)
    await ai_reply(ev,message)