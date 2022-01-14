import qqbot

appid = ""
token = ""

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
