from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import BlogPostForm

class IndexView(TemplateView):
    template_name ='index.html'


class articleCreateView(CreateView):
    form_class = BlogPostForm
    template_name = 'article/article_create.html'
    success_url = reverse_lazy('app:article_create_complete')

class articleCreateCompleteView(TemplateView):
    template_name = 'article/article_create_complete.html'