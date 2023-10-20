from django.shortcuts import render
from news.models.news_model import News


def news_home(request):
    context = {
        "news": News.objects.all()
    }
    return render(request, 'home.html', context)


def news_details(request, id):
    context = {
        "news": News.objects.get(id=id)
    }
    return render(request, 'news_details.html', context)
