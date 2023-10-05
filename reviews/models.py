from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from django.core.validators import MaxValueValidator, MinValueValidator

STATUS = ((0, "Draft"), (1, "Published"))


class Reviews(models.Model):
    """ a class for reviews model """
    reviews_id = models.AutoField(primary_key=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_reviews"
    )
    # add max and min possible inputs
    rating = models.IntegerField(
        default=5,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
            ])
    content = models.TextField()
    featured_image_url = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        related_name="products_image_url", null=True)
    product_name = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        related_name="products_name", null=True, limit_choices_to={'orderlineitem__isnull': False})
    created_date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.content
