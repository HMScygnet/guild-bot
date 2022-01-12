import qqbot
from qqbot.model.message import Message
from modules.service import get_token
from modules.service import on_message

token = get_token()

_on_message = qqbot.Handler(qqbot.HandlerType.MESSAGE_EVENT_HANDLER, on_message)

qqbot.async_listen_events(token, False, _on_message)
