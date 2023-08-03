from django.db import models
import datetime
import os
from django.contrib.auth.models import User


def getfilename(request,filename):
    now_time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    now_filename="%s%s"%(now_time,filename)
    return os.path.join('uploads/',now_filename)

class catagory(models.Model):
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=getfilename,null=True,blank=True)
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
    created=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name


class product(models.Model):
    catagory=models.ForeignKey(catagory,on_delete=models.CASCADE)
    product_name=models.CharField(max_length=150,null=False,blank=False)
    vendor=models.CharField(max_length=150,null=False,blank=False)
    product_image=models.ImageField(upload_to=getfilename,null=True,blank=True)
    quantity=models.IntegerField(null=False,blank=False)
    original_price=models.FloatField(null=False,blank=False)
    selling_price=models.FloatField(null=False,blank=False)
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
    trending=models.BooleanField(default=False,help_text="0-default,1-Hidden")
    created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.product_name