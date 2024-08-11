from django.shortcuts import render
from django.views.generic import TemplateView,ListView,UpdateView,DeleteView,DetailView
from django.urls import reverse_lazy
from .models import Product
# Create your views here.
class TopView(TemplateView):
    template_name = "top.html"

class ProductListView(ListView):
    model = Product
    template_name = "product_list.html"
    paginate_by = 3

class ProductUpdateView(UpdateView):
     model = Product
     fields = '__all__'
     template_name_suffix = '_update_form'

class ProductDeleteView(DeleteView):
     model = Product
     success_url = reverse_lazy('list')

class ProductDetailView(DetailView):
  model = Product
  template_name = "product_detail.html"