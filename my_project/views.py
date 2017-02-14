from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404
from .forms import UserForm, BookForm
import json

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

class BookSellView(ListView):
    model = book
    def get(self, request, *args, **kwargs):
        book = get_object_or_404(book, pk = kwargs['book-id'])
        book = model_to_dict(book)
        return JsonResponse(model_name : data_dict)
    def post(self, request, *args, **kwargs):
        data = request.body.decode('utf-8')
        data_dict = json.loads(data)
        form = BookForm(data_dict)
        return HttpResponse('Good')


class BookBuyView(ListView):
    model = book
    def get(self, request, *args, **kwargs):
        book = get_object_or_404(book, pk = kwargs['book-id'])
        book = model_to_dict(book)
        return JsonResponse(model_name : data_dict)
    def post(self, request, *args, **kwargs):
        data = request.body.decode('utf-8')
        data_dict = json.loads(data)
        #put this in John's views file
        form = BookForm(data_dict)
        #is_valid method to check if form valid before making database changes
        if form.is_valid() :
            if int(kwargs['book_id']) in sel.objects.values_list('pk', flat = True) :
                return self.update(kwards['book_id'], data_dict)
            form.save()
        return HttpResponse('Good')


class SellerView(ListView):
    model = seller
    def get(self, request, *args, **kwargs):
        book = get_object_or_404(seller, pk = kwargs['book-id'])
        book = model_to_dict(book)
        return JsonResponse(model_name : data_dict)
    def post(self, request, *args, **kwargs):
        data = request.body.decode('utf-8')
        data_dict = json.loads(data)


class BuyerView(ListView):
    model = buyer
    def get(self, request, *args, **kwargs):
        book = get_object_or_404(buyer, pk = kwargs['book-id'])
        book = model_to_dict(book)
        return JsonResponse(model_name : data_dict)
    def post(self, request, *args, **kwargs):
        data = request.body.decode('utf-8')
        data_dict = json.loads(data)
