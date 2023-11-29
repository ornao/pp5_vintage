from django.test import TestCase, Client
from .models import Contact
from .forms import ContactForm
from django.urls import reverse


class ContactModelTest(TestCase):
    """creates test case, saves to database,
    retrieves from database and checks they are the same"""
    def test_create_contact(self):
        """creates test contact"""
        contact = Contact(
            name="John Doe",
            email="john@example.com",
            subject="Test Subject",
            message="This is a test message."
        )

        contact.save()

        saved_contact = Contact.objects.get(pk=contact.pk)

        self.assertEqual(saved_contact.name, "John Doe")
        self.assertEqual(saved_contact.email, "john@example.com")
        self.assertEqual(saved_contact.subject, "Test Subject")
        self.assertEqual(saved_contact.message, "This is a test message.")


class ContactUrlTest(TestCase):
    """creates test case, tests contact url is
    accessing contact form correctly"""
    def test_contact_view_url_resolves(self):
        url = reverse('contact')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class ContactViewTests(TestCase):
    """creates test case, tests get contact form functionality,
    and tests valid form being sent and success functionality"""
    def setUp(self):
        """set up"""
        self.client = Client()

    def tearDown(self):
        """tear down"""
        Contact.objects.all().delete()

    def test_contact_view_get(self):
        """test contact view and url working"""
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')
        self.assertIsInstance(response.context['form'], ContactForm)

    def test_contact_view_post_valid_form(self):
        """test correct form used """
        data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'subject': 'Test Subject',
            'message': 'Test Message'
        }
        response = self.client.post(reverse('contact'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact_success.html')
        self.assertEqual(Contact.objects.count(), 1)
