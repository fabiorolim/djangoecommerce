from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#from catalog.models import Category


def index(request):
    #texts = ['Testando o django', 'Vamos com tudo', 'Deus nos abençõe']
    context = {
        'title': 'django e-commerce',
        #'categories': Category.objects.all()
        #'texts': texts
    }
    return render(request, 'index.html', context)


def contact(request):
    return render(request, 'contact.html')


# def product_list(request):
#     return render(request, 'product_list.html')


# def product(request):
#     return render(request, 'product.html')
