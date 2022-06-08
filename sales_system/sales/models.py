from django.db import models

# Create your models here.
from django.contrib.auth.models import User




class Employee(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    user_name=models.CharField(max_length=60)
    department= models.CharField(max_length=50)
    role= models.CharField(max_length=50)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return "{} ({})".format(self.user.first_name,self.department)
class Sale(models.Model):
    Emp_Id=models.ForeignKey(Employee,to_field='id',on_delete=models.CASCADE,)
    Emp_name=models.CharField(max_length=60)
    Emp_role=models.CharField(max_length=60)
    Emp_department= models.CharField(max_length=150)
    product_name=models.CharField(max_length=160)
    business_partner=models.CharField(max_length=160)
    order_quantity=models.IntegerField()
    price=models.IntegerField()
    Total_price=models.IntegerField()
    Country=models.CharField(max_length=150)
    Phone_number=models.IntegerField()
    Email_Id=models.EmailField()



   