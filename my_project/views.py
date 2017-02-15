from django.http import JsonResponse
from .forms import UserForm, BookForm
from .models import user, book
from django.shortcuts import render
import json

# Create your views here.
def index(request):
    return render(request, 'index.html', context=None)

def UserView(request):
    users = user.objects.all()
    UserIDs = []
    for usr in users:
        if (usr.id not in UserIDs):
            UserIDs.append(usr.id)
    return render(request, 'user_display.html', {'Users': UserIDs})

def viewUser(request, user_id):
    if user.objects.filter(id = user_id):
        theUser = user.objects.filter(id = user_id)
        theUser = theUser.get()
        json = {}
        json ['username'] = theUser.user_name
        json ['first name'] = theUser.first_name
        json ['last name'] = theUser.last_name
        json ['password'] = theUser.password
        json ['ID'] = theUser.id
        return JsonResponse(json)
    else:
        return JsonResponse({
                            "status":"error",
                            "message": "No user was found with that ID",
                            "data": None
                            })


def BookView(request):
    books = book.objects.all()
    BookIDs = []
    for bk in books:
        if (bk.id not in BookIDs):
            BookIDs.append(bk.id)
    return render(request, 'book_display.html', {'Books': BookIDs})

def viewBook(request, book_id):
    if book.objects.filter(id = book_id):
        theBook = book.objects.filter(id = book_id)
        theBook = theBook.get()
        json = {}
        json['title'] = theBook.title
        json['author'] = theBook.author
        json['publisher'] = theBook.publisher
        json['publication date'] = theBook.pub_date
        json['isbn'] = theBook.isbn_num
        json['price'] = theBook.price
        json['ID'] = theBook.id
        return JsonResponse(json)
    else:
        return JsonResponse({
                            "status":"error",
                            "message":"No book was found with that ID",
                            "data": None
                            })

def createUser(request):
    if request.method == "POST":
        form = UserForm(data=request.POST)
        if(form.is_valid()):
            userName = UserForm.userName_clean(form)
            firstName = UserForm.firstName_clean(form)
            lastName = UserForm.lastName_clean(form)
            password = UserForm.password_clean(form)
            p = user(user_name=userName, first_name=firstName, last_name=lastName, password=password)
            p.save()
            return render(request, 'index.html',{'message': "Account Created!!\n"})
        else: return render(request, 'createUser.html', {'form':form})
    form = UserForm()
    return render(request, 'createUser.html', {'form':form})


def createBook(request):
    if request.method == "POST":
        form = BookForm(data=request.POST)
        if(form.is_valid()):
            author = BookForm.author_clean(form)
            title = BookForm.title_clean(form)
            pub = BookForm.publisher_clean(form)
            pub_date = BookForm.date_clean(form)
            price = BookForm.price_clean(form)
            isbn = BookForm.isbn_clean(form)
            b = book(isbn_num=isbn, author=author, title=title, pub_date=pub_date, publisher=pub, price=price)
            b.save()
            return render(request, 'index.html',{'message': "Book Created!!\n"})
        else: return render(request, 'createBook.html', {'form':form})
    form = BookForm()
    return render(request, 'createBook.html', {'form':form})


def removeUser(request, user_id):
    if user.objects.filter(id = user_id):
        theUser = user.objects.filter(id = user_id)
        theUser = theUser.get()
        theUser.delete()
        response_data = {}
        response_data['result'] = '200'
        response_data['message'] = 'Succesfully removed user'
        return JsonResponse(response_data, safe = False)
    else:
        response_data = {}
        response_data['result'] = '404'
        response_data['message'] = "Not Found: user item not found"
        return JsonResponse(response_data, safe = False)


def removeBook(request, book_id):
    if book.objects.filter(id = book_id):
        theBook = book.objects.filter(id = book_id)
        theBook = theBook.get()
        theBook.delete()
        response_data = {}
        response_data['result'] = '200'
        response_data['message'] = 'Succesfully removed book'
        return JsonResponse(response_data, safe = False)
    else:
        response_data = {}
        response_data['result'] = '404'
        response_data['message'] = "Not Found: book item not found"
        return JsonResponse(response_data, safe = False)


#class BookSellView(ListView):
#    model = book
#    def get(self, request, *args, **kwargs):
#        book = get_object_or_404(book, pk = kwargs['book-id'])
#        book = model_to_dict(book)
#        return JsonResponse({ model_name : data_dict })
#    def post(self, request, *args, **kwargs):
#        data = request.body.decode('utf-8')
#        data_dict = json.loads(data)
#        form = BookForm(data_dict)
#        return HttpResponse('Good')
#
#
#class BookBuyView(ListView):
#    model = book
#    def get(self, request, *args, **kwargs):
#        book = get_object_or_404(book, pk = kwargs['book-id'])
#        book = model_to_dict(book)
#        return JsonResponse({ model_name : data_dict })
#    def post(self, request, *args, **kwargs):
#        data = request.body.decode('utf-8')
#        data_dict = json.loads(data)
#        #put this in John's views file
#        form = BookForm(data_dict)
#        #is_valid method to check if form valid before making database changes
#        if form.is_valid() :
#            if int(kwargs['book_id']) in sel.objects.values_list('pk', flat = True) :
#                return self.update(kwards['book_id'], data_dict)
#            form.save()
#        return HttpResponse('Good')
#
#
#class SellerView(ListView):
#    model = seller
#    def get(self, request, *args, **kwargs):
#        book = get_object_or_404(seller, pk = kwargs['book-id'])
#        book = model_to_dict(book)
#        return JsonResponse({ model_name : data_dict })
#    def post(self, request, *args, **kwargs):
#        data = request.body.decode('utf-8')
#        data_dict = json.loads(data)
#
#
#class BuyerView(ListView):
#    model = buyer
#    def get(self, request, *args, **kwargs):
#        book = get_object_or_404(buyer, pk = kwargs['book-id'])
#        book = model_to_dict(book)
#        return JsonResponse({ model_name : data_dict })
#    def post(self, request, *args, **kwargs):
#        data = request.body.decode('utf-8')
#        data_dict = json.loads(data)
