from django.urls import path, re_path
from .views import Lisdweets, DweetDetail, CommentDweet, FollowDweeters, Userlist, LikeDweet

urlpatterns = [
    # path('dweet/<slug:slug>',Lisdweets.as_view())
    # path('dweet/<slug:username>',Lisdweets.as_view()),
    path('dweet/<int:pk>/', DweetDetail.as_view()),
    re_path('^dweet/(?P<username>.+)/$', Lisdweets.as_view()),
    path('comment/', CommentDweet.as_view()),
    path('like/<int:pk>/', LikeDweet.as_view()),
    path('follow/', FollowDweeters.as_view()),
    path('users/', Userlist.as_view())

    # re_path('^dweet/(?P<username>.+)/(?P<pk>\d+)/$', Dweetdetail.as_view()),

]
