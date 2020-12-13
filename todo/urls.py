from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('<int:list_id>', views.detail, name= 'detail'),
    path('deleteList/<int:list_id>', views.deleteList, name= 'deleteList'),
    path('deleteItem/<int:item_id>', views.deleteItem, name= 'deleteItem'),
]