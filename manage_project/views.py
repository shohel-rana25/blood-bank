from django.shortcuts import render
from .models import Bloodlist
from .forms import BloodlistInfomation
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.db.models import Q

# Create your views here.

def home(request):
    bloodlist=Bloodlist.objects.all()
    return render(request, "home.html", {"bloodlist": bloodlist})

def list(request):
    bloodlist=Bloodlist.objects.all()
    return render(request, "list.html",{"bloodlist": bloodlist})



def A_pos(request):
    bloodlist=Bloodlist.objects.all()
    return render(request, "group/A_pos.html",{"bloodlist": bloodlist})

def A_neg(request):
    bloodlist=Bloodlist.objects.all()
    return render(request, "group/A_neg.html",{"bloodlist": bloodlist})

def AB_pos(request):
    bloodlist=Bloodlist.objects.all()
    return render(request, "group/AB_pos.html",{"bloodlist": bloodlist})

def AB_neg(request):
    bloodlist=Bloodlist.objects.all()
    return render(request, "group/AB_neg.html",{"bloodlist": bloodlist})

def B_pos(request):
    bloodlist=Bloodlist.objects.all()
    return render(request, "group/B_pos.html",{"bloodlist": bloodlist})


def B_neg(request):
    bloodlist=Bloodlist.objects.all()
    return render(request, "group/B_neg.html",{"bloodlist": bloodlist})

def O_pos(request):
    bloodlist=Bloodlist.objects.all()
    return render(request, "group/O_pos.html",{"bloodlist": bloodlist})


def O_neg(request):
    bloodlist=Bloodlist.objects.all()
    return render(request, "group/O_neg.html",{"bloodlist": bloodlist})

def Add_Donner(request):
    if request.method=="POST":
        fm=BloodlistInfomation(request.POST, request.FILES)
    
        if fm.is_valid():
            print(fm.cleaned_data)
            fm.save()
            return HttpResponseRedirect("/")
    else:
        fm=BloodlistInfomation()
    return render(request, "Add_Donner.html", {"form":fm})


    
def search(request):
    if request.method=="POST":
        search=request.POST.get("output")
        bloodlist=Bloodlist.objects.all()
        std=None
        if search:
            std=bloodlist.filter(
                Q(Name__icontains=search)|
                 Q(Phone__icontains=search)|
                  Q(Location__icontains=search)|
                   Q(Blood_Group__icontains=search)|
                    Q(Last_Donate__icontains=search))
        return render(request, "list.html",{"bloodlist":std})
    else:
        return HttpResponse("An Error")
