from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#requrest -> response
#request handler
#action

def say_hello(request):
    return render(request, 'home.html', { 'name': 'Nick'})
