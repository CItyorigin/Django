from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls')),  # mainapp 앱의 urls.py를 루트 경로에 연결
]