from django.db import models

class book(models.Model):
    title = models.CharField(max_length = 200)
    author = models.CharField(max_length = 200)
    publisher = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')
    isbn_num = models.charField(max_length = 10)

class user(models.Model):
    first_name = models.CharField(max_length=20)
    last_name  = models.CharField(max_length=20)
    user_name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

class sell_book(book):
    price_to_sell = models.IntegerField(default=0)

class seller(user):
    book_to_sell = models.ManyToManyField(sell_book)

class buy_book(car):
    price_to_offer = models.IntegerField(default=0)

class buyer(user):
    book_to_buy = models.ManyToManyField(buy_book)

class inventory(book):

class book_review(book):
