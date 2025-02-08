# gas/gas_app/urls.py : API urls.py
# from django.conf.urls import url

from django.urls import path, include
from .views import (
    GameListApiView, GameDetailApiView
)

urlpatterns = [
    path('api', GameListApiView.as_view()),
    path('api/<int:game_id>/', GameDetailApiView.as_view()),
]

