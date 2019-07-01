from django.db import models

# Create your models here.

class Staff(models.Model):
    staff_id = models.IntegerField(primary_key=True, max_length=8)
    name = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=15)
    address = models.CharField(max_length=150)
    job_title = models.CharField(max_length=50)
    class Meta:
        db_table = "staff"