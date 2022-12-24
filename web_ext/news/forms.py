from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['schema', 'name', 'type', 'rs_definition', 'term', 'text_definition']

        widgets = {
            'schema': TextInput(attrs={'class': 'form-control', 'placeholder': "Схема"}),
            'name': TextInput(attrs={'id': 'name_create', 'class': 'form-control2', 'placeholder': "Имя"}),
            'type': TextInput(attrs={'id': 'type_create', 'class': 'form-control2', 'placeholder': "Тип"}),
            'rs_definition': TextInput(attrs={'id': "inputSign", 'class': 'form-control', 'placeholder': "РС-определение"}),
            'term': TextInput(attrs={'class': 'form-control', 'placeholder': "Термин"}),
            'text_definition': Textarea(attrs={'class': 'form-control', 'placeholder': "Текстовое определение"}),
        }