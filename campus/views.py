from django.http import HttpResponse
from django.shortcuts import render
import joblib

def home(request):
    return render(request,'home.html')

def result(request):
    lr=joblib.load("model")

    res=[]
    res.append(request.POST.get('gender'))
    res.append(request.POST.get('SSC PERCENTAGE'))
    res.append(request.POST.get('SSC BRANCH'))
    res.append(request.POST.get('HSC PERCENTAGE'))
    res.append(request.POST.get('BOARD OF EDUCATION'))
    res.append(request.POST.get('HSC BRANCH'))
    res.append(request.POST.get('DEGREE PERCENTAGE'))
    res.append(request.POST.get('degree_specialisation'))
    res.append(request.POST.get('WORK EXPERIENCE'))
    res.append(request.POST.get('ETEST PERCENTAGE'))
    res.append(request.POST.get('MBA SPECIALISATION'))
    res.append(request.POST.get('MBA PERCENTAGE'))

    # r = request.POST.get('degree_specialisation')
    # return HttpResponse(r)
    
    ans=lr.predict([res])
    application_no = request.POST.get('application_no')

    return render(request,"result.html",{'ans':ans,'application_no':application_no})