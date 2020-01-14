from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

def profile(request):

    #name= request.user.get()

    #user=name

    return render(request,"profile.html")
