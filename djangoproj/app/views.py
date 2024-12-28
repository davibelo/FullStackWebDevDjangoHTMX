from app.models import Article
from django.shortcuts import render
from app.forms import CreateArticleForm
from django.shortcuts import redirect

def home(request):
    # load django ORM - Object Relational Mapper
    articles = Article.objects.all()
    # render html passing the request, template name and context
    return render(request, "app/home.html", {"articles": articles})


def create_article(request):
    if request.method == "POST":
        form = CreateArticleForm(request.POST)
        if form.is_valid():
            form.data = form.cleaned_data()
            new_article = Article(
                title = form.data["title"],
                status = form.data["status"],
                content = form.data["content"],
                word_count = form.data["word_count"],
                twitter_post = form.data["twitter_post"],
            )
            new_article.save()
            return redirect("home")
    else:
        form = CreateArticleForm()
    return render(request, "app/article_create.html", {"form": form})
