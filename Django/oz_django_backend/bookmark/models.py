from django.db import models


class Bookmark(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField('주소')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = '북마크'
        verbose_name_plural = '북마크 목록'


