from django.contrib import admin
from .models import Reviews

# Register your models here.

class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('reviews_id', 'rating', 'status', 'created_date')
    search_fields = ['rating']
    list_filter = ('status', 'created_date')


admin.site.register(Reviews, ReviewsAdmin)
