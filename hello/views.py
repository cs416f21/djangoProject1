from django.shortcuts import render
from django.http import HttpResponse


# This function takes request as a parameter and in turn returns an HttpResponse as the content of the page
# Each view you write is responsible for instantiating, populating, and returning an HttpResponse.
def goodbye(request):
    return HttpResponse("Goodbye, world!")


# This method renders an html page using the hello.html, which is in the template directory
# context is a dictionary that is passed to the template (i.e., hello.html) to be able use the carried information there
def hello(request, my_name):
    context = {
        'name': my_name,
        'last_name': 'White',
        'states': ['CT', 'MA', 'CA']
    }
    return render(request, 'hello.html', context)
