from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReviewsView.as_view(), name='reviews'),
    path("create/", views.ReviewsCreate.as_view(), name="create_reviews"),
    path("edit/<int:pk>/", views.ReviewsEdit.as_view(), name="edit_reviews"),
    path(
        "delete/<int:pk>/",
        views.ReviewsDelete.as_view(), name="delete_reviews"),
]
