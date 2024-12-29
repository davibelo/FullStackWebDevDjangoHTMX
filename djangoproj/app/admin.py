from django.contrib import admin
from app.models import UserProfile, Article

# Define a custom admin class for the Article model.
# This class customizes the appearance and behavior of 
# the Article model in the Django admin interface.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "word_count", "status", "created_at", "updated_at")
    list_filter = ("status",)
    search_fields = ("title", "content")
    date_hierarchy = "created_at"
    ordering = ("created_at",)
    readonly_fields = ("word_count", "created_at", "updated_at")

# Register your models here.
admin.site.register(Article, ArticleAdmin)
admin.site.register(UserProfile)


