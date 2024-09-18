from django.http import Http404


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
