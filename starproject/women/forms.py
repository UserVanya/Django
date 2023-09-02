from django import forms
from .models import *

class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255, label="Название", widget=forms.TextInput(attrs={"class": "form-input"}))
    slug = forms.SlugField(max_length=255, label="URL")
    content = forms.CharField(widget=forms.Textarea(attrs={"cols": 60, "rows": 10}), label="Контент")
    is_published = forms.BooleanField(label="Опубликовано", required=False, initial=True)
    #photo = forms.ImageField(label="Фото", required=False)
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), label="Категория", empty_label="Категория не выбрана")