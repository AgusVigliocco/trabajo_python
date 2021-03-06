from django import views
from django.urls import URLPattern, path
from .views import render_posts, post_detail

app_name = 'blog'

urlpatterns = [
    path('', render_posts, name='post'),
    path('<int:post_id>', post_detail, name='post_detail')
]
