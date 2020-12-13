from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import List,ListItem
from django.contrib import messages

# Create your views here.

@login_required(login_url="login")
def index(request):
    if request.method == 'POST': 
        listName = request.POST['listName'] 
        tlist = List(name=listName,user=request.user)
        tlist.save()
        messages.add_message(request,messages.SUCCESS,'Created New List.')
        return redirect('index')
    else:
        lists = List.objects.filter(user=request.user)
        return render(request,'index.html',{"lists": lists})
    
@login_required(login_url="login") 
def detail(request,list_id):
    items = ListItem.objects.filter(tList=list_id)
    title = List.objects.filter(pk=list_id).first().name
    return render(request,'detail.html',{"items": items,"title":title})