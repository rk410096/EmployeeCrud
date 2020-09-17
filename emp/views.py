from django.shortcuts import render,redirect
from emp.models import *
from emp.forms import *
# Create your views here.
def save(request):
    if request.method=='POST':
        eform=employeeform(request.POST)
        if eform.is_valid():
            try:
                eform.save()
                return redirect('/show')
            except:
                pass
    else:
        eform=employeeform()
    return render(request,'index.html',{'frm':eform})
def show(request):
    edata=employee.objects.all()
    return render(request,'show.html',{'ed':edata})
def edit(request,id):
    frm=employee.objects.get(id=id)
    return render(request,'edit.html',{'em':frm})
def update(request,id):
    empl=employee.objects.get(id=id)
    form=employeeform(request.POST, instance=empl)
    if form.is_valid():
        form.save()
    return redirect('/show')
def remove(request,id):
    frm1=employee.objects.get(id=id)
    frm1.delete()
    return redirect('/show')
