from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    """ class for admin contact model """
    list_display = ('name', 'email', 'subject', 'message')


admin.site.register(Contact, ContactAdmin)
