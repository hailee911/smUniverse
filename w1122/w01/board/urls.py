from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('blist/', views.blist, name='blist'), # 게시판리스트
    path('bwrite/', views.bwrite, name='bwrite'), # 글쓰기
    path('bview/<int:bno>/', views.bview, name='bview'), # 글 상세보기
    path('bmodify/<int:bno>/', views.bmodify, name='bmodify'), # 글 수정
    path('bdelete/<int:bno>/', views.bdelete, name='bdelete'), # 글 삭제
    path('breply/<int:bno>/', views.breply, name='breply'), # 답변 달기
]
