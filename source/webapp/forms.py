from django import forms
from django.forms import widgets
from webapp.models import PRODUCT_CATEGORY_CHOICES


class ProductForm(forms.Form):
    name = forms.CharField(max_length=200, required=True, label='Имя')
    description = forms.CharField(max_length=3000, required=True, label='Текст',   widget=widgets.Textarea)
    category = forms.ChoiceField(required=True, label='Катигория', choices=PRODUCT_CATEGORY_CHOICES)
    price = forms.DecimalField(required=True, label='Цина', min_value=0)
    amount = forms.IntegerField(required=True, label='Остаток', min_value=0)


class SeacrhForm(forms.Form):
    product_name = forms.CharField(max_length=200, required=True, label='Имя')