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
    path('latest_update/',views.latest_update),
    path('upd1/',views.upd1),
    path('upd2/',views.upd2),
    path('upd3/',views.upd3),
    path('upd4/',views.upd4),
    path('upd5/',views.upd5),
    path('upd6/',views.upd6),
    path('upd7/',views.upd7),
    path('upd8/',views.upd8),
    path('upd9/',views.upd9),
    path('upd10/',views.upd10),
    path('upd11/',views.upd11),
    path('upd12/',views.upd12),
    path('upd13/',views.upd13),
    path('upd14/',views.upd14),
    path('upd15/',views.upd15),
       
    path('books_notes/',views.book_notes),
    path('test_series/',views.test_series),
    path('result/',views.result),
    path('success-story1/',views.success_story1),
    path('success-story2/',views.success_story2),
    path('success-story3/',views.success_story3),
    path('success-story4/',views.success_story4),
    path('success-story5/',views.success_story5),
    path('success-story6/',views.success_story6),
    path('success-story7/',views.success_story7),
    path('success-story8/',views.success_story8),
    path('success-story9/',views.success_story9),
    path('success-story10/',views.success_story10),
    path('success-story11/',views.success_story11),
    path('success-story12/',views.success_story12),
    path('scholarship/',views.scholarship),
    path('faculty/',views.faculty),
    path('gallary/',views.gallary),
    path('blog/',views.blog),

    path('contact/',views.contact),
    

    path('admin/', admin.site.urls),
   

]
