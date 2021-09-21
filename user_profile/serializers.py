from rest_framework import serializers
from user_profile import Profile
from django.contrib.auth.models import User

class ProfileSerializer(serializers.Serializer):
    owner = serializers.PrimaryKeyRelatedField(User)

    class Meta:
        model = Profile
        fields = [
            'id', 'first_name', 'last_name'
        ]

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(many=False, queryset=Profile.objects.all())
    class Meta:
        model = User
        fields = ['id', 'email', 'profile']
    