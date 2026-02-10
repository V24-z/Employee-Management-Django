from django.db import models
from datetime import datetime
import os
 

class Department(models.Model):
        name=models.CharField(max_length=100,null=False)
        location=models.CharField(max_length=100)
        def __str__(self):
            return self.name

class Role(models.Model):
    name=models.CharField(max_length=100,null=False)
    def __str__(self):
        return self.name

    
def filepath(request, filename):
    """old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)"""
    return  f"employee/{datetime.now().strftime('%Y%m%d%H%M%S')}_{filename}"   
    
class Employee(models.Model):
    first_name = models.CharField(max_length=100 ,null=False)
    last_name = models.CharField(max_length=100)
    dept=models.ForeignKey(Department,on_delete=models.CASCADE)
    salary=models.IntegerField(default=0)
    bonus=models.IntegerField(default=0)
    role=models.ForeignKey(Role,on_delete=models.CASCADE)
    phone=models.IntegerField(default=0)
    image=models.ImageField(null=True,blank=True,upload_to=filepath)
    #hire_date=models.DateTimeField()

    def __str__(self):
        return "%s %s" %(self.first_name, self.last_name)
