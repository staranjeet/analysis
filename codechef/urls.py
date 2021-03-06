from django.conf.urls import patterns, include, url
from django.contrib import admin
from codechef import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^campus','codechef.views.campus',name='campus'),
    url(r'^analysis/$','codechef.views.analysis',name='analysis'),
    # url(r'^details/','codechef.views.updateProblems',name='updateProblems'),
    url(r'^checkprogress','codechef.views.userDetails',name='userDetails'),
    # url(r'^fetchusers','codechef.views.userList',name='userList'),
    url(r'^friends','codechef.views.addFriends',name='addFriends'),
    url(r'^getChapterList','codechef.views.getChapterList',name='getChapterList'),
    url(r'^chapter','codechef.views.chapter',name='chapter'),
    url(r'^up','codechef.views.updateProblems',name='updateProblems'),
)
