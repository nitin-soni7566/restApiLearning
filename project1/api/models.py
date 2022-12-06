from django.db import models

# Create your models here.


class Student(models.Model):

    name = models.CharField(max_length=20)
    stu_class = models.CharField(max_length=20)
    age = models.CharField(max_length=20)
    roll_number = models.IntegerField()

    def __str__(self):

        return self.name