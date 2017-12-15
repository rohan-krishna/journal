from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notebook(models.Model):
    title = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField('date created')
    updated_at = models.DateTimeField('date updated')
    cover = models.ImageField(upload_to='covers', blank=True)

    def __str__(self):
        return self.title

class Note(models.Model):
    title = models.CharField(max_length=200)
    body = models.BinaryField(blank=True)
    created_at = models.DateTimeField('date created')
    updated_at = models.DateTimeField('date updated')
    notebook = models.ForeignKey(Notebook, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
