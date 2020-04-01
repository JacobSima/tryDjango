from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request,*args,**kwargs):  # *args,  **kwargs
  print(args,kwargs)    # () {}
  print(request)  # <WSGIRequest: GET '/'>,
  print(request.user)
  # return HttpResponse("<h1>Hello There</h1>")      # String of HTML code
  return render(request,'home.html',{})


def contact_view(request,*args,**kwargs):
  # return HttpResponse("<h1>Contact Page</h1>")
  return render(request,'contact.html',{})

def about_view(request,*args,**kwargs):
  # return HttpResponse("<h1>About Page</h1>")
  my_context = {
    "title":"This is about me",
    "my_number":123,
    "my_list":[1,2,3,4,5,'abc'],
    "this_is_true":True,
    "my_html":"<h1>Hello world</h1>"
  }
  return render(request,'about.html', my_context)


def social_view(request,*args,**kwargs):
  return HttpResponse(
    "<h1>Social Page</h1>"
  )