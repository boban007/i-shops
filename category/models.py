from django.db import models

# Create your models here.
class Category(models.Model):
    named_id = models.SlugField(primary_key=True)
    is_active = models.BooleanField(default=True)
    position = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return self.named_id

    class Meta:
        ordering = ['position']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
