from django.db import models

# Create your models here.

class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    article_body = models.TextField()
    article_img = models.ImageField(upload_to='static/media')
    article_created = models.DateTimeField('date_published')

    def __str__(self):
        return self.title