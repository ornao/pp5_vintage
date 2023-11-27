from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.conf import settings
from .models import Order, OrderLineItem, Product
from .forms import OrderForm
from django.urls import reverse
from decimal import Decimal  


class OrderModelTest(TestCase):
    """creates a test order and tests 
    if created correctly"""
    def setUp(self):
        """creates a test order"""
        self.order = Order.objects.create(
            order_number='123456',
            full_name='John Doe',
            email='john@example.com',
            phone_number='123456789',
            country='US',
            postcode='12345',
            town_or_city='Test City',
            street_address1='123 Main St',
            street_address2='Apt 4',
            county='Test County',
            delivery_cost=5.00,
            order_total=50.00,
            grand_total=55.00,
            original_bag='test_bag_content',
            stripe_pid='test_stripe_pid'
        )


    def test_order_creation(self):
        """Test that an order is created correctly"""
        self.assertEqual(self.order.order_number, '123456')
        self.assertEqual(self.order.full_name, 'John Doe')
        self.assertEqual(self.order.email, 'john@example.com')
        self.assertEqual(self.order.phone_number, '123456789')
        self.assertEqual(self.order.country, 'US')
        self.assertEqual(self.order.postcode, '12345')
        self.assertEqual(self.order.town_or_city, 'Test City')
        self.assertEqual(self.order.street_address1, '123 Main St')
        self.assertEqual(self.order.street_address2, 'Apt 4')
        self.assertEqual(self.order.county, 'Test County')
        self.assertEqual(self.order.delivery_cost, 5.00)
        self.assertEqual(self.order.order_total, 50.00)
        self.assertEqual(self.order.grand_total, 55.00)
        self.assertEqual(self.order.original_bag, 'test_bag_content')
        self.assertEqual(self.order.stripe_pid, 'test_stripe_pid')

    def test_update_total(self):
        """Test that update_total method updates order_total, delivery_cost, and grand_total correctly"""
        self.order.update_total()

        expected_order_total = sum(item.lineitem_total for item in self.order.lineitems.all())
        expected_delivery_cost = (
            expected_order_total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        )
        expected_grand_total = expected_order_total + expected_delivery_cost

        updated_order = Order.objects.get(pk=self.order.pk)

        self.assertEqual(updated_order.order_total, expected_order_total)
        self.assertEqual(updated_order.delivery_cost, expected_delivery_cost)
        self.assertEqual(updated_order.grand_total, expected_grand_total)


class OrderLineItemModelTest(TestCase):
    """creates product and order test case, saves to database, 
    retrieves from database and checks they are the same"""
    def setUp(self):
        self.product = Product.objects.create(
            name='Test Product',
            price=20.00,
            description='Test Description',
        )

        self.order = Order.objects.create(
            order_number='123456',
            full_name='John Doe',
            email='john@example.com',
            phone_number='123456789',
            country='US',
            postcode='12345',
            town_or_city='Test City',
            street_address1='123 Main St',
            street_address2='Apt 4',
            county='Test County',
            delivery_cost=5.00,
            order_total=50.00,
            grand_total=55.00,
            original_bag='test_bag_content',
            stripe_pid='test_stripe_pid'
        )

    def test_order_line_item_creation(self):
        order_line_item = OrderLineItem.objects.create(
            order=self.order,
            product=self.product,
            quantity=1,
            lineitem_total=20.00 
        )

        saved_order_line_item = OrderLineItem.objects.get(pk=order_line_item.pk)

        self.assertEqual(saved_order_line_item.order, self.order)
        self.assertEqual(saved_order_line_item.product, self.product)
        self.assertEqual(saved_order_line_item.quantity, 1)
        self.assertEqual(saved_order_line_item.lineitem_total, 20.00)


class CheckoutUrlTest(TestCase):
    """creates test case, tests checkout url is 
    accessing order form correctly"""
    def test_checkout_view_url_resolves(self):
        url = reverse('checkout')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 302)
