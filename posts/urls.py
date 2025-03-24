from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='post-list'),
    path('<int:pk>/', views.PostDetail.as_view(), name='post-detail'),
    path('<int:pk>/comment_count/', views.PostDetail.comment_count, name='post-comment-count'),
]