from rest_framework import serializers

from .models import Post


class PostListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('name',)
