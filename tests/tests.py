from django.test import TestCase

from chat.models import Message


class UndeliveredTestCase(TestCase):
    fixtures = ['undelivered']

    def test_undelivered(self):
        """Undelivered method should return undelivered messages"""
        messages = Message.objects.undelivered()
        self.assertEqual(len(messages), 4,
                         'Total count of undelivered messages should be 4')

        messages = Message.objects.undelivered(to=1)
        self.assertEqual(len(messages), 1,
                         'User "user1" should have 1 undelivered message')

        messages = Message.objects.undelivered(to=2)
        self.assertEqual(len(messages), 1,
                         'User "user2" should have 1 undelivered message')

        messages = Message.objects.undelivered(to=3)
        self.assertEqual(len(messages), 0,
                         'User "user3" should have 0 undelivered messages')

        messages = Message.objects.undelivered(to=4)
        self.assertEqual(len(messages), 1,
                         'User "user4" should have 1 undelivered message')

        messages = Message.objects.undelivered(to=5)
        self.assertEqual(len(messages), 1,
                         'User "user5" should have 1 undelivered message')
