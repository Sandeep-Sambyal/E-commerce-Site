from django.db import models

# Create your models here.
class Products(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    desc=models.CharField(max_length=300)
    pub_date=models.DateField()
    price=models.IntegerField(default=0)
    category=models.CharField(max_length=50,default="")
    subcategorgy=models.CharField(max_length=50,default="")
    image=models.ImageField(upload_to="ecart/images",default="")

    def __str__(self):
        return  self.product_name
    
class CustomerData(models.Model):
    CustomerName=models.CharField(max_length=50,default='')
    email=models.CharField(max_length=100,default='',primary_key=True,unique=True)
    seller_profile=models.CharField(max_length=1,default='N')  #( Use N-No, Y-Yes, R-Request)
    phone=models.CharField(max_length=25,default='')
    issue=models.CharField(max_length=5000,default="")
    seller_address=models.CharField(max_length=500,default="")
    shipping_address=models.CharField(max_length=500,default="")
    country=models.CharField(max_length=20,default="")

    def __str__(self):
        return self.CustomerName




