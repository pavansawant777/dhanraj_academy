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
     path('upd1/',us.upd1),
    path('upd2/',us.upd2),
    path('upd3/',us.upd3),
    path('upd4/',us.upd4),
    path('upd5/',us.upd5),
    path('upd6/',us.upd6),
    path('upd7/',us.upd7),
    path('upd8/',us.upd8),
    path('upd9/',us.upd9),
    path('upd10/',us.upd10),
    path('upd11/',us.upd11),
    path('upd12/',us.upd12),
    path('upd13/',us.upd13),
    path('upd14/',us.upd14),
    path('upd15/',us.upd15),
    path('books_notes/',us.book_notes),
    path('test_series/',us.test_series),
    path('result/',us.result),
     path('success-story1/',us.success_story1),
    path('success-story2/',us.success_story2),
    path('success-story3/',us.success_story3),
    path('success-story4/',us.success_story4),
    path('success-story5/',us.success_story5),
    path('success-story6/',us.success_story6),
    path('success-story7/',us.success_story7),
    path('success-story8/',us.success_story8),
    path('success-story9/',us.success_story9),
    path('success-story10/',us.success_story10),
    path('success-story11/',us.success_story11),
    path('success-story12/',us.success_story12),
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
