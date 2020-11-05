from django import forms
from django.core.exceptions import ValidationError

from .models import Tags, Post


class TagForm(forms.ModelForm):
    """Создание тега к статье"""

    class Meta:
        model = Tags
        fields = (
            'title', 'url_tags'
        )
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'url_tags': forms.TextInput(attrs={'class': 'form-control'})
        }

    def clean_url_tags(self):
        new_tag = self.cleaned_data['url_tags'].lower()

        if new_tag == 'create':
            raise ValidationError('This is a reversed name')
        if Tags.objects.filter(url_tags__iexact=new_tag).count():
            raise ValidationError('Slug must be unique')
        return new_tag


class PostForm(forms.ModelForm):
    """Форма для создания статьи"""

    class Meta:
        model = Post
        fields = (
            'title', 'body_post', 'url', 'tags', 'image'
        )
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body_post': forms.Textarea(attrs={'class': 'form-control'}),
            'url': forms.TextInput(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }

    def clean_url(self):
        new_tag = self.cleaned_data['url'].lower()

        if new_tag == 'create':
            raise ValidationError('This is a reversed name')
