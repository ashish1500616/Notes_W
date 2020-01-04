from django.conf.urls import url
from django.urls import re_path
# from django.urls import path
from . import views

app_name = "notes_app"
urlpatterns = [
    url(r'^$', views.home, name='home'),
]
