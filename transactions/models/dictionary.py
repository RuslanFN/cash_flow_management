from django.db import models
from .Base import BaseModel

class BaseDict(models.Model):
    title = models.CharField(
        max_length=20,
        unique=True,
        verbose_name='Название')
    
    class Meta:
        abstract = True

    def __str__(self):
        return self.title

class Status(BaseDict):
    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы' 

class TypeTransaction(BaseDict):   
    class Meta:
        verbose_name = 'Тип транзакции'
        verbose_name_plural = 'Типы транзакций' 

class Category(BaseDict):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    
class SubCategory(BaseDict):
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE,
        related_name='subcategories',
        verbose_name='Категория')

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'
    