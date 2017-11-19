from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.Blog.as_view(), name='index'),
  
]