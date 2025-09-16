from django.http import HttpResponse
from django.shortcuts import render

def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    # return HttpResponse("<h1>Hello World</h1>") #string of HTML code
    return render(request,"home.html", {})


def contact_view(*args, **kwargs):
    return HttpResponse("<h1> Contact Page </h1>")