"""NIEC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from . import views

urlpatterns = [

   path('', views.index,name='registerindex'),
   path('admin/', admin.site.urls),
   #path('login/',include('login.urls'),name='login'),
   path('personal_detail',views.personal_detail,name='personal_detail'),
   path('Child',views.child,name='child'),
   path('Elder',views.elder,name='elder'),
   path('Feedback',views.feedback,name='feedback'),
   path(' ',views.personal,name='personal'),
   path('search/',views.search,name='searchindex'),
   
]