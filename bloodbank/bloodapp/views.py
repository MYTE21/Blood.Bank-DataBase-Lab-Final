from django.shortcuts import render, redirect
from bloodapp.forms import StaffForm
from bloodapp.models import Staff

def stf(request):
    if request.method == "POST":
        form = StaffForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/processConfirm")
            except:
                pass
    else:
        form = StaffForm()
    return render(request, "signup.html", {'form': form})

# def signup(request):
#     staffs = Staff.objects.all()
#     return render(request, "signup.html", {'staffs': staffs})

def login(request):
    return render(request, "login.html")

def index(request):
    return render(request, "index.html")

def processConfirm(request):
    return render(request, "processConfirm.html")

def loginConfirm(request, id):
    # staffs = Staff.objects.all()
    # for staff in staffs:
    #     if staff.id == id and staff.name == name:
    #         return render(request, "loginConfirm.html")

    staff = Staff.objects.get(staff_id=id)
    form = StaffForm(request.POST, instance=staff)
    if form.is_valid():
        return redirect('/index')
    else:
        pass
    return render(request, "loginConfirm.html", {'staff': staff})

