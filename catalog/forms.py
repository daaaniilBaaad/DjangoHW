from django.core.exceptions import ValidationError
from django.forms import ModelForm

from catalog.models import Product


BANNED_WORDS = [
    'казино', 'криптовалюта', 'крипта', 'биржа',
    'дешево', 'бесплатно', 'обман', 'полиция', 'радар'
]

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description','image', 'category', 'price')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите название продукта'
        })

        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите описание продукта'
        })

        self.fields['image'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['category'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['price'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите цену продукта'
        })

    def clean_name(self):
        name = self.cleaned_data['name']
        for word in BANNED_WORDS:
            if word.lower() in name.lower():
                raise ValidationError(f"Название содержит запрещённое слово: «{word}»")
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description', '')
        for word in BANNED_WORDS:
            if word.lower() in description.lower():
                raise ValidationError(f"Описание содержит запрещённое слово: «{word}»")
        return description

    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise ValidationError("Цена должна быть положительной")
        return price

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')

        if name and description and name == description:
            self.add_error(
                'description',
                ValidationError("Название и описание не должны совпадать")
            )
