from django import forms
# from .models import Category
from .models import News
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField, CaptchaTextInput
import re

class ContactForm(forms.Form):
    class_attr = {'class': 'form-control'}
    subject = forms.CharField(
        label='Тема',
        widget=forms.TextInput(attrs=class_attr))
    content = forms.CharField(
        label='Текст',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    captcha = CaptchaField()

class UserLoginForm(AuthenticationForm):
    class_attr = {'class': 'form-control'}
    class_attr_af = {**class_attr, **{'autofocus': ''}}
    username = forms.CharField(
        label='Имя пользователя',
        help_text='максимум 150 символов',
        widget=forms.TextInput(attrs=class_attr_af))
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs=class_attr))

class UserRegisterForm(UserCreationForm):
    class_attr = {'class': 'form-control'}
    class_attr_af = {**class_attr, **{'autofocus': ''}}
    username = forms.CharField(
        label='Имя пользователя',
        help_text='максимум 150 символов',
        widget=forms.TextInput(attrs=class_attr_af))
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs=class_attr))
    password2 = forms.CharField(
        label='Подтверждение пароля',
        widget=forms.PasswordInput(attrs=class_attr))
    email = forms.EmailField(
        label='E-mail',
        widget=forms.EmailInput(attrs=class_attr))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        """
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.TextInput(attrs={'class': 'form-control'}),
            'password2': forms.TextInput(attrs={'class': 'form-control'}),
        }
        """


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
