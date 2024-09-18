from django.urls import path
from .views import PostList, CreatePost

app_name = "cadmin"

urlpatterns = [
    path("", PostList.as_view(), name="post_list"),
    path("create_post", CreatePost.as_view(), name="create_post"),
]
