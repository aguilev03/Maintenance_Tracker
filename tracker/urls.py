from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.track_list, name='track_list'),
]
