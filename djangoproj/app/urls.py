from django.urls import path
from app.views import home, ArticleCreateView, ArticleListView, ArticleUpdateView, ArticleDeleteView


urlpatterns = [
    path("", ArticleListView.as_view(), name="home"),
    path("articles/create/", ArticleCreateView.as_view(), name="article_create"),        
    path("articles/<int:pk>/update/", ArticleUpdateView.as_view(), name="article_update"),
    path("articles/<int:pk>/delete/", ArticleDeleteView.as_view(), name="article_delete"),
    # int:pk is integer primary key
]
