from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReviewsView.as_view(), name='reviews'),
    path("create/", views.ReviewsCreate.as_view(), name="create_reviews"),
]