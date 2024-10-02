from django.urls import path
from .views import post_list_api_view, post_detail_api_view

urlpatterns = [
    path("posts/", post_list_api_view, name="post_list_api"),
    path("post/<int:id>/", post_detail_api_view, name="post_detail_api"),
]
