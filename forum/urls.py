from django.conf.urls import patterns, include, url
from forum import views

urlpatterns = patterns('',
    url(r'^tag/$', views.tag, name='tag'),
    url(r'^tag/(?P<id>\d+)/$', views.linktag, name='linktag'),
    url(r'^tag_search/$', views.tag_search, name='tag_search'),
    url(r'^tag/questions/(?P<id>\d+)/$', views.questions, name='questions'),
)
