from django.db import models

# Create your models here.
class News(models.Model):
    link = models.CharField(max_length=200)
    article = models.CharField(max_length=200)
    body = models.TextField()

    class Meta:
        verbose_name_plural = "news"
    
    def __str__(self):
        return self.article