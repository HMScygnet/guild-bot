import qqbot
import re
from .config import __bot__ as config

appid = config.APPID
token = config.TOKEN
sandbox = '4294901327'  #沙箱频道

def get_token():
    _token = qqbot.Token(appid, token)
    return _token

def msg_api():
    _msg_api = qqbot.AsyncMessageAPI(get_token(),False)
    return _msg_api

async def msg_send(mid,cid,msg="\n",image=""):
    send = qqbot.MessageSendRequest(msg,mid,image=image)
    await msg_api().post_message(cid,send)
    return

async def on_fullmatch(words,func,ev,message,cid='', only_to_me=False):
    is_word = isinstance(words,str)
    msg = message.content
    _cid = message.channel_id
    gid = message.guild_id
    if cid != '':
        if gid != sandbox:
            if cid != _cid:
                return
    _re = re.search(r'\u003c(.*)\u003e  (.*)',msg)
    try:
        msg = _re.group(2)
    except:
        if only_to_me == True:
            return

    if is_word:
        if words == msg:
           await func(ev,message)
    else:
        for word in words:
            if word == msg:
                await func(ev,message)