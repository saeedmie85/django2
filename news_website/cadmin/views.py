from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from blog.models import Post
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import FormValidMixin, FieldMixin, AuthorAccessMixin, SuperUserAccessMixin

# Create your views here.


class PostList(LoginRequiredMixin, ListView):
    # model = Post
    template_name = "cadmin/index.html"
    context_object_name = "posts"
    paginate_by = 2

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


class UpdatePostView(
    LoginRequiredMixin, AuthorAccessMixin, FormValidMixin, FieldMixin, UpdateView
):
    model = Post
    template_name = "cadmin/create_update_post.html"
    success_url = reverse_lazy("cadmin:post_list")


class DeletePostView(LoginRequiredMixin, SuperUserAccessMixin, DeleteView):
    model = Post
    template_name = "cadmin/delete_confirm_post.html"
    success_url = reverse_lazy("cadmin:post_list")
