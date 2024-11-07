from django.db import models
from django.contrib.auth.models import User

class News_post(models.Model):
    title = models.CharField('News title', max_length=100)
    short_description = models.CharField('Short news description', max_length=200)
    text = models.TextField('News')
    pub_date = models.DateTimeField('Publication date')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'News Post'
        verbose_name_plural = 'News Posts'

