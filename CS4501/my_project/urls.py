from django.conf.urls import url
from . import views


urlpatterns = [url(r'^createUser/', views.createUser),
               url(r'^createBook/', views.createBook),
               url(r'^user_display/(?P<user_id>[\w|\W]+)/$', views.viewUser),
               url(r'^book_display/(?P<book_id>[\w|\W]+)/$', views.viewBook),
               url(r'^user_display/', views.allUsers),
               url(r'^book_display/', views.allBooks),
               url(r'^removeUser/(?P<user_id>[\w|\W]+)/$', views.removeUser),
               url(r'^removeBook/(?P<book_id>[\w|\W]+)/$', views.removeBook),
               url(r'^recently_published/', views.recentlyPublished),
               url(r'login/', views.login),
               url(r'authenticate/', views.authenticate),
               url(r'^logout/', views.logout),]
