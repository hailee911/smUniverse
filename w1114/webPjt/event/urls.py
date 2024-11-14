from django.urls import path,include
from . import views
# . -> 현재폴더에서 views를 import
# 메인URL #

app_name = 'event'

urlpatterns = [
    path('eventView/', views.eventView, name='eventView'),
]
