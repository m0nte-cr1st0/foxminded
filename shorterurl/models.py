from hashlib import md5

from django.conf import settings
from django.db import models
from django.urls import reverse


class ShortUrl(models.Model):
    """Short url table"""

    url = models.URLField(unique=True)
    short_url = models.URLField(unique=True)
    visits_count = models.PositiveSmallIntegerField(default=0)

    def __repr__(self) -> str:
        return f"{self.url} - {self.short_url}"

    def update_counter(self):
        """Increases the visit counter by 1"""
        self.visits_count += 1
        self.save(update_fields=("visits_count",))

    def save(self, *args, **kwargs):
        if not self.id:
            self.short_url = settings.SITE_URL + md5(self.url.encode()).hexdigest()[:10]
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('url-detail', args=[self.pk])
