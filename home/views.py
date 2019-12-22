from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponse
from .models import Images
from django.db.models import Q
from django.contrib.auth.decorators import login_required
# Create your views here.
'''def index(request):
    return HttpResponse("<h1 style=text-align:center>Hello This is Home Page</h1>")'''
def index(request):
	return render(request,'home/index.html')

def homeid(request,home_id):
	content={}
	ohome =get_object_or_404(Images,pk=home_id)
	content['data'] =ohome
	return render(request,'home/home1.htm',content)
	
'''def search(request):
	if request.method =='GET':
		search_value =request.GET['search']
		search_result =Mobile_recharge.objects.filter(Operator__icontains=search_value)  # In Our Mobile_recharge Model it will get all the objects whose Operator actually contains the search_term
		return render(request,'home/search.html',{'show':search_value,'result':search_result})
	else:
		return render(request,'home/index.html')'''
#@login_required
'''def search(request):
	if request.method =='GET':
		search_value =request.GET['search']
		search_result =Mobile_recharge.objects.filter(
			Q(Operator__icontains=search_value) |
			Q(Recharge_Type__icontains=search_value) |
			Q(Circle__icontains=search_value) |
			Q(Recharge_Amount__iexact=search_value) |
			Q(Enter_Your_Mobile_Number__iexact=search_value)


		)  # In Our Mobile_recharge Model it will get all the objects whose Operator actually contains the search_term
		return render(request,'home/search.html',{'show':search_value,'result':search_result.filter(Currentuser=request.user)})
	else:
		return render(request,'home/index.html')
'''

'''def homeid1(request,home_id):
		 	content={}
		 	ohome =get_object_or_404(Images,pk=home_id)
		 	content['data'] = ohome
		 	return render(request,'home/home1.htm',content)'''	


# In Our Mobile_recharge Model it will get all the objects whose Operator actually contains the 


#@login_required

'''def history(request):
	result_of_mobile =Mobile_recharge.objects.filter(Currentuser=request.user)
	result_of_dth =Dth_recharge.objects.filter(Currentuser=request.user)
	result_of_datacard =Datacard_recharge.objects.filter(Currentuser=request.user)
	result_of_metro =Metro_recharge.objects.filter(Currentuser=request.user)


	#HERE WE CANNOT USE THE icontains feature here because icontains only used when the input coming is dynamic or unpredictable or depend on user but here we know the matching term is fixed i.e., request.user so it is static so we only use assign operator
	return render(request,'home/history.html',{'mobile':result_of_mobile,'dth':result_of_dth,'datacard':result_of_datacard,'metro':result_of_metro})
'''


def history(request):
	#HERE WE CANNOT USE THE icontains feature here because icontains only used when the input coming is dynamic or unpredictable or depend on user but here we know the matching term is fixed i.e., request.user so it is static so we only use assign operator
	return render(request,'home/history.html')
