from django.shortcuts import render

def movie_page(request):
    movies = ['기생충', '어벤져스', '인셉션', '스타워즈', '라라랜드']
    return render(request, 'movie.html', {'movies': movies})

def book_page(request):
    books = ['해리포터', '반지의 제왕', '나미야 잡화점의 기적', '어린왕자', '데미안']
    return render(request, 'book.html', {'books': books})

def gugudan_page(request):
    result = None
    number = None
    if request.method == 'POST':
        try:
            number = int(request.POST.get('number'))
            result = [f"{number} x {i} = {number * i}" for i in range(1, 10)]
        except (ValueError, TypeError):
            result = None
    return render(request, 'gugudan.html', {'result': result, 'number': number})
