from django.urls import path
from .views import PostList, CreatePost, UpdatePostView

app_name = "cadmin"

urlpatterns = [
    path("", PostList.as_view(), name="post_list"),
    path("create_post", CreatePost.as_view(), name="create_post"),
    path("update_post/<int:pk>", UpdatePostView.as_view(), name="update_post"),
]
