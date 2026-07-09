from django.db import models
import uuid
# BaseModel
class BaseModel(models.Model):
    id = models.UUIDField(
        primary_key=True,
        db_default=uuid.uuid4,
        editable=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='Дата создания')
    updated_at = models.DateTimeField(
        auto_now=True, 
        verbose_name='Дата изменения')
    class Meta:
        abstract = True
