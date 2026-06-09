"""
URL configuration for Dnynraj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from user import views 

urlpatterns = [
    path('',views.index),
    path('about/',views.about),
    path('course/',views.course),
    path('course_mpsc/',views.course_mpsc),
    path('course_police/',views.course_police),
    path('course_talathi/',views.course_talathi),
    path('course_vanrakshak/',views.course_vanrakshak),
    path('course_gramsevak/',views.course_gramsevak),   
    path('course_allexams/',views.course_allexams),
    path('latest_update/',views.latest_update),
    path('books_notes/',views.book_notes),
    path('test_series/',views.test_series),
    path('result/',views.result),
    path('scholarship/',views.scholarship),
    path('faculty/',views.faculty),
    path('gallary/',views.gallary),
    path('blog/',views.blog),

    path('contact/',views.contact),
    

    path('admin/', admin.site.urls),
   

]
