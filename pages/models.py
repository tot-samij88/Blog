from django.db import models
from datetime import datetime
from django.utils import timezone



class Post(models.Model):
    author = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photo_for_post', blank=True)
    title = models.CharField(max_length=200)
    preview_text = models.CharField(max_length=200)
    text_of_post = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)
    publish_date = models.DateField(default=timezone.now)
    creation_date = models.DateTimeField()
    last_modified = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.creation_date:
            self.creation_date = timezone.now()

        self.last_modified = timezone.now()
        return super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-creation_date',]

    def __str__(self):
        return self.title
