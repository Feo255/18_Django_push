from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def index(request):
    return render(request, 'index.html')

class Shop(TemplateView):
    template_name = 'shop.html'

class Box(TemplateView):
    template_name = 'box.html'