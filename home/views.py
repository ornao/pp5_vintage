from django.shortcuts import render
from django.contrib import messages
from django.template import RequestContext


def index(request):
    """ A view to return the index page and sucessful login message """

    return render(request, 'home/index.html')


# error handling found on slack without need for url, /
# adapted to include 403 and 400 error and work on /
# this version of django (Django==3.2.19)

def handler404(request, *args, **argv):
    """ handles 404 error """
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response
