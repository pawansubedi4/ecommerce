from django.db import models
# from category.models import Category




# Create your models here.
class category(models.Model):
    c_name=models.CharField(max_length=100)
    c_discount=models.IntegerField(default=0)
    c_image=models.ImageField(upload_to='category',blank=True,null=True)
    description=models.TextField(default='non')

    def __str__(self):
        return self.c_name
    
class productsnew(models.Model):
    p_name =models.CharField(max_length=100)
    p_price=models.IntegerField(default=0)
    p_discount=models.IntegerField(default=0)
    p_photo=models.ImageField(default='default.jpg')
    p_detail=models.CharField(max_length=1000)
    p_quantity=models.IntegerField(default=0)
    p_others=models.CharField(max_length=100)
    category=models.ForeignKey(category,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return self.p_name

class ordersnew(models.Model):
    o_name =models.CharField(max_length=100)
    o_price=models.IntegerField(default=0)
    o_discount=models.IntegerField(default=0)
    o_photo=models.ImageField(default='default.jpg')
    o_location=models.CharField(max_length=100)
    o_number=models.CharField(max_length=1000)
    o_total=models.IntegerField(default=0)

class delevary(models.Model):
    dm_name=models.CharField(max_length=100)
    dm_location=models.CharField(max_length=100)
    dm_number=models.CharField(max_length=100)
    dm_salary=models.IntegerField(default=0)
    dm_others=models.CharField(max_length=100)
    dm_photo=models.ImageField(default='default.jpg')
    password=models.CharField(max_length=1000 ,null=True,blank=True)

class storeprofiles(models.Model):
    sp_name=models.CharField(max_length=100)
    sp_location=models.CharField(max_length=100)
    sp_number=models.CharField(max_length=100)
    sp_salary=models.IntegerField(default=0)
    sp_others=models.CharField(max_length=100)
    sp_photo=models.ImageField(default='default.jpg')
    password=models.CharField(max_length=1000 ,null=True,blank=True)

class commentbox(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True,null=True,blank=True)
    phone_number=models.CharField(max_length=1000,null=True,blank=True)
    comments=models.TextField(default='non',null=True,blank=True)

