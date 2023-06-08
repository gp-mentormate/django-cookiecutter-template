# The `models.pyi` file defines the structure and behavior of
# the application's database models, allowing developers to create and
# manipulate database tables and their relationships.

import uuid

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_softdelete.models import (
    DeletedQuerySet,
    SoftDeleteModel,
    SoftDeleteQuerySet,
)

user_model = settings.AUTH_USER_MODEL


class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        return SoftDeleteQuerySet(self.model, self._db).filter(
            is_deleted=False)


class DeletedManager(models.Manager):
    def get_queryset(self):
        return DeletedQuerySet(self.model, self._db).filter(is_deleted=True)


class GlobalManager(models.Manager):
    pass


class CustomSoftDeleteModel(SoftDeleteModel):
    objects: SoftDeleteManager = SoftDeleteManager()
    deleted_objects: DeletedManager = DeletedManager()
    global_objects: GlobalManager = GlobalManager()

    deleted_by: models.ForeignKey = models.ForeignKey(
        to=user_model,
        verbose_name=_('Deleted by'),
        null=True,
        blank=True,
        related_name='%(class)s_deleted',
        on_delete=models.SET_NULL
    )

    class Meta:
        abstract = True


class BaseModel(CustomSoftDeleteModel):
    uid: models.UUIDField = models.UUIDField(
        verbose_name=_('UUID'),
        unique=True,
        default=uuid.uuid4,
        editable=False
    )

    created_by: models.ForeignKey = models.ForeignKey(
        to=user_model,
        verbose_name=_('Created by'),
        null=True,
        blank=True,
        related_name='%(class)s_created',
        on_delete=models.SET_NULL
    )

    created_at: models.DateTimeField = models.DateTimeField(
        verbose_name=_('Created at'),
        auto_now_add=True,
        editable=False,
        db_index=True
    )

    updated_by: models.ForeignKey = models.ForeignKey(
        to=user_model,
        verbose_name=_('Updated by'),
        null=True,
        blank=True,
        related_name='%(class)s_updated',
        on_delete=models.SET_NULL
    )

    updated_at: models.DateTimeField = models.DateTimeField(
        verbose_name=_('Updated at'),
        auto_now=True,
        null=True,
        blank=True
    )

    class Meta:
        abstract = True
