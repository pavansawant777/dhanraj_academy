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
from user import views as us
from adpanel import views as ad

urlpatterns = [
    path('',us.index),
    path('about/',us.about),
    path('course/',us.course),
    path('course_mpsc/',us.course_mpsc),
    path('course_police/',us.course_police),
    path('course_talathi/',us.course_talathi),
    path('course_vanrakshak/',us.course_vanrakshak),
    path('course_gramsevak/',us.course_gramsevak),   
    path('course_allexams/',us.course_allexams),
    path('latest_update/',us.latest_update),
    path('books_notes/',us.book_notes),
    path('test_series/',us.test_series),
    path('result/',us.result),
    path('scholarship/',us.scholarship),
    path('faculty/',us.faculty),
    path('gallary/',us.gallary),
    path('blog/',us.blog),

    path('contact/',us.contact),
    

    # path('admin/', admin.site.urls),

    # admin urls
    path('admin/',ad.index),
    path('admin/about/',ad.about),
    path('save_train/',ad.about_save, name="save_train"),
    path('delete_about/<int:id>/',ad.delete_about, name="delete_about"),
   

]
