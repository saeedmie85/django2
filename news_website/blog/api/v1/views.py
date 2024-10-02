from django.shortcuts import get_object_or_404
from blog.models import Post
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .serializers import PostSerializer
from rest_framework.response import Response
from rest_framework import status


@api_view(["get", "post"])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_list_api_view(request):
    if request.method == "GET":
        posts = Post.objects.filter(status="published")
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["get", "put", "delete"])
@permission_classes([IsAuthenticated])
def post_detail_api_view(request, id):
    post = get_object_or_404(Post, id=id, status="published")
    if request.method == "GET":
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer = PostSerializer(instance=post, data=request.data)
        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        post.delete()
        return Response(
            {"deleted": "Successfully deleted"}, status=status.HTTP_204_NO_CONTENT
        )
