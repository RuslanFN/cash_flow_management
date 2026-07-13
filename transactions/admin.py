from django import forms
from django.contrib import admin
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from .models import Category, SubCategory, Status, TypeTransaction, Transaction
# Register your models here.
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Status)
admin.site.register(TypeTransaction)

class TransactionAdminForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'

    def clean(self):
        try:
            # Пытаемся запустить стандартную валидацию Django
            return super().clean()
        except ObjectDoesNotExist:
            # ПЕРЕХВАТЫВАЕМ ошибку библиотеки smart-selects
            # и превращаем её в красивое сообщение для пользователя
            raise ValidationError({
                'sub_category': 'Это поле обязательно для заполнения.'
            })
    
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    form = TransactionAdminForm 