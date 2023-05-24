from django import forms
# from .models import Category
from .models import News
from django.core.exceptions import ValidationError
import re

"""
class NewsForm(forms.Form):
    title = forms.CharField(
        max_length=150,
        label='Название',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(
        label='Текст',
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    is_published = forms.BooleanField(
        label='Опубликовано?',
        initial=True,
        widget=forms.TextInput(attrs={'class': 'form-check-input', 'type': 'checkbox', 'checked': True, 'required': None}))
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        label='Категория',
        empty_label='Выберете категорию',
        widget=forms.Select(attrs={'class': 'form-control'}))
"""


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        # fields = '__all__'
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'is_published': forms.TextInput(attrs={'class': 'form-check-input', 'type': 'checkbox', 'checked': True, 'required': None}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            text = 'Название не должно называться с цыфры'
            raise ValidationError(text)
        return title
