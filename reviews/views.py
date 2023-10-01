from django.shortcuts import render
from django.views import View
from .models import Reviews


class ReviewsView(View):
    """A custom class-based view for displaying reviews."""

    def get(self, request):

        reviews = Reviews.objects.filter(status=1).order_by('-created_date')
        context = {
            'reviews': reviews,
        }

        return render(request, 'reviews/reviews.html', context)