from django import forms
from .models import Article, ArtCat


class ArticleForm(forms.ModelForm):
    
    code = forms.CharField(
        label="Код товара", 
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Код товара',
                'class': 'form-control',
                }
            )
        )
    
    name = forms.CharField(
        label="Наименование", 
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Наименование товара',
                'class': 'form-control',
                }
            )
        )
    
    is_active = forms.NullBooleanField(
        label="Активность товара", 
        widget=forms.NullBooleanSelect(
            attrs={
                'class':'form-select',
                }
            )
        )
    
    artcat = forms.ModelChoiceField(
        queryset=ArtCat.objects.all(), 
        label="Категория товара",
        widget=forms.Select(attrs={
            'class':'form-select',
        })
        )
    
    
    class Meta:
        model = Article
        fields = '__all__'