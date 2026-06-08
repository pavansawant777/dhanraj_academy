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
