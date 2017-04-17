"""Chat related models"""
from __future__ import unicode_literals

import django.utils.timezone
from django.db import models
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver

from .manager import MessageManager


class Room(models.Model):
    """A class describing a chat room"""
    name = models.CharField(max_length=255, null=False, blank=False,
                            verbose_name='Room name')
    created_at = models.DateTimeField(default=django.utils.timezone.now,
                                      verbose_name='Created date')
    created_by = models.ForeignKey('auth.User', db_column='created_by',
                                   null=False, blank=True,
                                   related_name='my_chat_rooms')
    users = models.ManyToManyField('auth.User', blank=False,
                                   related_name='chat_rooms')


class Message(models.Model):
    """A class describing a chat message"""
    room = models.ForeignKey('chat.Room', null=False, blank=False,
                             on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey('auth.User', null=False, blank=False)
    message = models.TextField()
    created_at = models.DateTimeField(default=django.utils.timezone.now,
                                      verbose_name='Created date')

    objects = MessageManager()


class MessageDelivery(models.Model):
    """A class describing a message delivery status"""
    message = models.ForeignKey('chat.Message', null=False, blank=False,
                                on_delete=models.CASCADE,
                                related_name='deliveries')
    receiver = models.ForeignKey('auth.User', null=False, blank=False)
    delivered_at = models.DateTimeField(null=True, blank=True)


@receiver(post_save, sender=Message)
def set_delivery_status(instance, created, **kwargs):
    """post save signal to fill delivery status to false"""
    if created:
        users = instance.room.users.exclude(pk=instance.sender.pk)
        MessageDelivery.objects.bulk_create([
            MessageDelivery(message=instance, receiver=user)
            for user in users
        ])
