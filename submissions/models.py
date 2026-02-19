from django.db import models


# class ITAssetAppSubmission(models.Model):

#     employee_email = models.CharField(
#         db_column='Employee_Email',
#         max_length=255
#     )

#     submitted_for = models.CharField(
#         db_column='Submitted_For',
#         max_length=255
#     )

#     asset_owner_email_id = models.CharField(
#         db_column='Asset_Owner_Email_Id',
#         max_length=255
#     )

#     asset_id = models.CharField(
#         db_column='Asset_Id',
#         max_length=100
#     )

#     serial_no = models.CharField(
#         db_column='Serial_No',
#         max_length=100
#     )

#     date = models.DateTimeField(
#         db_column='Date'
#     )

#     class Meta:
#         managed = False
#         db_table = 'IT_AssetApp_Submission'

#     def __str__(self):
#         return self.employee_email


class ITAssetAppSubmission(models.Model):

    employee_email = models.CharField(
        db_column='Employee_Email',
        max_length=255
    )

    submitted_for = models.CharField(
        db_column='Submitted_For',
        max_length=255
    )

    asset_owner_email_id = models.CharField(
        db_column='Asset_Owner_Email_Id',
        max_length=255
    )

    asset_id = models.CharField(
        db_column='Asset_Id',
        max_length=100
    )

    serial_no = models.CharField(
        db_column='Serial_No',
        max_length=100
    )

    date = models.DateTimeField(
        db_column='Date',
        primary_key=True   # 👈 ADD THIS
    )

    class Meta:
        managed = False
        db_table = 'IT_AssetApp_Submission'
