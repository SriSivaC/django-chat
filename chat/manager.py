import django

from .query import MessageQuerySet

if django.VERSION < (1, 7):
    from django.db.models.manager import Manager

    class MessageManager(Manager):
        """Message manager"""

        def get_queryset(self):
            return MessageQuerySet(self.model, using=self._db)

        # Django 1.4 & 1.5 compatible
        get_query_set = get_queryset

        def undelivered(self, to=None):
            """Fetch only undelivered messages"""
            return self.get_queryset().undelivered(to)
else:
    from django.db.models.manager import BaseManager

    class MessageManager(BaseManager.from_queryset(MessageQuerySet)):
        """Message manager"""
        pass
