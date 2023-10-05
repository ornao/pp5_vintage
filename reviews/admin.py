from django.contrib import admin
from .models import Reviews


class ReviewsAdmin(admin.ModelAdmin):
    """class for reviews admin"""
    list_display = ('rating', 'status', 'created_date')
    search_fields = ['rating']
    list_filter = ('status', 'created_date')


admin.site.register(Reviews, ReviewsAdmin)
