from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req,"user/index.html")

def about(req):
    return render(req,"user/about.html")

def course(req):
    return render(req,"user/course.html")

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

