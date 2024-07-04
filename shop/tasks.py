from celery import shared_task
from django.utils import timezone

from .models import ProductImage


@shared_task
def delete_invalid_images(workers: int, worker_id: int):
    ProductImage.objects.filter(product__isnull=True,
                                created_at__lte=timezone.now()-timezone.timedelta(seconds=30)).delete()
