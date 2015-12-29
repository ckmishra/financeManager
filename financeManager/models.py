
from django.db import models
from django.contrib import auth

# Create your models here.
class financeDetails(models.Model):
    name = models.CharField(max_length= 20)
    policyNumber =models.CharField( unique =True, max_length= 20)
    financeType = models.CharField(max_length= 20)
    issueDate = models.DateField()
    maturityDate = models.DateField()
    amount = models.IntegerField()
    remarks = models.CharField(max_length= 200)
    userName = models.ForeignKey(auth.models.User)