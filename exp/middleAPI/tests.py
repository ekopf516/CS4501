from django.test import TestCase, Client
import json
from middleAPI.models import *

# Create your tests here.
class GetDetailsTestCase(TestCase):
    fixtures = ['db.json']

    def setUp(self):
        pass

    def test_foundAllBooks(self):
        c = Client()
        response = c.get('^book_display/')
        result = response.content.decode('utf-8')
        result = json.loads(result)
        correct = {"status": true, "resp": {"match": [{"pub_date": "2017-02-27", "isbn_num": "9737223329", "publisher": "TKE", "author": "Moose", "price": 25, "title": "Goats: a how to", "id": 1}, {"pub_date": "1212-12-12", "isbn_num": "1235555", "publisher": "old stuff ince", "author": "old guy", "price": 70, "title": "Hydrating the Goats", "id": 2}, {"pub_date": "1220-12-12", "isbn_num": "1236666", "publisher": "old stuff inc", "author": "old guy", "price": 70, "title": "Goat training; a 9 week process", "id": 3}, {"pub_date": "1995-09-14", "isbn_num": "1212121212", "publisher": "the wicked cool people company", "author": "John Marshall", "price": 2000, "title": "John's Life; living like john", "id": 4}, {"pub_date": "2017-02-28", "isbn_num": "703346444", "publisher": "Tke", "author": "Moose", "price": 2000, "title": "Goat; a survival guide", "id": 5}, {"pub_date": "2017-01-05", "isbn_num": "667500504", "publisher": "sic! stuff books", "author": "John Marshall", "price": 80, "title": "The college kids guide to alcoholism", "id": 6}]}}
        self.assertEquals(result, correct)
    
    
    def test_foundAllUsers(self):
        c = Client()
        response = c.get('^user_display/')
        result = response.content.decode('utf-8')
        result = json.loads(result)
        correct = {"status": true, "resp": {"match": [{"id": 1, "first_name": "John", "user_name": "johnmars", "last_name": "Marshall", "password": "wickedwicked!!"}, {"id": 2, "first_name": "aaron", "user_name": "AA ron", "last_name": "aguhob", "password": "ISA........."}, {"id": 3, "first_name": "emma", "user_name": "M ah", "last_name": "kopf", "password": "more cs"}, {"id": 4, "first_name": "iantheta", "user_name": "ian123", "last_name": "zhang", "password": "123456"}, {"id": 5, "first_name": "billy joe", "user_name": "cowboy", "last_name": "howdy", "password": "yee haha"}, {"id": 6, "first_name": "lamar", "user_name": "my real name", "last_name": "pinckney", "password": "deep down"}]}}
        self.assertEquals(result, correct)


    def test_recentlyPublished(self):
        c = Client()
        response = c.get('^recently_published/')
        result = response.content.decode('utf-8')
        result = json.loads(result)
        correct = {"status": true, "resp": {"match": [{"pub_date": "2017-02-27", "isbn_num": "9737223329", "publisher": "TKE", "author": "Moose", "price": 25, "title": "Goats: a how to", "id": 1}, {"pub_date": "2017-02-28", "isbn_num": "703346444", "publisher": "Tke", "author": "Moose", "price": 2000, "title": "Goat; a survival guide", "id": 5}, {"pub_date": "2017-01-05", "isbn_num": "667500504", "publisher": "sic! stuff books", "author": "John Marshall", "price": 80, "title": "The college kids guide to alcoholism", "id": 6}]}}
        self.assertEquals(result, correct)


class bookCreateTest(TestCase):
    fixtures = ['db.json']
    
    def setUp(self):
        pass
    
    
    def test_bookCreate(self):
        c = Client()
        post = {'title': "Internet Scale Applications", 'author': "Emma Kopf", 'publisher': "University of Virginia", 'pub_date': "1996-05-16T00:00:00Z", 'isbn_num': "987654321", 'price':30}
        response = c.post('^createBook', json.dumps(post), 'json')
        result = response.content.decode('utf-8')
        result = json.loads(result)
        correct = {'status': True, 'resp' : 'book has been created.'}
        self.assertEquals(result, correct)
    
    
    def tearDown(self):
        pass


class userCreateTest(TestCase):
    fixtures = ['db.json']
    
    def setUp(self):
        pass
    
    
    def test_userCreate(self):
        c = Client()
        post = {'first_name': "Bob", 'last_name': "Johnson", 'user_name': "bobjohnson", 'password': "temp1234"}
        response = c.post('^createUser', json.dumps(post), 'json')
        result = response.content.decode('utf-8')
        result = json.loads(result)
        correct = {'status': True, 'resp': 'user has been created.'}
        self.assertEquals(result, correct)
    
    
    def tearDown(self):
        pass


class bookDeleteTest(TestCase):
    fixtures = ['db.json']
    
    def setUp(self):
        pass
    
    
    # remove a book that exists
    def test_removeBookFound(self):
        c = Client()
        response = c.get('^removeBook/1/')
        result = response.content.decode('utf-8')
        result = json.loads(result)
        correct = {'status': True, 'resp': 'Book Deleted'}
        self.assertEquals(result, correct)
    
    
    # remove a book that doesn't exist
    def test_removeBookNotFound(self):
        c = Client()
        response = c.get('^removeBook/8/')
        result = response.content.decode('utf-8')
        result = json.loads(result)
        correct = {'status': False, 'resp': 'Book Not Found'}
        self.assertEquals(result, correct)
    
    
    def tearDown(self):
        pass


class userDeleteTest(TestCase):
    fixtures = ['db.json']
    
    def setUp(self):
        pass
    
    
    # test removing a user that exists
    def test_removeUserFound(self):
        c = Client()
        response = c.get('^removeUser/3/')
        result = response.content.decode('utf-8')
        result = json.loads(result)
        correct = {'status': True, 'resp': 'User Deleted'}
        self.assertEquals(result, correct)
    
    
    # test removing a user that does not exist
    def test_removeUserNotFound(self):
        c = Client()
        response = c.get('/^removeUser/29/')
        result = response.content.decode('utf-8')
        result = json.loads(result)
        correct = {'status': False, 'resp': 'User Not Found'}
        self.assertEquals(result, correct)
    
    
    def tearDown(self):
        pass

