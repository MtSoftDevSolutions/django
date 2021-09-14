from django.db import models


class DjangoClasses(models.Model):
    Title = models.CharField(max_length=100)
    Course_Number = models.IntegerField()
    Instructor_Name = models.CharField(max_length=100)
    Duration = models.FloatField()


a = DjangoClasses(Title='Defense Against the Dark Arts', Course_Number=101, Instructor_Name='Snape', Duration=2.5)
a.save()
b = DjangoClasses(Title='Herbology', Course_Number=50, Instructor_Name='Sprout', Duration=2)
b.save()
c = DjangoClasses(Title='Muggle Studies', Course_Number=10, Instructor_Name='Burbage', Duration=1)
c.save()
