from django import forms
from .models import Category


class NewsForm(forms.Form):
    title = forms.CharField(
        max_length=150,
        label='Название',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(
        label='Текст',
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    id_published = forms.BooleanField(
        label='Опубликовано?',
        initial=True,
        widget=forms.TextInput(attrs={'class': 'form-check-input', 'type': 'checkbox', 'checked': True, 'required': None}))
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        label='Категория',
        empty_label='Выберете категорию',
        widget=forms.Select(attrs={'class': 'form-control'}))
