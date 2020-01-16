"""nexus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from register import views as v
from home import views as h
from userprofile import views as p
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v.registration,name ='register'),
    #path('',v.registration,name='register1')'''
    path('home/',h.home,name='home'),
    path('profile/',p.profile,name='profile'),
    path('',include("django.contrib.auth.urls")),

]
