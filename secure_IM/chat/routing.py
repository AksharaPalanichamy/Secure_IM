from django.urls import path
from . import users

websocket_urlpatterns=[
    path('chat/',users.ChatUser.as_asgi()),
]