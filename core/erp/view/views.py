from ast import Try
from email import contentmanager
from multiprocessing import context
from django.views.generic import ListView, CreateView, UpdateView
from django.shortcuts import render
from core.erp.forms import CategoryForm
from core.erp.models import Category
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy

def category_list(request):

    data = { 'title': 'Listando Categorias', 'category': Category.objects.all() }
  
    return render(request, 'category/list.html', data)


class CategoryListView(ListView):
    model = Category
    template_name = 'category/list.html'
    context_object_name = 'category'

# utilizado para recuperar o get e o post antes de iniciar o o get e post
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
        context['create_url'] = reverse_lazy('erp:category_create')
        context['list_url'] = reverse_lazy('erp:category_list')
        context['entity'] = "Categorias"
        return context

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/create.html'
    success_url = reverse_lazy('erp:category_list')

    def post(self, request, *args, **kwargs):
        data={}
        try:
            action = request.POST['action']
            if action == 'add':
                #form = CategoryForm(request.POST) uma forma de obter o formulario
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'Não há nenhum opção'
            #data = Category.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)


    # def post(self, request, *args, **kwargs):
    #     print(request.POST)
    #     form = CategoryForm(request.POST)
    #     print(dir(form))

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['title'] = 'Formulario Categorias'
        context['list_url'] = reverse_lazy('erp:category_list')
        context['entity'] = "Categorias"
        context['action'] = "add"

        return context

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/create.html'
    success_url = reverse_lazy('erp:category_list')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)
    

    def post(self, request, *args, **kwargs):
        data={}
        try:
            action = request.POST['action']
            if action == 'edit':
                #form = CategoryForm(request.POST) uma forma de obter o formulario
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'Não há nenhum opção'
            #data = Category.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['title'] = 'Edição Categorias'
        context['list_url'] = reverse_lazy('erp:category_list')
        context['entity'] = "Categorias"
        context['action'] = "edit"

        return context