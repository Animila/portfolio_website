from django.db import models


class News(models.Model):
    title = models.CharField(max_length=100)
    time = models.DateField()
    description = models.TextField()
    image = models.ImageField(upload_to='news_image', blank=True)

    class Meta:
        verbose_name_plural = "Новости"

    def __str__(self):
        return self.title
