from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#from catalog.models import Category

from .forms import ContactForm


def index(request):
    #texts = ['Testando o django', 'Vamos com tudo', 'Deus nos abençõe']
    context = {
        'title': 'django e-commerce',
        #'categories': Category.objects.all()
        #'texts': texts
    }
    return render(request, 'index.html', context)


def contact(request):
    if (request.method == 'POST'):
        form = ContactForm(request.POST)
    else:
        form = ContactForm()
    context = {
        'form': form
    }
    return render(request, 'contact.html', context)

# def product_list(request):
#     return render(request, 'product_list.html')

# def product(request):
#     return render(request, 'product.html')
