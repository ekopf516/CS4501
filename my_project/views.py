from django.shortcuts import render
from django.views.generic import TemplateView

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


class BookBuyView(ListView):

class SellerView(ListView):

class BuyerView(ListView):



class CarSellView(ListView):
    model = car_to_sell
    
    def get(self, request, *args, **kwargs):
        car = get_object_or_404(car_to_sell, pk=kwargs['car_id'])
        car = model_to_dict(car)
        return _success(car, 'car_to_sell', 200)
    
    def post(self, request, *args, **kwargs):
        def post(self, request, *args, **kwargs):
            data = request.body.decode('utf-8')
            data_dict = json.loads(data)
            form = CarSellForm(data_dict)
            if form.is_valid() :
                form.save()
                return HttpResponse('Success')
            else :
                return HttpResponse('Bad Post Request')
