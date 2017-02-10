from django.conf.urls import url
from my_project import views
from . import views
from .views import *

index = [url(r'^$', views.index),]

book = [
