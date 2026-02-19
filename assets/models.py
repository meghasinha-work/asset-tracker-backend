from django.db import models

class AssetMaster(models.Model):
    AssetTagID = models.CharField(max_length=100, primary_key=True)
    AssetSerialNo = models.CharField(max_length=100, null=True, blank=True)
    AssignedTo = models.CharField(max_length=200, null=True, blank=True)
    EmailId = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        managed = False
        db_table = "IT_Asset_Details"
