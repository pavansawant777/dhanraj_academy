from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req,"user/index.html")

def about(req):
    return render(req,"user/about.html")

def course(req):
    return render(req,"user/course.html")

def course_mpsc(req):
    return render(req,"user/course_mpsc.html")

def course_police(req):
    return render(req,"user/course_police.html")

def course_talathi(req):
    return render(req,"user/course_talathi.html")
    

def course_vanrakshak(req):
    return render(req,"user/course_vanrakshak.html")


def course_gramsevak(req):
    return render(req,"user/course_gramsevak.html")


def course_allexams(req):
    return render(req,"user/course_allexams.html")


def latest_update(req):
    return render(req,"user/latest_update.html")

def book_notes(req):
    return render(req,"user/books_notes.html")

def test_series(req):
    return render(req,"user/test_series.html")

def scholarship(req):
    return render(req,"user/scholarship.html")

def result(req):
    return render(req,"user/result.html")

def faculty(req):
    return render(req,"user/faculty.html")

def gallary(req):
    return render(req,"user/gallary.html")

def blog(req):
    return render(req,"user/blog.html")

def contact(req):
    return render(req,"user/contact.html")

