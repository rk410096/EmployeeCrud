from django.db import models

# Create your models here.
class employee(models.Model):
    empno=models.IntegerField()
    ename=models.CharField(max_length=30)
    salary=models.FloatField()
    add=models.CharField(max_length=50)
    class Meta:
        db_table='employee'
