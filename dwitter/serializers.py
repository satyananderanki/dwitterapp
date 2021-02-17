from rest_framework import serializers
from .models import Dweet, Comments, Follow
from django.contrib.auth.models import User


class Dweetserializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Dweet
        fields = ['owner', 'content', 'likes']


class Userserializer(serializers.ModelSerializer):
    tweets = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('username', 'tweets')


class Commentserializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = "__all__"


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = "__all__"


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dweet
        fields = "__all__"
        read_only_fields = ("owner", 'content')
