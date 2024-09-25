from django.urls import path
from .views import PostList, CreatePost, UpdatePostView, DeletePostView

app_name = "cadmin"

urlpatterns = [
    path("", PostList.as_view(), name="post_list"),
    path("page/<int:page>/", PostList.as_view(), name="post_list"),
    path("create_post/", CreatePost.as_view(), name="create_post"),
    path("update_post/<int:pk>/", UpdatePostView.as_view(), name="update_post"),
    path("delete_post/<int:pk>/delete/", DeletePostView.as_view(), name="delete_post"),
]
