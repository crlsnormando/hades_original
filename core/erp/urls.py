from django.urls import path, include
from.view.views import category_list, CategoryListView

app_name = 'erp'

urlpatterns = [
    path('category/list', CategoryListView.as_view(), name='category_list' ),
   
]
