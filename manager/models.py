from django.db import models

# Create your models here.
class Customer(models.Model):
    company_name = models.CharField(max_length=255, null=False, verbose_name="Company Name")
    
    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"
        ordering = ['company_name']
        db_table = 'customers'  # Custom table name

class Salesman(models.Model):  # Changed from Salesmen to Salesman (singular) to follow naming convention.
    first_name = models.CharField(max_length=255, null=False, verbose_name="First Name")
    last_name = models.CharField(max_length=255, null=False, verbose_name="Last Name")
    department = models.CharField(max_length=255, null=False, verbose_name="Department")
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Salesman"
        verbose_name_plural = "Salesmen"
        ordering = ['last_name', 'first_name']
        db_table = 'salesmen'  # Custom table name

class TechnicalLead(models.Model):
    first_name = models.CharField(max_length=255, null=False, verbose_name="First Name")
    last_name = models.CharField(max_length=255, null=False, verbose_name="Last Name")
    department = models.CharField(max_length=255, null=False, verbose_name="Department")
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Technical Lead"
        verbose_name_plural = "Technical Leads"
        ordering = ['last_name', 'first_name']
        db_table = 'technical_leads'  # Custom table name
