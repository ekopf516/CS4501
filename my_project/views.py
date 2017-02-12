from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404

import json

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

class BookSellView(ListView):
    model = sell_book
    def get(self, request, *args, **kwargs):
        book = get_object_or_404(sell_book, pk = kwargs['book-id'])
        book = model_to_dict(book)
        return JsonResponse(model_name : data_dict)
    def post(self, request, *args, **kwargs):
        data = request.body.decode('utf-8')
        data_dict = json.loads(data)
        return HttpResponse('Good')


class BookBuyView(ListView):
    model = buy_book
    def get(self, request, *args, **kwargs):
        book = get_object_or_404(buy_book, pk = kwargs['book-id'])
        book = model_to_dict(book)
        return JsonResponse(model_name : data_dict)
    def post(self, request, *args, **kwargs):
        data = request.body.decode('utf-8')
        data_dict = json.loads(data)
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
