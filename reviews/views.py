from django.shortcuts import render
from django.views import generic
from .models import Reviews


class ReviewsList(generic.ListView):
    """ a class for reviews view """
    model = Reviews
    queryset = Reviews.objects.filter(status=1).order_by('-created_date')
    template_name = "reviews.html"
