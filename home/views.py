from django.shortcuts import render
from django.contrib import messages

# Create your views here.

def index(request):
    """ A view to return the index page and sucessful login message """

    return render(request, 'templates/home/index.html')
