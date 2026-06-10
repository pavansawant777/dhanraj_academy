from django.shortcuts import render,redirect
from . import models
from user import views as us

# Create your views here.

def index(req):
    return render(req,"admin/index.html")


def about(req):
   
    about_data = models.aboutdahanraj.objects.all()
    
    return render(req,"admin/about.html",{"about_data":about_data})

def about_save(req):
    if req.method == "POST":
        print(req.POST)
        data = models.aboutdahanraj(
            heading = req.POST.get('heading'),
            paragraph = req.POST.get('paragraph'),
            train_number = req.POST.get('train_number'),
           
            stu_num = req.POST.get('selc_stud'),
          
            expfac_num = req.POST.get('expfac_num'),
            
            course_num =req.POST.get('course_num'),
           
        )
        data.save()
        print("Saved Successfully!")

        return redirect('/admin/about/')
    
def update_about(req):
    return render(req,"admin/update_about.html")
    
def delete_about(req,id):
    delete_data = models.aboutdahanraj.objects.get(id=id)

    delete_data.delete()
    return redirect('/admin/about/')


    