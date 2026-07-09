from django.db import models
from .dictionary import Status, TypeTransaction, Category, SubCategory
from .Base import BaseModel

class Transaction(BaseModel):
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        related_name='transactions_by_statys',
        verbose_name='Статус'
        )
    type_transaction = models.ForeignKey(
        TypeTransaction,
        on_delete=models.PROTECT,
        related_name='transactions_by_type',
        verbose_name='Тип транзакции')
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='transactions_by_category',
        verbose_name='Категория'
    )    
    sub_category = models.ForeignKey(
        SubCategory,
        on_delete=models.PROTECT,
        related_name='transactions_by_sub_category',
        verbose_name='Подкатегория'
    )

    amount = models.DecimalField(
        verbose_name='Сумма',
        max_digits='10',
        decimal_places=2
    )

    comment = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name='Комментарий',
    )