from rest_framework import serializers
from django.contrib.auth.models import User

from blog.models import Post


class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(many=True, view_name='post-detail', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'posts', 'liked_posts']


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )
        return user

    class Meta:
        model = User
        fields = ["id", "username", "password"]


class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ['id', 'url', 'title', 'text', 'author', 'created_at', 'updated_at', 'like_count', 'liked_by']


class LikeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'url']

    def update(self, instance, user):
        if instance.liked_by.filter(id=user.id).exists():
            instance.liked_by.remove(user)
        else:
            instance.liked_by.add(user)
        instance.save()
