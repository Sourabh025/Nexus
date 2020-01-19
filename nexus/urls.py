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
from register import views as pr
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v.registration,name ='register'),
    #path('',v.registration,name='register1'),
    path('home/',h.home,name='home'),
    #path('profile/',pr.ProfileUpdateView,name='profile'),  # wrong way to import class this will genrate an error because we are importing class as a function
    path('',include("django.contrib.auth.urls")),
    path('profile_update/', pr.ProfileUpdateView.as_view(), name='phome'), #always import class based view as it. other wise it will give error that one extra argument given
    path('profile/', pr.ProfileView.as_view(), name='prhome')
]


from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

