from django.urls import path
from app.views import home, ArticleCreateView


urlpatterns = [
    path("", home, name="home"),
    path("articles/create/", ArticleCreateView.as_view(), name="create_article"),
]
