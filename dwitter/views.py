from .models import Dweet, Comments, Follow
from .serializers import Dweetserializer, Commentserializer, Userserializer, FollowSerializer, LikeSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticatedOrReadOnly


# Create your views here.

class Lisdweets(generics.ListCreateAPIView, IsAuthenticatedOrReadOnly):
    serializer_class = Dweetserializer

    def get_queryset(self):
        username = self.kwargs['username']
        usernames = []
        following = Follow.objects.filter(target_owner__username__in=username).values_list('username', flat=True)
        usernames.append(username)
        for follower in following:
            usernames.append(follower)

        return Dweet.objects.filter(owner__username__in=usernames)


# class Dweetdetail(generics.RetrieveDestroyAPIView):
# serializer_class = Dweetserializer
# def get_queryset(self):
#   username = self.kwargs['username']
#  return Dweet.objects.filter(owner__username=username)


class DweetDetail(APIView):

    def get(self, request, pk, format=None):
        """

        :param request:
        :param pk:
        :param format:
        :return:
        """
        obj = Dweet.objects.get(pk=pk)
        serializer = Dweetserializer(obj)
        return Response(serializer.data)

    def put(self, request, pk):
        obj = Dweet.objects.get(pk=pk)
        serializer = Dweetserializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDweet(generics.ListCreateAPIView):
    serializer_class = Commentserializer
    queryset = Comments.objects.all()


# Class FollowDweet()

class Userlist(generics.ListCreateAPIView, IsAuthenticatedOrReadOnly):
    queryset = User.objects.all()
    serializer_class = Userserializer


class FollowDweeters(generics.ListCreateAPIView):
    serializer_class = FollowSerializer
    queryset = Follow.objects.all()


class LikeDweet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dweet.objects.all()
    serializer_class = LikeSerializer
