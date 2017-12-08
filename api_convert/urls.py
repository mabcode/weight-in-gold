from django.conf.urls import url

from . import views

app_name = "weightInGold"
urlpatterns = [

    # /weightInGold/weightAPI?n=[some non-negative number]
    url(r'^weightAPI$', views.weightAPI, name='weightAPI'),

]