from rest_framework import serializers
from blog.models import Post


class PostSuperUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = "__all__"


class PostAuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        read_only_fields = ["id", "publish", "created", "updated", "status", "author"]
        exclude = ["author"]
