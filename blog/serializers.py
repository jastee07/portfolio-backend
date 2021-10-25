from rest_framework import serializers
from blog.models import Post, Tag, Category
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'first_name', 'last_name'
        ]

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            'id', 'name'
        ]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id', 'name'
        ]

class PostSerializer(serializers.ModelSerializer):
    owner = AuthorSerializer(read_only=True)
    slug = serializers.SerializerMethodField(method_name='get_slug')
    categories = CategorySerializer(many=True, required=False)
    tags = TagSerializer(many=True, required=False)
    class Meta:
        model = Post
        fields = [
                'id', 'owner', 'title', 'body',
                'published', 'published_at', 'created_at',
                'updated_at', 'slug', 'categories', 'tags'
            ]
        lookup_field = 'slug'

    def get_slug(self, obj):
        return slugify(obj.title)
