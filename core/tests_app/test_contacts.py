from django.test import TestCase
from core.models import Contact


class TestContact(TestCase):
    
    def setUp(self):
        self.data1 = {
            'full_name' : 'NUMAN',
            'email' : 'numan@gmail.com',
            'phone' : 994503476083,
            'subject' : 'ddd',
            'message' : 'aaaa'
        }


        self.contact1 = Contact.objects.create(**self.data1)


    def test_contact_data(self):
        self.assertEqual(self.data1['message'], self.contact1.message)