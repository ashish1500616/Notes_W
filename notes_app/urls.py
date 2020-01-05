from django.conf.urls import url
from django.urls import re_path
from django.urls import path
from . import views

app_name = "notes_app"
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^edit/(?P<id>\d+)/$',views.edit,name="edit_note"),
    # url(r'^update/(?P<id>\d+)/$',views.edit,name="update_note"),
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),  
    url(r'^delete/(?P<id>\d+)/',views.edit,name="delete_note"),
]
