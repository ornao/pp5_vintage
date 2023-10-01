from . import views
from django.urls import path

# renders view to user
urlpatterns = [
    path("", views.ReviewsList.as_view(), name="reviews"),
]