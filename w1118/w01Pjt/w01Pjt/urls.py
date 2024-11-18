from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/',include('students.urls')), # url 추가
    path('',include('home.urls')),
    path('board/',include('board.urls')),
]
