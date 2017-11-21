from django.conf.urls import url

from . import views

app_name = "blogs"
urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^$', views.ArchiveView.as_view(), name='archive'),
    url(r'^(?P<pk>[0-9]+)/$', views.ArticleView.as_view(), name='article'),
    url(r'^(?P<blog_id>[0-9]+)/comments/$', views.postComment, name='comments'),
  
]