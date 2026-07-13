from django.db import models
from django.core.exceptions import ValidationError
from smart_selects.db_fields import ChainedForeignKey
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
    sub_category = ChainedForeignKey(
        SubCategory,
        chained_field='category',
        chained_model_field='category',
        show_all=False,
        auto_choose=False,
    ) 

    amount = models.DecimalField(
        verbose_name='Сумма',
        max_digits=10,
        decimal_places=2
    )

    comment = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name='Комментарий',
    )
    class Meta:
        verbose_name = 'Транзация'
        verbose_name_plural = 'Транзации'

    def clean(self):
        super().clean()
        if self.sub_category_id == None or self.category_id == None:
            raise ValidationError(
                message='Обязательное поле'
            )
        elif self.sub_category.category != self.category:
            raise ValidationError(
                message='Нельзя выбрать податегорию из другой категории'
            )

    def __str__(self):
        return f'{self.type_transaction} {self.amount}'