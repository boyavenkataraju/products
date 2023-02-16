from django.shortcuts import render
from application2.forms import EmployeesForm,RegistrationForm
from application2.models import Employees,Registration

def Test_case1(request):
    return render(request,"application2/main_page.html")

def Test_case2(request):
    form=RegistrationForm()
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    context1={'form':form}
    return render(request,"application2/Registration.html",context1)

def Test_case3(request):
    return render(request,"application2/Login_form.html")

def Test_case4(request):
    form=EmployeesForm()
    if request.method=="POST":
        form=EmployeesForm(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,"application2/Information.html",context)

def Test_case5(request):
    data=Registration.objects.all()
    return render(request,"application2/Registerinfo.html",{'data':data})
    
def Test_case6(request):
    data=Employees.objects.all()
    return render(request,"application2/get_information.html",{'data':data})



