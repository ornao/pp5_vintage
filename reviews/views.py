from django.shortcuts import render
from django.views import View
from django.views import generic
from .models import Reviews, Product
from django.urls import reverse, reverse_lazy
from .forms import ReviewsForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


class ReviewsView(generic.ListView):
    """ a class for reviews display """
    model = Reviews
    template_name = "reviews/reviews.html"
    queryset = Reviews.objects.filter(status=1).order_by('-created_date')
    context_object_name = 'reviews'


class ReviewsCreate(LoginRequiredMixin, generic.CreateView):
    """ a class for creating reviews """
    model = Reviews
    template_name = "reviews/create_reviews.html"
    form_class = ReviewsForm

    success_url = reverse_lazy('reviews')

    def form_valid(self, form):
        """assigns logged-in user to user field in database"""
        form.instance.author = self.request.user
        messages.success(self.request, "Review created successfully")

        return super().form_valid(form)


class ReviewsEdit(LoginRequiredMixin, generic.UpdateView):
    """ a class for editing reviews """
    model = Reviews
    form_class = ReviewsForm
    template_name = 'reviews/edit_reviews.html'
    success_url = reverse_lazy('reviews')

    def form_valid(self, form):
        """ Updates the review and adds a success message """
        messages.success(self.request, "Review updated successfully")
        return super().form_valid(form)


class ReviewsDelete(LoginRequiredMixin, generic.DeleteView):
    """ a class for deleting reviews """
    model = Reviews
    template_name = 'reviews/confirm_delete.html'
    success_url = reverse_lazy("reviews")

    def delete(self, request, *args, **kwargs):
        """ Deletes the review and adds a success message """
        messages.success(request, "Review deleted successfully")
        return super().delete(request, *args, **kwargs)
