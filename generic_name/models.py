from django.db import models

# Create your models here.
class GenericName(models.Model):
    named_id = models.SlugField(primary_key=True)

    def __str__(self):
        return self.named_id
