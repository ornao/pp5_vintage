from django.shortcuts import render
from django.views import View
from django.views import generic
from .models import Reviews
from django.urls import reverse, reverse_lazy
from .forms import ReviewsForm


class ReviewsView(generic.ListView):
    """ a class for reviews display """
    model = Reviews
    template_name = "reviews/reviews.html"
    queryset = Reviews.objects.filter(status=1).order_by('-created_date').distinct()
    context_object_name = 'reviews'

class ReviewsCreate(generic.CreateView):
    """ a class for creating bookings """
    model = Reviews
    template_name = "reviews/create_reviews.html"
    form_class = ReviewsForm
    success_url = reverse_lazy('reviews')

    def form_valid(self, form):
        """assigns logged-in user to user field in database"""
        form.instance.user = self.request.user
        return super().form_valid(form)

class ReviewsEdit(generic.UpdateView):
    """ a class for editing reviews """
    model = Reviews
    form_class = ReviewsForm
    template_name = 'edit_reviews.html'
    success_url = reverse_lazy('reviews')

class ReviewsDelete(generic.DeleteView):
    """ a class for deleting reviews """
    model = Reviews
    template_name = 'reviews/confirm_delete.html'
    success_url = reverse_lazy("reviews")
