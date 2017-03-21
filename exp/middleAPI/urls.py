from django.conf.urls import url
from . import views


urlpatterns = [url(r'^user_display/(?P<user_id>[\w|\W]+)/$', views.userInfo),
               url(r'^book_display/(?P<book_id>[\w|\W]+)/$', views.bookInfo),
               url(r'^home_page/', views.homepage),
               url(r'^book_display/', views.allBooks),]
