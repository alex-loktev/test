from django.db import models


class Article(models.Model):
    text = models.TextField(blank=True, null=True)
    docfile = models.FileField(upload_to='media/documents/%Y/%m/%d', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_file_name(self):
        return self.docfile.name.split('/')[-1]
