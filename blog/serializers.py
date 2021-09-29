from rest_framework import serializers
from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = [
                'id', 'owner', 'title', 'body',
                'published', 'published_at', 'created_at',
                'updated_at', 'slug'
            ]
        lookup_field = 'slug'
