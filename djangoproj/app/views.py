from app.models import Article
from django.shortcuts import render

def home(request):
    # load django ORM - Object Relational Mapper
    articles = Article.objects.all() 
    # render html passing the request, template name and context
    return render(request, 'app/home.html', {'articles': articles})