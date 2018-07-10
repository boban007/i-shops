from django.db import models

# Create your models here.
class GenericName(models.Model):
    named_id = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.named_id
