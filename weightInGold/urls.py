from django.conf.urls import url

from . import views

app_name = "weightInGold"
urlpatterns = [
	# /weightInGold/
    url(r'^$', views.index, name='index'),
]