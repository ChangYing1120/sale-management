from django.db import models
from project.models import Project
from product.models import Product
from manager.models import TechnicalLead

# Create your models here.
class ServiceCall(models.Model):
    project = models.ForeignKey(Project, related_name="service_calls", on_delete=models.CASCADE, verbose_name="Project")
    category = models.CharField(max_length=255, null=False, verbose_name="Category")
    product = models.ForeignKey(Product, related_name="service_calls", on_delete=models.CASCADE, verbose_name="Product")
    description = models.TextField(verbose_name="Description")
    solution_description = models.TextField(verbose_name="Description", null=True, blank=True)
    is_failure = models.BooleanField(default=False, verbose_name="Is Failure")
    technical_lead = models.ForeignKey(TechnicalLead, related_name="service_calls", on_delete=models.CASCADE, verbose_name="Technical Lead")
    status = models.CharField(max_length=20, choices=[
            ('pending', 'Pending'),
            ('in_progress', 'In Progress'),
            ('done', 'Done')
        ])
    opening_date = models.DateField(verbose_name="Opening Date")
    closing_date = models.DateField(null=True, blank=True, verbose_name="Closing Date")  # Made closing_date optional

    def __str__(self):
        return f"Service Call for {self.product.product_name}"

    class Meta:
        db_table = 'service_calls'
        verbose_name = "Service Call"
        verbose_name_plural = "Service Calls"
        ordering = ['-opening_date']  # Orders by most recent first
