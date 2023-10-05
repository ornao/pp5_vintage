from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """config class for checkout"""
    name = 'checkout'

    def ready(self):
        import checkout.signals
