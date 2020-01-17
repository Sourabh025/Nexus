from django.shortcuts import render,redirect

from django.contrib.auth import login,authenticate
from django.http import HttpResponseRedirect

from django.contrib.auth.mixins import LoginRequiredMixin   #--- this mixins required to check if user is logged in or not---

from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages

from .forms import ProfileForm,UserForm  #--- import feilds from forms.py to used in templates forms---

from django.contrib.auth.models import  User

from userprofile.models import profile  #--- importing from userprofile app model to here---

from django.views.generic import TemplateView, CreateView

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


class profileview(LoginRequiredMixin, TemplateView):
    template_name='profile.html'


class ProfileUpdateView(LoginRequiredMixin,TemplateView):
    user_form = UserForm
    profile_form = ProfileForm
    template_name = 'profile_update.html'  # this will open template

    def post(self, request):

        post_data = request.POST or None  #storing post request  data that is entered by a user
        file_data= request.FILES or None # storing file in this case file is image
        user_form = UserForm(post_data, instance=request.user)  #storing userform data from User login (User model)
        profile_form = ProfileForm(post_data, file_data, instance=request.user.profile)  #loading profile_form with all data

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return render(request,'profile.html')

        context = self.get_context_data(
                                        user_form=user_form,
                                        profile_form=profile_form
                                    )

        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

