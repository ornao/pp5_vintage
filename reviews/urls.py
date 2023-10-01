from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReviewsView.as_view(), name='reviews'),
]