from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin


class ArticleAdmin(SummernoteModelAdmin):
    summernote_fields = ('text',)


admin.site.register(Article, ArticleAdmin)