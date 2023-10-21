from django.shortcuts import render, redirect
from news.models.news_model import News
from news.models.category_model import Categories
from news.forms import CreateCategoryForm
from news.forms import CreateNewsForm


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


def create_news_form(request):
    if request.method == "POST":
        form = CreateNewsForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            author = form.cleaned_data['author']
            created_at = form.cleaned_data['created_at']
            image = form.cleaned_data['image']
            News.objects.create(
                title=title,
                content=content,
                author=author,
                created_at=created_at,
                image=image
            )
            return redirect('home-page')
    form = CreateNewsForm()
    context = {
        "form": form
    }
    return render(request, 'news_form.html', context)
