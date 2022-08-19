from multiprocessing import context
from django.views.generic import ListView
from django.shortcuts import render
from core.erp.models import Category

def category_list(request):

    data = { 'title': 'Listando Categorias', 'category': Category.objects.all() }
  
    return render(request, 'category/list.html', data)


class CategoryListView(ListView):
    model = Category
    template_name = 'category/list.html'
    context_object_name = 'category'

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'GET':
            print(request)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['title'] = 'Listando Categorias'
        return context