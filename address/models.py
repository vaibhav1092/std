from django.db import models
from employee.models import Employee
# Create your models here.
class Address(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE,null=False)

    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    code = models.CharField(max_length=50)

    class Meta():
        db_table = "address"

