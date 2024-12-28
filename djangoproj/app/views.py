from django.shortcuts import render
from django.urls import reverse_lazy
from app.models import Article
from django.views.generic import CreateView


def home(request):
    # load django ORM - Object Relational Mapper
    articles = Article.objects.all()
    # render html passing the request, template name and context
    return render(request, "app/home.html", {"articles": articles})


class ArticleCreateView(CreateView):
    template_name = "app/article_create.html"
    model = Article
    fields = ["title", "status", "content", "word_count", "twitter_post"]
    template_name = "app/article_create.html"
    success_url = reverse_lazy("home")
