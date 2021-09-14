from django.db import models #importing models from django.db


class DjangoClasses(models.Model): #defining a class that will have a Title, Course Number, Instructor Name, and Duration
    objects = models.Manager()
    Title = models.CharField(max_length=100)
    Course_Number = models.IntegerField()
    Instructor_Name = models.CharField(max_length=100)
    Duration = models.FloatField()


# a-c are objects of the class DjangoClasses a.save() works to save the objects to the db
a = DjangoClasses(Title='Defense Against the Dark Arts', Course_Number=101, Instructor_Name='Snape', Duration=2.5)
a.save()
b = DjangoClasses(Title='Herbology', Course_Number=50, Instructor_Name='Sprout', Duration=2)
b.save()
c = DjangoClasses(Title='Muggle Studies', Course_Number=10, Instructor_Name='Burbage', Duration=1)
c.save()
