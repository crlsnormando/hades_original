from django.urls import path, include
from.view.views import CategoryCreateView, CategoryListView, CategoryUpdateView
app_name = 'erp'

urlpatterns = [
    path('category/list', CategoryListView.as_view(), name='category_list' ),
    path('category/add', CategoryCreateView.as_view(), name='category_create' ),
    path('category/adit/<int:pk>/', CategoryUpdateView.as_view(), name='category_edit' ),
   
]
