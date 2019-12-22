from django.shortcuts import render,redirect
from django.http import HttpResponse
from home.models import Images
from login.urls import path
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required   
#from django.contrib import messages
from .models import Personal  # importing the class
def index(request):
    if request.method == 'POST':
        if request.POST['name'] and request.POST['email'] and request.POST['username'] and request.POST['pass'] and request.POST['repeat-pass']:
            #it means all the fields must be properly otherwise it show warning.
            

            # user want to create the account
            if request.POST['pass'] == request.POST['repeat-pass']:
                try:
                    user = User.objects.get(username=request.POST['username'])
                    return render(request,'register/index.html',{'error': 'Username is already taken' })
                except User.DoesNotExist:
                    user =  User.objects.create_user(request.POST['username'] ,password=request.POST['pass'])
                    # Update fields and then save again
                    user.first_name = request.POST['name']
                    user.email =request.POST['email']
                    user.save()
                    #messages.success(request,'Your Account Has been Sucessfully Created')
                    auth.login(request,user)
                    return redirect('personal_detail')
            else:
                return render(request,'register/index.html',{'error': 'Password Must be matched' })
        else:
            return render(request,'register/index.html',{'warning':"All fields Must be Filled."})



    else:
        #USer want to enter info
        return render(request,'register/index.html')

#Here user is tha object which we have created and we perform all the accesing of Users attributes using this object..


def personal_detail(request):
    return render(request,'register/personal.htm')

def child(request):
    return render(request,'register/child.htm')

def elder(request):
    return render(request,'register/elder.htm')


def feedback(request):
    return render(request,'register/feedback.htm')


@login_required
def personal(request):
    if request.method == 'POST':
        if request.POST['aadhar'] and request.POST['DOB'] and request.POST['Religion'] and request.POST['Address'] and request.POST['Annual_Income'] and request.POST['Occupation']:
            per = Personal()  #here created the object of the class to access their features
            per.Aadhar_Number =request.POST['aadhar']
            per.DOB =request.POST['DOB']
            per.Religion=request.POST['Religion']
            per.Address =request.POST['Address']
            per.Annual_income =request.POST['Annual_Income']
            per.Occupation =request.POST['Occupation']
            per.save()

            return redirect('homeindex')
        else:
            return render(request,'recharge/personal.htm',{'warning':'All Fields Must be Filled.'})

    else:
        return render(request,'recharge/personal.htm')



def search(request):
    if request.method=='GET':
        value=request.GET['search']
