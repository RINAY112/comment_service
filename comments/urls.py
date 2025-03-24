from django.urls import path
from . import views

urlpatterns = [
    path('', views.CommentList.as_view(), name='comment-list'),
    path('<int:pk>/', views.CommentDetail.as_view(), name='comment-detail'),
    path('<int:pk>/user_comment_count/', views.CommentDetail.user_comment_count, name='comment-user-comment-count'),
]