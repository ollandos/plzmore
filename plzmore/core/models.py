from django.db import models


class Video(models.Model):
    plzid = models.SlugField(
        max_length=11, unique=True,
    )
