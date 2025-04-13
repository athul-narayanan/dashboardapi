from django.db import models


class EcomCountry(models.Model):
    class Meta:
        db_table = 'ecom-country'

    country_name = models.CharField(max_length=255)

class Sales(models.Model):
    class Meta:
        db_table = 'sales'

    invoice_no = models.CharField(max_length=255)
    stock_code = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    quantity = models.IntegerField(max_length=30)
    invoice_date = models.DateTimeField()
    unit_price = models.FloatField()
    customer_id = models.IntegerField()
    country = models.CharField(max_length=255)

class CustomerSummary(models.Model):
    class Meta:
        db_table = 'customer-summary'

    customer_id = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    invoice_count = models.IntegerField()
    product_count = models.IntegerField()