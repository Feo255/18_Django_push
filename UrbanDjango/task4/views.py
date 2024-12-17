from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def index(request):
    return render(request, 'index.html')

def shop(request):
    context = {'games':['Atomic Heart', 'Cyberpunk 2077']}
    return render(request, 'shop.html')

def box(request):
    return render(request, 'box.html')

