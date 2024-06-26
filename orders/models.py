from django.db import models

class Order(models.Model):
    order_number = models.CharField(max_length=100, unique=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    customer_name = models.CharField(max_length=200)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.order_number
