from ipaddress import ip_address
from django.db import models

class Equipment(models.Model):
    name = models.CharField(max_length=255)
    ip_address = models.GenericIPAddressField()
    status = models.CharField(max_length=50, choices=[('Active','Active'),('Inactive','Inactive')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name