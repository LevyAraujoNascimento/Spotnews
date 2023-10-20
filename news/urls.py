from django.urls import path
from news.views import news_home, news_details, create_categories_form


urlpatterns = [
    path("", news_home, name="home-page"),
    path("news/<int:id>", news_details, name="news-details-page"),
    path("categories/", create_categories_form, name="categories-form")
]
