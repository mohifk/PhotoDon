from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse

from django.contrib import messages

def Home_page_view(request):
    return render(request,'.\website_temp\index.html')

def about_view(request):
    return render(request ,'.\website_temp\\about.html')

def contact_view(request):

    return render(request,'.\website_temp\contact.html')
