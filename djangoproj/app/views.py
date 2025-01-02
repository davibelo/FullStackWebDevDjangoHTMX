from typing import Any
from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from app.models import Article
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class ArticleListView(LoginRequiredMixin, ListView):
    template_name = "app/home.html"
    model = Article
    context_object_name = "articles"

    def get_queryset(self) -> QuerySet(Any):
        return Article.objects.filter(creator=self.request.user).order_by("-created_at")

class ArticleCreateView(LoginRequiredMixin, CreateView):
    template_name = "app/article_create.html"
    model = Article
    fields = ["title", "status", "content", "twitter_post"]
    success_url = reverse_lazy("home")
    # Set the creator field to the current user when creating a new article.
    # This is done by overriding the form_valid method and setting the creator field to self.request.user.
    # The super().form_valid(form) call then saves the form with the updated creator field.
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "app/article_update.html"
    model = Article
    fields = ["title", "status", "content", "twitter_post"]
    success_url = reverse_lazy("home")
    context_object_name = "article"

    # The test_func method checks if the current user is the creator of the article.
    def test_func(self) -> bool | None:
        article = self.get_object()
        return self.request.user == article.creator

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "app/article_delete.html"
    model = Article
    success_url = reverse_lazy("home")
    context_object_name = "article"

    # The test_func method checks if the current user is the creator of the article.
    def test_func(self) -> bool | None:
        article = self.get_object()
        return self.request.user == article.creator
