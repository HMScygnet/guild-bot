import qqbot
from qqbot.model.message import Message
from bot.bot_api import get_token
from bot.service import handler_message


token = get_token()

_handler_message = qqbot.Handler(qqbot.HandlerType.MESSAGE_EVENT_HANDLER, handler_message)


qqbot.async_listen_events(token, False, _handler_message)