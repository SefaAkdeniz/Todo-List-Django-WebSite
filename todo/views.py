from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import List,ListItem

# Create your views here.

@login_required(login_url="login")
def index(request):
    lists = List.objects.filter(user=request.user)
    return render(request,'index.html',{"lists": lists})
    
