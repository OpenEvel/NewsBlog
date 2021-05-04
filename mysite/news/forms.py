from django import forms

from .models import *
import re
from django.core.exceptions import ValidationError


# 1 Вариант добавления формы "forms.Form"
# class NewsForm(forms.Form):
#     title = forms.CharField(max_length=150, label='Зголовок', widget=forms.TextInput(attrs={"class": "form-control"}))
#     content = forms.CharField(label='Контент', required=False,
#                               widget=forms.Textarea(attrs={"class": "form-control", "rows": 5}))
#     is_published = forms.BooleanField(label='Опубликовано?', initial=True)
#     category = forms.ModelChoiceField(label='Категория', queryset=Category.objects.all(), empty_label='--Выберите категорию--',
#                                       widget=forms.Select(attrs={"class": "form-control"}))



class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        # fields = '__all__' # не рекомендуемый способ
        fields = {'title', 'content', 'is_published', 'category'}
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean(self):
        """
        Для валидации CreateView использовать функцию clean()
        :rtype: object
        """
        cleaned_data = super().clean()
        title = self.cleaned_data['title']
        if re.match('\d', title):
            raise ValidationError('Название не должно начинаться с цифры')

""" 
    # для функций во view дял валидации можно использовать такой синтаксис
    def clean_title(self):
        cleaned_data = super().clean()
        title = self.cleaned_data['title']
        if re.match('\d', title):
            raise ValidationError('Название не должно начинаться с цифры')
"""

