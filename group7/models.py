from django.db import models
from login.models import *
from group6.models import *


class Order(models.Model):
        Projectg7 = models.ForeignKey(ProjectG6)
	Date = models.DateField()
        name=models.CharField(max_length=200)
        
    	 #Link to Project entity one to one #Name_thai

        
class Orderinfo(models.Model):
    	Order = models.ForeignKey(Order) #temp date from Order table
    	Item_name = models.CharField(max_length=200)
    	Amount = models.IntegerField(default=0)
    	Cost = models.IntegerField(default=0)
    	Cost_total = models.IntegerField(default=0)
        OrderID=models.CharField(max_length=200,null=True)
        Company=models.CharField(max_length=200)
        


        
class Status_Of(models.Model):
    	Order = models.ForeignKey(Order)
        Date= models.DateField()
	State = models.CharField(max_length=200)
    	Status = models.CharField(max_length=200)	
    	Moreabout = models.CharField(max_length=200,null=True)
	Prove = models.CharField(max_length=200)
    
class Requisition(models.Model):
	Status_of = models.ForeignKey(Status_Of)
	Date = models.DateField()
    	##Project_name = models.CharField(max_length=200) link from ProjectG7
	Requisition_Id = models.CharField(max_length=200)
    	##Amount = models.IntegerField(default=0) link from orderinfo
    	##Item_name = models.CharField(max_length=200) link from orderinfo
    	##Cost_total = models.IntegerField(default=0) link from orderinfo
    	Moreabout = models.CharField(max_length=200)
