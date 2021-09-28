from rest_framework import serializers
from blog.models import Post
from django.contrib.auth.models import User

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'first_name', 'last_name'
        ]


class PostSerializer(serializers.ModelSerializer):
    owner = AuthorSerializer(read_only=True)
    class Meta:
        model = Post
        fields = [
                'id', 'owner', 'title', 'body',
                'published', 'published_at', 'created_at',
                'updated_at', 'slug'
            ]
        lookup_field = 'slug'
