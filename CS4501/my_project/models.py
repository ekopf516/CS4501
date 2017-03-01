from django.db import models

class book(models.Model):
    title = models.CharField(max_length = 200)
    author = models.CharField(max_length = 200)
    publisher = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')
    isbn_num = models.CharField(max_length = 10)
    price = models.IntegerField(default=0)

class user(models.Model):
    first_name = models.CharField(max_length=20)
    last_name  = models.CharField(max_length=20)
    user_name = models.CharField(max_length=30)
    password = models.CharField(max_length=30, default="password")
    bag = models.ManyToManyField(book, default=None)

#class seller(user):
#    book_to_sell = models.ManyToManyField(book)
#
#class buyer(user):
#    book_to_buy = models.ManyToManyField(book)

#class inventory(book):
#   book = models.ForeignKey(book, on_delete=models.CASCADE)
#   stock = models.IntegerField()

#class book_review(book):
#    book = models.ForeignKey(book, on_delete=models.CASCADE)
#   rating = models.IntegerField()
#   reviews = models.CharField(max_length=500)
#   reviewer_name = models.CharField(max_length=300)
#   rev_date = models.DateTimeField('date published')
