from django.conf.urls import url
from . import views


urlpatterns = [ url(r'^book_display/(?P<book_id>[\w|\W]+)/$', views.bookView),
                url(r'^book_display/', views.recentlyPublished),]
