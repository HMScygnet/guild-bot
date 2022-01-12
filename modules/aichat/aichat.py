import json
import random


import qqbot
from qqbot.model.message import Message



from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.nlp.v20190408 import nlp_client, models


black_word = ['猜头像']

try:
    import ujson as json
except ImportError:
    import json

def get_token():
    appid = ""
    token = ""
    token = qqbot.Token(appid, token)
    return token

msg_api = qqbot.AsyncMessageAPI(get_token(),False)


DEFAULT_AI_CHANCE = 10   # 默认的AI回复概率
SecretId = "" #  填你的SecretId
SecretKey = ""#  填你的SecretKey


def aichat(text):
    cred = credential.Credential(SecretId, SecretKey) 
    httpProfile = HttpProfile()
    httpProfile.endpoint = "nlp.tencentcloudapi.com"

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = nlp_client.NlpClient(cred, "ap-guangzhou", clientProfile) 

    req = models.ChatBotRequest()
    params = {
        "Query": text,
    }
    req.from_json_string(json.dumps(params))

    resp = client.ChatBot(req)
    param = resp.to_json_string()
    reply = json.loads(param)
    msg = reply['Reply']
    return msg



async def ai_reply(ev, message):
    msg = message.content
    mid = message.id
    cid = message.channel_id

    if not random.randint(1,100) <= DEFAULT_AI_CHANCE:
        return
    else:           
        if msg == '' or (msg in black_word):
            return
        try: 
            msg = aichat(msg)
            send = qqbot.MessageSendRequest(msg,mid)
            await msg_api.post_message(cid,send)
        except TencentCloudSDKException as err: 
            print(err) 