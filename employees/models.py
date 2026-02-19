from django.db import models

class EmployeeMaster(models.Model):
    employee_id = models.IntegerField(primary_key=True)
    full_name = models.CharField(max_length=255)
    company_email_id = models.EmailField(db_column='company_email_id')
    date_of_exit = models.DateField(null=True, blank=True, db_column='date_of_exit')

    class Meta:
        managed = False   
        db_table = 'dbo.vw_AM_EmployeeMaster'
