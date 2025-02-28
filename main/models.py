from django.db import models

# Create your models here.

class Class(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    full_name = models.CharField(max_length=100)
    price = models.FloatField()
    clas = models.ManyToManyField(Class)

    def __str__(self):
        return self.full_name


class Student(models.Model):
    full_name = models.CharField(max_length=100)
    clas = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name
