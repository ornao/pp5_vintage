from django.contrib import admin
from .models import Reviews

class ReviewsAdmin():
    """ a class for reviews admin """

    list_display = ('rating', 'status', 'created_date')
    search_fields = ['rating']
    list_filter = ('status', 'created_date')
    summernote_fields = ('content',)