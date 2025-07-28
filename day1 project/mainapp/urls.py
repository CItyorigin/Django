from django.urls import path
from . import views

urlpatterns = [
    path('gugudan/', views.gugudan_page, name='gugudan'),
    path('books/', views.book_page, name='books'),
    path('movies/', views.movie_page, name='movies'),
]
