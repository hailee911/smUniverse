from django.urls import path,include
from . import views
# . -> 현재폴더에서 views를 import
# 메인URL #

app_name = 'students'

urlpatterns = [
    path('write/', views.write, name='write'),
]
