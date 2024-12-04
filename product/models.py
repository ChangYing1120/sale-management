from django.db import models

# Product Model
class Product(models.Model):
    product_name = models.CharField(max_length=255, null=False, verbose_name="Product Name")
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, verbose_name="Price")
    delivery_time = models.IntegerField(verbose_name="Delivery Time (days)")  # Added unit for clarity
    sales_commission = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Sales Commission")  # Changed to DecimalField for accuracy

    def __str__(self):
        return self.product_name

    class Meta:
        db_table = 'products'
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ['product_name']
