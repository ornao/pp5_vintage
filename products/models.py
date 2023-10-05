from django.db import models


class Category(models.Model):
    """class for category model"""

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """class fro products model"""
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)

    CONDITION_CHOICES = [
        ('never worn', 'Never worn'),
        ('very good', 'Very Good'),
        ('good', 'Good'),
        ('fair', 'Fair'),
    ]

    condition = models.CharField(max_length=100, choices=CONDITION_CHOICES)

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('U', 'Unisex'),
    ]

    gender = models.CharField(
        max_length=100, null=True, blank=True, choices=GENDER_CHOICES)
    size = models.CharField(max_length=20)
    material = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    date_listed = models.DateTimeField(auto_now_add=True)
    is_sold = models.BooleanField(default=False)

    def __str__(self):
        return self.name
