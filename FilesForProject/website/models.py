from django.db import models

#New data models
class Patient(models.Model):
    System_Number = models.CharField(max_length=10)
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    DOB = models.DateField()

    def __str__(self):
        return(f'{self.System_Number}')

class Drug(models.Model):
    Drug_Name = models.CharField(max_length=100)
    Brand_Name = models.CharField(max_length=100)

    def __str__(self):
        return(f"{self.Drug_Name}")
    
class Route(models.Model):
    Administration_Route = models.CharField(max_length=100)

    def __str__(self):
        return(f"{self.Administration_Route}")

class Transaction(models.Model):
    System_Number = models.ForeignKey(Patient, on_delete=models.CASCADE)
    Drug_Name = models.ForeignKey(Drug, on_delete=models.CASCADE)
    Dose = models.CharField(max_length=20)
    Administration_Route = models.ForeignKey(Route,on_delete=models.CASCADE)
    Administration_DateTime = models.DateTimeField("Administration Date & Time")

    def __str__(self):
        return(f'{self.System_Number} administered {self.Drug_Name} on {self.Administration_DateTime}')