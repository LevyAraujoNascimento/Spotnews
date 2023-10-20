from django.shortcuts import render, redirect
from news.models.news_model import News
from news.models.category_model import Categories
from news.forms import CreateCategoryForm


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


def create_categories_form(request):
    if request.method == "POST":
        form = CreateCategoryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            Categories.objects.create(name=name)
            return redirect('home-page')
    form = CreateCategoryForm()
    context = {
        "form": form
    }
    return render(request, 'categories_form.html', context)
