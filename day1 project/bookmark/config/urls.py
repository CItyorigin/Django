"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path
from django.shortcuts import redirect

from bookmark import views

movie_list = [
    {"title": "파묘", "director": "장재현"},
    {"title": "원카", "director": "폴킴"},
    {"title": "듐2", "director": "드니 빌뇌브"},
    {"title": "시민덕히", "director": "방영주"},
]


def index(request):
    return HttpResponse("<h1>Hello World<h1>")

def book_list(request):

    # book_text = ""
    # for i in range(0,10):
    #     book_text += f"Book {i+1}<br>"

    return render(request, template_name='book list.html', context={'range': range(0, 10)})

def book(request, num):
    book_text = f"book {num}번 페이지 입니다.<br>"
    return  render(request, template_name='book_detail.html', context={'num': num})
def language(request, lang):
    return HttpResponse(f"<h1>{lang} 언어 페이지 입니다.")

def python(request):
    return HttpResponse("python 페이지 입니다.")

def movies(request):
    # movie_titles = [
    #    f'<a href="/movie/{index}/">{movie["title"]}</a><br>'
    #    for index, movie in enumerate(movie_list)]

    #movie_title =[]
    ##for movie in movie_list:
    #    #movie_title.append(movie["title"])

    #responses_text = '<br>'.join(movie_titles)

    #for index, title in enumerate(movie_titles):
    #    responses_text += f"<a href = '/movie/{index}/'>{title}</h1>"

    #return HttpResponse(responses_text)
    return render(request, template_name="movies.html", context={"movie_list": movie_list})



def movie_detail(request, index):
    def movie_detail(request, index):
        if index < 0 or index >= len(movie_list):
            raise Http404

    #movie = movie_list[index]
    #response_text = f"<h1>{movie['title']}</h1> <p>{movie['director']}</p>"
    #return render(request, template_name="movie_detail.html", context={"movie": movie})
    movie = movie_list[index]
    context = {'movie': movie}
    return render(request, template_name='movie.html', context=context)


def gugu(request, num):
    context = {
        'num': num,
        'results': [num * i for i in range(1, 10)]
    }
    return render(request, 'gugu.html', context)


    # if num < 2:
    #     return redirect('/gugu/2/')
    #
    # context = {
    #     'num': num,
    #     'range': range(1, 10)
    #     # 또는 'results': [(i, num * i) for i in range(1, 10)]
    # }
    #
    # return render(request, 'gugu.html', context)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gugu/<int:num>/', gugu),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('book_list/', book_list),
    path('book_list/<int:num>/', book),
    path("language/<str:lang>", language),
    path("language/python/", language),
    path("movies/", movies),
    path("movie/<int:index>/", movie_detail),
    path("gugu/<int:num>/", gugu),

    path("bookmark/", views.bookmark_list),
    path("bookmark/<int:index>/", views.bookmark),
]
