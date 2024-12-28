from django.urls import path
from app.views import home
from app.views import create_article
urlpatterns = [
    path("", home, name="home"),
    path("articles/create/", create_article, name="create_article"),
]
