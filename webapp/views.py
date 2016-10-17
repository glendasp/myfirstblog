from django.shortcuts import render
from .crawler import crawl
# from .models import Post


def crawler(request):
    return render(request, 'webapp/crawler.html')


def results(request):
    if request.method == 'POST':
        article = request.POST.get('search')
        articles = crawl(article)
        return render(request, 'webapp/results.html', {'articles': articles})


def about(request):
    return render(request, 'webapp/about.html')
