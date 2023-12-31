from django.shortcuts import render
from .forms import ContactForm


def contact_view(request):
    """contact view"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact/contact_success.html')
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})
