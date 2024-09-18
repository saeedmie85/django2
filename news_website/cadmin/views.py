from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from blog.models import Post
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import FormValidMixin, FieldMixin

# Create your views here.


class PostList(LoginRequiredMixin, ListView):
    # model = Post
    template_name = "cadmin/index.html"
    context_object_name = "posts"

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            self.queryset = Post.objects.all()
        else:
            self.queryset = Post.objects.filter(author=user)
        return super().get_queryset()


class CreatePost(LoginRequiredMixin, FormValidMixin, FieldMixin, CreateView):
    model = Post
    template_name = "cadmin/create_update_post.html"
    success_url = reverse_lazy("cadmin:post_list")
