from django.conf.urls import url
from . import views


urlpatterns = [url(r'^createUser/', views.createUser),
               url(r'^createBook/', views.createBook),
               url(r'^user_display/(?P<user_id>[\w|\W]+)/$', views.viewUser),
               url(r'^removeUser/(?P<user_id>[\w|\W]+)/$', views.removeUser),
               url(r'^book_display/(?P<book_id>[\w|\W]+)/$', views.viewBook),
               url(r'^removeBook/(?P<book_id>[\w|\W]+)/$', views.removeBook),]
