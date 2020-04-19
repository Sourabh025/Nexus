from django.shortcuts import render,redirect

from django.contrib.auth import login,authenticate

from django.urls import reverse_lazy

from django.http import HttpResponseRedirect

from django.contrib.auth.mixins import LoginRequiredMixin   #--- this mixins required to check if user is logged in or not---


from django.contrib import messages

from .forms import ProfileForm,UserForm  #--- import feilds from forms.py to used in templates forms---

from django.contrib.auth.models import  User
from .forms import reg   # reg is used to import form.py 
from userprofile.models import profile  #--- importing from userprofile app model to here---
from django.views.generic import TemplateView, CreateView

# Create your views here.
# we are using form.py not usercreationform 

def registration(request):
    print("check1")
    if request.method=="POST":
        form=reg(request.POST)  #using reg form  forms.py 
        if form.is_valid():
            form.save()
        return  redirect('login')
    else:
        form=reg()
    return render(request,"reg.html",{"form": form})

#profile functionality starts from here

class ProfileView(LoginRequiredMixin, TemplateView):  #this will render profile of user onlyif user is loggedin 
    template_name='profile.html'

#if user is logged in then this class render profile_update form if he wants to edit his/her profile 
class ProfileUpdateView(LoginRequiredMixin,TemplateView):
    user_form = UserForm
    profile_form = ProfileForm
    template_name = 'profile_update.html'  # this will open template if user logged in 

    #this post method will work if user enter submit button with some data in profile_update template form and save and authenticate data
    def post(self, request):

        post_data = request.POST  #storing post request  data that is entered by a user
        file_data= request.FILES  # storing file in this case file is image
        user_form = UserForm(post_data, instance=request.user)  #storing userform data which is entered by user for user model 
        profile_form = ProfileForm(post_data, file_data, instance=request.user.profile)  #loading profile_form with all data to profile model

        if profile_form.is_valid() and user_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile successfully updated!')
            return render(request,'profile.html')#after submit button user will be redirected to his newly updated profile
        #context will always run 
        else:
            messages.success(request,'sorry some error occured')
        context = self.get_context_data(
                                        user_form=user_form,           #context will be used when we use variable in html file {form.as_p}
                                        profile_form=profile_form
                                    )

        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):        #get method will run when user request is get 
        return self.post(request, *args, **kwargs)

