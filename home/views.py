from django.shortcuts import render
from django.contrib import messages

# Create your views here.

def index(request):
    """ A view to return the index page and sucessful login message """

    return render(request, 'home/index.html')

def mobile_view(request):
    user_agent = request.user_agent

    is_mobile = user_agent.is_mobile
    is_tablet = user_agent.is_tablet

    context = {
        'is_mobile': is_mobile,
        'is_tablet': is_tablet,
    }

    return render(request, 'base.html', context)

