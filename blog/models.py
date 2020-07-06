from django.db import models

# Create your models here.

class blogpost(models.Model):
    blog_id=models.AutoField(primary_key=True)
    blog_author=models.CharField(max_length=100)
    blog_title=models.CharField(max_length=500,default="")
    blog_heading=models.CharField(max_length=500,default="")
    blog_description=models.CharField(max_length=15000,default="")
    pub_date=models.DateField()
    image=models.ImageField(upload_to="blog/images",default="")

    def __str__(self):
        return self.blog_author



