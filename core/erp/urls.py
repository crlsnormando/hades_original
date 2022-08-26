from django.urls import path, include
from.view.views import CategoryCreateView, CategoryListView

app_name = 'erp'

urlpatterns = [
    path('category/list', CategoryListView.as_view(), name='category_list' ),
    path('category/add', CategoryCreateView.as_view(), name='category_create' ),
   
]
