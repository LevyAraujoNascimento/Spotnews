from django.urls import path
from news.views import news_home, news_details


urlpatterns = [
    path("", news_home, name="home-page"),
    path("news/<int:id>", news_details, name="news-details-page")
]
