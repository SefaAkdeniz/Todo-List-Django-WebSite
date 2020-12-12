from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import List,ListItem

# Create your views here.

@login_required(login_url="login")
def index(request):
    lists = List.objects.filter(user=request.user)
    return render(request,'index.html',{"lists": lists})
    
@login_required(login_url="login") 
def detail(request,list_id):
    items = ListItem.objects.filter(tList=list_id)
    title = List.objects.filter(pk=list_id).first().name
    return render(request,'detail.html',{"items": items,"title":title})