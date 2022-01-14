import json
import random


import qqbot
from qqbot.model.message import Message
from ..priconne import bot_api


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

msg_send = bot_api.msg_send


DEFAULT_AI_CHANCE = 10   # AI回复概率
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



async def ai_reply(ev, message: Message):
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
            await msg_send(mid,cid,msg)
        except TencentCloudSDKException as err: 
            print(err) 