from uuid import uuid4
from django.db import models


# Abstract model to add UUID field to other models
class UUIDModel(models.Model):
    """
    Abstract Class with UUID field
    """
    uuid = models.UUIDField(db_index=True, default=uuid4, editable=False)

    class Meta:
        abstract = True


# Abstract model to add timestamps to other models
class TimeStampedModel(models.Model):
    """
    Abstract Class with create and update dates
    """

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True