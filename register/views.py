from django.shortcuts import render,redirect

from django.contrib.auth import login,authenticate

from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def registration(request):

    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return  redirect('login')
    else:
        form=UserCreationForm()     
    return render(request,"register.html",{"form": form})




