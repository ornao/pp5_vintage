from django.shortcuts import render, redirect, reverse
from django.contrib import messages
import os

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': os.environ.get('STRIPE_KEY', 'pk_test_51NgWZzLHAE7MTuBZ36qHXhMYWe1co9lOaTxk9dT56RYoVYwg7zI90iTVU9P9gCNSxmG7L1iUhCl0YwwxPqAZ2b0f005ASF8Eeb'),
        'stripe_client_secret': os.environ.get('STRIPE_SECRET', ''),
    }

    return render(request, template, context)