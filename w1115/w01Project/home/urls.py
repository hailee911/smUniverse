from django.urls import path
from . import views

# url에 아무것도 들어가지 않았을 때
app_name = ''

urlpatterns = [
  # views.py 연결 - 함수 호출, app 함수이름
  path('',views.index, name='index'),
]