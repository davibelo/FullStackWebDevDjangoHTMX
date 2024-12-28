from django.urls import path
from app.views import home, ArticleCreateView, ArticleListView, ArticleUpdateView, ArticleDeleteView


urlpatterns = [
    path("", home, name="home"),
    path("articles/", ArticleListView.as_view(), name="article_list"),
    path("articles/create/", ArticleCreateView.as_view(), name="article_create"),    
    # int:pk integer primary key
    path("articles/<int:pk>/update/", ArticleUpdateView.as_view(), name="article_update"),
    path("articles/<int:pk>/delete/", ArticleDeleteView.as_view(), name="article_delete"),
]
