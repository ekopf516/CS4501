from django.conf.urls import url
from my_project import views
from . import views
from .views import *

index = [url(r'^$', views.index),]

book = [url(r'book/sale/(?P<book_id>[0-9]+)', BookSellView.as_view()),
       url(r'book/buy/(?P<book_id>[0-9]+)', BookBuyView.as_view()),
       url(r'user/seller/(?P<user_id>[0-9]+)', SellerView.as_view()),
       url(r'user/buyer/(?P<user_id>[0-9]+)', BuyerView.as_view()),
       url(r'create/user/seller', SellerView.as_view()),
       url(r'create/user/buyer', BuyerView.as_view()),
       ]

urlpatterns = index + car
