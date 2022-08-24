from ast import Try
from multiprocessing import context
from django.views.generic import ListView
from django.shortcuts import render
from core.erp.models import Category
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def category_list(request):

    data = { 'title': 'Listando Categorias', 'category': Category.objects.all() }
  
    return render(request, 'category/list.html', data)


class CategoryListView(ListView):
    model = Category
    template_name = 'category/list.html'
    context_object_name = 'category'

# utilizado para recuperar o get e o post
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        if request.method == 'GET':
            print(request)
        return super().dispatch(request, *args, **kwargs)

    
    def post(self, request, *args, **kwargs):

        data = {}

        try:
            data = Category.objects.get(pk=request.POST['id']).toJson()
          
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

  

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['title'] = 'Listando Categorias'
        return context