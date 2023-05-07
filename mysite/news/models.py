from django.db import models

# Create your models here.

DB = {
    'id': 'id',
    'title': 'title',
    'content': 'content',
    'created': 'created_at',
    'updated': 'updated_at',
    'photo': 'photo',
    'published': 'id_published',
}


class News(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    id_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
