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

class Order(models.Model):
    order_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200,default="")
    email=models.CharField(max_length=70,default="")
    phone=models.CharField(max_length=15,default="")
    address=models.CharField(max_length=500,default="")
    city=models.CharField(max_length=70,default="")
    state=models.CharField(max_length=70,default="")
    zip_code=models.CharField(max_length=10,default="")
    prod_list=models.CharField(max_length=2000,default="")


class orderdetail(models.Model):
    order_id=models.IntegerField(default="")
    update_id=models.AutoField(primary_key=True)
    update_desc=models.CharField(max_length=5000)
    timestamp=models.DateTimeField(auto_now_add=True)


    """docstring for orderdetail"""
    def __str__(self):
        return str(self.order_id)+","+self.update_desc[0:20]+"..."
        
