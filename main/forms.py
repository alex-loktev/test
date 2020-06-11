from django import forms
from.models import *
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('text', 'docfile')
        widgets = {
            'text': SummernoteWidget(),
        }