from django.db import models

# Create your models here.

class Book(models.Model):
	title = models.CharField(max_length=200)
	author = models.CharField(max_length=300)
	publisher = models.CharField(max_length=200)
	pub_date = models.DateTimeField()
	ISBN_num = models.CharField(max_length=10)
	#in_stock = models.BooleanField()
class book-review(models.Model):
	book = models.ForeignKey(Book, on_delete=models.CASCADE)
	rating = models.IntegerField()
	reviews = models.CharField(max_length=500)
	reviewer_name = models.CharField(max_length=300)
	rev_date = models.DateTimeField()
class inventory(models.Model):
	book = models.ForeignKey(Book, on_delete=models.CASCADE)
	stock = models.IntegerField()	
