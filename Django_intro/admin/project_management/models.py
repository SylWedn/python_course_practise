from django.db import models
from authentication.models import User


class Label(models.Model):
    name = models.CharField(max_length=20, unique=True, null=False)

    def __str__(self):
        return self.name


class Project(models.Model):
    code = models.CharField(max_length=30, unique=True, null=False)
    name = models.CharField(max_length=100, null=False)
    description = models.TextField(max_length=1000, null=True)
    label = models.ManyToManyField(Label)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.name} {self.code}'
