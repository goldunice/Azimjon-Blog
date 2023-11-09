from django.contrib import admin
from .models import *


@admin.register(Maqola)
class BlogAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "date", "text", "photo"]
    list_filter = ["date"]
