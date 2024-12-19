from django.db import models
from django.shortcuts import reverse
from django.utils import timezone


class News(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    short_content = models.TextField()
    long_content = models.TextField()
    category = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'News'

    def get_detail_url(self):
        return reverse('news:detail', args=[self.pk])