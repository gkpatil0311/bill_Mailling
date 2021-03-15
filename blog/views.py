from django.shortcuts import render
#from django.http import HttpResponse
from django.template import Context, loader

# Create your views here.
 
posts = [
    {
        'author':'gaurav',
        'title':'blog post',
        'content':'first post content',
        'date_posted':'August 27, 2019'
    },
    {
        'author':'suchita',
        'title':'blog post',
        'content':'first post content',
        'date_posted':'August 27, 2019'
    }
]



def home(request):
    #return HttpResponse('<h1> Blog Home</h1>')
    context = {
        'posts':posts
    }
    return render(request,"blog/home.html",context)

def about(request):
    #return HttpResponse('<h1>Blog About</h1>') 
    return render(request,"blog/about.html",{'title':'About'})

def login(request):
    #return HttpResponse('<h1>Blog About</h1>') 
    return render(request,"blog/login.html")

