from django.urls import path

from . import views


app_name = 'blog'


urlpatterns = [
    path('posts/', views.PostListView.as_view(), name='post-list'),
]
