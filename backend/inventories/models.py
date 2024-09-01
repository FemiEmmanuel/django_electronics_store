from django.db import models

class Inventory(models.Model):
    quantity = models.PositiveIntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Inventory for Product {self.product.name}"

    class Meta:
        verbose_name_plural = "Inventories"