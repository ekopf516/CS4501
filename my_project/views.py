from django.http import JsonResponse
from .forms import UserForm, BookForm
from .models import user, book

# Create your views here.
def index(request):
    return render(request, 'index.html', context=None)
def UserView(request):
    users = user.objects
    UserIDs = []
    for usr in users:
        if (usr.id not in UserIDs):
            UserIDs.append(usr.id)
    return render(request, 'user_display.html', {'Users': UserIDs})

def viewUser(request, user):
    theUser = user.objects.filter(id = user)
    theUser = theUser.get()
    json = {}
    json ['username'] = theUser.username
    json ['first name'] = theUser.first_name
    json ['last name'] = theUser.last_name
    json ['password'] = theUser.password
    json ['ID'] = theUser.id
    return JsonResponse(json)


def BookView(request):
    books = book.objects
    BookIDs = []
    for book in books:
        if (book.id not in BookIDs):
            BookIDs.append(book.id)
    return render(request, 'book_display.html', {'Books': BookIDs})

def viewBook(request, book):
    theBook = book.objects.filter(id=user)
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
