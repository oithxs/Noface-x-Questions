from django.urls import path
from . import views

app_name = 'app'

urlpatterns= [
    path('',views.IndexView.as_view(),name='index'),
    path('create/', views.articleCreateView.as_view(), name='article_create'),
    path('create/complete/', views.articleCreateCompleteView.as_view(), name='article_create_complete'),
]