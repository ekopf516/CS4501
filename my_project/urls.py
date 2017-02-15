from django.conf.urls import url
from my_project import views
from . import views
from .views import *

index = [url(r'^$', views.index),]

book = [#url(r'book/sale/(?P<book_id>[0-9]+)', BookSellView.as_view()),
        #url(r'book/buy/(?P<book_id>[0-9]+)', BookBuyView.as_view()),
        #url(r'user/seller/(?P<user_id>[0-9]+)', SellerView.as_view()),
        #url(r'user/buyer/(?P<user_id>[0-9]+)', BuyerView.as_view()),
        #url(r'book/add/$', views.BookCreate.as_view(), name='add-book'),
        #url(r'create/user/seller', SellerView.as_view()),
        #url(r'create/user/buyer', BuyerView.as_view()),
       ]
views = [url(r'^createUser/', views.createUser),
         url(r'^user_display/(?P<user_id>[\w|\W]+)/$', views.viewUser),
         url(r'^user_display/', views.UserView),
         #url(r'^user_display/(?P<user>[\w|\W]+)/$', views.viewUser),
         url(r'^book_display/(?P<book_id>[\w|\W]+)/$', views.viewBook),
         url(r'^book_display/', views.BookView),
         #url(r'^book_display/(?P<book_id>[\w|\W]+)/$', views.viewBook),
         url(r'^createBook/', views.createBook)]
#user = [url(r'user/add/$', views.UserCreate.as_view(), name='add-user'),
# ]
urlpatterns = index + book + views