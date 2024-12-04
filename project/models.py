from django.db import models
from manager.models import Customer, Salesman, TechnicalLead

def content_file_project(instance, filename):
    # Improved format string to reflect file path more clearly
    return 'projects/{0}/{1}'.format(instance.project_name, filename)

# Create your models here.
class Project(models.Model):
    project_name = models.CharField(
        max_length=255,
        null=False,
        verbose_name="Project Name"
    )
    customer = models.ForeignKey(
        Customer,
        related_name="projects",
        on_delete=models.CASCADE,
        verbose_name="Customer"
    )
    salesman = models.ForeignKey(
        Salesman,
        related_name="projects",
        on_delete=models.CASCADE,
        verbose_name="Salesman"
    )
    technical_lead = models.ForeignKey(
        TechnicalLead,
        related_name="projects",
        on_delete=models.CASCADE,
        verbose_name="Technical Lead"
    )
    site = models.CharField(
        max_length=255,
        null=False,
        verbose_name="Site"
    )
    start_date = models.DateField(
        verbose_name="Start Date"
    )
    end_date = models.DateField(
        verbose_name="End Date"
    )
    status = models.CharField(
        max_length=20,
        choices=[
            ('active', 'Active'),
            ('archive', 'Archive')
        ],
        default='active',  # Setting a default value
        verbose_name="Project Status"
    )
    file = models.FileField(
        null=True,
        blank=True,
        upload_to=content_file_project,
        verbose_name="File Attachment"
    )

    def __str__(self):
        return self.project_name

    class Meta:
        db_table = 'projects'
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ['project_name']
        indexes = [
            models.Index(fields=['project_name'], name='project_name_idx'),
            models.Index(fields=['start_date', 'end_date'], name='project_date_idx'),
        ]

