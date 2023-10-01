from .models import Reviews
from django import forms
from django.core.exceptions import ValidationError
from django.shortcuts import redirect


# code adapted django documentation form validation

class ReviewsForm(forms.ModelForm):
    """ a class for reviews form """
    def clean(self):
        cleaned_data = super().clean()
        rating = cleaned_data.get("rating")
        content = cleaned_data.get("content")
        product_name = cleaned_data.get(
            "product_name")
        featured_image_url = cleaned_data.get("featured_image_url")
        status = cleaned_data.get(
            "status")


    class Meta:
        model = Reviews
        fields = (
            "author", "rating", "content", "product_name", "featured_image_url", "status" )