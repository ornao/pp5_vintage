from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all() 
    query = None
    categories = None
    sort = None
    direction = None
    gender_param = None

    all_categories = Category.objects.all()

    if request.GET:
        # Gender filtering
        if 'gender' in request.GET:
            gender_param = request.GET['gender'].upper()
            products = products.filter(gender=gender_param)
            genders = Product.objects.filter(gender=gender_param)

        # Category filtering
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        # Sorting logic
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        # Search logic
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'
   


    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'all_categories': all_categories, 
        'current_sorting': current_sorting,
        'current_genders': genders
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)