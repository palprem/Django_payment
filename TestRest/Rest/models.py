from django.db import models
import datetime
from uuid import uuid4
from rest_framework.permissions import BasePermission

# Create your models here.

class Pdataile(models.Model):
    transection_date = models.DateField(blank=True, null=True)
    amount = models.IntegerField()
    Order_no  = models.IntegerField()
    customer_Id  = models.IntegerField()
    f = models.CharField(default='generateUUID', max_length=36, unique=True, editable=False)
    # status = models.BooleanField(False)
    date_recieve = models.DateField(blank=True, null=True)
    tranjection_code = models.IntegerField()
    tranjection_text = models.CharField(max_length=200)
   
