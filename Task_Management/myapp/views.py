from django.shortcuts import render,redirect
from .models import Task,TaskRestore,About
from .forms import Aboutform
# Create your views here.

def home(request):
    read=Task.objects.all()
    b={'read':read}
    return render(request,'home.html',b)

def create(request):
    if request.method=='POST':
        title=request.POST['title']
        desc=request.POST['desc']
        Task.objects.create(title=title,desc=desc)
        return redirect('home')
    return render(request,'create.html')

def dele(request,id):
    d=Task.objects.get(id=id)
    t=TaskRestore.objects.create(title=d.title,desc=d.desc)
    t.save()
    d.delete()
    return redirect('home')

def history(request):
    b=TaskRestore.objects.all()
    d={'b':b}
    return render(request,'history.html',d)

def upd(request,id):
    s=Task.objects.get(id=id)
    if request.method=='POST':
        s.title=request.POST['title']
        s.desc=request.POST['desc']
        #Task.objects.create(title=s.title,desc=s.desc)
        s.save()
        return redirect('home')
    d={'k':s}
    return render(request,'create.html',d)
def restore(request,id):
    b=TaskRestore.objects.get(id=id)
    a=Task.objects.create(title=b.title,desc=b.desc)
    b.delete()
    a.save()
    return redirect('history')
def dele_restore(request,id):
    b=TaskRestore.objects.get(id=id)
    b.delete()
    return redirect('history')
def restore_all(request):
    b=TaskRestore.objects.all()
    for i in b:
        title=i.title
        desc=i.desc
        a=Task.objects.create(title=title,desc=desc)
        a.save()
    b.delete()
    return redirect('history')

def deleteall(request):
    b=TaskRestore.objects.all()
    b.delete()
    return redirect('history')

def about(request):
    
    return render(request,'about.html')