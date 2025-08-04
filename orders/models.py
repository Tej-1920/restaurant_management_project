from django.db import models
from django.contrib.auth.models import User
from products.models import Menu
# Create your models here.
class Order(models.Model):
    STATUS_CHOICES=[
        ('PENDING','Pending'),
        ('DELIVERED','Delivered'),
        ('CANCELLED','Cancelled'),
    ]
    customer=models.ForeignKey(User,on_delete=models.CASCADE)
    items=models.ManyToManyField(Menu)
    total_amount=models.DecimalField(max_digit=8,decimal_places=2)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='PENDING')
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} by {self.customer.username}"
