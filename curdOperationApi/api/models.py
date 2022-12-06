from django.db import models

# Create your models here.
class Student(models.Model):

    name = models.CharField(max_length=100)
    student_class = models.CharField(max_length=100)
    age = models.IntegerField()
    roll_no = models.IntegerField()
    def __str__(self):
        return self.name