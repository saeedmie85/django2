from blog.models import Post
from .serializers import PostAuthorSerializer, PostSuperUserSerializer


class AuthorMixin:

    def get_serializer_class(self):
        user = self.request.user
        if user.is_superuser:
            serializer = PostSuperUserSerializer
        else:
            serializer = PostAuthorSerializer
        return serializer

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            queryset = Post.objects.all()
        else:
            queryset = Post.objects.filter(author=user)
        return queryset
