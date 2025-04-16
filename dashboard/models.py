from django.db import models


class Dashboards(models.Model):
    """
    This model define dashboard
    """
    class Meta:
        db_table = 'dashboards'

    type = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    created_time = models.DateField(auto_now=True)
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

class DashboardFile(models.Model):
    """
    This model defines file associated with a dashboard
    """
    class Meta:
        db_table = 'files'

    file_name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    