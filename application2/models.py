from django.db import models

class Employees(models.Model):
    Eid=models.IntegerField()
    Ename=models.CharField(max_length=30)
    Esal=models.FloatField()
    Design=models.CharField(max_length=30)
    Company=models.CharField(max_length=30)
    Join_Date=models.DateField()
    Location=models.CharField(max_length=30)

class Registration(models.Model):
    First_Name=models.CharField(max_length=30)
    Last_Name=models.CharField(max_length=30)
    User_Name=models.CharField(max_length=30)
    Password=models.IntegerField()
    Email=models.CharField(max_length=50)
    Mobile_No=models.IntegerField()

