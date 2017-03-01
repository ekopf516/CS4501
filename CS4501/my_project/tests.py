from django.test import TestCase, Client
import json
from my_project.models import *

# Create your tests here.
class GetDetailsTestCase(TestCase):
    fixtures = ['db.json']
    
    def setUp(self):
        pass
    
    # retrieving an existing book
    def test_foundBook(self):
        c = Client()
        response = c.get('^book_display/1')
        result = response.content.decode('utf-8')
        result = json.loads(result)
        correct = {'status':True, 'resp':{"title": "Goats: a how to", "author": "Moose", "publisher": "TKE", "pub_date": "2017-02-27T00:00:00Z", "isbn_num": "9737223329", "price": 25}}
        self.assertEquals(result, correct)
    
    
    # retrieving an existing user
    def test_foundUser(self):
        c = Client()
        response = c.get('^user_display/2')
        result = response.content.decode('utf-8')
        result = json.loads(result)
        correct = {'status':True, 'resp':{"first_name": "aaron", "last_name": "agohub", "user_name": "AA ron", "password": "ISA.........", "bag": []}}
        self.assertEquals(result, correct)
    
    
    # try retrieving a book that doesn't exist
    def test_bookNotFound(self):
        c = Client()
        response = c.get('^book_display/7')
        result = response.content.decode('utf-8')
        result = json.loads(result)
        correct = {'status': False, 'message': "No book was found with that ID", 'data': None}
        self.assertEquals(result, correct)
    
    
    # try retrieving a user that doesn't exist
    def test_userNotFound(self):
        c = Client()
        response = c.get('^user_display/9')
        result = response.content.decode('utf-8')
        result = json.loads(result)
        correct = {'status': False, 'message': "No user was found with that ID", 'data': None}
        self.assertEquals(result, correct)
    
    
    def tearDown(self):
        pass

# books: title, author, publisher, pub_date, isbn_num, price
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


# user : first_name, last_name, user_name, password
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
        response = c.get('^removeBook/1')
        result = response.content.decode('utf-8')
        result = json.loads(result)
        correct = {'status': True, 'resp': 'Book Deleted'}
        self.assertEquals(result, correct)
    
    
    # remove a book that doesn't exist
    def test_removeBookNotFound(self):
        c = Client()
        response = c.get('^removeBook/8')
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
        response = c.get('^removeUser/3')
        result = response.content.decode('utf-8')
        result = json.loads(result)
        correct = {'status': True, 'resp': 'User Deleted'}
        self.assertEquals(result, correct)
    
    
    # test removing a user that does not exist
    def test_removeUserNotFound(self):
        c = Client()
        response = c.get('/^removeUser/29')
        result = response.content.decode('utf-8')
        result = json.loads(result)
        correct = {'status': False, 'resp': 'User Not Found'}
        self.assertEquals(result, correct)
    
    
    def tearDown(self):
        pass
