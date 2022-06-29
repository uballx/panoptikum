from django.db import models
from django.template.defaultfilters import slugify


class Galeria(models.Model):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name="galerias")
    title = models.CharField(max_length=250)
    slug = models.SlugField()
    description = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to="covers/%Y/%m/%d")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __repr__(self):
        return f"{self.title} by {self.owner}"

    def __str__(self):
        return self.__repr__()

