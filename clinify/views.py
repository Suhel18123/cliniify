from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home (request):
    return render(request,'login.html')

def signup(request):
    category=request.GET.get('category')
    context={
        'step': 2 if category else 1,
        'selected_category':category

    }
    return render(request,'signup.html',context)