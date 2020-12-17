#from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing
import alert.routing
from alert.middlewares import TokenAuthMiddleware

"""application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter(chat.routing.websocket_urlpatterns)
    ),
})"""

application = ProtocolTypeRouter({
    "websocket": TokenAuthMiddleware(
        URLRouter(alert.routing.websocket_urlpatterns)
    ),
})