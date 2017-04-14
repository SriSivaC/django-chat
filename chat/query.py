"""Message related query sets"""
from django.db.models.query import QuerySet


class MessageQuerySet(QuerySet):
    """Message query set"""

    def undelivered(self, to):
        """Fetch only undelivered messages"""
        queryset = self.filter(deliveries__delivered_at__isnull=True)
        if to is not None:
            queryset = queryset.filter(deliveries__receiver=to)
        return queryset
