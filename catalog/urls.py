from django.conf.urls import url, re_path
from django.urls import path
from .views import product_list, category

urlpatterns = [
    path('', product_list, name='product_list'),
    re_path(r'^(?P<slug>[\w_-]+)/$', category, name='category')
]