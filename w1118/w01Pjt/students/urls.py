from django.urls import path,include
from . import views

app_name = 'students' # name:url시 사용

urlpatterns = [
    path('list/',views.list, name='list'), # 학생리스트페이지
    path('write/',views.write, name='write1'), # 학생입력페이지
    path('<str:name>/view/',views.view, name='view'), # 학생상세페이지 <이름 받기>
    path('<str:name>/modify/',views.modify, name='modify'), # 학생수정페이지 <이름 받기>
    path('modify2/',views.modify2,name='modify2'), # 학생수정페이지2 <이름 받기>
    path('<str:name>/modify3/',views.modify3, name='modify3'), # 학생수정페이지3 <이름 받기>
    
    path('<str:name>/delete/',views.delete, name='delete'), # 학생삭제
    
    # path('doWrite/',views.doWrite, name='doWrite1')
]
