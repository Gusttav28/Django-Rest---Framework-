from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=200)
    
    
    def __str__(self):
        return self.name


class TodoList(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    quantity = models.IntegerField()
    done = models.BooleanField(default=False)