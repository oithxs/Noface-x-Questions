from django.contrib import admin

# Register your models here.

# 追加
from .models import BlogPost

# Blogpostを登録する
admin.site.register(BlogPost)