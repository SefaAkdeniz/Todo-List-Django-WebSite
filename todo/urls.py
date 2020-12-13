from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('<int:list_id>', views.detail, name= 'detail'),
    path('addList<int:list_id>', views.addList, name= 'addList'),
]