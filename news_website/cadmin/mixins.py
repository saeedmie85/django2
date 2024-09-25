from django.http import Http404
from django.shortcuts import get_object_or_404
from blog.models import Post


class FieldMixin:

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            self.fields = [
                "title",
                "category",
                "thumbnail",
                "slug",
                "body",
                "author",
                "publish",
                "status",
                "tags",
            ]
        elif request.user.is_author:
            self.fields = [
                "title",
                "category",
                "thumbnail",
                "slug",
                "body",
                "tags",
            ]
        else:
            raise Http404
        return super().dispatch(request, *args, **kwargs)


class FormValidMixin:

    def form_valid(self, form):
        if self.request.user.is_superuser:
            form.save()
        else:
            self.obj = form.save(commit=False)
            self.obj.author = self.request.user
            self.obj.status = "draft"

        return super().form_valid(form)


class AuthorAccessMixin:

    def dispatch(self, request, pk, *args, **kwargs):
        user = request.user
        post = get_object_or_404(Post, pk=pk)
        if user == post.author or user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        raise Http404("دسترسی غیر مجاز")


class SuperUserAccessMixin:

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            raise Http404("دسترسی غیر مجاز")
        return super().dispatch(request, *args, **kwargs)
