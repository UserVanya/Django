from typing import Any, Dict, Mapping, Optional, Type, Union
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import *
from django.core.exceptions import ValidationError

class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwrgs) -> None:
        super().__init__(*args, **kwrgs)
        self.fields['cat'].empty_label = "Выберите категорию"
    class Meta:
        model = Women
        fields = ['title', 'slug', 'content', 'photo', 'is_published',  'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Введите название статьи'}),
            'content': forms.Textarea(attrs={'cols':100, 'rows':10, 'placeholder': 'Введите текст статьи'}),
        }
    
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError("Длина превышает 200 символов")
        return title