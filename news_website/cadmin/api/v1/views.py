from django.shortcuts import get_object_or_404
from blog.models import Post
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
    IsAdminUser,
)
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from .permisions import IsAuthorUser
from .mixins import AuthorMixin


# class PostListApiView(APIView):
#     def get(self, request):
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)


class PostListApiView(AuthorMixin, generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsAuthorUser]


class PostDetailApiView(AuthorMixin, generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsAuthorUser]
