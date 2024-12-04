from django.db import models
from project.models import Project
from product.models import Product

# Create your models here.
class Order(models.Model):
    project = models.ForeignKey(Project, related_name="orders", on_delete=models.CASCADE, verbose_name="Project")
    created_date = models.DateField(verbose_name="Created Date")
    need_date = models.DateField(verbose_name="Need By Date")
    is_purchased = models.BooleanField(default=False, verbose_name="Is Purchased")
    
    def __str__(self):
        return f"Order for {self.project.project_name} - Created on {self.created_date}"

    class Meta:
        db_table = 'orders'
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        ordering = ['-created_date']
        indexes = [
            models.Index(fields=['created_date'], name='order_created_date_idx'),
            models.Index(fields=['need_date'], name='order_need_date_idx'),
        ]


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, related_name="products_in_order", on_delete=models.CASCADE, verbose_name="Order")
    product = models.ForeignKey(Product, related_name="product_orders", on_delete=models.CASCADE, verbose_name="Product")
    quantity = models.IntegerField(verbose_name="Quantity")
    customer_price = models.DecimalField(max_digits=10, decimal_places=2, null=False, verbose_name="Customer Price")
    discount = models.DecimalField(max_digits=10, decimal_places=2, null=False, verbose_name="Discount")
    custom_need_date = models.DateField(verbose_name="Custom Need By Date")
    
    def __str__(self):
        return f"{self.product.product_name} - Quantity: {self.quantity}"

    class Meta:
        db_table = 'product_in_orders'
        verbose_name = "Product in Order"
        verbose_name_plural = "Products in Order"
        ordering = ['product__product_name']
