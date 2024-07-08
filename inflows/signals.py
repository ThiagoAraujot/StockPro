from django.db.models.signals import post_save
from django.dispatch import receiver
from inflows.models import InFlow


@receiver(post_save, sender=InFlow)
def update_product_quantity(sender, instance, created, **kwargs):
    if created:
        if instance.quantity > 0:
            product = instance.product
            product.quantity += instance.quantity
            product.save()
