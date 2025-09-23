from django.db import models
from django.utils import timezone
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 254)
    content = models.TextField(max_length = 400)
    number = models.CharField(max_length = 15, blank = True, null = True)
    created_at = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.name