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
    return render(request,'detail.html',{"items": items,"title":title,"list_id":list_id})

@login_required(login_url="login") 
def deleteList(request,list_id):
    List.objects.filter(pk=list_id).delete()
    messages.add_message(request,messages.SUCCESS,'Deleted List.')
    return redirect('index')

@login_required(login_url="login") 
def deleteItem(request,item_id):
    if request.method == 'POST': 
        listId = request.POST['listId']
        ListItem.objects.filter(pk=item_id).delete()
        messages.add_message(request,messages.SUCCESS,'Deleted Item.')
        return redirect('/'+str(listId))

@login_required(login_url="login") 
def changeStatus(request,item_id):
    try:
        if request.method == 'POST': 
            listId = request.POST['listId']
            ListItem.objects.filter(pk=item_id).update(status=True)
            messages.add_message(request,messages.SUCCESS,'Change Status.')
            return redirect('/'+str(listId))
    except:
        return('index')