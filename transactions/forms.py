from django import forms

class TransactionForm(forms.Form):
    created_at_from = forms.DateTimeField(
        input_formats='%Y-%m-%d %H:%M:%S',
        required=False,
        label='От',
        widget=forms.DateTimeInput(
            attrs={
                'type': 'datetime-local', 
                'class': 'form-control', 
            }
        ),
    )
    created_at_to = forms.DateTimeField(
        input_formats='%Y-%m-%d %H:%M:%S',
        required=False,
        label='До',
        widget=forms.DateTimeInput(
            attrs={
                'type': 'datetime-local', 
                'class': 'form-control', 
            }
        ),
    )
    status = forms.IntegerField( 
        label='Статус',
        required=False,
        widget=forms.Select)
    type_transaction = forms.IntegerField(
        label='Тип',
        required=False,
        widget=forms.Select)
    category = forms.IntegerField(
        label='Категория',
        required=False,
        widget=forms.Select)
    sub_category = forms.IntegerField(
        label='Подкатегория',
        required=False,
        widget=forms.Select)
    
    def __init__(self, *args, **kwargs):
        choises_data = []
        if 'choises_data' in kwargs:
            choises_data = kwargs.pop('choises_data')
        super().__init__(*args, **kwargs)
        if choises_data:
            self.fields['status'].widget.choices = choises_data['statuses']
            self.fields['type_transaction'].widget.choices = choises_data['type_transactions']
            self.fields['category'].widget.choices = choises_data['categories']
