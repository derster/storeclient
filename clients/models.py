from django.db import models

from datetime import datetime

class Client(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=datetime.now())
    def __src__(self):
        return self.name
