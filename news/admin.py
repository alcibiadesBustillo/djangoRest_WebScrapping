from django.contrib import admin

# Register your models here.
from .models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass