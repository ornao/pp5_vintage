from .models import Reviews, Product
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

    class Meta:
        model = Reviews
        fields = (
              "product_name", "rating", "content", )

