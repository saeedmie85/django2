from django.urls import path
from .views import PostListApiView, PostDetailApiView

urlpatterns = [
    path("posts/", PostListApiView.as_view(), name="post_list_api"),
    path("post/<int:pk>", PostDetailApiView.as_view()),
]
