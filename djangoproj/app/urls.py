from django.urls import path
from app.views import home, ArticleCreateView, ArticleListView, ArticleUpdateView, ArticleDeleteView


urlpatterns = [
    path("", home, name="home"),
    path("articles/create/", ArticleCreateView.as_view(), name="article_create"),
]
