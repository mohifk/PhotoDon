from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from PhotoDon.settings import STATIC_URL
from website.views import *


app_name='website'

urlpatterns = [

    path ('',Home_page_view,name='index'),
    path ('about/',about_view,name='about'),
    path ('contact/',contact_view,name='contact'),
     path('blog/',include('blog.urls')),
]