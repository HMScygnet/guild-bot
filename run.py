import qqbot
from qqbot.model.message import Message
from bot.bot_api import get_token
from bot.service import on_message, on_message_atme


token = get_token()

_on_message = qqbot.Handler(qqbot.HandlerType.MESSAGE_EVENT_HANDLER, on_message)
_on_message_atme = qqbot.Handler(qqbot.HandlerType.AT_MESSAGE_EVENT_HANDLER, on_message_atme)

qqbot.async_listen_events(token, False, _on_message,_on_message_atme)