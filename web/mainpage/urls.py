from django.conf.urls import url
from . import views


urlpatterns = [ url(r'^book_display/(?P<book_id>[\w|\W]+)/$', views.bookView),
                url(r'^home/', views.homePage),
                url(r'^login/', views.login),
                url(r'^logout/', views.logout),
                url(r'^create_user/', views.create_user),
                url(r'^create_book_listing', views.create_book_listing),]
