from django.db import models
import os
import uuid

from django.dispatch import receiver
from django.db.models.signals import post_delete

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.PositiveBigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


def get_upload_path(instance, filename):
    return f"products/images/{uuid.uuid4()}-{filename}"


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to=get_upload_path, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


@receiver(post_delete, sender=ProductImage)
def add_to_inventory(sender, instance, **kwargs):
    os.remove(instance.image.path)
